from src.infra.database.repositories.users_repository import UsersRepository
from src.data.uses_cases.user_register import UserRegister
from src.presentation.controllers.user_register_controller import UserRegisterController


def user_register_composer():
    repository = UsersRepository()
    use_case = UserRegister(repository)
    controller = UserRegisterController(use_case)

    return controller.handle
