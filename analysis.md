# Анализ задачи

### Что было сделано:
Я создал программу, которая собирает данные: (цитаты, авторы, теги) с сайта https://quotes.toscrape.com/ и сохраняет их в формате JSON. 

### Откуда были получены данные:
Данные были получены с сайта https://quotes.toscrape.com/

### Как осуществлялся сбор:
Для получения данных использовались библиотеки requests (для запросов к сайту) и BeautifulSoup для парсинга HTML страниц.

### Почему был выбран тот или иной метод/инструмент, а не другой:
Библиотека requests является одной из самых стабильных и часто используемых для HTTP запросов.
Библиотека BeautifulSoup является довольно распространенной для парсинга HTML страниц и хорошо подходит для нашей задачи.