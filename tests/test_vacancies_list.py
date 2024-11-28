import pytest

from src.vacancy.class_vacancy import Vacancy

from src.vacancy.vacancies_list import VacanciesProcessing


@pytest.fixture()
def example_salary_min_zero():
    return 0


@pytest.fixture()
def example_salary_min():
    return 50000


@pytest.fixture()
def example_salary_min_1():
    return 70000


@pytest.fixture()
def example_salary_max_zero():
    return 0


@pytest.fixture()
def example_salary_max():
    return 80000


@pytest.fixture()
def example_salary_max_1():
    return 150000


@pytest.fixture()
def example_vacancy_list():
    return [Vacancy(name='Учитель информатики',
                    url='https://zheleznodorozhniy.superjob.ru/vakansii/uchitel-informatiki-36344427.html',
                    area='Железнодорожный', salary_min=50000, salary_max=0, currency='rub',
                    experience='Без опыта',
                    requirements='С 1 сентября 2024 года. \nОбязанности:\n• Осуществляет обучение и воспитание '
                                 'обучающихся с учетом специфики преподаваемого предмета, проводит уроки и другие '
                                 'занятия в соответствии с расписанием.\n• В своей работе по предмету использует '
                                 'разнообразные приемы, методы и средства обучения.\n• Реализует образовательные '
                                 'программы.\n• Подготовка обучающихся к сдаче ГИА и участию в олимпиадах и конкурсах.'
                                 '\n• Ведение дополнительных занятий и факультативов. \n'
                                 '• Программирование: Перволого/Логомиры, Scratch, Кумир, '
                                 'Паскаль/Дельфи, C/C++, Python\nСАПР: Компас, AutoCAD CorelDRAW и др.\nВеб-дизайн и '
                                 'разработка: JavaScript, Adobe Photoshop, Flash.\nАдминистрирование: Windows, '
                                 'Linux\nУсловия:\n• Выплата компенсации за аренду жилья (при отсутствии недвижимости '
                                 'в Московской области)\n• Помощь в устройстве детей в дошкольные или школьные '
                                 'учреждения города.', responsibility='None'),
            Vacancy(name='Педагог на направление Программирование на языке Java / С# / Python',
                    url='https://novokuznetsk.superjob.ru/vakansii/pedagog-na-napravlenie-programmirovanie-na-yazyke'
                        '-java-43502923.html',
                    area='Новокузнецк', salary_min=25000, salary_max=50000, currency='rub',
                    experience='Без опыта',
                    requirements='Обязанности:\nпедагоги-наставники на направления: Python, Java, С#:\n• обучение детей'
                                 ' и молодежи по программам дополнительного образования;\n• помощь и поддержка '
                                 'обучающихся в освоении языка программирования;\n• разработка совместных проектов с '
                                 'учащимися;\n• оформление готовых продуктов;\n• участие в массовых мероприятиях с '
                                 'учащимися.\n Требования:\n• образование высшее или средне-специальное '
                                 '(рассматриваются студенты начиная с 4-го курса);\n• опыт работы приветствуется '
                                 '(рассматриваются начинающие специалисты);\n• умение доводить дело до логического '
                                 'завершения.\nУсловия:\n• соблюдение правил внутреннего распорядка;\n• исполнительская'
                                 ' дисциплина;\n• справка об отсутствии судимости;\n• наличие санитарной книжки '
                                 '(ежегодный медосмотр, санминимум для работников сферы образования).\nДля вас:\n• '
                                 'полный социальный пакет;\n• стабильная з/п два раза в месяц;\n• дружный коллектив;\n•'
                                 ' ежегодный отпуск 42 дня;\n• оформление по ТК РФ.', responsibility='None'),
            Vacancy(name='Учитель по программированию',
                    url='https://mo.superjob.ru/vakansii/uchitel-po-programmirovaniyu-45698486.html',
                    area='Ржавки', salary_min=0, salary_max=60000, currency='rub',
                    experience='Без опыта',
                    requirements='Обязанности:\n• \nОбучение детей (4-14 лет) в группах программированию \n• '
                                 '\nФормирование у учеников логического системного мышления и развитие технических '
                                 'творческих способностей \n\n• Обучение детей основам проектной работы в IT\n• '
                                 'Поддержание интереса и мотивации учеников \nТребования:\n• \nОпыт работы с детьми '
                                 '(аниматор, репетитор, воспитатель, вожатый, учитель, опытный родитель или старший '
                                 'брат/сестра\n• Уверенное владение компьютером. В идеале, знание основ '
                                 'алгоритмического языка и программирования. (Предпочтительно: Scratch JR, Scratch, '
                                 'Snap, Stencyl, Tynker, Blockly, Перволого, Пиктомир)\n• Умение объяснять сложное '
                                 'простыми (иногда детскими) словами \n• Любовь к детям и умение направить их энергию в'
                                 ' нужное русло \n\n• Знание текстовых языков программирования Python, Java и прочее -'
                                 ' желательно \n\nУсловия:\n• \nУдобный график (очень многое можно скорректировать '
                                 'совместно с администратором) \n• Возможность обучать мотивированных детей, которые '
                                 'стремятся узнать все о современных технологиях и не только \n• Увлеченная команда '
                                 'преподавателей \n\n• Интересные и амбициозные задачи\n• Профессия квалифицированного'
                                 ' детского IT тренера - одна из самых востребованных на рынке труда',
                    responsibility='None')]


