import unittest
import os
from virtual_file_system import VirtualFileSystem
from commands import ls, cd, pwd, cat, wc

class TestShellCommands(unittest.TestCase):
    def setUp(self):
        # Подготовьте zip-файл с тестовыми данными
        self.vfs = VirtualFileSystem("test_fs.zip")

    def test_ls(self):
        # Проверьте, что файлы корректно отображаются
        self.assertIn('file1.txt', ls(self.vfs))

    def test_cd(self):
        # Переход в поддиректорию и проверка текущей директории
        cd(self.vfs, 'documents')
        expected_path = os.path.normpath('home/user/documents/')
        self.assertEqual(self.vfs.current_dir, expected_path)

    def test_pwd(self):
        # Проверка текущей директории
        expected_pwd = os.path.normpath('home/user/')
        self.assertEqual(pwd(self.vfs), expected_pwd)

    def test_cat(self):
        # Проверка команды cat
        content = cat(self.vfs, 'testfile.txt')
        self.assertEqual(content, 'This is a test file.\n')

    def test_wc(self):
        # Проверка подсчёта строк, слов и символов
        lines, words, chars = wc(self.vfs, 'testfile.txt')
        self.assertEqual(lines, 0)
        self.assertEqual(words, 3)
        self.assertEqual(chars, 14)

if __name__ == "__main__":
    unittest.main()
