from src.get_vacancy import GetVacancy
from src.json_save_vacancy import JsonSaveVacancy
from src.vacancy import Vacancy
from src.working_with_vacancies import filter_vacancies, get_vacancies_by_salary, get_top_vacancies


def main():

    user_vacancy = input("Введите название вакансии для поиска:\n")
    user_top_n = int(input("Введите количество ТОП вакансий для просмотра:\n"))
    user_keywords = input("Введите ключевые слова для фильтрации:\n").capitalize().split()
    user_salary = input("Укажите диапазон желаемой заработной платы через \"-\":\n")

    hh_api = GetVacancy()

    hh_vacancies = hh_api.get_vacancy_from_api(user_vacancy)

    file_json = JsonSaveVacancy('vacancy.json')
    file_json.add_vacancies(hh_vacancies)

    vacancies_list = Vacancy.get_list_vacancies(hh_vacancies["items"])

    filtering_vacancies = filter_vacancies(vacancies_list, user_keywords)

    range_vacancies = get_vacancies_by_salary(filtering_vacancies, user_salary)
    sorted_vacancies = sorted(range_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, user_top_n)

    print("Результаты по Вашему запросу:")
    print(top_vacancies)


if __name__ == '__main__':
    main()
