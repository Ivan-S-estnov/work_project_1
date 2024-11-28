# Импортируем библиотеку string для удобной фильтрации по ключевому слову
from string import punctuation
# Импортируем класс для работы и отправки запросов на сервис по подбору вакансий
from src.integration_api.service import HeadHunterAPI
# Импортируем функцию для определения окончания слова "сайт"
from src.func.help_func import end_word_question
# Импортируем класс для преобразования информации с сервиса в список вакансий
from src.vacancy.class_vacancy import Vacancy
# Импортируем класс для работы со списком вакансий
from src.vacancy.vacancies_list import VacanciesProcessing
# Импортируем класс для работы с JSON файлами
from src.write_json.work_with_data import JSONManager


# Функция для взаимодействия с пользователем
def user_interaction():
    """
    Функцию для взаимодействия с пользователем через консоль. Данная функция реализует:

    Ввод поискового запроса для запроса вакансий из со всех поддерживаемых программой сервисов вакансий;
    Получение количества вакансий по зарплате (количество запрашивает у пользователя);
    Получение вакансии с ключевым словом в описании.

    """
    # Создание экземпляров классов для работы с API всех сайтов с вакансиями, которые доступны программе, и добавление
    # их в словарь для выбора варианта работы программы с запросом по всем сервисам
    all_services = []
    services_for_requests = {}
    user_services_list = []
    number_var = 0
    hh_api = HeadHunterAPI()
    all_services.append(hh_api)


    for services in all_services:
        number_var += 1
        services_for_requests[str(number_var)] = services

    number_var += 1
    services_for_requests[str(number_var)] = all_services

    def work_options():
        var_user_request = ''
        for key, values in services_for_requests.items():
            if values == all_services:
                values = f'Со всех поддерживаемых сервисов ?'
            var_user_request += f'{key}. {values.__str__()} \n'
        return var_user_request

    print(f'\nВас приветствует приложение для получения и сохранения в файл информации по вакансиям с '
          f'{end_word_question(len(all_services))} {", ".join(map(str, [x for x in all_services]))}. Если Вы в момент '
          f'запроса приложения не укажите верхний или нижний порог по заработной плате для фильтрации списка полученных'
          f' с {end_word_question(len(all_services))} вакансий, или не укажите оба значения, программа все равно '
          f'отсортирует вакансии по верхнему порогу. Если не укажите количество вакансий для вывода в топ, выведется '
          f'по умолчания топ 20.')

    salary_agreement = input('\nЗапросить информацию по вакансиям без конкретно указанной зарплаты (по договоренности)?'
                             ' Введите: "да" или "нет": ').lower()
    while salary_agreement != 'да' or salary_agreement != 'нет':
        if salary_agreement == 'да' or salary_agreement == 'нет':
            break
        else:
            print("\nВы ввели некорректное значение. Введите корректный ответ.")
            salary_agreement = input('\nЗапросить информацию по вакансиям без конкретно указанной зарплаты (по '
                                     'договоренности)? Введите: "да" или "нет": ').lower()

    user_request = input(f"\nВы хотите получить список вакансий с: \n{work_options()} \nВведите цифру выбранного "
                         f"варианта от 1 до {len(services_for_requests)}: ")
    user_request_no = ('нет', 'Нет', 'no', 'No', '')

    while user_request not in services_for_requests:
        print("\nВы ввели некорректное значение. Введите корректный ответ.\n")
        user_request = input(f"Вы хотите получить список вакансий с: \n{work_options()} \nВведите цифру выбранного "
                             f"варианта от 1 до {len(services_for_requests)}: ")

    if int(user_request) != len(services_for_requests):
        user_services_list = [(services_for_requests[user_request])]
        services_for_requests.popitem()
        del services_for_requests[user_request]
        while services_for_requests != {}:
            if services_for_requests == {}:
                print("\nВы указали все доступные для программы сайты для запроса вакансий. Перейдем к запросу.")
                break
            if len(user_services_list) > 1:
                user_request_2 = \
                    input(f'\nВы хотите получить вакансии с {end_word_question(len(user_services_list))} '
                          f'{", ".join(map(str, [x for x in user_services_list]))}. '
                          f'Вы можете добавить к списку получаемых вакансий также вакансии с '
                          f'{", ".join(map(str, [x + ". " + y.__str__() for x, y in services_for_requests.items()]))}. '
                          f'Если хотите получить вакансии с какого-либо еще сайта с вакансиями из предложенных, '
                          f'введите цифру соответствующую сервису. Если нет - введите "нет" или нажмите '
                          f'просто "Enter": ')
            else:
                user_request_2 = \
                    input(f'\nВы хотите получить вакансии с {end_word_question(len(user_services_list))} '
                          f'{"".join(map(str, [x for x in user_services_list]))}. '
                          f'Вы можете добавить к списку получаемых вакансий также вакансии с '
                          f'{", ".join(map(str, [x + ". " + y.__str__() for x, y in services_for_requests.items()]))}. '
                          f'Если хотите получить вакансии с какого-либо еще сайта с вакансиями из предложенных, '
                          f'введите цифру соответствующую сервису. Если нет - введите "нет" или нажмите '
                          f'просто "Enter": ')
            if user_request_2 in user_request_no:
                print(f'\nВы отказались добавить для программы оставшиеся предложенные сервисы для запроса '
                      f'вакансий. Вы хотите получить вакансии с {end_word_question(len(user_services_list))} '
                      f'{"".join(map(str, [x for x in user_services_list]))}. Перейдем к запросу.')
                break
            if user_request_2 in services_for_requests:
                user_services_list.append(services_for_requests[user_request_2])
                del services_for_requests[user_request_2]
            else:
                print("\nВы ввели некорректное значение. Введите корректный ответ.")
        else:
            print("\nВы указали все доступные для программы сайты для запроса вакансий. Перейдем к запросу.")
    else:
        user_services_list.extend(all_services)
        print("\nВы указали все доступные для программы сайты для запроса вакансий. Перейдем к запросу.")

    search_query = input("\nВведите поисковый запрос: ")
    data_for_vacancies = []
    for service in user_services_list:
        service.params = salary_agreement
        data_for_vacancies.extend(service.get_vacancies(search_query))

    vacancies_list = Vacancy.cast_to_object_list(data_for_vacancies)

    user_file_name = input('\nСписок с вакансиями по запросу будет сохранен в файл. По умолчанию файл будет назван '
                           '"file_with_data". Вы можете задать имя файла или нажать "Enter" и пропустить этот шаг: ')

    json_file = JSONManager(user_file_name)
    json_file.file_name = user_file_name
    json_file.write_to_file(vacancies_list)
    data_load = json_file.load_from_file()
    data_load_for_vac = Vacancy.cast_to_object_list(data_load)
    vacancies_for_processing = VacanciesProcessing(data_load_for_vac)

    filter_words = input("\nВведите ключевые слова для фильтрации вакансий: ")
    if filter_words in punctuation or filter_words == '':
        filtered_vacancies = vacancies_for_processing.vacancies
    else:
        filtered_vacancies = vacancies_for_processing.filter_vacancies(vacancies_list, filter_words)

    try:
        salary_min = int(input('\nВведите нижнюю границу диапазона зарплат в найденных вакансиях. '
                               'Либо нажмите "Enter", если не хотите её указывать: '))
        if salary_min < 0:
            print('\nЭто не приемлемо. Вы же хотите зарабатывать? Для сортировки будет '
                  'взято то же число, что Вы ввели, только с положительным знаком. ')
            salary_min = abs(salary_min)
    except ValueError:
        salary_min = 0

    try:
        salary_max = int(input('\nВведите верхнюю границу диапазона зарплат в найденных вакансиях. '
                               'Либо нажмите "Enter", если не хотите её указывать: '))
        if salary_max < 0:
            print('\nЭто не приемлемо. Вы же хотите зарабатывать? Для сортировки будет '
                  'взято то же число, что Вы ввели, только с положительным знаком. ')
            salary_max = abs(salary_max)
        if salary_min > salary_max > 0:
            ValueError('Значение верхней границы диапазона зарплат не может быть меньше значения нижней границы. Для '
                       'корректной фильтрации вакансий по зарплате, программа возьмет в качестве верхней границы '
                       'введенное Вами значение нижней границы. А в качестве нижней, наоборот, введенное Вами значение'
                       ' нижней границы.')
            new_salary_min = salary_max
            new_salary_max = salary_min
            salary_min = new_salary_min
            salary_max = new_salary_max
    except ValueError:
        salary_max = 0

    try:
        top_n = int(input('\nВведите количество вакансий для вывода в топ. '
                          'Либо нажмите "Enter", если не хотите его указывать: '))
        if top_n < 0:
            print('\nВведите количество вакансий для вывода в топ не может быть отрицательным или. '
                  'Для ранжирования по убывания будет взято то же число, что Вы и ввели, только с положительным '
                  'знаком.')
            top_n = abs(top_n)
        if top_n == 0:
            print('\nКоличество вакансий для вывода в топ не может быть ноль. Будет взято значение по умолчанию - 20.')
            top_n = 20
    except ValueError:
        top_n = 20

    ranged_vacancies = vacancies_for_processing.get_vacancies_by_salary(filtered_vacancies, salary_min, salary_max)
    sorted_vacancies = vacancies_for_processing.sort_vacancies(ranged_vacancies)
    top_vacancies = vacancies_for_processing.get_top_vacancies(sorted_vacancies, top_n)
    json_file.write_to_file_top_n_vac(top_vacancies)

    print("\n\n")
    for vacancy in top_vacancies:
        print(vacancy, end="\n\n\n")

    print(f'ТОП-{top_n} отсортированных по заработной плате вакансии выведенных на экран будут перезаписаны в файл '
          f'{json_file.file_name} формата json.')

    print(f'\nРабота приложения завершена. Спасибо, всего доброго!')
    exit()


user_interaction()