@pytest.fixture()
def sorted_vacancy_list():
    return [Vacancy(name='Учитель по программированию',
                    url='https://mo.superjob.ru/vakansii/uchitel-po-programmirovaniyu-45698486.html',
                    area='Ржавки', salary_min=0, salary_max=60000, currency='rub',
                    experience='Без опыта',
                    requirements='Обязанности:\n• \nОбучение детей (4-14 лет) в группах программированию \n• '
                                 '\nФормирование у учеников логического системного мышления и развитие технических '
                                 'творческих способностей \n\n• Обучение детей основам проектной работы в IT\n• '
                                 'Поддержание интереса и мотивации учеников \nТребования:\n• \nОпыт работы с детьми '
                                 '(аниматор, репетитор, воспитатель, вожатый, учитель, опытный родитель или старший '
                                 'брат/сестра\n• Уверенное владение компьютером. В идеале, знание основ '
                                 'алгоритмического языка и программирования. (Предпочтительно: Scratch JR, Scratch, '
                                 'Snap, Stencyl, Tynker, Blockly, Перволого, Пиктомир)\n• Умение объяснять сложное '
                                 'простыми (иногда детскими) словами \n• Любовь к детям и умение направить их энергию в'
                                 ' нужное русло \n\n• Знание текстовых языков программирования Python, Java и прочее -'
                                 ' желательно \n\nУсловия:\n• \nУдобный график (очень многое можно скорректировать '
                                 'совместно с администратором) \n• Возможность обучать мотивированных детей, которые '
                                 'стремятся узнать все о современных технологиях и не только \n• Увлеченная команда '
                                 'преподавателей \n\n• Интересные и амбициозные задачи\n• Профессия квалифицированного'
                                 ' детского IT тренера - одна из самых востребованных на рынке труда',
                    responsibility='None'),
            Vacancy(name='Педагог на направление Программирование на языке Java / С# / Python',
                    url='https://novokuznetsk.superjob.ru/vakansii/pedagog-na-napravlenie-programmirovanie-na-yazyke'
                        '-java-43502923.html',
                    area='Новокузнецк', salary_min=25000, salary_max=50000, currency='rub',
                    experience='Без опыта',
                    requirements='Обязанности:\nпедагоги-наставники на направления: Python, Java, С#:\n• обучение детей'
                                 ' и молодежи по программам дополнительного образования;\n• помощь и поддержка '
                                 'обучающихся в освоении языка программирования;\n• разработка совместных проектов с '
                                 'учащимися;\n• оформление готовых продуктов;\n• участие в массовых мероприятиях с '
                                 'учащимися.\n Требования:\n• образование высшее или средне-специальное '
                                 '(рассматриваются студенты начиная с 4-го курса);\n• опыт работы приветствуется '
                                 '(рассматриваются начинающие специалисты);\n• умение доводить дело до логического '
                                 'завершения.\nУсловия:\n• соблюдение правил внутреннего распорядка;\n• исполнительская'
                                 ' дисциплина;\n• справка об отсутствии судимости;\n• наличие санитарной книжки '
                                 '(ежегодный медосмотр, санминимум для работников сферы образования).\nДля вас:\n• '
                                 'полный социальный пакет;\n• стабильная з/п два раза в месяц;\n• дружный коллектив;\n•'
                                 ' ежегодный отпуск 42 дня;\n• оформление по ТК РФ.', responsibility='None'),
            Vacancy(name='Учитель информатики',
                    url='https://zheleznodorozhniy.superjob.ru/vakansii/uchitel-informatiki-36344427.html',
                    area='Железнодорожный', salary_min=50000, salary_max=0, currency='rub',
                    experience='Без опыта',
                    requirements='С 1 сентября 2024 года. \nОбязанности:\n• Осуществляет обучение и воспитание '
                                 'обучающихся с учетом специфики преподаваемого предмета, проводит уроки и другие '
                                 'занятия в соответствии с расписанием.\n• В своей работе по предмету использует '
                                 'разнообразные приемы, методы и средства обучения.\n• Реализует образовательные '
                                 'программы.\n• Подготовка обучающихся к сдаче ГИА и участию в олимпиадах и конкурсах.'
                                 '\n• Ведение дополнительных занятий и факультативов. \n'
                                 '• Программирование: Перволого/Логомиры, Scratch, Кумир, '
                                 'Паскаль/Дельфи, C/C++, Python\nСАПР: Компас, AutoCAD CorelDRAW и др.\nВеб-дизайн и '
                                 'разработка: JavaScript, Adobe Photoshop, Flash.\nАдминистрирование: Windows, '
                                 'Linux\nУсловия:\n• Выплата компенсации за аренду жилья (при отсутствии недвижимости '
                                 'в Московской области)\n• Помощь в устройстве детей в дошкольные или школьные '
                                 'учреждения города.', responsibility='None')
            ]


