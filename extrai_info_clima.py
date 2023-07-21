import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=6)

# formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Araras'
key = 'WNSHRU6ESNHWKM3W7CYX92A3L'

URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
            f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL)
print(dados)

file_path = f'C:/Users/carlos.perez/developer/WeatherPipeline/results/semana={data_inicio}/'

# Verificar se o diretório já existe
if os.path.exists(file_path):
    # Remover o diretório e todos os arquivos dentro dele
    for root, dirs, files in os.walk(file_path, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(file_path)

os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv', mode='w')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv', mode='w')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv', mode='w')

