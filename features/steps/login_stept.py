from behave import given,when,then
from pages.login_page import LoginPage
from utils.logger import logger

@given("que el usuario se encuentre en la pagina del login")
def step_usuario_en_login(context):
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)

@when('ingresa en los campos de datos "{usuario}" y "{password}"')
def step_ingresar_credenciales(context,usuario,password):
    if usuario == "VACIO":
        usuario = ""

    if password == "VACIO":
        password = ""

    context.usuario = usuario
    context.password = password

@when("hace click en el boton de login")
def step_click_login(context):
    context.login_page.login(context.usuario, context.password)

@then("deberia ingresar al inventario")
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url
    logger.info("Login exitoso, se ingreso al inventario correctamente")

@then('deberia mostrase el mensaje de error "{mensaje}"')
def step_validar_mensaje_error(context,mensaje):
    error = context.login_page.obtener_mensaje_error()
    print(error)
    assert mensaje in error, f"Se esperaba '{mensaje}', pero se obtuvo '{error}'"
    logger.info("Mensaje de error verificado correctamente")