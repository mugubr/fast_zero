from http import HTTPStatus


def test_read_root_should_return_ok_and_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'teste',
            'password': 'teste',
            'email': 'teste@teste.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'teste',
        'email': 'teste@teste.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'teste',
                'email': 'teste@teste.com',
            }
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'teste',
        'email': 'teste@teste.com',
    }


def test_read_user_should_return_404(client):
    response = client.get(
        '/users/2',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'teste2',
            'email': 'teste2@teste2.com',
            'password': 'teste2',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'teste2',
        'email': 'teste2@teste2.com',
        'id': 1,
    }


def test_update_user_should_return_404(client):
    response = client.put(
        '/users/2',
        json={
            'id': 2,
            'username': 'teste2',
            'password': 'teste',
            'email': 'teste2@teste2.com',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete(
        '/users/1',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_should_return_404(client):
    response = client.delete(
        '/users/2',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
