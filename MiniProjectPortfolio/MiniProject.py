from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to the login page
    page.goto("https://www.saucedemo.com/")

    # Test Case 1: Valid Login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("[data-test='login-button']")
    assert "inventory.html" in page.url, "Valid login failed!"
    print("Login successful with valid credentials!")

    # Log out
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test='logout-sidebar-link']").scroll_into_view_if_needed()
    page.click("[data-test='logout-sidebar-link']")
    assert "saucedemo.com" in page.url, "Logout failed!"
    print("Logout successful!")

    # Test Case 2: Invalid Login
    page.fill("#user-name", "invalid_user")
    page.fill("#password", "wrong_password")
    page.click("[data-test='login-button']")
    error_message = page.text_content(".error-message-container")
    print(f"Error Message: {error_message.strip()}")
    assert "Username and password do not match" in error_message, "Invalid login error message not displayed!"
    print("Error message displayed as expected for invalid login!")

    browser.close()
