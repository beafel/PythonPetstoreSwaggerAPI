import pytest
import requests


# 2 - Teste de API - utilize https://petstore.swagger.io
base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}

# 2.1 - Cadastre o gato "Bichento"
def test_create_pet():
    # Configurações : arquivo pet_post.json
    # Resultados esperados
    status_code = 200
    pet_id = 1245
    pet_name = 'Bichento'
    tags_name = 'ginger'

    # Executa
    response = requests.post(url=f'{base_url}/pet',
                             data=open('json/pet_post.json', 'rb'),
                             headers=headers
                             )
    # Valida
    print(response)
    response_body = response.json()
    print(response_body)

    assert response.status_code == status_code
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['tags'][0]['name'] == tags_name


# 2.2 - Cadastre a usuária "Hermione Granger"
def test_create_user():
    # Configurações : arquivo user_post.json
    user_id = 784512
    # Resultados esperados
    status_code = 200
    code = 200
    type = 'unknown'
    message = str(user_id)

    # Executa
    response = requests.post(url=f'{base_url}/user',
                             data=open('json/user_post.json', 'rb'),
                             headers=headers
                             )
    # valida
    print(response)
    response_body = response.json()
    print(response_body)

    assert response.status_code == status_code
    assert response_body['code'] == code
    assert response_body['type'] == type
    assert response_body['message'] == message


# 2.3 - Venda o "Bichento" para a "Hermione Granger"
def test_create_store_order_pet():
    # Configurações : arquivo store_order_post.json
    order_id = 9
    # Resultados esperados
    status_code = 200
    pet_id = 1245
    status = 'placed'
    complete = True

    # Executa
    response = requests.post(url=f'{base_url}/store/order',
                             data=open('json/store_order_post.json', 'rb'),
                             headers=headers
                             )
    # Valida
    print(response)
    response_body = response.json()
    print(response_body)

    assert response.status_code == status_code
    assert response_body['id'] == order_id
    assert response_body['petId'] == pet_id
    assert response_body['status'] == status
    assert response_body['complete'] == complete


def test_update_pet():
    # Configurações : arquivo pet_put.json
    # Resultados esperados
    status_code = 200
    pet_id = 1245
    pet_name = 'Bichento'
    tags_name = 'ginger'

    # Executa
    response = requests.post(url=f'{base_url}/pet',
                             data=open('json/pet_put.json', 'rb'),
                             headers=headers
                             )
    # Valida
    print(response)
    response_body = response.json()
    print(response_body)

    assert response.status_code == status_code
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['tags'][0]['name'] == tags_name


# 2.4 - Consulte o status do animal após a venda
def test_research_pet():
    # Configurações
    pet_id = 1245
    # Resultados esperados
    status_code = 200
    pet_name = 'Bichento'
    category_name = 'Cat'
    status = 'sold'

    # Executa
    response = requests.get(url=f'{base_url}/pet/{pet_id}',
                            headers=headers
                            )
    # Valida
    print(response)
    response_body = response.json()
    print(response_body)

    assert response.status_code == status_code
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == category_name
    assert response_body['status'] == status


# 2.5 - Consulte a ordem de venda do animal
def test_research_store_order_pet():
    # Configurações
    order_id = 9
    # Resultados esperados
    status_code = 200
    pet_id = 1245
    status = 'placed'
    complete = True

    # Executa
    response = requests.get(url=f'{base_url}/store/order/{order_id}',
                            headers=headers
                            )
    # Valida
    print(response)
    response_body = response.json()
    print(response_body)

    assert response.status_code == status_code
    assert response_body['petId'] == pet_id
    assert response_body['status'] == status
    assert response_body['complete'] == complete
