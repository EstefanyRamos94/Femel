import pymysql 
from dotenv import load_dotenv

# Usar la funcion de dotenv:
load_dotenv()

pymysql.install_as_MySQLdb()