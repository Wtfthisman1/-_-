# -_-
Игра "Угадай число"
=====================

Компьютер сам загадывает и сам угадывает число
----------------------------------------------

### Описание

Это простая консольная игра, в которой компьютер использует бинарный поиск для угадывания числа, загаданного пользователем или сгенерированного случайным образом.

Установка

1. Скачайте или клонируйте репозиторий.
2. Убедитесь, что у вас установлен Python 3.x и библиотека numpy.
3. Запустите игру, выполнив файл `main.py`.

 Использование

После запуска игры, вам будет предложено выбрать, хотите ли вы загадать число самостоятельно или желаете, чтобы компьютер сделал это за вас. В первом случае, вам нужно будет загадать целое число от 1 до 1000 и отвечать на вопросы компьютера, сообщая, большее или меньшее загаданное вами число, чем предложенное компьютером. Во втором случае, компьютер сам загадает число и будет угадывать его, используя бинарный поиск.

После того, как компьютер угадает число, ему будет присвоено количество попыток, которое он использовал для угадывания. Если вы решите сыграть еще раз, то количество попыток, использованных компьютером в следующей игре, будет добавлено к его общему количеству попыток.

Функции

`binary_search_predict(number: int = 1) -> int:`

Эта функция использует бинарный поиск для угадывания числа, загаданного пользователем или сгенерированного случайным образом. Она принимает один необязательный аргумент - `number` - целое число, которое нужно угадать. По умолчанию, этот аргумент равен 1. Функция возвращает количество попыток, которое она использовала для угадывания числа.

#### `score_game(binary_search_predict) -> int:`

Эта функция используется для подсчета среднего количества попыток, которое использует функция `binary_search_predict` для угадывания числа. Она принимает один аргумент - `binary_search_predict` - функцию, которую нужно использовать для угадывания числа. Функция `score_game` генерирует 1000 случайных чисел от 1 до 100 и использует функцию `binary_search_predict` для угадывания каждого из них. Затем, она вычисляет среднее количество попыток, которое использовала функция `binary_search_predict` для угадывания этих чисел, и возвращает его.

#### `main()`

Эта функция содержит основной код игры. Она вызывает функцию `score_game` для подсчета среднего количества попыток, которое использует функция `binary_search_predict` для угадывания числа, и затем запускает цикл, в котором пользователь может сыграть в игру "Угадай число" сколько угодно раз.

### Лицензия

Этот проект распространяется под лицензией MIT. Смотрите файл `LICENSE` для подробностей.
