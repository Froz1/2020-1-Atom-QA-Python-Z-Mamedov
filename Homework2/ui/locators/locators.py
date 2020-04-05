from selenium.webdriver.common.by import By
    
    
class MainPageLocators():
    CREATE_NEW_COMPANY = (By.XPATH, '//span[contains(@data-loc-ru, "Создать кампанию")]')
    CREATE_ZERO_COMPANY = (By.PARTIAL_LINK_TEXT, 'создайте')    
    TYPE_OF_COMPANY = (By.PARTIAL_LINK_TEXT, 'создайте')
    FIELD_OF_URL = (By.XPATH, '//input[contains(@class, "input__inp js-form-element")]')
    FIELD_OF_NAME_COMPANY = (By.XPATH, '(//input[contains(@class, "input__inp js-form-element")])[2]')
    BANNER = (By.ID, '214')
    DOWNLOAD_PICTURE = (By.XPATH, '//div[contains(text(), "Загрузить 1080 x 607")]')
    ADD_COMPANY = (By.XPATH, '//div[contains(text(), "Добавить объявление")]')
    AUDITORIUM = (By.CLASS_NAME, 'center-module-button-cQDNvq center-module-segments-3y1hDo center-module-activeButton-3i8iSI')
    NEW_SEGMENTUM = (By.PARTIAL_LINK_TEXT, 'Создайте')
    CREATE_SEGMENTUM = (By.XPATH, '//div[contains(@class, "button__text")]')
    FIELD_OF_NAME_SEGMENTUM = (By.XPATH, '(//input[contains(@class, "input__inp js-form-element")])[2]')
    ADD_SEGMENTS = (By.XPATH, '//span[contains(@data-loc-ru, "Добавить аудиторные сегменты...")]')
    TYPE_OF_SEGMENTUM = (By.XPATH, '//div[contains(text(), "Приложения (ОК и МойМир)")]')
    CHECKBOX = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox js-main-source-checkbox")]')
    BUTTON_ADD_SEGMENTUM = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]')
    CREATE_SEGMENTUM = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    DELETE_SEGMENTUM = (By.CLASS_NAME, 'icon-cross')
    DELETE_BUTTON = (By.XPATH, '//div[contains(text(), "Удалить")]')
    CHECK_NAME = (By.XPATH, '//a[contains(@class, "adv-camp-cell adv-camp-cell_name")]')

   
class AuthPageLocators():
    ENTER_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUCCESS_AUTH = (By.CLASS_NAME, "right-module-userNameWrap-34ibLS")
    FAIL_AUTH = (By.CLASS_NAME, "formMsg_title")
