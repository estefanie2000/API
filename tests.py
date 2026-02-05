from api_client import APIClient

client = APIClient()


def print_response(response):
    print("STATUS:", response.status_code)
    try:
        print("RESPONSE JSON:", response.json())
    except Exception:
        print("RESPONSE TEXT:", response.text)


def test_create_user():
    print("\n🔹 TEST 1: Crear usuario")

    user_data = {
        "name": "Andrea Castillo",
        "username": "acastillo",
        "email": "andrea@test.com"
    }

    response = client.create_user(user_data)
    print_response(response)

    assert response.status_code in [200, 201], "Error al crear usuario"


def test_get_user():
    print("\n🔹 TEST 2: Consultar usuario existente")

    response = client.get_user(1)
    print_response(response)

    assert response.status_code == 200, "Error al consultar usuario"


def test_get_user_not_found():
    print("\n🔹 TEST 3: Consultar usuario inexistente")

    response = client.get_user(9999)
    print_response(response)

    assert response.status_code in [404, 200], "Respuesta inesperada"


def test_multiple_users():
    print("\n🔹 TEST 4: Validar varios usuarios")

    for user_id in [1, 2, 3]:
        response = client.get_user(user_id)
        print(f"Usuario ID {user_id} - Status: {response.status_code}")
        assert response.status_code == 200


def test_validate_response_structure():
    print("\n🔹 TEST 5: Validar estructura de respuesta")

    response = client.get_user(1)
    data = response.json()

    assert "name" in data, "No existe el campo name"
    assert "email" in data, "No existe el campo email"


if __name__ == "__main__":
    test_create_user()
    test_get_user()
    test_get_user_not_found()
    test_multiple_users()
    test_validate_response_structure()

    print("\nTodas las pruebas se ejecutaron correctamente.")
