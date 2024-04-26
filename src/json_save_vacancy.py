import json

from abc_class import AbstractJson


class JsonSaveVacancy(AbstractJson):
    """
    Класс для работы с json файлом
    """

    def __init__(self, filename):
        self.filename = filename

    def add_vacancies(self, value):
        """
       Функция добавляет данные в файл
        """
        with open(self.filename, 'a', encoding='UTF-8') as file:
            json.dump(value, file, indent=2, ensure_ascii=False)
            file.write('\n')

    def open_file(self):
        """
        Открывает файл для чтения
        :return: open file
        """
        with open(self.filename, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def delete_vacancy(self):
        """
        Функция удаляет данные из файла
        """
        with open(self.filename, 'w'):
            pass
