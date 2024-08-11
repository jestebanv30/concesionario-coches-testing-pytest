import httpx
import pytest
import random
import string

from Features.presignIn import prerrequisito_iniciarSesion

@pytest.mark.asyncio
async def test_positivo_crear_coche(prerrequisito_iniciarSesion):
    async with httpx.AsyncClient() as client:
        token_response = await prerrequisito_iniciarSesion
        token = token_response["token"]

        reference = f"Cartest_{''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 10)))}"
        price = round(random.uniform(1, 9999999999.99), 2)
        model_year = random.randint(1990, 2023)
        color = random.choice(["Negro", "Blanco", "Rojo", "Azul"])
        horsepower = random.randint(101, 1000)
        number_door = random.choice([2, 4])
        engine_displacement = random.randint(1, 999999)
        transmission = random.choice(["Transmisión Manual", "Transmisión automática"])
        fuel_type = random.choice(["Gasolina", "Diesel"])
        number_seat = random.randint(2, 8)
        traction = random.choice(["Tracción delantera", "Tracción trasera", "Tracción a las cuatro ruedas"])
        steering = random.choice(["Dirección de piñón y cremallera", "Dirección asistida eléctricamente", "Dirección asistida hidráulicamente"])
        category = random.choice(["Automóvil", "Camioneta", "Deportivo"])
        stock = random.randint(1, 100)
        image_path = f"https://evaldostesting.com/images/{random.randint(1, 100)}.jpg"

        response = await client.post(
            "http://localhost:8080/api/cars",
            json={
                "carBrandId": 1,
                "reference": reference,
                "price": price,
                "modelYear": model_year,
                "color": color,
                "horsepower": horsepower,
                "numberDoor": number_door,
                "engineDisplacement": engine_displacement,
                "transmission": transmission,
                "fuelType": fuel_type,
                "numberSeat": number_seat,
                "traction": traction,
                "steering": steering,
                "category": category,
                "stock": stock,
                "imagePath": image_path
            },
            headers={"Authorization": f"Bearer {token}"}  # Incluir el token en las cabeceras
        )

        print("Respuesta del servidor:")
        print(response.json())

        # Asserts
        # Verificamos que el status sea 201 "created"
        assert response.status_code == 201

        # Verificamos que los campos que se guardaron sean los mismos que enviamos
        assert response.json()["reference"] == reference
        assert response.json()["modelYear"] == model_year
        assert response.json()["color"] == color
        assert response.json()["horsepower"] == horsepower
        assert response.json()["numberDoor"] == number_door
        assert response.json()["engineDisplacement"] == engine_displacement
        assert response.json()["transmission"] == transmission
        assert response.json()["fuelType"] == fuel_type
        assert response.json()["numberSeat"] == number_seat
        assert response.json()["traction"] == traction
        assert response.json()["steering"] == steering
        assert response.json()["category"] == category
        assert response.json()["stock"] == stock
        assert response.json()["imagePath"] == image_path

        # Verificamos que el campo "id" sea un integer no null
        assert isinstance(response.json()["codeCar"], int)

@pytest.mark.asyncio
async def test_negativo_crear_coche_null(prerrequisito_iniciarSesion):
    async with httpx.AsyncClient() as client:
        
        token_response = await prerrequisito_iniciarSesion
        token = token_response["token"]

        response = await client.post(
            "http://localhost:8080/api/cars",
            json={
                "carBrandId": None, #null
            },
            headers={"Authorization": f"Bearer {token}"}  # Incluir el token en las cabeceras
        )

        print("Respuesta del servidor: ")
        print(response.json())

        #Asserts
        assert response.status_code == 400

@pytest.mark.asyncio
async def test_negativo_crear_coche_con_string_vacio(prerrequisito_iniciarSesion):
    async with httpx.AsyncClient() as client:
        
        token_response = await prerrequisito_iniciarSesion
        token = token_response["token"]

        response = await client.post(
            "http://localhost:8080/api/cars",
            json={
                "nombre": "", #null
            },
            headers={"Authorization": f"Bearer {token}"}  # Incluir el token en las cabeceras
        )

        print("Respuesta del servidor: ")
        print(response.json())

        #Asserts
        assert response.status_code == 400
        assert response.json()["detail"], str