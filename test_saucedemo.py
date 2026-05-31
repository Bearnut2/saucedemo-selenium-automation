import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class SauceDemoComprehensiveTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.base_url = "https://www.saucedemo.com/"
        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.quit()

    def helper_login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    # ==========================================================================
    # --- POSITIVE SKENARIO (01 - 20) ---
    # ==========================================================================

    def test_01_login_success_standard(self):
        self.helper_login("standard_user", "secret_sauce")
        self.assertIn("inventory.html", self.driver.current_url)

    def test_02_login_success_problem_user(self):
        self.helper_login("problem_user", "secret_sauce")
        self.assertIn("inventory.html", self.driver.current_url)

    def test_03_login_success_glitch_user(self):
        self.helper_login("performance_glitch_user", "secret_sauce")
        self.assertIn("inventory.html", self.driver.current_url)

    def test_04_login_success_error_user(self):
        self.helper_login("error_user", "secret_sauce")
        self.assertIn("inventory.html", self.driver.current_url)

    def test_05_login_success_visual_user(self):
        self.helper_login("visual_user", "secret_sauce")
        self.assertIn("inventory.html", self.driver.current_url)

    def test_06_catalog_add_first_item(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(badge, "1")

    def test_07_catalog_add_second_item(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(badge, "2")

    def test_08_catalog_remove_item_direct(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(len(badges), 0)

    def test_09_catalog_sort_az(self):
        self.helper_login("standard_user", "secret_sauce")
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("az")
        item_text = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        self.assertEqual(item_text, "Sauce Labs Backpack")

    def test_10_catalog_sort_za(self):
        self.helper_login("standard_user", "secret_sauce")
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("za")
        item_text = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        self.assertEqual(item_text, "Test.allTheThings() T-Shirt (Red)")

    def test_11_catalog_sort_low_to_high(self):
        self.helper_login("standard_user", "secret_sauce")
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("lohi")
        price_text = self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        self.assertEqual(price_text, "$7.99")

    def test_12_catalog_sort_high_to_low(self):
        self.helper_login("standard_user", "secret_sauce")
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("hilo")
        price_text = self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        self.assertEqual(price_text, "$49.99")

    def test_13_catalog_open_detail_via_image(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "item_4_img_link").click()
        self.assertIn("inventory-item.html", self.driver.current_url)

    def test_14_catalog_open_detail_via_title(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "item_4_title_link").click()
        self.assertIn("inventory-item.html", self.driver.current_url)

    def test_15_cart_open_page(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.assertIn("cart.html", self.driver.current_url)

    def test_16_cart_delete_item(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(items), 0)

    def test_17_cart_continue_shopping(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "continue-shopping").click()
        self.assertIn("inventory.html", self.driver.current_url)

    def test_18_checkout_open_form(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.assertIn("checkout-step-one.html", self.driver.current_url)

    def test_19_checkout_verify_overview_page(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        self.assertIn("checkout-step-two.html", self.driver.current_url)

    def test_20_checkout_complete_purchase(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()
        time.sleep(1)
        thanks = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        self.assertEqual(thanks, "Thank you for your order!")

    # ==========================================================================
    # --- NEGATIVE SKENARIO (21 - 40) ---
    # ==========================================================================

    def test_21_login_failed_wrong_password(self):
        self.helper_login("standard_user", "wrong_pass")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Username and password do not match", error)

    def test_22_login_failed_wrong_username(self):
        self.helper_login("wrong_user", "secret_sauce")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Username and password do not match", error)

    def test_23_login_failed_empty_username(self):
        self.helper_login("", "secret_sauce")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Username is required", error)

    def test_24_login_failed_empty_password(self):
        self.helper_login("standard_user", "")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Password is required", error)

    def test_25_login_failed_all_empty(self):
        self.helper_login("", "")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Username is required", error)

    def test_26_login_failed_locked_user(self):
        self.helper_login("locked_out_user", "secret_sauce")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Sorry, this user has been locked out.", error)

    def test_27_security_bypass_inventory_directly(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("You can only access '/inventory.html' when you are logged in", error)

    def test_28_security_bypass_cart_directly(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("You can only access '/cart.html' when you are logged in", error)

    def test_29_security_bypass_checkout_directly(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("You can only access '/checkout-step-one.html' when you are logged in", error)

    def test_30_cart_checkout_empty_items(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.assertIn("checkout-step-one.html", self.driver.current_url)

    def test_31_checkout_failed_empty_firstname(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("First Name is required", error)

    def test_32_checkout_failed_empty_lastname(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Last Name is required", error)

    def test_33_checkout_failed_empty_postal(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "continue").click()
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Postal Code is required", error)

    def test_34_checkout_failed_empty_first_and_last(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("First Name is required", error)

    def test_35_checkout_failed_empty_last_and_postal(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "continue").click()
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("Last Name is required", error)

    def test_36_checkout_failed_all_fields_empty(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "continue").click()
        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn("First Name is required", error)

    def test_37_checkout_cancel_at_form_page(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "cancel").click()
        self.assertIn("cart.html", self.driver.current_url)

    def test_38_checkout_cancel_at_overview_page(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        
        # Klik cancel pada halaman overview
        self.driver.find_element(By.ID, "cancel").click()
        
        # Beri jeda dinamis menunggu halaman kembali ke inventory.html
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("inventory.html")
        )
        self.assertIn("inventory.html", self.driver.current_url)

    def test_39_sidebar_logout(self):
        self.helper_login("standard_user", "secret_sauce")
        
        # 1. Klik tombol burger menu untuk membuka sidebar
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        
        # 2. Tunggu elemen logout tersedia di dalam DOM 
        logout_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "logout_sidebar_link"))
        )
        
        # 3. Gunakan JavaScript Click agar bypass animasi transisi CSS yang menjebak
        self.driver.execute_script("arguments[0].click();", logout_btn)
        
        # 4. Tunggu sampai URL berhasil kembali ke halaman login utama
        WebDriverWait(self.driver, 5).until(
            EC.url_to_be(self.base_url)
        )
        self.assertEqual(self.driver.current_url, self.base_url)

    def test_40_security_bypass_complete_page_directly(self):
        self.helper_login("standard_user", "secret_sauce")
        self.driver.get("https://www.saucedemo.com/checkout-complete.html")
        header = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        self.assertTrue(len(header) > 0)

if __name__ == '__main__':
    unittest.main()