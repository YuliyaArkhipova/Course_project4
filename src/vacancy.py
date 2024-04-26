class Vacancy:
    """Класс для работы с вакансиями
    """

    def __init__(self, name_vacancy: str, city: str, salary_from: int, salary_to: int, requirement: str, url: str, ):
        self.name_vacancy = name_vacancy
        self.city = city

        if salary_from:
            self.salary_from = salary_from
        else:
            self.salary_from = 0

        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0
        self.requirement = requirement
        self.url = url

    def __repr__(self):
        """
        Магический метод для отображения вакансии для пользователя
        """
        if self.salary_from == 0 and self.salary_to == 0:
            return (f'\nНазвание вакансии: {self.name_vacancy}\n'
                    f'Город: {self.city}\n'                    
                    f'Заработная плата не указана\n'
                    f'Требования: {self.requirement}\n'
                    f'Cсылка на HH.ru: {self.url}\n')
        elif self.salary_from == 0 and self.salary_to != 0:
            return (f'\nНазвание вакансии: {self.name_vacancy}\n'
                    f'Город: {self.city}\n'                    
                    f'Заработная плата: до {self.salary_to}\n'
                    f'Требования: {self.requirement}\n'
                    f'Cсылка на HH.ru: {self.url}\n')
        elif self.salary_from != 0 and self.salary_to == 0:
            return (f'\nНазвание вакансии: {self.name_vacancy}\n'
                    f'Город: {self.city}\n'                    
                    f'Заработная плата: от {self.salary_from}\n'
                    f'Требования: {self.requirement}\n'
                    f'Cсылка на HH.ru: {self.url}\n')
        else:
            return (f'\nНазвание вакансии: {self.name_vacancy}\n'
                    f'Город: {self.city}\n'
                    f'Заработная плата: {self.salary_from} - {self.salary_to}\n'
                    f'Требования: {self.requirement}\n'
                    f'Cсылка на HH.ru: {self.url}\n')

    def __lt__(self, other):
        """
        Магический метод для сравнения ЗП
        """
        if self.salary_from < other.salary_from:
            return True

    @classmethod
    def get_list_vacancies(cls, vacancies):
        list_vacancies = []
        for vacancy in vacancies:
            if vacancy.get('salary'):
                list_vacancies.append(cls(vacancy.get('name'),
                                          vacancy.get('area').get('name'),
                                          vacancy.get('salary').get('from'),
                                          vacancy.get('salary').get('to'),
                                          vacancy.get('snippet').get('requirement'),
                                          vacancy.get('alternate_url')
                                          ))
            else:
                list_vacancies.append(cls(vacancy.get('name'),
                                          vacancy.get('area').get('name'),
                                          0,
                                          0,
                                          vacancy.get('snippet').get('requirement'),
                                          vacancy.get('alternate_url')
                                          ))
        return list_vacancies
