import os
# To set enviromebtal variables
# SMG_TYPE_STORAGE = storage type to use (db or filestorage)
# SMG_MYSQL_USER = my sql username
# SMG_MYSQL_PWD = mysql user password
# SMG_MYSQL_HOST = mysql host
# SMG_MYSQL_DB = mysql database
# SMG_ENV = testing enviroment or production


#  Use the code below to set your enviromental variable automativally.
#  Just replace the empty strings with the appropriate values
os.environ["SMG_TYPE_STORAGE"] = 'file'
# os.environ["SMG_MYSQL_USER"] = ''
# os.environ["SMG_MYSQL_PWD"] = ''
# os.environ["SMG_MYSQL_HOST"] = ''
# os.environ["SMG_MYSQL_DB"] = ''
# os.environ["SMG_ENV"] = ''

storage_t = os.getenv("SMG_TYPE_STORAGE")

if  storage_t == "db":
    from models.engine.db_storage import DbStorage
    storage = DbStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()