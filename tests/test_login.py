
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(browser):
    browser.get("https://demoblaze.com")
    browser.find_element(By.ID, "login2").click()
    browser.find_element(By.ID, "loginusername").send_keys("testuser")
    browser.find_element(By.ID, "loginpassword").send_keys("testpass")
    browser.find_element(By.XPATH, "//button[text()='Log in']").click()
    assert "Welcome" in browser.page_source
