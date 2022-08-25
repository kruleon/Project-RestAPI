from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="C:\\Users\\leon\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("http://127.0.0.1:5001/users/get_user_data/1")

try:

    if driver.find_element(by=By.ID, value='user').is_displayed():
        web_element_user = driver.find_element(by=By.ID, value='user').text
        print(web_element_user)
    else:
        # web_element_user = print(driver.find_element_by_id("user").text)
        web_element_error = driver.find_element(by=By.ID, value='error').text
        print(web_element_error)

except NoSuchElementException as a_e:
    print(a_e)
