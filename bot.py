import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

def wait_and_click(driver, by, value, timeout=100):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except TimeoutException:
        print(f"Element nicht gefunden oder nicht klickbar: {value}")

def main():
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.maximize_window()

    driver.get("https://store.steampowered.com")
    time.sleep(1)
    wait_and_click(driver, By.ID, "global_action_menu")
    wait_and_click(driver, By.ID, "account_pulldown")
    wait_and_click(driver, By.ID, "global_actions")
    
    
    time.sleep(500)

    driver.quit()

if __name__ == "__main__":
    main()