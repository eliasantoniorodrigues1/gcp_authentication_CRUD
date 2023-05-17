import pandas as pd
from google.cloud import bigquery

# this code needs to be at google colab to work properly
from google.colab import auth
auth.authenticate_user()

# project data
project_id = 'your_project_id'
table = 'dataset.moedas_historico_cotacoes'

# client data
client = bigquery.Client(project=project_id)
table = client.get_table(table)

# dataset
df = pd.read_csv('currency_history_rates_USD_missing.csv')

new_columns = ['paridade', 'nome', 'unidades_por_codigo', 'code_por_unidade', 'data_atualizacao', 'codigo']
df.drop(columns=['index'], inplace=True)
df.columns = new_columns

columns = df.columns.tolist()
print(columns)

# changing position of columns on dataset
new_position_column = df.pop(columns[-1])
df.insert(0, 'codigo', new_position_column)

# dict compherension
generate_schema = [{'name': i.name, 'type': i.field_type} for i in table.schema]
generate_schema


# inserting with generate Schema
df.to_gbq(project_id=project_id, destination_table=table, table_schema=generate_schema, progress_bar=True, if_exists='append')
