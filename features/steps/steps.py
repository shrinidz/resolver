import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
)

def setup_driver(context):
    service = ChromeService("D:/chromedriver/chromedriver-win64/chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.get("D:/python projects/resolver/pythonProject1/QE-index.html")
    context.driver.implicitly_wait(10)  # Adding implicit wait

@given('I am on the home page')
def step_impl(context):
    if not hasattr(context, "driver"):
        setup_driver(context)

@then('I should see email address and password inputs and the login button')
def step_impl(context):
    try:
        email_input = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        time.sleep(5)
        password_input = context.driver.find_element(By.XPATH, "//input[@id='inputPassword']")
        login_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
        assert email_input.is_displayed(), "Email input not displayed"
        assert password_input.is_displayed(), "Password input not displayed"
        assert login_button.is_displayed(), "Login button not displayed"
    except (NoSuchElementException, TimeoutException) as e:
        raise AssertionError(f"Element not found: {e}")

@when('I enter email "{email}" and password "{password}"')
def step_impl(context, email, password):
    try:
        email_input = context.driver.find_element(By.XPATH, "//input[@type='email']")
        password_input = context.driver.find_element(By.XPATH, "//input[@id='inputPassword']")
        email_input.send_keys(email)
        password_input.send_keys(password)
    except NoSuchElementException as e:
        raise AssertionError(f"Element not found: {e}")

@then('the login form should be submitted')
def step_impl(context):
    try:
        login_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
    except NoSuchElementException as e:
        raise AssertionError(f"Element not found: {e}")

@then('I should see 3 items in the list group in test 2 div')
def step_impl(context):
    try:
        test_2_div = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "test-2-div"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView();", test_2_div)
        list_items = test_2_div.find_elements(By.CLASS_NAME, "list-group-item")
        time.sleep(5)
        assert len(list_items) == 3, f"Expected 3 list items, but found {len(list_items)}"
    except (NoSuchElementException, TimeoutException) as e:
        raise AssertionError(f"Element not found: {e}")

@then('the second list item\'s text should be "List Item 2"')
def step_impl(context):
    try:
        test_2_div = context.driver.find_element(By.ID, "test-2-div")
        list_items = test_2_div.find_elements(By.CLASS_NAME, "list-group-item")
        second_list_item_text = list_items[1].text
        assert "List Item 2" in second_list_item_text, f"Expected 'List Item 2' in '{second_list_item_text}'"
    except NoSuchElementException as e:
        raise AssertionError(f"Element not found: {e}")

@then('the second list item\'s badge value should be 6')
def step_impl(context):
    try:
        test_2_div = context.driver.find_element(By.ID, "test-2-div")
        second_list_item = test_2_div.find_elements(By.CLASS_NAME, "list-group-item")[1]
        badge_value = second_list_item.find_element(By.CLASS_NAME, "badge").text
        assert badge_value == "6", f"Expected badge value '6', but found '{badge_value}'"
    except NoSuchElementException as e:
        raise AssertionError(f"Element not found: {e}")

@then('"Option 1" should be the default selected value in the dropdown')
def step_impl(context):
    try:
        test_3_div = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "test-3-div"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView();", test_3_div)
        dropdown_button = test_3_div.find_element(By.ID, "dropdownMenuButton")
        time.sleep(5)
        assert dropdown_button.text.strip() == "Option 1", f"Expected 'Option 1', but found '{dropdown_button.text.strip()}'"
    except (NoSuchElementException, TimeoutException) as e:
        raise AssertionError(f"Element not found: {e}")

@when('I select "Option 3" from the dropdown')
def step_impl(context):
    try:
        test_3_div = context.driver.find_element(By.ID, "test-3-div")
        dropdown_button = test_3_div.find_element(By.ID, "dropdownMenuButton")
        dropdown_button.click()
        option_3 = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Option 3']"))
        )
        option_3.click()
    except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
        raise AssertionError(f"Element interaction failed: {e}")

@then('"Option 3" should be the selected value in the dropdown')
def step_impl(context):
    try:
        test_3_div = context.driver.find_element(By.ID, "test-3-div")
        dropdown_button = test_3_div.find_element(By.ID, "dropdownMenuButton")
        assert dropdown_button.text == "Option 3", f"Expected 'Option 3', but found '{dropdown_button.text.strip()}'"
    except NoSuchElementException as e:
        raise AssertionError(f"Element not found: {e}")

@then('the first button in test 4 div should be enabled')
def step_impl(context):
    try:
        test_4_div = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "test-4-div"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView();", test_4_div)
        buttons = test_4_div.find_elements(By.TAG_NAME, "button")
        time.sleep(5)
        first_button = buttons[0]
        assert first_button.is_enabled(), "First button is not enabled"
    except NoSuchElementException as e:
        raise AssertionError(f"Element not found: {e}")

@then('the second button in test 4 div should be disabled')
def step_impl(context):
    try:
        test_4_div = context.driver.find_element(By.ID, "test-4-div")
        buttons = test_4_div.find_elements(By.TAG_NAME, "button")
        second_button = buttons[1]
        assert not second_button.is_enabled(), "Second button is not disabled"
    except NoSuchElementException as e:
        raise AssertionError(f"Element not found: {e}")

@when('I wait for the button to be displayed in test 5 div')
def step_impl(context):
    try:
        test_5_div = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "test-5-div"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView();", test_5_div)
        time.sleep(5)
        context.button = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "test5-button"))
        )
    except (NoSuchElementException, TimeoutException) as e:
        raise AssertionError(f"Element not found: {e}")

@when('I click the button in test 5 div')
def step_impl(context):
    try:
        context.button.click()
    except ElementClickInterceptedException as e:
        raise AssertionError(f"Element click failed: {e}")

@then('I should see a success message in test 5 div')
def step_impl(context):
    try:
        success_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "test5-alert"))
        )
        assert success_message.is_displayed(), "Success message is not displayed"
    except (NoSuchElementException, TimeoutException) as e:
        raise AssertionError(f"Element not found: {e}")

@then('the button in test 5 div should be disabled')
def step_impl(context):
    try:
        assert not context.button.is_enabled(), "Button is not disabled after clicking"
    except NoSuchElementException as e:
        raise AssertionError(f"Element not found: {e}")

@when('I get the value of the cell at row {row}, column {col}')
def step_impl(context, row, col):
    row = int(row)
    col = int(col)
    context.cell_value = get_cell_value(context.driver, row, col)

@then('the cell value should be "Ventosanzap"')
def step_impl(context):
    try:
        assert context.cell_value == "Ventosanzap", f"Expected cell value 'Ventosanzap', but found '{context.cell_value}'"
    except AssertionError as e:
        raise AssertionError(f"Assertion failed: {e}")

def get_cell_value(driver, row, col):
    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='test-6-div']//table"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", table)
        time.sleep(5)
        cell = table.find_element(By.XPATH, f"//tbody/tr[{row + 1}]/td[{col + 1}]")
        return cell.text
    except (NoSuchElementException, TimeoutException) as e:
        raise AssertionError(f"Element not found: {e}")
