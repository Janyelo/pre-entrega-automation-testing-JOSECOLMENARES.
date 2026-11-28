
import pytest
import pathlib
import base64
import pytest_html
  

from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {"x-api-key": "pub_783d5513e8da2f53809762c00c7af7c18f1af6d976edac9d063755fcddde21cc"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            carpeta = pathlib.Path("reports/screenshots")
            carpeta.mkdir(parents=True, exist_ok=True)
            archivo = carpeta / f"{item.name}.png"
            driver.save_screenshot(str(archivo))

            imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
            report.extra= [pytest_html.extras.png(imagen, name="screenshot")]