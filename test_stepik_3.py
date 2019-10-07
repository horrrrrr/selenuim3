from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time
import math
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



driver = WebDriver(executable_path='C:\Python33\chromedriver_win32\chromedriver')




# подставляем переменные в текст ошибки с помощью f и {}
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"




# s = 'My Name is Julia'
#
# if 'Name' in s:
#     print('Substring found')
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

