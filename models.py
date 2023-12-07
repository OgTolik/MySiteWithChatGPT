class Document:
    def __init__(self, title, content, folder):
        # Конструктор класса Document, инициализирующий его атрибуты
        self.title = title  # Название документа
        self.content = content  # Создание документа
        self.folder = folder # Папка, к которой привязан документ

    def rename(self, new_title):
        # Метод переименования документа
        self.title = new_title

    def delete(self):
        # Метод удаления документа
        del self  # Удаление объекта документа

class Folder:
    def __init__(self, name):
        # Конструктор класса Folder, инициализирующий его атрибуты
        self.name = name  # Название папки
        self.document = []  # Список документов в этой папке

    def add_document(self, document):
        # Метод добавления документа в папку
        self.document.append(document)  # Добавление переданного документа в список документов папки

    def rename(self, new_name):
        # Метод переименования папки
        self.name = new_name

    def delete_document(self, document):
        # Метод удаления документа из папки
        self.document.remove(document)

    def delete(self):
        # Метод удаления папки
        del self  # Удаление объекта папки


# Создаем папку
folder_1 = Folder("Folder 1")

# Создаем документы
doc_1 = Document("Document 1", "Content 1", folder_1)
doc_2 = Document("Document 2", "Content 2", folder_1)
doc_3 = Document("Document 3", "Content 3", folder_1)

# Добавляем документы в папку
folder_1.add_document(doc_1)
folder_1.add_document(doc_2)
folder_1.add_document(doc_3)

# Проверяем содержимое папки перед удалением
print("Document in Folder 1 before deletion:")
for document in folder_1.document:
    print(document.title)

# Удаляем один из документов из папки
folder_1.delete_document(doc_2)

# Переименовываем один из оставшихся документов
doc_3.rename("Renamed Document 3")

# Проверяем содержимое паки после удаления и переименовывания
print("\nDocuments in Folder 1 after deletion and renaming:")
for document in folder_1.document:
    print(document.title)

# Удаляем папку
folder_1.delete()

sdbdsddfv  # test regesdvfsdvsdsd
sfdvsd
sdv
