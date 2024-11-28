def end_word_question(count_services):
    """Определяем окончание для слова "сайт"."""
    last_digit_questions = count_services % 10
    if last_digit_questions == 1:
        end_word_questions = "сайта"
    else:
        end_word_questions = "сайтов"
    return end_word_questions