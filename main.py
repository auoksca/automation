from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
#options.add_argument('--headless')  # Optional
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# Initialize driver
driver = webdriver.Chrome(options=options)
try:
    # Open the site
    driver.get("https://sales.trasccon.in")
    time.sleep(3)
    # Login process
    driver.find_element(By.NAME, "user_name").send_keys("Harshitha")
    driver.find_element(By.NAME, "pass_word").send_keys("Harshitha@123")
    Select(driver.find_element(By.NAME, "role_s")).select_by_visible_text("RFQ Tracker")
    driver.find_element(By.CLASS_NAME, "login-button").click()
    # Wait for Send Mail button
    send_mail_button_xpath = "//button[normalize-space()='Send Mail']"
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, send_mail_button_xpath)))
    # Click Send Mail button
    driver.find_element(By.XPATH, send_mail_button_xpath).click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print("Alert detected:", alert_text)
    alert.accept()

except Exception as e:
    print("❌ Error:", str(e))

finally:
    driver.quit()
