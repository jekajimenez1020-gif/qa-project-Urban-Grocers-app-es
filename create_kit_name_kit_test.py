import sender_stand_request
import data

# función  para obtener el token de autorización al crear un nuevo usuario
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json().get("authToken")
    return auth_token

# Función que modifica el cuerpo de la solicitud "name"
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["Name"] = name
    return current_body

# Función para pruebas positivas del parametro "name" en la creación de un kit
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]
    print(f"Código de respuesta: {response.status_code}")
    print(f"Token: {response.json().get('authToken', 'No token')}")

# Función de prueba negativa
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
    print(f"Código de respuesta: {response.status_code}")
    print(f"Token: {response.json().get('authToken', 'No token')}")
    print(f"Mensaje completo: {response.json()['message']}")

# Función de prueba negativa cuando el parametro "name" no existe
def negative_assert_missing_name_parameter(kit_body):
    auth_token = get_new_user_token()
    print(f"Token generado: {auth_token}")
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["name"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Prueba 1. Creación de un nuevo kit
# El parámetro "Name" contiene 1 caracteres
def test_create_kit_1_letter_in_name_get_error_response():
    positive_assert( {"name": "a"})

# Prueba 2. Creación de un nuevo kit
# El parámetro "Name" contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_error_response():
    positive_assert({"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})

# Prueba 3. Error Creación de un nuevo kit
# El parámetro "Name" contiene 0 caracteres
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400( {"name": ""})

# Prueba 4. Error Creación de un nuevo kit
# El parámetro "Name" contiene 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400({"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"})

# Prueba 5. Creación de un nuevo kit
# El parámetro "Name" contiene un string con caracteres especiales
def test_create_kit_has_especial_symbol_in_name_get_error_response():
    positive_assert({"name": "\"№%@\","})

# Prueba 6. Creación de un nuevo kit
# El parámetro "Name" contiene palabras con espacios
def test_create_kit_has_space_in_name_get_error_response():
    positive_assert({"name" : "A Aaa"})

# Prueba 7. Creación de un nuevo kit
# El parámetro "Name" contiene un string de números
def test_create_kit_has_numbers_in_name_get_error_response():
    positive_assert({"name" : "123"})

# Prueba 8. Error Creación de un nuevo kit
# El parámetro "Name" no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    print(f"Status code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    negative_assert_missing_name_parameter(kit_body)

# Prueba 9. Error Creación de un nuevo kit
# El parámetro "Name" contiene números
def test_create_kit_has_number_type_in_name_get_error_response():
    negative_assert_code_400({"name" : 123})