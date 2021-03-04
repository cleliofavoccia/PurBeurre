"""Functionnal test on Chrome session"""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Call chrome options class
chrome_options = webdriver.ChromeOptions()
# Headless mode
chrome_options.add_argument('--headless')
# Navigate in a certain window
chrome_options.add_argument('window-size=1920x1080')


class ChromeFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        """Create a Chrome session
        and define his behavior"""
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            executable_path=str(
                settings.BASE_DIR / 'webdrivers' / 'chromedriver'
            ),
            options=chrome_options,
        )
        # Wait wait for a certain amount of time
        # before it throws a "No Such Element Exception"
        cls.driver.implicitly_wait(30)
        # Reduces the chances of Selenium scripts
        # missing out on web elements they must interact
        # with during automated tests
        cls.driver.maximize_window()

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
        self.driver.find_element_by_css_selector('#button-logout').click()
        # Test disconnection
        self.driver.find_element_by_css_selector('#button-login').click()

    def test_user_can_sign_in(self):
        """Test if user with a Chrome session can sign in
         to the website"""
        self.driver.get(self.live_server_url)
        # Sign in
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#button-sign_in').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testuser2"
        )
        self.driver.find_element_by_css_selector('#id_email').send_keys(
            "testuser2@test.com"
        )
        self.driver.find_element_by_css_selector('#id_password1').send_keys(
            "eofh5jf8"
        )
        self.driver.find_element_by_css_selector('#id_password2').send_keys(
            "eofh5jf8"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()
        # Connect
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testuser2"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "eofh5jf8"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()
        # Test connection
        self.driver.find_element_by_css_selector('#button-account').click()

    def test_user_can_access_to_his_page_account(self):
        """Test if user with a Chrome session can access
        to his page account"""
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
        self.driver.find_element_by_css_selector('#button-account').click()
        # Proof is in account
        self.driver.find_element_by_css_selector('#modify-email').send_keys(
            "testuser@live.fr"
        )

    def test_user_can_type_a_request_in_substitute_forms(self):
        """Test if user with a Chrome session can make a request
        in differents substitute forms on the website"""
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#id_research').send_keys(
            "nutella"
        )

    def test_user_can_add_to_favorite_a_substitute_if_is_connected(self):
        """Test if user with a Chrome session can add a substitute
        in his favorites list if he is connected"""
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
        self.driver.find_element_by_css_selector('#id_research').send_keys(
            "nutella"
        )
        (self.driver.find_element_by_css_selector('#id_research')
         .send_keys(Keys.ENTER))
        self.driver.find_element_by_tag_name('input').click()  # Error

    def test_user_can_consult_product_detail(self):
        """Test if user with a Chrome session can consult
        a product page with clicking on it"""
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#id_research').send_keys(
            "nutella"
        )
        (self.driver.find_element_by_css_selector('#id_research')
         .send_keys(Keys.ENTER))
        self.driver.find_element_by_tag_name('a').click()  # Error

    def test_user_can_access_to_his_favorites_page(self):
        """Test if user with a Chrome session can access
        to his favorites pages (list of substitutes add
        to favorites)"""
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
        self.driver.find_element_by_css_selector('#button-favorites')
