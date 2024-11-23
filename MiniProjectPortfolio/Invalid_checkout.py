from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) #Open Browser
    page = browser.new_page() #Open Page

    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("[data-test='login-button']") #clicking the login button the idea here is that we are getting data-test as a locator

    page.click("[data-test='add-to-cart-sauce-labs-backpack']") #same idea, adding sauce labs backpack
    page.click(".shopping_cart_link")

    page.click("[data-test='checkout']")
    page.fill("[data-test='firstName']", "Usama")
    page.fill("[data-test='lastName']", "")
    page.fill("[data-test='postalCode']","12345")
    page.click("[data-test='continue']")

    error_message = page.locator("[data-test='error']").text_content()
    print(f"Error Message:{error_message.strip()}")

    assert  "Error: Last Name is required" in error_message, "Error message mismatch!"

    browser.close()