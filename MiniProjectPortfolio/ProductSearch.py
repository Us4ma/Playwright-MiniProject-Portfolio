from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Step 1: Navigate to the e-commerce site
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("[data-test='login-button']")

    # Step 2: Search for a product (simulate search by filtering products)
    product_name = "Sauce Laps Backpack"
    product_locator = page.locator("[data-test='item-4-title-link']")

    assert product_locator.is_visible(), f"Product '{product_name}' not found!"

    # Step 3: Validate product details
    product_price_locator = page.locator(".inventory_item_price", has_text="$29.99")
    assert product_price_locator.is_visible(), f"Price for '{product_name}' not matching!"

    print(f"Product '{product_name}' found with the correct price!")

    browser.close()
