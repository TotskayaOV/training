import httplib2
import apiclient
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


class GoogleApi:
    def __init__(self):
        # Файл, полученный в Google Developer Console
        CREDENTIALS_FILE = 'creds.json'
        # ID Google Sheets документа (можно взять из его URL)
        self.spreadsheet_id = '16Dn_xxIVur5XOk0HJee1GNW5ZwbQJ27Vjvy8OyM_nN0'

        # Авторизуемся и получаем service — экземпляр доступа к API
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        self.service = discovery.build('sheets', 'v4', http=httpAuth)

    def read_to_sheets(self, list_name, range):
        '''
        Запрос на получение данных таблицы
        :param list_name: Название листа таблицы
        :param range: Диапозон ячеек (A10:B20)
        :return: Данные ячеек
        '''
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=f'{list_name}!{range}',
            majorDimension='COLUMNS'
        ).execute()
        return values['values'][0]

    def write_to_sheets(self, list_name, range, item):
        '''
        Запрос на запись данных в таблицу
        :param list_name: Название листа в таблице
        :param range: Диапозон ячеек (A10:B20)
        :param item: Набор данных на запись
        '''
        values = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": f"{list_name}!{range}",
                     "majorDimension": "ROWS",
                     "values": item}
                ]
            }
        ).execute()

    def create_new_list(self, new_sheet_title):
        '''
        Создание нового листа
        :param new_sheet_title: Название нового листа
        '''
        requests = []

        requests.append({
            'addSheet': {
                'properties': {
                    'title': new_sheet_title
                }
            }
        })

        body = {
            'requests': requests
        }

        response = self.service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body=body).execute()

    def get_list(self):
        '''
        Получение всех листов таблицы
        :return: Массив листов
        '''
        sheet_metadata = self.service.spreadsheets().get(spreadsheetId=self.spreadsheet_id).execute()
        properties = sheet_metadata.get('sheets')

        return [item.get("properties").get('title') for item in properties]

    def clear_list(self, list_name, range):
        '''
        Запрос на очистку данных таблицы
        :param list_name: Название листа таблицы
        :param range: Диапозон ячеек (A10:B20)
        '''
        self.service.spreadsheets().values().clear(
            spreadsheetId=self.spreadsheet_id,
            range=f'{list_name}!{range}'
        ).execute()
