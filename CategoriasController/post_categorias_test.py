import secrets
import httpx
import pytest

@pytest.mark.asyncio
async def test_positivo_crear_nota_correctamente():
    async with httpx.AsyncClient() as client:

        randomString = secrets.token_hex(5)
        nombreCategoria = f"Categoria_{randomString}"
        response = await client.post(
            "http://localhost:8000/api/v1/categorias",  # declaramos la ruta del endpoint
            json={                                      # declaramos el body que le vamos a entregar
                "nombre": nombreCategoria,
            }
        )

        print("Respuesta del servidor:")
        print(response.json())

        #Asserts
        assert response.status_code == 200        #verificamos que el status sea 200
        assert response.json()["nombre"] == nombreCategoria #verificamos que el nombre de la categoria sea el mismo que enviamos
        assert isinstance(response.json()["id"], str) # verificamos que el campo "id" sea un string no null



@pytest.mark.asyncio
async def test_negativo_crear_nota_null():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/v1/categorias",  
            json={                                     
                "nombre": None,
            }
        )

        print("Respuesta del servidor:")
        print(response.json())

        #Asserts
        assert response.status_code == 422 



@pytest.mark.asyncio
async def test_negativo_crear_nota_con_string_vacio():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/v1/categorias",  
            json={                                     
                "nombre": "",
            }
        )

        print("Respuesta del servidor:")
        print(response.json())

        #Asserts
        assert response.status_code == 409
        assert response.json()["detail"], str 

