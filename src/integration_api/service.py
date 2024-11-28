from src.integration_api.class_for_api import VacanciesAPI
# Импортируем функцию urljoin для построения абсолютного url-адреса
from urllib.parse import urljoin
# Импортируем библиотеку requests для отправки http-запросов
import requests


class HeadHunterAPI(VacanciesAPI):
    """Класс для получения вакансий с сервиса hh.ru по API."""

    def __init__(self):
        super().__init__()
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._base_url = 'https://api.hh.ru'
        self._params = {'text': '', 'per_page': 20}
        self._vacancies = []

    @property
    def params(self):
        """Геттер параметров для отправки запроса на сервис.
        Предоставляет доступ к атрибуту для изменения его значения."""
        return self._params

    @params.setter
    def params(self, salary_agreement):
        """Сеттер параметров для отправки запроса на сервис. Изменяет значение атрибута."""
        if salary_agreement == 'нет':
            self._params['only_with_salary'] = True
        else:
            pass

    def get_vacancies(self, keyword: str, pages_count: int = 99) -> list:
        """Получает ответ на get-запрос и записывает его в список вакансий при подключении к API сервиса с
        вакансиями."""
        url = urljoin(self._base_url, 'vacancies')
        self._params['text'] = keyword

        for page in range(pages_count + 1):
            self._params['page'] = page
            response = requests.get(url, headers=self._headers, params=self._params)
            response.raise_for_status()

            for item in response.json()['items']:
                if item['salary'] is None or item['salary'] == {}:
                    item['salary'] = {'from': None, 'to': None, 'currency': None}
                self._vacancies.append({'name': item['name'], 'link': item['alternate_url'],
                                        'city': item['area']['name'], 'salary_from': item['salary']['from'],
                                        'salary_to': item['salary']['to'], 'currency': item['salary']['currency'],
                                        'experience': item['experience']['name'],
                                        'busy': item['employment']['name'], 'schedule': item['schedule']['name'],
                                        'requirements': str(item['snippet']['requirement']).
                                       replace('<highlighttext>', '').replace('</highlighttext>', ''),
                                        'duties': str(item['snippet']['responsibility']).
                                       replace('<highlighttext>', '').replace('</highlighttext>', '')})
        return self._vacancies

    def __str__(self):
        """Выводим для пользователя наименование сервиса, в который отправлен запрос."""
        return f"HeadHunter"
