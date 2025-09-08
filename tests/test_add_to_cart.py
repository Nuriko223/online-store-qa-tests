
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart(browser):
    browser.get("https://demoblaze.com")
    browser.find_element(By.LINK_TEXT, "Laptops").click()
    time.sleep(1)
    browser.find_element(By.LINK_TEXT, "Sony vaio i5").click()
    time.sleep(1)
    browser.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    browser.find_element(By.ID, "cartur").click()
    assert "Sony vaio i5" in browser.page_source
