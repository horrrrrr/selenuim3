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


def test_