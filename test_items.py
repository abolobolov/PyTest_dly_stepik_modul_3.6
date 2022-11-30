from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
import time
def test_should_be_button_add_to_cart(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    button_add_to_cart = browser.find_element(By.XPATH, '//form[@id = "add_to_basket_form"]//button')
    assert browser.find_element(By.XPATH, '//form[@id = "add_to_basket_form"]//button').is_enabled(), \
        'Кнопка добавления товара в корзину отсутсвует'