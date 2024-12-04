import pandas as pd
import os

def export_data_to_csv(data, filename):
    ''' Функция сохранения данных как CSV файла '''

    file_path = f'{os.path.dirname(__file__)}\\database'
    full_filename = f"{file_path}\\{filename}.csv"
    ''' Задание полного имени файла '''
    data.to_csv(full_filename, sep='\t', encoding='utf-8', index=False, header=True)
    ''' Запись данных в файл '''
    print(f"Данные записаны в файл {full_filename}")
    ''' Сообщение о записи файла '''
