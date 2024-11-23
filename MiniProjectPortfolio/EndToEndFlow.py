from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Step 1: Log in to the site
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("[data-test='login-button']")
    print("Login successful!")
    sleep(2)
    # Step 2: Dynamically add products to the cart

    product_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
    for product in product_names:
        formatted_name = product.lower().replace(" ", "-").replace("'", "")
        locator = f"[data-test='add-to-cart-{formatted_name}']"
        page.click(locator)
        print(f"'{product}' added to the cart!")

        sleep(2)

        # Step 3: Navigate to the cart

    page.click(".shopping_cart_link")

    cart_items = page.locator(".cart_item")

    # Validate the cart contents

    for idx,product_name in enumerate (product_names):
        cart_product_name = cart_items.nth(idx).locator(".inventory_item_name").text_content()
        assert cart_product_name == product_name, f"Expected '{product_name}', but found '{cart_product_name}'"
    print("Cart Validation successful!")

    sleep(2)

    # Step 4: Proceed to checkout
    page.click("[data-test='checkout']")
    page.fill("[data-test='firstName']","Usama")
    page.fill("[data-test='lastName']", "Qamar")
    page.fill("[data-test='postalCode']", "12345")
    page.click("[data-test = 'continue']")

    # Validate the order summary

    summary_items = page.locator(".cart_item")
    for idx,product_name in enumerate(product_names):
        summary_product_name = summary_items.nth(idx).locator(".inventory_item_name").text_content()
        assert summary_product_name == product_name, f"Expected '{product_name}', but found '{summary_product_name}'!"
    print("Order summary validation successful!")

    sleep(2)

    # Step 5: Complete checkout
    page.click("[data-test='finish']")
    success_message = page.locator("[data-test='complete-header']").text_content()
    assert success_message == "Thank you for your order!", "Order completion failed!"
    print("Checkout completed successfully")

    sleep(2)

    browser.close()