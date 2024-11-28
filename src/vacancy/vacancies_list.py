from src.vacancy.class_vacancy import Vacancy


class VacanciesProcessing:
    """Класс для работы с вакансиями."""

    def __init__(self, vacancies: list[Vacancy]) -> None:
        self._vacancies = vacancies

    def __len__(self) -> int:
        """Возвращает количество вакансий в списке."""
        return len(self.vacancies)

    @property
    def vacancies(self):
        """Геттер списка вакансий. Предоставляет доступ к атрибуту для изменения его значения."""
        return self._vacancies

    @staticmethod
    def filter_vacancy_by_keywords(vacancy: Vacancy, filter_words: str) -> bool:
        """Фильтрация по ключевому слову для одной вакансии."""
        for attr in vacancy.__slots__:
            x = Vacancy.__getattribute__(vacancy, attr)
            if filter_words in str(x):
                return True
        return False

    def filter_vacancies(self, vacancies: list[Vacancy], filter_words: str) -> list[Vacancy]:
        """Фильтрация по ключевому слову для всех вакансии."""

        filtered_vacancies = list(
            filter(
                lambda vacancy: self.filter_vacancy_by_keywords(vacancy, filter_words),
                vacancies
            )
        )

        return filtered_vacancies

    @staticmethod
    def get_vacancies_by_salary(filtered_vacancies: list[Vacancy], salary_min: int, salary_max: int) -> list[Vacancy]:
        """Возвращает вакансии с определенной зарплатной вилкой."""

        for vac_raw in filtered_vacancies:
            if vac_raw.currency == 'UZS':
                vac_raw._currency = 'рубли'
                try:
                    vac_raw._salary_min = round((vac_raw.salary_min / 133.36), -3)
                except ZeroDivisionError:
                    pass
                try:
                    vac_raw._salary_max = round((vac_raw.salary_max / 133.36), -3)
                except ZeroDivisionError:
                    pass
            if vac_raw.currency == 'KZT':
                vac_raw._currency = 'рубли'
                try:
                    vac_raw._salary_min = round((vac_raw.salary_min / 4.99), -3)
                except ZeroDivisionError:
                    pass
                try:
                    vac_raw._salary_max = round((vac_raw.salary_max / 4.99), -3)
                except ZeroDivisionError:
                    pass

        if salary_max < salary_min and salary_min >= 0:
            salary_max = max([int(vac.salary_max) for vac in filtered_vacancies if vac.salary_max != 0])

        if salary_max == 0 and salary_min == 0:
            salary_max = max([int(vac.salary_max) for vac in filtered_vacancies if vac.salary_max != 0])

        if salary_min == 0 and salary_max > 1:
            salary_min = 1

        ranged_vacancies = list(
            filter(
                lambda vacancy: salary_min <= vacancy.salary_min and salary_max >= vacancy.salary_max,
                filtered_vacancies
            )
        )

        return ranged_vacancies

    @staticmethod
    def sort_vacancies(ranged_vacancies: list[Vacancy]) -> list[Vacancy]:
        """Возвращает отсортированные по зарплате вакансии."""

        sorted_vacancies = sorted(ranged_vacancies, key=lambda vacancy: vacancy.salary_max, reverse=True)

        return sorted_vacancies

    @staticmethod
    def get_top_vacancies(sorted_vacancies: list[Vacancy], n: int) -> list[Vacancy]:
        """Возвращает топ n вакансий."""

        top_vacancies = sorted_vacancies[0:n]
        return top_vacancies

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии."""
        self.vacancies.append(vacancy)

    def del_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии."""
        self.vacancies.remove(vacancy)
            