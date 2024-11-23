from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Step 1: Navigate to the e-commerce site and log in
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("[data-test='login-button']")

    # Step 2: Add a product to the cart
    product_name = "Sauce Labs Backpack"
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    print(f"'{product_name}' added to the cart!")

    # Step 3: Navigate to the cart
    page.click(".shopping_cart_link")

    # Step 4: Initiate checkout
    page.click("[data-test='checkout']")
    page.fill("[data-test='firstName']", "Usama")
    page.fill("[data-test='lastName']", "Qamar")
    page.fill("[data-test='postalCode']", "12345")
    page.click("[data-test='continue']")

    # Step 5: Validate order summary
    summary_product_name = page.locator(".inventory_item_name").text_content()
    summary_product_price = page.locator(".inventory_item_price").text_content()

    assert product_name in summary_product_name, "Product name in order summary does not match!"
    assert summary_product_price == "$29.99", "Product price in order summary does not match!"
    print("Order summary validation successful!")

    # Step 6: Complete checkout
    page.click("[data-test='finish']")
    success_message = page.locator("[data-test='complete-header']").text_content().strip()

    # Dynamic Validation
    assert success_message, "No success message displayed!"
    print(f"Success Message: {success_message}")

    print("Checkout completed successfully!")

    browser.close()
