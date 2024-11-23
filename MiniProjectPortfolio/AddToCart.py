from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("[data-test='login-button']")

    # Step, Add to cart
    product_name = "Sauce Labs Backpack"
    add_to_cart_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    print(f"'{product_name}' added to the cart! ")
    
    #Step 3: Navigating to the Cart
    page.click(".shopping_cart_link")
    
    #Step 4: Validating cart contents

    cart_product_name = page.locator(".inventory_item_name").text_content()
    cart_product_price = page.locator(".inventory_item_price").text_content()

    assert product_name in cart_product_name, "Product name in cart does not match!"
    assert cart_product_price == "$29.99", "Product price in cart does not match!"
    print("Cart Validation successful!")
    browser.close()
    