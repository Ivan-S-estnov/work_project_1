class Vacancy:
    """Класс для работы с вакансией."""

    # Указываем в специальном атрибуте допустимый набор атрибутов
    __slots__ = ('_name', '_url', '_area', '_salary_min', '_salary_max', '_currency', '_experience',
                 '_requirements', '_responsibility')

    def __init__(self, name: str, url: str, area: str | None, salary_min: int | None,
                 salary_max: int | None, currency: str | None, experience: str | None, requirements: str | None,
                 responsibility: str | None) -> None:
        self._name = name
        self._url = url
        self._area = area
        self._salary_min = salary_min
        self._salary_max = salary_max
        self._currency = currency
        self._experience = experience
        self._requirements = requirements
        self._responsibility = responsibility

    @property
    def name(self) -> str:
        """Геттер названия вакансии.
        Предоставляет доступ к атрибуту для изменения его значения."""
        return self._name

    @property
    def url(self) -> str:
        """Геттер ссылки на вакансию. Предоставляет доступ к атрибуту для изменения его значения."""
        return self._url

    @property
    def area(self) -> str | None:
        """Геттер города, указанного в вакансии. Предоставляет доступ к атрибуту для изменения его значения."""
        return self._area

    @property
    def salary_min(self) -> int | None:
        """Геттер минимальной зарплаты, указанной в вакансии.
        Предоставляет доступ к атрибуту для изменения его значения."""
        return self._salary_min

    @property
    def salary_max(self) -> int | None:
        """Геттер максимальной зарплаты, указанной в вакансии. Предоставляет доступ к атрибуту для изменения его
        значения."""
        return self._salary_max

    @property
    def currency(self) -> str | None:
        """Геттер валюты, указанной в вакансии. Предоставляет доступ к атрибуту для изменения его значения."""
        return self._currency

    @property
    def experience(self) -> str:
        """Геттер опыта работы, требуемого от соискателя. Предоставляет доступ к атрибуту для изменения его значения."""
        return self._experience

    @property
    def requirements(self) -> str | None:
        """Геттер требований к вакансии. Предоставляет доступ к атрибуту для изменения его значения."""
        return self._requirements

    @property
    def responsibility(self) -> str | None:
        """Геттер обязанностей, указанных в вакансии. Предоставляет доступ к атрибуту для изменения его значения."""
        return self._responsibility

    @classmethod
    def cast_to_object_list(cls, data_for_vacancies):
        """Преобразование набора данных в список объектов."""

        vacancies_list = []
        for data in data_for_vacancies:
            attributes = [data.get('name'),
                          data.get('link'),
                          data.get('city'),
                          data.get("salary_from", 0) or 0,
                          data.get("salary_to", 0) or 0,
                          data.get('currency'),
                          data.get('experience'),
                          data.get('requirements'),
                          data.get('duties')]

            vacancy = Vacancy(*attributes)
            vacancies_list.append(vacancy)

        return vacancies_list

    def __str__(self):
        """Понятное отображение вакансии."""
        lst_out = [f"Вакансия\n"]
        name_k = ['Название вакансии', 'Ссылка на вакансию', 'Город', 'Зарплата от', 'Зарплата до', 'Валюта',
                  'Опыт работы', 'Требования', 'Обязанности']

        vac_value = []
        for atr in Vacancy.__slots__:
            x = Vacancy.__getattribute__(self, atr)
            if x is None or x == "None" or x == 0:
                x = 'Не указано'
            vac_value.append(f"{x}")
        vac_dict = dict(zip(name_k, vac_value))
        buffer_vac_dict = vac_dict.copy()
        del buffer_vac_dict['Обязанности']
        del buffer_vac_dict['Требования']
        for key, value in vac_dict.items():
            if key == 'Требования' or key == 'Обязанности':
                buffer_vac_dict['Описание вакансии'] = vac_dict['Требования']
            if vac_dict['Зарплата до'] == 0:
                buffer_vac_dict['Зарплата до'] = 'Не указано'
        for x, y in buffer_vac_dict.items():
            lst_out.append(f'{x}: {y}')
        str_out = "\n".join(lst_out)
        return str_out
    