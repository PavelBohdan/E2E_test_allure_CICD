import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class PersonalinfoPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ('xpath', '//input[@name="firstName"]')
    SAVE_BUTTON = ('xpath', '(//button[@type="submit"])[1]')
    SUCCESS_INFO_FIELD = (
        'xpath', '//div[@class="oxd-toast-content oxd-toast-content--success"]')
    LOADER = ('xpath', '//div[@class="oxd-form-loader"]')

    def change_name(self, newname):
        with allure.step(f'Change name on "{newname}"'):
            first_name_field = self.wait.until(
                EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL, "a", Keys.DELETE)
            text = first_name_field.get_attribute('value')
            assert text == '', f'There is text {text}'
            first_name_field.send_keys(newname)
            self.name = newname

    @allure.step('Save changes')
    def save_changes(self):
        self.wait.until(EC.invisibility_of_element(self.LOADER))
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step('Changes saved')
    def changes_saved(self):
        self.wait.until(EC.presence_of_element_located(
            self.SUCCESS_INFO_FIELD))
