# x-api-key: pub_783d5513e8da2f53809762c00c7af7c18f1af6d976edac9d063755fcddde21cc

import requests
import pytest_check as check
from utils.logger import logger

def test_obtener_usuario(base_url,headers):
    url = f"{base_url}/users/2"

    response = requests.get(url,headers=headers)

    # NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 200
    logger.info(f"Codigo de respuesta: {codigo} - Peticion GET exitosa")

    # NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]
    logger.info(f"Tipo de contenido: {response.headers['Content-Type']} - Tipo de contenido valido")

    # NIVEL 3: ESTRUCTURA
    data = response.json()

    assert isinstance(data,dict) # Validar que el contenido sea un diccionario
    logger.info(f"Estructura de datos: {type(data)} - Estructura valida")
    assert "data" in data
    logger.info(f"Clave 'data' presente en la respuesta - Estructura valida")
    assert isinstance(data["data"],dict)
    logger.info(f"Estructura de datos 'data': {type(data['data'])} - Estructura valida")

    assert "id" in data["data"]

    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    # NIVEL 4: CONTENIDO
    assert data["data"]["id"] == 2
    logger.info(f"ID del usuario: {data['data']['id']} - Contenido valido")
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    logger.info("Contenido de la respuesta valido")

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2
    logger.info(f"Tiempo de respuesta: {response.elapsed.total_seconds()} segundos - Tiempo de respuesta valido")

def test_crear_usuario(base_url,headers):
    url = f"{base_url}/users/"

    usuario = {
        "email":"jose.montezuma@bue.edu.ar",
        "first_name":"Jose",
        "last_name":"Montezuma",
        "job":"Instructor"
    }

    response = requests.post(url,headers=headers,json=usuario)

    # NIVEL 1
    assert response.status_code == 201
    logger.info(f"Codigo de respuesta: {response.status_code} - Peticion POST exitosa")
    # NIVEL 2
    assert "application/json" in response.headers["Content-Type"]
    logger.info(f"Tipo de contenido: {response.headers['Content-Type']} - Tipo de contenido valido")

    # NIVEL 3
    data = response.json()
    check.is_in("email",data) #assert "email" in data
    check.is_in("first_name",data) #assert "first_name" in data
    check.is_in("last_name",data) #assert "last_name" in data
    check.is_in("id",data) #assert "id" in data

    # NIVEL 4
    check.equal(data["email"],usuario["email"]) # assert data["email"] == usuario["email"]
    check.equal(data["first_name"],usuario["first_name"]) # assert data["first_name"] == usuario["first_name"]

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2
    logger.info(f"Tiempo de respuesta: {response.elapsed.total_seconds()} segundos - Tiempo de respuesta valido")

def test_eliminar_usuario(base_url,headers):
    url = f"{base_url}/users/2"
    
    response = requests.delete(url,headers=headers)
    
    # NIVEL 1: STATUS CODE
    assert response.status_code == 204
    logger.info(f"Codigo de respuesta: {response.status_code} - Peticion DELETE exitosa")
    
    # NIVEL 2: HEADERS
    assert "Content-Type" not in response.headers
    logger.info(f"Tipo de contenido: {response.headers.get('Content-Type')} - Tipo de contenido valido")

    # NIVEL 3 Y 4: ESTRUCTURA Y CONTENIDO
    assert len(response.content) == 0
    logger.info("Estructura y contenido de la respuesta validos")
    
    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2
    logger.info(f"Tiempo de respuesta: {response.elapsed.total_seconds()} segundos - Tiempo de respuesta valido")

"""
{
    "data":{
        "id":2,
        "email":"jose.montezuma@bue.edu.ar",
        "nombre":"Jose",
        "apellido":"Montezuma"
    },
    "support":{}
}
"""