import os

import os

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.fs = {}
        self.current_dir = os.path.join('home', 'user')
        self.load_zip()

    def load_zip(self):
        import zipfile
        with zipfile.ZipFile(self.zip_path, 'r') as z:
            for file in z.namelist():
                self.fs[os.path.normpath(file)] = z.read(file).decode('utf-8')
                print(f"Loaded file: {file}")

    def list_dir(self):
        result = []
        for path in self.fs.keys():
            norm_path = os.path.normpath(path)
            if norm_path.startswith(self.current_dir):
                parts = norm_path[len(self.current_dir):].strip(os.sep).split(os.sep)
                if len(parts) == 1:
                    result.append(parts[0])
        return result

    def change_dir(self, path):
        new_dir = os.path.join(self.current_dir, path)
        new_dir = os.path.normpath(new_dir)  # Преобразуем путь
        if new_dir in self.fs or new_dir + os.sep in self.fs:
            self.current_dir = new_dir
        else:
            print("Directory not found")


    def read_file(self, filename):
        return self.fs.get(filename, "File not found")

    def get_pwd(self):
        return self.current_dir
