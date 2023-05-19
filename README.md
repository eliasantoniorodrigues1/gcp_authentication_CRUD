# GCP Authentication CRUD

Simple repository to authenticate on Google GCP and insert a dataset into it

You can use different ways off authenticating in Google GCP, by putting your credentials
in your enviroment variables or just using the auth method in your Colab account.

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
    
Exemplo 2:

