from yandex import Yandex_user


def test_Yandex_user():
    # вместо folder_test вставьте имя папки и токен вместо token
    newFolder = Yandex_user('folder_test', 'token')
    result = newFolder.new_folder()
    assert result == 201
