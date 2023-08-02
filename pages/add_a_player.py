from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    login_url = ('https://dareit.futbolkolektyw.pl/en/login?redirected=true')
    password_field_xpath =  "//*[@id='password']"
    sign_in_button_xpath = '//*[@id="__next"]/form/div/div[2]/button/span[1]'
    remind_passowrd_button_xpath = "//*[@id='__next']/form/div/div[1]/a"
    select_leangue_button_xpath = '//*[@id="__next"]/form/div/div[2]/div/div'
    expected_title = 'Scouts panel - sign in'
    dodaj_gracza_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
    name_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input'
    age_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input'
    position_xpath ='//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input'
    sumbit_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[1]'

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

    def type_name (self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_surname (self, surname):
        self.field_send_keys (self.surname_xpath, surname)

    def click_age (self, number):
        self.field_send_keys(self.age_xpath, number)

    def type_postion (self, position):
        self.field_send_keys(self.position_xpath, position)
    def click_submit (self):
        self.click_on_the_element(self.sumbit_xpath)

