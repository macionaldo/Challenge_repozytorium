from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    password_field_xpath =  "//*[@id='password']"
    sign_in_button_xpath = '//*[@id="__next"]/form/div/div[2]/button/span[1]'
    remind_passowrd_button_xpath = "//*[@id='__next']/form/div/div[1]/a"
    select_leangue_button_xpath = '//*[@id="__next"]/form/div/div[2]/div/div'
    expected_title = 'Scouts panel - sign in'
    dodaj_gracza_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)


    def type_password (self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_login (self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page (self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def dodaj_gracza (self):
        self.click_on_the_element(self.dodaj_gracza_xpath)