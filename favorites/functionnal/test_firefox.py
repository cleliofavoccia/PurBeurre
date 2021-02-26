from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf.settings import BASE_DIR # Pourquoi marche pas ici ?
from selenium import webdriver


firefox_options = webdriver.FirefoxOptions() # Call firefox options class
firefox_options.headless = True # Headless mode ?


class FirefoxFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Firefox web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        """Create a Firefox session
        and define his behavior"""
        super().setUpClass()
        cls.driver = webdriver.Firefox(
            executable_path=str(BASE_DIR / 'webdrivers' / 'geckodriver'),
            options=firefox_options,
        )
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        """Close a Firefox session"""
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        """Create an user"""
        User = get_user_model()
        User.objects.create_user(
            username="testuser", password="PdfjqX458s"
        )

    def test_user_can_connect_and_disconnect(self):
        """Test if user with a Firefox session can connect and
        disconnect to the website"""
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "tchappui"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "openClassrooms.2020"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()
        logout = self.driver.find_element_by_css_selector('#button-logout')
        self.assertEqual(
            logout.text,
            "Déconnexion",
            "Disconnect button should be available.",
        )