import requests
import pytest

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

