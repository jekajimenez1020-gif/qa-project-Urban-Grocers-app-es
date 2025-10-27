import configuration
import requests
import data

# Solicitud para crear un usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers)

# Solicitud para crear un kit
def post_new_client_kit(kit_body,auth_token):
    headers = data.headers.copy()
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers) # Agrega la autorización
