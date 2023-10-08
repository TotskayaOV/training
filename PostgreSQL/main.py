import psycopg2
import datetime
import decimal
from google_api import GoogleApi
from config import logpass


class UpdateSheets(GoogleApi):
    def __init__(self, logpass: tuple):
        GoogleApi.__init__(self)
        self.dbname, self.user, self.password, self.host = logpass
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)

    def get_data_string(self, string_data: list):
        '''
        Обработка данных

        :param string_data: Набор данных
        :return: Набор преобразованных данных
        '''
        string = []
        for item in string_data:
            if isinstance(item, datetime.datetime):
                string.append(item.strftime('%Y-%m-%d %H:%M'))
            elif isinstance(item, datetime.date):
                string.append(item.strftime('%Y-%m-%d'))
            elif isinstance(item, str):
                string.append(item)
            elif isinstance(item, decimal.Decimal):
                string.append(float(item))
            else:
                string.append(item)
        return string

    def read_data_db(self, request_sql):
        '''
        Чтение данных из PostgreSQL

        :return: Данные запроса
        '''

        cursor = self.conn.cursor()
        cursor.execute(request_sql)
        data = [[desc[0] for desc in cursor.description]]
        for string_data in cursor.fetchall():
            data.append(self.get_data_string(string_data))
        return data

    def start_update(self, list_name, request_sql):
        '''
        Метод реализует запуск скрипта
        '''
        api = GoogleApi()
        
        data = self.read_data_db(request_sql=request_sql)
        api.clear_list(list_name, f'A:Z')
        api.write_to_sheets(list_name, f'A1:{len(data)}', data)


if __name__ == '__main__':
    sheet = UpdateSheets(logpass)
    sheet.start_update('По рассылкам', '''with tmp_2 AS DESC''')
    sheet.start_update('По дням', '''with tmp AS ime DESC''')
