# Anteproyecto de automatizacion de pruebas

## Propósito del Proyecto
Este proyecto tiene como objetivo automatizar las pruebas funcionales de la plataforma de comercio electrónico **SauceDemo** (https://www.saucedemo.com/). A través de un conjunto de scripts automatizados, se verifican flujos críticos del sistema como:
- Autenticación de usuarios (login exitoso y validaciones de interfaz).
- Visualización y verificación del catálogo de productos.
- Interacción con el carrito de compras (agregar/remover elementos, actualización del contador de la interfaz y presencia de productos en el carrito).
- Generación automática de reportes de ejecución en formato HTML.

---

## Tecnologías Utilizadas
- **Python 3.x**: Lenguaje de programación principal.
- **Selenium WebDriver**: Herramienta para la automatización de navegadores web.
- **pytest**: Framework de pruebas para la gestión y ejecución de casos de prueba.
- **pytest-html**: Plugin de pytest para generar reportes visuales en formato HTML.

---

## Instalación de Dependencias

1. **Clonar o descargar el repositorio** en tu equipo local.
2. **Abrir la terminal** en la carpeta raíz del proyecto (`preentrega`).
3. **Instalar las librerías necesarias** ejecutando el siguiente comando:

```bash
pip install pytest selenium pytest-html