from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Step 1: Log in to the e-commerce site
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("[data-test='login-button']")

    # Step 2: Add two products to the cart
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("[data-test='add-to-cart-sauce-labs-bike-light']")
    print("Two products added to the cart!")

    # Step 3: Navigate to the cart
    page.click(".shopping_cart_link")

    # Step 4: Remove one product from the cart
    page.click("[data-test='remove-sauce-labs-bike-light']")
    print("One product removed from the cart!")

    # Step 5: Validate remaning product
    remaining_product_name = page.locator(".inventory_item_name").text_content()
    remaining_product_price = page.locator(".inventory_item_price").text_content()

    assert remaining_product_name == "Sauce Labs Backpack", "Remaining product name does not match!"
    assert remaining_product_price == "$29.99", "Remaining product price does not match!"
    print("Cart validation successful after removing a product!")

    browser.close()
