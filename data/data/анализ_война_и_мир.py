# Импортируем библиотеку для выполнения HTTP-запросов
import requests

# Скачиваем текстовый файл
data = requests.get('https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt').text

# Предобрабатываем текстовый файл
data = data.split('\n')
data.remove('')
data = data + ['[new chapter]']

# Разделяем текст на главы
chapter_data = []
chapter_words = []

for word in data:
    if word == '[new chapter]':
        chapter_data.append(chapter_words)
        chapter_words = []
    else:
        chapter_words.append(word)

# Инициализируем список для хранения количества слов в каждой главе
chapter_words_count = []

# Считаем количество слов в каждой главе
for chapter_words in chapter_data:
    temp = {}
    for word in chapter_words:
        if word not in temp:
            temp[word] = 1
        else:
            temp[word] += 1
    chapter_words_count.append(temp)

# Проверяем, что список chapter_words_count определен
print("Список chapter_words_count определен и содержит", len(chapter_words_count), "элементов.")

# Считаем общее количество слов в каждой главе
chapter_total_words = []
for chapter in chapter_data:
    chapter_total_words.append(len(chapter))

# Считаем частоту встречаемости слов (TF) для каждой главы
tf_per_chapter = []
for chapter_num in range(len(chapter_words_count)):
    chapter_dict = chapter_words_count[chapter_num]
    chapter_total = chapter_total_words[chapter_num]
    tf_chapter_dict = {}
    for word in chapter_dict:
        tf_chapter_dict[word] = chapter_dict[word] / chapter_total
    tf_per_chapter.append(tf_chapter_dict)

# Считаем частоту документов (DF) для каждого слова
word_set = set()
for chapter in chapter_data:
    for word in chapter:
        word_set.add(word)

df_dict = {}
total_chapters = len(chapter_words_count)
for word in word_set:
    contain_word_chapters = 0
    for chapter_dict in chapter_words_count:
        if word in chapter_dict:
            contain_word_chapters += 1
    df_dict[word] = contain_word_chapters / total_chapters

# Считаем нормализованное TF-IDF для каждого слова в каждой главе
tf_idf_per_chapter = []
for chapter_tf_dict in tf_per_chapter:
    tf_idf_chapter_dict = {}
    for word in chapter_tf_dict:
        if len(word) > 3 and df_dict[word] > 0:
            tf_idf_chapter_dict[word] = chapter_tf_dict[word] / df_dict[word]
    tf_idf_per_chapter.append(tf_idf_chapter_dict)

# Проверяем, что tf_idf_per_chapter корректно определен
print("TF-IDF per chapter:", tf_idf_per_chapter[0])

# Получаем топ-3 слова с наивысшим TF-IDF в заданной главе
target_chapter = 120  # Измените на нужный номер главы
if target_chapter <= len(tf_idf_per_chapter):
    chapter_tf_idf_dict = tf_idf_per_chapter[target_chapter - 1]

    # Сортируем слова по значению TF-IDF в порядке убывания
    sorted_tf_idf = sorted(chapter_tf_idf_dict.items(), key=lambda item: item[1], reverse=True)

    # Печатаем топ-3 слова
    print("Топ-3 слова с наивысшим TF-IDF в главе", target_chapter)
    for word, tf_idf in sorted_tf_idf[:3]:
        print(word, tf_idf)
else:
    print("Ошибка: Номер главы превышает количество глав в тексте.")
