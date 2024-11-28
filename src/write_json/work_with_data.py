# Импортируем библиотеку json для взаимодействия с JSON-объектами
import json
# Строим пути к файлам с учетом особенностей ОС.
import os
# Импортируем абстрактный класс объекта из файла base_class.py
from src.write_json.base_class import WorkWithData
# Импортируем класс вакансий из файла class_vacancy.py
from src.vacancy.class_vacancy import Vacancy


class JSONManager(WorkWithData):
    """Класс для работы с файлами формата JSON, хранящими данные о вакансиях."""

    def __init__(self, _file_name: str, file_name='file_with_data') -> None:

        self._file_name = file_name
        root_path_src_dir = os.path.split(os.path.abspath(__file__))
        root_path_main_dir = os.path.split(os.path.split(root_path_src_dir[0])[0])[0]
        file_with_data = str(os.path.join(root_path_main_dir, 'data', self._file_name)) + '.json'
        if os.path.exists(file_with_data):
            if not os.path.abspath(file_with_data).endswith('.json'):
                raise ValueError('Файл должен быть формата JSON.')
        else:
            pass
        super().__init__()

    @property
    def file_name(self):
        """Геттер имени файла. Предоставляет доступ к атрибуту для изменения его значения."""
        return self._file_name

    @file_name.setter
    def file_name(self, user_file_name: str):
        """Сеттер имени файла. Изменяет значение атрибута."""
        if user_file_name == '':
            pass
        else:
            self._file_name = user_file_name

    def write_to_file(self, for_write_vacancies_list: list[Vacancy]):
        """Добавляет список вакансий в JSON файл."""

        root_path_src_dir = os.path.split(os.path.abspath(__file__))
        root_path_main_dir = os.path.split(os.path.split(root_path_src_dir[0])[0])[0]
        file_with_data = str(os.path.join(root_path_main_dir, 'data', self._file_name)) + '.json'

        list_not_double = list(set(for_write_vacancies_list))
        list_for_write = []
        for vac in list_not_double:
            list_for_write.append({'name': vac.name, 'link': vac.url, 'city': vac.area,
                                   'salary_from': vac.salary_min, 'salary_to': vac.salary_max,
                                   'currency': vac.currency, 'experience': vac.experience,
                                   'requirements': vac.requirements, 'duties': vac.responsibility})

        try:
            with open(file_with_data, "r", encoding="utf-8") as file_vac:
                json_content = json.load(file_vac)
                json_content.extend(list_for_write)
                with open(file_with_data, "w", encoding="utf-8") as file_vac_for_update:
                    json.dump(json_content, file_vac_for_update, indent=2, ensure_ascii=False)
        except FileNotFoundError:
            with open(file_with_data, "w", encoding="utf-8") as file_vac_new:
                json.dump(list_for_write, file_vac_new, indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            with open(file_with_data, "w", encoding="utf-8") as file_vac_for_update:
                json.dump(list_for_write, file_vac_for_update, indent=2, ensure_ascii=False)

    def write_to_file_top_n_vac(self, for_write_top_n_vac_list: list[Vacancy]):
        """Записывает список ТОП-n вакансий в JSON файл."""

        root_path_src_dir = os.path.split(os.path.abspath(__file__))
        root_path_main_dir = os.path.split(os.path.split(root_path_src_dir[0])[0])[0]
        file_with_data = str(os.path.join(root_path_main_dir, 'data', self._file_name)) + '.json'

        list_top_n_vac_for_write = []
        for vac in for_write_top_n_vac_list:
            list_top_n_vac_for_write.append({'name': vac.name, 'link': vac.url, 'city': vac.area,
                                             'salary_from': vac.salary_min, 'salary_to': vac.salary_max,
                                             'currency': vac.currency, 'experience': vac.experience,
                                             'requirements': vac.requirements, 'duties': vac.responsibility})

        try:
            with open(file_with_data, "w", encoding="utf-8") as file_vac_for_update:
                json.dump(list_top_n_vac_for_write, file_vac_for_update, indent=2, ensure_ascii=False)
        except FileNotFoundError:
            with open(file_with_data, "w", encoding="utf-8") as file_vac_new:
                json.dump(list_top_n_vac_for_write, file_vac_new, indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            with open(file_with_data, "w", encoding="utf-8") as file_vac_for_update:
                json.dump(list_top_n_vac_for_write, file_vac_for_update, indent=2, ensure_ascii=False)

    def load_from_file(self):
        """Получает данные из файла и преобразовывает их в словарь вакансий."""

        root_path_src_dir = os.path.split(os.path.abspath(__file__))
        root_path_main_dir = os.path.split(os.path.split(root_path_src_dir[0])[0])[0]
        file_with_data = str(os.path.join(root_path_main_dir, 'data', self._file_name)) + '.json'

        try:
            with open(file_with_data, "r", encoding="utf-8") as f:
                json_string = f.read()

            raw_vacancies = json.loads(json_string)
            return raw_vacancies
        except FileNotFoundError:
            list_for_write = []
            with open(file_with_data, "w", encoding="utf-8") as file_new:
                json.dump(list_for_write, file_new, indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            list_for_write = []
            with open(file_with_data, "w", encoding="utf-8") as file_for_adjustment:
                json.dump(list_for_write, file_for_adjustment, indent=2, ensure_ascii=False)

    def delete_from_file(self):
        """Удаляет информацию о вакансиях."""

        root_path_src_dir = os.path.split(os.path.abspath(__file__))
        root_path_main_dir = os.path.split(os.path.split(root_path_src_dir[0])[0])[0]
        file_with_data = str(os.path.join(root_path_main_dir, 'data', self._file_name)) + '.json'

        with open(file_with_data, "w") as f:
            f.write('')

    def __str__(self):
        """Удобное отображение наименования файла."""

        return f'{self._file_name}'
