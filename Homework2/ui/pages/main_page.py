from .base_page import BasePage
from ui.locators.locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    locators = MainPageLocators()

    def create_company(self, name, url, picture):
        try:
            self.click(self.locators.CREATE_NEW_COMPANY)
        except Exception:
            self.click(self.locators.CREATE_ZERO_COMPANY)
        self.click(self.locators.TYPE_OF_COMPANY)
        url_field = self.find(self.locators.FIELD_OF_URL)
        self.click(self.locators.FIELD_OF_URL)
        url_field.clear()
        url_field.send_keys(url)
        name_field = self.find(self.locators.FIELD_OF_NAME_COMPANY)
        self.click(self.locators.FIELD_OF_NAME_COMPANY)
        name_field.clear()
        name_field.send_keys(name)
        self.click(self.locators.BANNER)
        new_element = self.find(self.locators.DOWNLOAD_PICTURE)
        new_element.send_keys(picture)
        self.click(self.locators.ADD_COMPANY)
        
        
    def create_segmentum(self, name):
        self.click(self.locators.AUDITORIUM)
        try:
            self.click(self.locators.NEW_SEGMENTUM)
        except Exception:
            self.click(self.locators.CREATE_SEGMENTUM)
        name_field = self.find(self.locators.FIELD_OF_NAME_SEGMENTUM)
        self.click(self.locators.FIELD_OF_NAME_SEGMENTUM)
        name_field.clear()
        name_field.send_keys(name)
        self.click(self.locators.ADD_SEGMENTS)
        self.click(self.locators.TYPE_OF_SEGMENTUM)
        self.click(self.locators.CHECKBOX)
        self.click(self.locators.BUTTON_ADD_SEGMENTUM)
        self.click(self.locators.CREATE_SEGMENTUM)
        
    def delete_segmentum(self):
        self.click(self.locators.DELETE_SEGMENTUM)
        self.click(self.locators.DELETE_BUTTON)   