@pytest.fixture()
def example_vacancy():
    return Vacancy(name='Учитель информатики',
                   url='https://zheleznodorozhniy.superjob.ru/vakansii/uchitel-informatiki-36344427.html',
                   area='Железнодорожный', salary_min=50000, salary_max=0, currency='rub',
                   experience='Без опыта',
                   requirements='С 1 сентября 2024 года. \nОбязанности:\n• Осуществляет обучение и воспитание '
                                'обучающихся с учетом специфики преподаваемого предмета, проводит уроки и другие '
                                'занятия в соответствии с расписанием.\n• В своей работе по предмету использует '
                                'разнообразные приемы, методы и средства обучения.\n• Реализует образовательные '
                                'программы.\n• Подготовка обучающихся к сдаче ГИА и участию в олимпиадах и конкурсах.'
                                '\n• Ведение дополнительных занятий и факультативов. \n'
                                '• Программирование: Перволого/Логомиры, Scratch, Кумир, '
                                'Паскаль/Дельфи, C/C++, Python\nСАПР: Компас, AutoCAD CorelDRAW и др.\nВеб-дизайн и '
                                'разработка: JavaScript, Adobe Photoshop, Flash.\nАдминистрирование: Windows, '
                                'Linux\nУсловия:\n• Выплата компенсации за аренду жилья (при отсутствии недвижимости '
                                'в Московской области)\n• Помощь в устройстве детей в дошкольные или школьные '
                                'учреждения города.', responsibility='None')


@pytest.fixture()
def example_vacancy_1():
    return Vacancy(name='Педагог на направление Программирование на языке Java / С# / Python',
                   url='https://novokuznetsk.superjob.ru/vakansii/pedagog-na-napravlenie-programmirovanie-na-yazyke'
                       '-java-43502923.html',
                   area='Новокузнецк', salary_min=25000, salary_max=50000, currency='rub',
                   experience='Без опыта',
                   requirements='Обязанности:\nпедагоги-наставники на направления: Python, Java, С#:\n• обучение детей'
                                ' и молодежи по программам дополнительного образования;\n• помощь и поддержка '
                                'обучающихся в освоении языка программирования;\n• разработка совместных проектов с '
                                'учащимися;\n• оформление готовых продуктов;\n• участие в массовых мероприятиях с '
                                'учащимися.\n Требования:\n• образование высшее или средне-специальное '
                                '(рассматриваются студенты начиная с 4-го курса);\n• опыт работы приветствуется '
                                '(рассматриваются начинающие специалисты);\n• умение доводить дело до логического '
                                'завершения.\nУсловия:\n• соблюдение правил внутреннего распорядка;\n• исполнительская'
                                ' дисциплина;\n• справка об отсутствии судимости;\n• наличие санитарной книжки '
                                '(ежегодный медосмотр, санминимум для работников сферы образования).\nДля вас:\n• '
                                'полный социальный пакет;\n• стабильная з/п два раза в месяц;\n• дружный коллектив;\n•'
                                ' ежегодный отпуск 42 дня;\n• оформление по ТК РФ.', responsibility='None')


