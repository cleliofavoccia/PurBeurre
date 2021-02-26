import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import reverse
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()  # Call chrome options class
chrome_options.add_argument('--headless')  # Headless mode ?
chrome_options.add_argument('window-size=1920x1080')  # Navigate in a certain window


class ChromeFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        """Create a Chrome session
        and define his behavior"""
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            executable_path=str(settings.BASE_DIR / 'webdrivers' / 'chromedriver'),
            options=chrome_options,
        )
        cls.driver.implicitly_wait(30)  # Wait wait for a certain amount of time
        # before it throws a "No Such Element Exception"
        cls.driver.maximize_window()  # Reduces the chances of Selenium scripts
        # missing out on web elements they must interact with during automated tests

    @classmethod
    def tearDownClass(cls):
        """Close a Chrome session"""
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        """Create an user"""
        User = get_user_model()
        User.objects.create_user(
            username="testuser", password="PdfjqX458s"
        )

    def test_user_can_connect_and_disconnect(self):
        """Test if user with a Chrome session can connect and
        disconnect to the website"""
        self.driver.get(self.live_server_url)
        # Connect
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testuser"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "PdfjqX458s"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()
        # Disconnect
        self.driver.find_element_by_css_selector('#button-logout')
        # # Test disconnection
        # response = self.driver.find_element_by_css_selector('#button-account')
        # self.assertEqual(response.status_code, 302)

    def test_user_can_sign_in_and_connect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#button-sign_in').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testuser2"
        )
        self.driver.find_element_by_css_selector('#id_email').send_keys(
            "testuser2@test.com"
        )
        self.driver.find_element_by_css_selector('#id_password1').send_keys(
            "eofh5jf"
        )
        self.driver.find_element_by_css_selector('#id_password2').send_keys(
            "eofh5jf"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()
        # Connect
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testuser2"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "eofh5jf"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()

    def test_user_can_access_to_his_page_account(self):
        self.driver.get(self.live_server_url)
        # Connect
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testuser"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "PdfjqX458s"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()

    def test_user_can_type_a_request_in_substitute_forms(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#id_research').send_keys(
            "nutella"
        )

    def test_user_can_add_to_favorite_a_substitute(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#id_research').send_keys(
            "nutella"
        )
        self.driver.find_element_by_css_selector('#button-save').click()

    def test_user_can_consult_product_detail(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#id_research').send_keys(
            "nutella"
        )
        self.driver.find_element_by_css_selector('.results').click()

    def test_user_can_access_to_his_favorites_page(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-favorites')
