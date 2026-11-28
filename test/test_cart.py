from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.card_page import CartPage
import pytest
from utils.reader import read_productos_json
from utils.logger import logger

def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    producto = read_productos_json()[0]
    print(producto)
    inventory_page.agregar_producto(producto["nombre"])
    inventory_page.ir_al_carrito()
    assert cart_page.obtener_nombre_producto() == producto["nombre"]
    logger.info("Nombre del primer producto en el carrito verificado correctamente")
    assert cart_page.obtener_precio_producto() == producto["precio"]
    logger.info("Precio del producto en el carrito verificado correctamente")
