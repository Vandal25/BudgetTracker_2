import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Elephant = True


def get_database():
    if Elephant:
        return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'qeglgaai',
            'USER': 'qeglgaai',
            'PASSWORD': '2qY3GsbrjA1jwsFGq1FwMAdRvuJJ5NTE',
            'HOST': 'rogue.db.elephantsql.com',
            'PORT': '5432'
        }
    else:
        return{
            'ENGINE' : 'django.db.backends.sqlite3' ,
            'NAEM' : os.path.join(BASE_DIR, 'db.sqlite3')
         }
