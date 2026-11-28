# Automatización de Pruebas E2E y API - SauceDemo

Proyecto final de automatización de pruebas funcionales End-to-End (E2E) y pruebas de API desarrollado en Python. Implementa el patrón de diseño **Page Object Model (POM)** junto con **Data-Driven Testing (CSV/JSON)** utilizando **Pytest**, **Selenium WebDriver**, **Requests** y **Behave (BDD)**.

##  Propósito del Proyecto

Este proyecto tiene como objetivo automatizar las pruebas funcionales End-to-End (E2E) y de servicios API de la plataforma de comercio electrónico **SauceDemo** (https://www.saucedemo.com/), aplicando buenas prácticas de arquitectura de software como **Page Object Model (POM)** y **Data-Driven Testing**.

A través de suites automatizadas con **Pytest** y escenarios **BDD (Behave)**, se verifican los siguientes flujos críticos del sistema:

- **Autenticación de usuarios (UI y BDD):** Validación de inicio de sesión exitoso y manejo de errores ante credenciales inválidas o campos vacíos mediante datos parametrizados (`users.csv`) y escenarios Gherkin.
- **Verificación del catálogo de productos:** Comprobación de carga del inventario, visualización de artículos y validación de atributos clave.
- **Interacción con el carrito de compras:** Selección y agregado de productos desde fuentes externas (`products.json`), verificación de nombres, precios y estado dentro del carrito.
- **Pruebas de API REST:** Validación automatizada de endpoints, códigos de estado HTTP y estructura de respuestas mediante `requests`.
- **Trazabilidad y reportes:** Registro detallado paso a paso en archivos de log (`logs/`) y generación automática de reportes visuales de ejecución en formato HTML (`reports/reporte.html`).


##  Tecnologías y Librerías Utilizadas

* **Python 3.x**
* **Selenium WebDriver:** Automatización de interacciones en navegador web.
* **Pytest:** Framework principal de ejecución de pruebas unitarias, funcionales y de API.
* **Pytest-HTML:** Generación de reportes visuales de ejecución en formato `.html`.
* **Pytest-Check / Pytest-Rerunfailures:** Aserciones múltiples y reintentos automáticos ante fallos intermitentes.
* **Behave (Gherkin):** Automatización de escenarios bajo enfoque BDD (Behavior-Driven Development).
* **Requests:** Ejecución de pruebas automatizadas sobre servicios REST API.

## Estructura del Proyecto

```text
entrega_final/
├── data/                   # Archivos de datos externos (users.csv, products.json)
├── features/               # Escenarios Gherkin (.feature), steps/ y environment.py (Behave)
├── logs/                   # Registros detallados de ejecución generados por el logger
├── pages/                  # Clases Page Object Model (login_page.py, inventory_page.py, card_page.py)
├── reports/                # Reportes HTML generados tras la ejecución de Pytest
├── test/                   # Suites de pruebas automatizadas (API, Login, Inventario, Carrito)
├── utils/                  # Utilidades auxiliares (lectores CSV/JSON en reader.py y logger.py)
├── conftest.py             # Configuración global y fixtures de Selenium para Pytest
├── pytest.ini              # Configuración de ejecución y generación automática de reporte HTML
├── requirements.txt        # Dependencias del proyecto
└── readme.md               # Documentación del proyecto