from config_reader import read_config
from virtual_file_system import VirtualFileSystem
from shell_gui import ShellGUI

if __name__ == "__main__":
    # Чтение конфигурационного файла
    user_name, computer_name, zip_path, script_path = read_config(r"C:\Users\Vegas\Desktop\Configuration_management_practice_1-main\config.xml")
    
    # Создание виртуальной файловой системы
    vfs = VirtualFileSystem(zip_path)
    
    # Запуск графического интерфейса
    app = ShellGUI(user_name, computer_name, vfs)
    app.mainloop()
