import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import Select



# Initialize the Chrome driver

service = Service("D:/chromedriver/chromedriver-win64/chromedriver.exe")
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode
driver = webdriver.Chrome(service=service, options=chrome_options)
file_path = "D:/python projects/resolver/pythonProject1/QE-index.html"
driver.get(file_path)


def get_cell_value(row, col):
    table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='test-6-div']//table"))
        )

        # Get the cell value
    cell = table.find_element(By.XPATH, f".//tbody/tr[{row + 1}]/td[{col + 1}]")
    return cell.text


driver.maximize_window()
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
)

# Assert that the email input is present
assert email_input is not None, "Email input not found"
time.sleep(5)

password_input = driver.find_element(By.XPATH, "//input[@id='inputPassword']")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Assert that the password input and login button are present
assert password_input is not None, "Password input not found"
assert login_button is not None, "Login button not found"

# Enter email and password
email_input.send_keys("test@example.com")
password_input.send_keys("password")

time.sleep(5)

test_2_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "test-2-div"))
    )
driver.execute_script("arguments[0].scrollIntoView();", test_2_div)

time.sleep(3)
# Find all list items in the test 2 div
list_items = test_2_div.find_elements(By.CLASS_NAME, "list-group-item")

# Assert that there are three values in the list group
assert len(list_items) == 3, f"Expected 3 list items, but found {len(list_items)}"

# Assert that the second list item's value is "List Item 2"
# Assert that the second list item's value contains "List Item 2"
second_list_item_text = list_items[1].text
assert "List Item 2" in second_list_item_text, f"Expected 'List Item 2' in '{second_list_item_text}'"

# Assert that the second list item's badge value is 6
second_list_item_badge = list_items[1].find_element(By.CLASS_NAME, "badge")
assert second_list_item_badge.text == "6", f"Expected badge value '6', but found '{second_list_item_badge.text}'"

test_3_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "test-3-div"))
    )
driver.execute_script("arguments[0].scrollIntoView();", test_3_div)

time.sleep(3)

dropdown_button = test_3_div.find_element(By.ID, "dropdownMenuButton")
assert dropdown_button.text.strip() == "Option 1", f"Expected default selected value 'Option 1', but found '{dropdown_button.text.strip()}'"


try:
    dropdown_button.click()
except ElementClickInterceptedException:
    # Handle if the dropdown button is not clickable, try an alternative method
    driver.execute_script("arguments[0].click();", dropdown_button)

# Locate the option to select
option_3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Option 3']"))
    )
option_3.click()

    # Assert that "Option 3" is now selected
assert dropdown_button.text == "Option 3", f"Expected selected value 'Option 3', but found '{dropdown_button.text.strip()}'"

test_4_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "test-4-div"))
    )
driver.execute_script("arguments[0].scrollIntoView();", test_4_div)

# Locate the first and second buttons within test 4 div
buttons = test_4_div.find_elements(By.TAG_NAME, "button")
first_button = buttons[0]
second_button = buttons[1]

# Assert that the first button is enabled
assert first_button.is_enabled(), "First button is not enabled"

# Assert that the second button is disabled
assert not second_button.is_enabled(), "Second button is not disabled"

test_5_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "test-5-div"))
    )
driver.execute_script("arguments[0].scrollIntoView();", test_5_div)

# Wait for the button to be displayed (with a maximum timeout of 20 seconds)
button = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "test5-button"))
    )

# Click the button
button.click()

# Wait for the success message to be displayed
success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "test5-alert"))
    )

# Assert that the success message is displayed
assert success_message.is_displayed(), "Success message is not displayed"

# Assert that the button is now disabled
assert not button.is_enabled(), "Button is not disabled after clicking"

test_6_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "test-6-div"))
    )
driver.execute_script("arguments[0].scrollIntoView();", test_6_div)

# Use the method to find the value of the cell at coordinates (2, 2)
cell_value = get_cell_value(2, 2)
print(f"The value of the cell at coordinates (2, 2) is: {cell_value}")

# Assert that the value of the cell is "Ventosanzap"
assert cell_value == "Ventosanzap", f"Expected cell value 'Ventosanzap', but found '{cell_value}'"


