import pytest
import httpx
from Features.presignIn import prerrequisito_iniciarSesion
    

@pytest.mark.asyncio
async def test_buscar_nota_existente(prerrequisito_crear_categoria):
    prerrequisito = await prerrequisito_crear_categoria
    print("\nRespuesta del prerrequisito:")
    print(prerrequisito)
    categoria_id = prerrequisito["id"]
    nombre_categoria = prerrequisito["nombre"]

    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/api/v1/categorias/{categoria_id}")

        print("\nRespuesta del servidor:")
        print(response.json())

        assert response.status_code == 200
        assert response.json()["nombre"] == nombre_categoria

