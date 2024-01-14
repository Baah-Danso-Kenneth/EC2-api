import pytest
from core.user.models import User

data_user = {
    "username": "tester_user",
    "email": "testing@gmail.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "test_password"
}


@pytest.fixture
def user(db):
    return User.objects.create_user(**data_user)