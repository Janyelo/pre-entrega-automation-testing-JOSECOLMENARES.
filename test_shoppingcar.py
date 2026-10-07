import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_agregar_al_carrito():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()

        boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        boton_agregar.click()

        boton_remover = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        
        assert boton_remover.text == "Remove"

        badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge_carrito.text == "1"

        
        icono_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        icono_carrito.click()

        
        item_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name")

        assert item_en_carrito.text == "Sauce Labs Backpack"

        print("OK test")

    finally:
        driver.quit()