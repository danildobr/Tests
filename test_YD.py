import requests
import pytest
# Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

# Пример положительных тестов:

# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.

class TestYDCreateFolder:
    def setup_method(self) -> None:
        self.headers = {
            'Authorization': 'OAuth токен '
            }
    
    @pytest.mark.parametrize(
        'param,folder_name,status',
        (
                ('path', 'Photos', 201),
                ('path', 'VK_Photos', 409),
                ('path', '', 400),
        )
    )
    def test_create_folder(self, param, folder_name, status):
        params = {
            param: folder_name
        }

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        assert response.status_code == status

