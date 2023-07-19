import os
import unittest
import time

import dashboard as dashboard
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_player import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAdding(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_player (self):
        user_login = AddPlayer(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_password('Test-1234')
        user_login.click_login()
        time.sleep(5)
        user_login.dodaj_gracza()
        time.sleep(5)
        user_login.type_name("Krzychu")
        user_login.type_surname("Piącha")
        user_login.click_age("12121995")
        user_login.type_postion('Napastnik')
        time.sleep(5)
        user_login.click_submit()
        time.sleep(10)
