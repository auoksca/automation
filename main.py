from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import tempfile
import time

# Setup Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Temporary profile to avoid session errors
temp_profile = tempfile.mkdtemp()
options.add_argument(f'--user-data-dir={temp_profile}')

# Start browser
driver = webdriver.Chrome(options=options)

# Open website
driver.get("https://sales.trasccon.in")
time.sleep(3)

# Login
driver.find_element(By.NAME, "user_name").send_keys("Harshitha")
driver.find_element(By.NAME, "pass_word").send_keys("Harshitha@123")
Select(driver.find_element(By.NAME, "role_s")).select_by_visible_text("RFQ Tracker")
driver.find_element(By.CLASS_NAME, "login-button").click()

# Click Send Mail
send_mail_button_xpath = "//button[normalize-space()='Send Mail']"
button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, send_mail_button_xpath))
)
driver.execute_script("arguments[0].scrollIntoView(true);", button)
ActionChains(driver).move_to_element(button).pause(0.5).click().perform()

# Let backend send the mail
time.sleep(5)

# Done
print("✅ Send Mail button clicked successfully.")

# Quit browser
driver.quit()
