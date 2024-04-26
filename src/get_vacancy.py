
import requests

from src.abc_class import AbstractApiHh


class GetVacancy(AbstractApiHh):
    """Класс для работы с платформой hh.ru
    """
    def connect_to_api(self):
        """
        Подключение к HH.ru
        """
        response = requests.get('https://api.hh.ru/vacancies')
        return response.status_code

    def get_vacancy_from_api(self, user_vacancy):
        """Получение информации о вакансиях"""
        if self.connect_to_api() != 200:
            raise NameError(f"\n Ошибка подключения")
        else:
            params = {'text': f'NAME:{user_vacancy}', 'area': 113, 'per_page': 100}
            response = requests.get('https://api.hh.ru/vacancies', params=params)
            return response.json()
