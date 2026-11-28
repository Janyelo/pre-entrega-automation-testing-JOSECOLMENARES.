from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
from utils.reader import read_users_csv
from utils.logger import logger


def test_inventory_page(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    products = inventory_page.obtener_productos()

    assert len(products) > 0

    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
    logger.info("Nombre del primer producto verificado correctamente")
    assert inventory_page.obtener_precio_primer_producto() == "$29.99"
    logger.info("Precio del primer producto verificado correctamente")
    assert inventory_page.menu_visible()
    logger.info("Menú visible correctamente")
    assert inventory_page.filtro_visible()
    logger.info("Filtro visible correctamente")
