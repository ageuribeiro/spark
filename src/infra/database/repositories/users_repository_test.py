import pytest
from sqlalchemy import text
from src.infra.database.settings.connection import DBConnectionHandler
from .users_repository import UsersRespository


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensive Test")
def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 51

    users_repository = UsersRepository()
    users_repository.insert_user(
        mocked_first_name,
        mocked_last_name,
        mocked_age
    )

    query = """
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
        AND age = {}
    """.format(
        mocked_first_name,
        mocked_last_name,
        mocked_age
    )

    response = connection.execute(text(query))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age


    connection.execute(
        text(
            f"""
            DELETE FROM users
            WHERE id = '{registry.id}'

            """
        )
    )

    connection.commit()


@pytest.mark.skip(reason="Sensive Test")
def test_select_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 51

    connection.execute(
        text(
            f"""
            INSERT INTO users (first_name, last_name, age)
            VALUES ('{mocked_first_name}', '{mocked_last_name}', {mocked_age})
            """
        )
    )

    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_first_name)

    assert users[0].first_name == mocked_first_name
    assert users[0].last_name == mocked_last_name
    assert users[0].age == mocked_age

    connection.execute(
        text(
            f"""
            DELETE FROM users
            WHERE first_name = '{mocked_first_name}'
            """
        )
    )

    connection.commit()
