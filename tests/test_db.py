from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='teste', email='teste@teste.com', password='teste')

    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'teste@teste.com')
    )

    assert result.username == user.username
    assert result.email == user.email
    assert result.password == user.password
