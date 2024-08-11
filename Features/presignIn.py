import pytest
import httpx
import secrets

@pytest.fixture
async def prerrequisito_iniciarSesion():
    async with httpx.AsyncClient() as client:
        
        email = "juanesdev@gmail.com";
        password = "LKkiyqyw";

        response = await client.post(
            "http://localhost:8080/api/auth/sign-in", 
            json={
                "email": email,
                "password": password
            }
        )

        token = response.json()["token"]
        return {"token": token, "response": response}