import pytest

from tests.base import BaseCase



class Test(BaseCase):

    #@pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_positive_auth(self):
        self.auth_page.auth('test_atom1@mail.ru', '12ab..')
        assert self.auth_page.find(self.auth_page.locators.SUCCESS_AUTH) is not None
		
		
    #@pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_negative_auth(self):
        self.auth_page.auth('abc@rgsgfsdef.ru', '123456')
        assert self.auth_page.find(self.auth_page.locators.FAIL_AUTH) is not None

    #@pytest.mark.skip(reason='TEMP')    
    @pytest.mark.UI
    def test_create_company(self, authorization, download_picture, name_company="TestCompany"):
        self.auth_page.auth('test_atom1@mail.ru', '12ab..')
        self.main_page.create_company(name_company, "https://ok.ru/game/sparta", download_picture)
        company_page = self.main_page.find(self.main_page.locators.NAME_COMPANY)
        assert company_page.get_attribute('title') == name_company
        
    #@pytest.mark.skip(reason='TEMP')    
    @pytest.mark.UI
    def test_create_segmentum(self, authorization, name="TestSegmentum"):
        self.auth_page.auth('test_atom1@mail.ru', '12ab..')
        self.main_page.create_segmentum(name)
        assert self.main_page.locators.CHECK_NAME.get_attribute('title') == name
        
    #@pytest.mark.skip(reason='TEMP')    
    @pytest.mark.UI
    def test_delete_segmentum(self, authorization, name="TestSegmentum"):
        self.auth_page.auth('test_atom1@mail.ru', '12ab..')     
        self.main_page.create_segmentum(name)
        self.main_page.delete_segmentum()
        assert self.main_page.locators.CHECK_ELEMENT is None
