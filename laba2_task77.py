import urllib.request
import re

class MyFile:
    def __init__(self, location, mode="read"):
        # location - путь к файлу или URL
        # mode - режим работы: read, write, append, url
        self.location = location
        self.mode = mode
        self.file_handler = None
        
    def read(self):
        # Читаем локальный файл
        if self.mode != "read":
            raise ValueError("Режим не поддерживает чтение файлов")
        
        try:
            with open(self.location, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            # Если что-то пошло не так
            return f"Ошибка при чтении файла: {e}"
    
    def write(self, text_data):
        # Записываем или добавляем текст
        if self.mode == "write":
            try:
                with open(self.location, 'w', encoding='utf-8') as f:
                    f.write(text_data)
                return f"Данные записаны в {self.location}"
            except Exception as e:
                return f"Ошибка при записи: {e}"
        
        elif self.mode == "append":
            try:
                with open(self.location, 'a', encoding='utf-8') as f:
                    f.write(text_data)
                return f"Данные добавлены в {self.location}"
            except Exception as e:
                return f"Ошибка при добавлении: {e}"
        else:
            raise ValueError("Этот режим не для записи")
    
    def read_url(self):
        # Скачиваем содержимое веб-страницы
        if self.mode != "url":
            raise ValueError("Это не URL-объект")
        
        try:
            with urllib.request.urlopen(self.location) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"Ошибка при загрузке страницы: {e}"
    
    def count_urls(self):
        # Считаем сколько URL на странице
        if self.mode != "url":
            raise ValueError("Только для URL-режима")
        
        page_content = self.read_url()
        
        # Ищем все ссылки на странице
        url_regex = r'(?:https?://|www\.)[\w\-]+(?:\.[\w\-]+)+(?:[/?][\w\-\./?=&%]*)?'
        
        url_matches = re.findall(url_regex, page_content)
        return len(url_matches)
    
    def write_url(self, output_filename):
        # Сохраняем страницу в файл
        if self.mode != "url":
            raise ValueError("Не могу сохранить не-URL")
        
        url_content = self.read_url()
        
        # Проверяем, что загрузка прошла успешно
        if not url_content.startswith("Ошибка"):
            try:
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(url_content)
                return f"Страница сохранена как {output_filename}"
            except Exception as e:
                return f"Не удалось сохранить: {e}"
        return url_content
    
    def __enter__(self):
        # Для работы с with
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        # Закрываем файл при выходе
        if self.file_handler:
            self.file_handler.close()
    
    def close(self):
        # Ручное закрытие
        if self.file_handler:
            self.file_handler.close()
            self.file_handler = None


# Тестируем работу
if __name__ == "__main__":
    # 1. Чтение файла
    file = MyFile("text.txt", "read")
    text = file.read()
    print(text)
    
    # 2. Перезапись файла
    file = MyFile("text.txt", "write")
    result = file.write("привет!")
    print(result)
    
    # 3. Добавление в файл
    file = MyFile("text.txt", "append")
    result = file.write(" еще текст")
    print(result)
    
    # 4. Работа с сайтом
    file = MyFile("https://pycode.ru/python_tasks_1.html", "url")
    
    # Смотрим что на странице
    text = file.read_url()
    print(text[:500] + "...")
    
    # Считаем ссылки
    count = file.count_urls()
    print(f"Ссылок на странице: {count}")
    
    # Сохраняем страницу
    result = file.write_url("page_copy.txt")
    print(result)
    
    # Закрываем
    file.close()
