from abc import ABC, abstractmethod


class WorkWithData(ABC):
    """Абстрактный класс для работы с файлами, хранящими данные о вакансиях."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def write_to_file(self, raw_vacancies_list: list[dict]):
        """Добавляет список вакансий в JSON файл."""
        pass

    @abstractmethod
    def load_from_file(self):
        """Получает данные из файла и преобразовывает их в словарь вакансий."""
        pass

    @abstractmethod
    def delete_from_file(self):
        """Удаляет информацию о вакансиях."""
        pass
