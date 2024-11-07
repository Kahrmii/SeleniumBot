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
        
def TwitchSignIn(driver, usr, pw):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'root')))
    time.sleep(0.1)
    keyboard.write(usr, 0.1)
    time.sleep(0.1)
    keyboard.send('tab')
    keyboard.write(pw, 0.1)
    time.sleep(0.1)
    keyboard.send('Enter')

def main():
    driver = webdriver.Chrome()

    driver.get("https://twitch.facepunch.com/connect")
    wait_and_click(driver, By.XPATH, "//button[contains(@class, 'button steam')]")
    wait_and_click(driver, By.ID, "imageLogin")
    wait_and_click(driver, By.XPATH, "//button[contains(@class, 'button twitch')]")
    TwitchSignIn(driver, 'Username', 'Password')
    
    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    main()