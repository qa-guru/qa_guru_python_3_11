from dataclasses import dataclass

import pytest


def test_with_param():
    pass


def test_with_matrix_param(browser, test_user):
    pass


def test_with_param_marks(browser, test_user):
    pass


# parametrize it
def browser():
    pass


def test_with_parametrized_fixture(browser):
    pass


def test_with_indirect_parametrization(browser):
    assert browser == "Chrome"


personal = pytest.mark.parametrize("account", ["personal"], indirect=True)


@personal
def test_with_account(account):
    pass




@dataclass
class User:
    id: int
    name: str
    age: int
    description: str

    # def __repr__(self):
    #     return f"{self.name} ({self.id})"


user1 = User(id=1, name="Mario", age=32, description="something " * 10)
user2 = User(id=2, name="Wario", age=62, description="else " * 10)


def show_user(user):
    return f"{user.name} ({user.id})"


@pytest.mark.parametrize("user", [user1, user2], ids=show_user)
def test_users(user):
    print()
