def filter_vacancies(list_vacancies, user_keywords):
    """
    Функция для фильтрации вакансий по ключевому слову, полученному от пользователя
    """
    filtered_vacancies = []
    for vacancy in list_vacancies:
        for word in user_keywords:
            if word in str(vacancy):
                filtered_vacancies.append(vacancy)
                break
    if len(filtered_vacancies) != 0:
        return filtered_vacancies
    else:
        return f'Вакансии не найдены'


def get_vacancies_by_salary(filtered_vacancies, user_salary):
    """
    Функция для получения вакансий по зарплате
    """
    ranged_vacancies = []
    if user_salary == "":
        user_salary = f"Зарплата не указана"
    else:
        for vacancy in filtered_vacancies:
            if user_salary != 0:
                ranged_vacancies.append(vacancy)
        return ranged_vacancies


def get_top_vacancies(range_vacancies, user_top_n):
    """
    Функция для получения топовых вакансий
    """
    return range_vacancies[:user_top_n]
