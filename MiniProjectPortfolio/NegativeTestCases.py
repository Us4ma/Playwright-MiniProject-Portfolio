from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Step 1: Navigate to the login page
    page.goto("https://www.saucedemo.com/")

    # Step 2: Enter invalid credentials
    page.fill("#user-name", "invalid_user")
    page.fill("#password", "invalid_password")
    page.click("[data-test='login-button']")

    # Step 3: Validate error message
    error_message = page.locator("[data-test='error']").text_content()
    print(f"Error Message: {error_message.strip()}")
    assert "Username and password do not match any user in this service" in error_message, "Error message mismatch!"

    browser.close()
