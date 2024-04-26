from abc import ABC, abstractmethod


class AbstractApiHh(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_vacancy_from_api(self, param):
        pass


class AbstractJson(ABC):
    """Абстрактный класс для работы с JSON"""

    @abstractmethod
    def add_vacancies(self, vacancy):
        pass

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass
