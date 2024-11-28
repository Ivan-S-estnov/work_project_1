import pytest

from src.integration_api.service import HeadHunterAPI


@pytest.fixture()
def hh_params_for_request():
    return HeadHunterAPI()


@pytest.fixture()
def example_answers_yes():
    return 'да'


@pytest.fixture()
def example_answers_no():
    return 'нет'


@pytest.fixture()
def example_answers_any():
    return ''


@pytest.fixture()
def example_answers_no2():
    return 'нет'


@pytest.fixture()
def keyword_for_get_vacancies():
    return 'python'


@pytest.fixture()
def keyword_for_get_vacancies1():
    return 'сантехник'


@pytest.fixture()
def part_response_for_request_hh():
    return {'name': 'Backend разработчик', 'link': 'https://hh.ru/vacancy/108828750', 'city': 'Москва',
            'salary_from': 90000, 'salary_to': None, 'currency': 'RUR', 'experience': 'От 1 года до 3 лет',
            'busy': 'Полная занятость', 'schedule': 'Полный день',
            'requirements': 'Знание SQL. Опыт проектирования БД от 1 года. Опыт работы с какой либо СУБД (желательно '
                            'PostgreSQL). Навыки алгоритмизации. ',
            'duties': 'Анализ задач и проектирование под них БД. Разработка бизнес логики под требования компании '
                      '(имеется собственная платформа). Внедрение и поддержка новых...'}


@pytest.fixture()
def part_response_for_request_hh1():
    return {'name': 'Бармен в ресторан', 'link': 'https://hh.ru/vacancy/109468226', 'city': 'Алматы',
            'salary_from': 500000, 'salary_to': None, 'currency': 'KZT', 'experience': 'От 1 года до 3 лет',
            'busy': 'Полная занятость', 'schedule': 'Полный день',
            'requirements': 'Опыт работы от 2-х лет. Работоспособный (бережное отношение к ресторанному имуществу). '
                            'Пунктуальный. Желание развиваться и расти вместе с нами!',
            'duties': 'Приготовление напитков из барного меню ресторана. Разлив пива. Уход за барной стойкой.'}


@pytest.fixture()
def part_response_for_request_hh2():
    return {'name': 'Слесарь - сантехник', 'link': 'https://hh.ru/vacancy/109181768', 'city': 'Алматы',
            'salary_from': 250000, 'salary_to': None, 'currency': 'KZT', 'experience': 'Нет опыта',
            'busy': 'Полная занятость', 'schedule': 'Полный день', 'requirements': 'Знание города.',
            'duties': 'Мелкосрочный ремонт, связанный с ремонтом канализации, водопровода и отопления.'}


def test_params(hh_params_for_request, example_answers_yes, example_answers_no,
                example_answers_any, example_answers_no2):
    hh_params_for_request.params = example_answers_yes
    assert hh_params_for_request.params == {'text': '', 'per_page': 20}
    hh_params_for_request.params = example_answers_any
    assert hh_params_for_request.params == {'text': '', 'per_page': 20}
    hh_params_for_request.params = example_answers_no
    assert hh_params_for_request.params == {'text': '', 'per_page': 20, 'only_with_salary': True}
    hh_params_for_request.params = example_answers_no2
    assert hh_params_for_request.params == {'text': '', 'per_page': 20, 'only_with_salary': True}
