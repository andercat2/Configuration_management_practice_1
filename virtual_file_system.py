import zipfile
import os

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.fs = {}
        # Устанавливаем начальную директорию как корневую
        self.current_dir = '/home/user/'  
        self.load_zip()

    def load_zip(self):
        with zipfile.ZipFile(self.zip_path, 'r') as z:
            for file in z.namelist():
                self.fs[file] = z.read(file).decode('utf-8')
                print(f"Loaded file: {file}")
    
    def list_dir(self):
        # Фильтруем только те файлы и папки, которые непосредственно находятся в текущей директории
        result = []
        for path in self.fs.keys():
            # Убираем начальный '/' если есть и делим путь
            path = path.strip('/')
            # Проверяем, что файл находится непосредственно в текущей директории
            if path.startswith(self.current_dir.strip('/')) and len(path.split('/')) == len(self.current_dir.strip('/').split('/')) + 1:
                result.append(path.split('/')[-1])  # Возвращаем имя файла/папки
        return result
    
    def change_dir(self, path):
    # Переход на уровень выше
        if path == '..':
            self.current_dir = '/'.join(self.current_dir.strip('/').split('/')[:-1]) + '/'
            if self.current_dir == '':
                self.current_dir = '/'
        else:
            # Переход в относительную директорию
            new_path = os.path.join(self.current_dir.strip('/'), path).strip('/')
            if new_path + '/' in self.fs:
                self.current_dir = '/' + new_path + '/'
            else:
                print("Directory not found")

    def read_file(self, filename):
        return self.fs.get(filename, "File not found")

    def get_pwd(self):
        return self.current_dir
