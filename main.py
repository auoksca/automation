from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import tempfile
import time

# Set Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')  # Use new headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Avoid "user data dir already in use" error
temp_profile = tempfile.mkdtemp()
options.add_argument(f'--user-data-dir={temp_profile}')

# Start the browser
driver = webdriver.Chrome(options=options)

# Step 1: Open website
driver.get("https://sales.trasccon.in")
print("🌐 Opened site")
time.sleep(2)

# Step 2: Login
driver.find_element(By.NAME, "user_name").send_keys("Harshitha")
driver.find_element(By.NAME, "pass_word").send_keys("Harshitha@123")
Select(driver.find_element(By.NAME, "role_s")).select_by_visible_text("RFQ Tracker")
driver.find_element(By.CLASS_NAME, "login-button").click()
print("🔐 Submitted login")

# Step 3: Wait for dashboard after login
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Welcome')]"))
)
print("✅ Logged in. URL:", driver.current_url)

# Step 4: Print page source for debugging
print("🧾 Page Source after login:")
print(driver.page_source)

# Step 5: Find and click "Send Mail"
send_mail_button_xpath = "//button[normalize-space()='Send Mail']"
button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, send_mail_button_xpath))
)

driver.execute_script("arguments[0].scrollIntoView(true);", button)
ActionChains(driver).move_to_element(button).pause(0.5).click().perform()
print("📧 Clicked 'Send Mail' button")

# Let backend process the request
time.sleep(5)

# Step 6: Done
print("✅ Mail send action triggered.")

# Cleanup
driver.quit()
