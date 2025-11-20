ua_letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
ua_letters_upper = ua_letters.upper()

def is_ukrainian(word: str):
    if not word:
        return False
    return word[0] in ua_letters or word[0] in ua_letters_upper


def sort_words(words):
    return sorted(words, key=lambda w: (1 if not is_ukrainian(w) else 0, w.lower()))


words_list = [
    'English', 'інформація', 'android', 'Windows', 'Добрий день',
    'матриця', 'актова зала', 'біоресурси', 'Єдиний', 'кава'
]

print("Заданий список:")
print(words_list)

sorted_list = sort_words(words_list)

print("\nВідсортований список:")
print(sorted_list)
