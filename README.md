## 🚀 TESTING CON PYTEST

## Requerimientos

### 1. Instalar Python

En Windows: Descarga el instalador de Python desde [Aqui](https://www.python.org/downloads/windows/).

Asegúrate de marcar la casilla **"Add Python to PATH"** al comienzo de la instalación. Sigue las instrucciones del instalador para completar la instalación.

### 2. Instalar Entorno Virtual (obligatorio para instalar pytest y las dependencias)

Clona el repositorio y abre la terminal para introducir los siguientes comandos:

- Clonar el repo

` git clone https://github.com/jestebanv30/concesionario-coches-testing-pytest.git`

- En el directorio raiz del proyecto instala el paquete de virtualenv

```
  pip install virtualenv
```

- Crea un nuevo entorno virtual dentro de la carpeta llamado "venv"

```
  python -m venv venv
```

- Activar el entorno virtual

```
  . venv\Scripts\activate
  o (Bash)
  source venv/Scripts/activate
```

- Desactivar el entorno virtual

```
  deactivate
```

### 3. Instalar Dependencias

Asegúrate de que esté activado el entorno virtual. Verifica que tienes el archivo **"requirements.txt"** en el directorio de tu proyecto, luego ejecuta:

```
pip install -r requirements.txt
```

Esto instalará las dependencias necesarias para trabajar con pytest. Tambien puedes descargarlas de forma manual, una por una con el comando:

```
pip install <paquete a instalar>
```

### 5. Ejecutar pruebas con Pytest

Con el entorno virtual activado y las dependencias instaladas, puedes empezar a usar Pytest. Para instalar:

```
pip install pytest
```

- Verifica que Pytest está instalado correctamente

```
pytest --version
```

Para ejecutar las pruebas con Pytest, navega al directorio donde se encuentran tus archivos de prueba (.py) y ejecuta:

```
pytet post_cartest.py
```

Esto generará un reporte donde podrás comprobar el estado de tus pruebas.

Tener en cuenta que previamente tendrías que haber descargado el backend que está en mi repositorio: **"concesionario-coches-spring"**, y registrarle un usuario admin para que pueda realizar solicitud post y realizar pruebas referente a entradas y salidas esperadas.

Este usuario se establece en Feature/presignin.py y se obtiene el token que devuelve el servidor y es utilizado para realizar las pruebas en post_cartest.py

## Visual

video de youtube en miniatura en desarrollo

## Ejemplo básico

```javascript
import secrets
import httpx
import pytest

@pytest.mark.asyncio
async def test_positivo_crear_nota_correctamente():
    async with httpx.AsyncClient() as client:

        randomString = secrets.token_hex(5)
        nombreCategoria = f"Categoria_{randomString}"
        response = await client.post(
            "http://localhost:8000/api/v1/categorias",
            json={
                "nombre": nombreCategoria,
            }
        )

        print("Respuesta del servidor:")
        print(response.json())


        assert response.status_code == 200
        assert response.json()["nombre"] == nombreCategoria
        assert isinstance(response.json()["id"], str)
```

### Explicación

Este código es una prueba unitaria escrita para Python utilizando las bibliotecas httpx, pytest, y secrets, junto con el decorador **@pytest.mark.asyncio** para indicar que se trata de una prueba asíncrona.

La prueba verifica que una solicitud **HTTP POST** a una API para crear una nueva categoría se maneje correctamente. A continuación, se desglosa cada parte del código para entender su propósito y funcionamiento:

### Importaciones:

- **secrets**: Se utiliza para generar un string hexadecimal aleatorio, garantizando que cada prueba use un nombre de categoría único.
- **httpx**: Una biblioteca HTTP para Python que permite realizar solicitudes HTTP asíncronas. Es similar a requests pero con soporte completo para asyncio.
- **pytest**: Un marco de pruebas para Python que facilita la escritura de pequeñas pruebas, pero puede escalar para soportar pruebas funcionales complejas.

### Definición de la Prueba Asíncrona:

- **@pytest.mark.asyncio**: Un decorador de pytest que marca la función como una prueba asíncrona. Esto le dice a pytest que debe ejecutar la función de prueba en un bucle de eventos asyncio.
- **async def test_positivo_crear_nota_correctamente()**: Define una función de prueba asíncrona. El nombre de la función sigue la convención de nombrado de pytest, empezando con test\_, lo cual es necesario para que pytest reconozca automáticamente la función como una prueba.

### Cuerpo de la Prueba:

- **async with httpx.AsyncClient() as client:** Crea un cliente asíncrono usando httpx. Este cliente se utilizará para hacer solicitudes HTTP asíncronas dentro de un contexto que garantiza el cierre adecuado del cliente al finalizar la prueba.
- **randomString = secrets.token_hex(5)**: Genera un string hexadecimal aleatorio de 10 caracteres (5 bytes) para asegurar que el nombre de la categoría sea único en cada ejecución de la prueba.
- **nombreCategoria = f"Categoria\_{randomString}"**: Construye el nombre de la categoría combinando un prefijo estático con el string aleatorio generado.
- **response = await client.post(...)**: Realiza una solicitud POST asíncrona a la API, enviando un objeto JSON con el nombre de la categoría. await se utiliza para esperar que la solicitud se complete antes de continuar con la ejecución.
- **print(response.json())**: Imprime la respuesta de la API convertida a un objeto Python mediante el método **.json()**. Esto es útil para fines de depuración, para ver los datos que la API retorna en respuesta a la solicitud POST.

### Aserciones:

- **assert response.status_code == 200**: Verifica que el código de estado de la respuesta HTTP sea 200, indicando una operación exitosa.
- **assert response.json()["nombre"] == nombreCategoria**: Comprueba que el nombre de la categoría retornado por la API en el cuerpo de la respuesta coincide con el que se envió en la solicitud.
- **assert isinstance(response.json()["id"], str)**: Asegura que el id retornado en la respuesta es una cadena de caracteres (str). Esto verifica indirectamente que se creó una nueva categoría y que la API devolvió un identificador para ella.

### Testing con postman

Para testear los status code:

```
pm.test("Test status Code", function () {
    pm.expect(pm.response.code).to.eql(200);
});
```

Para crear strings aleatorios, y posteriormente guardar ese string en varibales de entorno:

```
function generateRandomString(length) {
    let result = '';
    let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

let randomString = generateRandomString(10);
pm.environment.set("randomString", randomString);
```
