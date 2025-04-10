from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import tempfile
import time

# Setup Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')  # Modern headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Fix: avoid "user data dir is in use" error
temp_profile = tempfile.mkdtemp()
options.add_argument(f'--user-data-dir={temp_profile}')

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

try:
    # Open the website
    driver.get("https://sales.trasccon.in")
    time.sleep(3)

    # Fill in login details
    driver.find_element(By.NAME, "user_name").send_keys("Harshitha")
    driver.find_element(By.NAME, "pass_word").send_keys("Harshitha@123")
    Select(driver.find_element(By.NAME, "role_s")).select_by_visible_text("RFQ Tracker")
    driver.find_element(By.CLASS_NAME, "login-button").click()

    # Wait for the page to load and locate the "Send Mail" button
    send_mail_button_xpath = "//button[normalize-space()='Send Mail']"
    button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, send_mail_button_xpath))
    )

    # Scroll into view and simulate real user click
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    ActionChains(driver).move_to_element(button).pause(0.5).click().perform()

    # Wait for the alert and handle it
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print("✅ Alert detected:", alert_text)
    alert.accept()

except Exception as e:
    print("❌ Error:", str(e))

finally:
    driver.quit()
