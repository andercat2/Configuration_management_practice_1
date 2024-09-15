import os


def ls(vfs):
    return vfs.list_dir()

def cd(vfs, path):
    vfs.change_dir(path)

def pwd(vfs):
    return vfs.get_pwd()

def cat(vfs, filename):
    # Создаем полный путь к файлу
    full_path = os.path.join(vfs.current_dir.strip('/'), filename).strip('/')
    
    # Выведем полный путь для отладки
    print(f"Trying to open file: {full_path}")
    
    # Проверяем, существует ли файл в виртуальной файловой системе
    if full_path in vfs.fs:
        return vfs.fs[full_path]
    else:
        return "File not found"

def wc(vfs, filename):
    content = vfs.read_file(filename)
    lines = content.count('\n')
    words = len(content.split())
    chars = len(content)
    return lines, words, chars