@pytest.fixture()
def example_vacancy_2():
    return Vacancy(name='Учитель по программированию',
                   url='https://mo.superjob.ru/vakansii/uchitel-po-programmirovaniyu-45698486.html',
                   area='Ржавки', salary_min=0, salary_max=60000, currency='rub',
                   experience='Без опыта',
                   requirements='Обязанности:\n• \nОбучение детей (4-14 лет) в группах программированию \n• '
                                '\nФормирование у учеников логического системного мышления и развитие технических '
                                'творческих способностей \n\n• Обучение детей основам проектной работы в IT\n• '
                                'Поддержание интереса и мотивации учеников \nТребования:\n• \nОпыт работы с детьми '
                                '(аниматор, репетитор, воспитатель, вожатый, учитель, опытный родитель или старший '
                                'брат/сестра\n• Уверенное владение компьютером. В идеале, знание основ '
                                'алгоритмического языка и программирования. (Предпочтительно: Scratch JR, Scratch, '
                                'Snap, Stencyl, Tynker, Blockly, Перволого, Пиктомир)\n• Умение объяснять сложное '
                                'простыми (иногда детскими) словами \n• Любовь к детям и умение направить их энергию в'
                                ' нужное русло \n\n• Знание текстовых языков программирования Python, Java и прочее -'
                                ' желательно \n\nУсловия:\n• \nУдобный график (очень многое можно скорректировать '
                                'совместно с администратором) \n• Возможность обучать мотивированных детей, которые '
                                'стремятся узнать все о современных технологиях и не только \n• Увлеченная команда '
                                'преподавателей \n\n• Интересные и амбициозные задачи\n• Профессия квалифицированного'
                                ' детского IT тренера - одна из самых востребованных на рынке труда',
                   responsibility='None')


@pytest.fixture()
def example_filter_word():
    return 'Python'


@pytest.fixture()
def example_filter_word1():
    return 'Администрирование'


@pytest.fixture()
def example_digit_n():
    return 1


@pytest.fixture()
def example_digit_n_1():
    return 3


@pytest.fixture()
def example_digit_n_2():
    return 5


def test_filter_vacancy_by_keywords(example_vacancy, example_vacancy_1, example_vacancy_2, example_filter_word,
                                    example_filter_word1):
    assert VacanciesProcessing.filter_vacancy_by_keywords(example_vacancy, example_filter_word) == True
    assert VacanciesProcessing.filter_vacancy_by_keywords(example_vacancy, example_filter_word1) == True
    assert VacanciesProcessing.filter_vacancy_by_keywords(example_vacancy_1, example_filter_word) == True
    assert VacanciesProcessing.filter_vacancy_by_keywords(example_vacancy_1, example_filter_word1) == False
    assert VacanciesProcessing.filter_vacancy_by_keywords(example_vacancy_2, example_filter_word) == True
    assert VacanciesProcessing.filter_vacancy_by_keywords(example_vacancy_2, example_filter_word1) == False


def test_filter_vacancies(example_vacancy, example_vacancy_list, example_filter_word, example_filter_word1):
    test_list = VacanciesProcessing(example_vacancy_list)
    assert test_list.filter_vacancies(example_vacancy_list, example_filter_word1)[0].requirements == \
           example_vacancy_list[0].requirements
    with pytest.raises(IndexError):
        assert test_list.filter_vacancies(example_vacancy_list, example_filter_word1)[1].requirements == \
               example_vacancy_list[1].requirements
    with pytest.raises(AssertionError):
        assert test_list.filter_vacancies(example_vacancy_list, example_filter_word1) == \
               example_vacancy_list
    with pytest.raises(AssertionError):
        assert test_list.filter_vacancies(example_vacancy_list, example_filter_word1) == \
               example_vacancy


