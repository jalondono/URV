from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from flask import Flask
from models import storage
import json

"""Test to web"""


class TestWeb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_post(self):
        driver = self.driver
        self.driver.set_page_load_timeout("10")
        driver.get("http://127.0.0.1:5000/")
        self.assertIn('Unique Registry of Victims', driver.title)
        element_vict = driver.find_element_by_id('victims')
        element_vict.send_keys('50')
        element_submit = driver.find_element_by_id('save')
        element_submit.click()

    def test_reload(self):
        """serialize the file path to JSON file path
        """
        self.objects = {}
        try:
            with open("../file.json", 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.objects[key] = value
        except FileNotFoundError:
            pass

    def test_find_value(self):
        for obj in self.objects.values():
            if obj.place == 'Amazonas':
                id = obj.id
                break
        self.assertEqual(self.objects[id].victims, 50, "Should be 50")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
