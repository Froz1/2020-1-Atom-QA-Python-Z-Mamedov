import pytest
import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.auth_page import AuthPage


class UnsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='function')
def auth_page(driver):
    return AuthPage(driver)
	

@pytest.fixture(scope='function')
def authorization(driver):
    page = AuthPage(driver)
    page.auth(email='test_atom1@mail.ru', password='12ab..')
    return MainPage(page.driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']

    if browser == 'chrome':
        if not selenoid:
            options = ChromeOptions()
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                  options=options,
                                  desired_capabilities={'acceptInsecureCerts': True}
                                  )
        else:
            capabilities = {'browserName': browser,
                            'version': '80.0',
                           }
            options = ChromeOptions()

            driver = webdriver.Remote(command_executor=selenoid,
                                  options=options,
                                  desired_capabilities=capabilities
                                  )

    else:
        raise UnsupportedBrowserException(f'Unsupported browser: "{browser}"')
        
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.close()
	

@pytest.fixture(scope="function")
def download_picture():
    new_path = os.path.dirname(__file__)
    path = os.path.join(new_path, "..", "test_image.jpeg")
    path = os.path.abspath(path)
    return path
