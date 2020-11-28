# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
# Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

# def int_func(text):
#     return text.title()
#
# print(int_func('text'))
# print(int_func('some words here.'))

# самостоятельная реализация

def int_func(text):
    CASE_OFFSET = 32

    def to_upper_first_ltr(text):
        return chr(ord(text[0]) - CASE_OFFSET) + text[1:]

    text_words = text.split()
    for i in range(len(text_words)):
        text_words[i] = to_upper_first_ltr(text_words[i])
    return ' '.join(text_words)

print(int_func('one two three alpha beta gamma'))
