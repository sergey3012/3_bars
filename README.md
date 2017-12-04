# Ближайшие бары
Скрипт парсит файл json-формата, который содержит список московских баров. На основании данных из файла
скрипт рассчитает:

* самый большой бар;
* самый маленький бар;
* самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры).


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск:

```$ python3 bars.py bars.json
Введите адрес файла: bars.json
Введите координаты долготы (Пример ввода: 38.2323): 34.987
Введите координаты широты (Пример ввода: 38.2323): 12.0971
Самый большой бар -  Спорт бар «Красная машина» , Количество мест: 450
Самый маленький бар -  БАР. СОКИ , Количество мест:  0
Ближайший к Вам бар -  Staropramen , адрес:  Садовая-Спасская улица, дом 19, корпус 1 , Количество мест:  50

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
