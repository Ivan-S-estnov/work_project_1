from abc import ABC, abstractmethod

class VacanciesAPI(ABC):
    """Абстрактный класс для работы c API сервисами с вакансиями."""

    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, pages_count: int) -> list:
        """Получает ответ на get-запрос и записывает его в список вакансий при подключении к API сервисам с
        вакансиями."""
        pass