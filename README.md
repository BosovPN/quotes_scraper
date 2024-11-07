# Quotes_scraper

## Программа для сбора цитат с сайта quotes.toscrape.com и сохранения их в формате JSON
## Пример выходного файла:

```sh
  [
   {
      "quote": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
      "author": "Albert Einstein",
      "tags": [
         "change",
         "deep-thoughts",
         "thinking",
         "world"
      ]
   },
   {
      "quote": "“It is our choices, Harry, that show what we truly are, far more than our abilities.”",
      "author": "J.K. Rowling",
      "tags": [
         "abilities",
         "choices"
      ]
   }
  ]  
```

## Инструкция по запуску:
### Клонируйте репозиторий с помощью команды ниже:
```bash
git clone https://github.com/BosovPN/quotes_scraper.git
```

### Перейдите в папку, где находятся файлы проекта:
```bash
cd quotes_scraper
```

### Создайте виртуальное окружение в этой папке и активируйте его:
```bash
python -m venv venv
```

На Windows:
```bash
venv\Scripts\activate
```

На macOS и Linux:
```bash
source venv/bin/activate
```

### Установите зависимости с помощью файла requirements.txt
```bash
pip install -r requirements.txt
```

### Для запуска программы выполните следующую команду:
```bash
python main.py
```
