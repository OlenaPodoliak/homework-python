from Lesson_5_OOP import FeedRecord
import os

class RecordFromFile(FeedRecord):
    def __init__(self, text):
        self.name = "Text"
        FeedRecord.__init__(self, self.name)
        self.text = text

    def format(self):
        super().format()  # Сначала вызываем родительский метод
        return f"{super().format()}\n{self.text}\n\n"


class ParseFile:
    def __init__(self, filepath="files/input_ad.txt"):
        self.filepath = filepath
        self.filename = "news_feed.txt"

    def parse(self, line=0):
        try:
            with open(self.filepath, 'r') as file:
                if line == 1:
                    record = file.readline()
                else:
                    record = file.read()
            return record
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    def publish(self, record):
        try:
            with open(self.filename, 'a') as file:
                file.write(record.format())
            os.remove(self.filepath)
            print(f"Файл '{self.filepath}' успешно записан и удалён.")
        except Exception as e:
            print(f"Ошибка при записи или удалении файла: {e}")

file1 = ParseFile()
file1.publish(RecordFromFile(file1.parse()))

file2 = ParseFile("files/input_news_1.txt")
file2.publish(RecordFromFile(file2.parse(1)))