def test_get_vacancies_by_salary(example_salary_max, example_salary_max_1, example_salary_max_zero, example_salary_min,
                                 example_salary_min_zero, example_salary_min_1, example_vacancy_list):
    test_list = VacanciesProcessing(example_vacancy_list)
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_zero, example_salary_max_zero)[0] \
               .name == example_vacancy_list[0].name
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_zero, example_salary_max_zero)[0] \
               .salary_min == example_vacancy_list[0].salary_min
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_zero, example_salary_max_zero)[0] \
               .salary_max == example_vacancy_list[0].salary_max
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_zero, example_salary_max)[1] \
               .name == example_vacancy_list[1].name
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_zero, example_salary_max)[1] \
               .salary_min == example_vacancy_list[1].salary_min
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_zero, example_salary_max)[1] \
               .salary_max == example_vacancy_list[1].salary_max
    with pytest.raises(IndexError):
        assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_zero,
                                                 example_salary_max_zero)[2].name == example_vacancy_list[2].name
        assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_zero,
                                                 example_salary_max_zero)[2].salary_min == example_vacancy_list[2]. \
                   salary_min
        assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_1, example_salary_max_1)[2] \
                   .salary_max == example_vacancy_list[2].salary_max
        assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_1, example_salary_max_1)[2] \
                   .name == example_vacancy_list[2].name
        assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_1, example_salary_max_1)[2] \
                   .salary_min == example_vacancy_list[2].salary_min
        assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min_1, example_salary_max_1)[2] \
                   .salary_max == example_vacancy_list[2].salary_max
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min, example_salary_max)[0] \
               .name == example_vacancy_list[0].name
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min, example_salary_max)[0] \
               .salary_min == example_vacancy_list[0].salary_min
    assert test_list.get_vacancies_by_salary(example_vacancy_list, example_salary_min, example_salary_max)[0] \
               .salary_max == example_vacancy_list[0].salary_max


def test_sort_vacancies(example_vacancy_list, sorted_vacancy_list):
    test_list = VacanciesProcessing(example_vacancy_list)
    assert test_list.sort_vacancies(example_vacancy_list)[0].name == sorted_vacancy_list[0].name
    assert test_list.sort_vacancies(example_vacancy_list)[0].salary_max == sorted_vacancy_list[0].salary_max
    assert test_list.sort_vacancies(example_vacancy_list)[1].name == sorted_vacancy_list[1].name
    assert test_list.sort_vacancies(example_vacancy_list)[1].salary_max == sorted_vacancy_list[1].salary_max
    assert test_list.sort_vacancies(example_vacancy_list)[2].name == sorted_vacancy_list[2].name
    assert test_list.sort_vacancies(example_vacancy_list)[2].salary_max == sorted_vacancy_list[2].salary_max


def test_get_top_vacancies(sorted_vacancy_list, example_digit_n, example_digit_n_1, example_digit_n_2):
    test_list = VacanciesProcessing(sorted_vacancy_list)
    assert test_list.get_top_vacancies(sorted_vacancy_list, example_digit_n)[0].name == sorted_vacancy_list[0].name
    assert test_list.get_top_vacancies(sorted_vacancy_list, example_digit_n)[0].salary_max == sorted_vacancy_list[0] \
        .salary_max
    assert test_list.get_top_vacancies(sorted_vacancy_list, example_digit_n_1)[1].name == sorted_vacancy_list[1].name
    assert test_list.get_top_vacancies(sorted_vacancy_list, example_digit_n_1)[1].salary_max == sorted_vacancy_list[1] \
        .salary_max
    assert test_list.get_top_vacancies(sorted_vacancy_list, example_digit_n_2)[2].name == sorted_vacancy_list[2].name
    assert test_list.get_top_vacancies(sorted_vacancy_list, example_digit_n_2)[2].salary_max == sorted_vacancy_list[2] \
        .salary_max