# GCP Authentication CRUD

Simple repository to authenticate on Google GCP and insert a dataset into it

You can use different ways off authenticating in Google GCP, by putting your credentials
in your enviroment variables or just using the auth method in your Colab account.

#### Use this method when writing a Script / Function in your code
Exemple:

        import os
        import sys

        sys.path.append('..')
        # base directory
        BASE_DIR = os.path.join(os.path.dirname('__file__'))

        # adding credentials in enviroment variable
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
            BASE_DIR, 'folder/credential.json')

        # data configuration
        project_id = 'your_project_id'
        table_name = 'dataset.table'
    
#### Use this method when usign Google Colab
Exemplo 2:
        import pandas as pd
        from google.cloud import bigquery

        # this code needs to be at google colab to work properly
        from google.colab import auth
        auth.authenticate_user()

#### Function to Insert data by Pandas DataFrame
        def insert_gcp(df: pd.DataFrame, project_id: str, table: str, method='append'):
          '''
              this function find out the destination schema and perform an insert
              into the table passed as a parameter
              params: df : your dataset with record to be inserted into a table
              params: project_id: A string containing a name of your project
              params: table: A name using dataset.table notation to set a destination
              to your insert process.

          '''
          # rename to columns from my dataset according to my table
          df.columns = [i.name for i in table.schema]

          # inserting with generate Schema
          df.to_gbq(destination_table=table_name, project_id=project_id, table_schema=generate_schema, if_exists='append')
          
#### Execute a SELECT statment
        # create client object
        client = bigquery.Client()

        query = f'''SELECT max(data_atualizacao) as data FROM `{table}`'''
        query_job = client.query(query)
