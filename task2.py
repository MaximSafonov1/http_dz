from pprint import pprint
import requests

class YaUploader:

  def __init__(self, token):
    self.token = token

  def get_headers(self):
    return {'Content-Type': 'application/json',
    'Authorization': 'OAuth {}'.format(self.token)}

  def get_files_list(self):
    file_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    headers = self.get_headers()
    response = requests.get(file_url, headers=headers)
    return response.json()

  def get_upload_link(self, disk_file_path):
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = self.get_headers()
    params = {"path": disk_file_path, "overwrite": "true"}
    response = requests.get(upload_url, headers=headers, params=params)
    return response.json()

  def upload_file_to_disk(self, disk_file_path, filename):
    href = self.get_upload_link(disk_file_path=disk_file_path).get('href', '')
    response = requests.put(href, data=open(filename, 'rb'))
    if response.status_code == 201:
      print('Загрузка выполнена успешно.')



if __name__ == '__main__':
  file = YaUploader(token='')
  file.upload_file_to_disk('Netology_dz/file_news.txt', 'Krasnodar_news')