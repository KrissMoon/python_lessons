# 6. Реализовать функцию int_func(),
# принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(words):
    word_list = words.split(' ')
    word_list_result = [i.title() for i in word_list]
    return ' '.join(word_list_result)

user_str = input('Введите cлова из маленьких латинских букв: ')
print(int_func(user_str))
