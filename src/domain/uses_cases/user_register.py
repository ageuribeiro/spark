from abc import ABC, abstractmethod
from typing import Dict


class UserRegister(ABC):

    @abstractmethod
    def register_user(self, user_data: Dict) -> Dict:
        pass
