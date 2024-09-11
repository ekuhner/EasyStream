""" Postgresql connection """
from configparser import ConfigParser
import psycopg2

class pconnect:
    """ Postgresql connection """
    def connect(self,config):
        
        """ Connect to the PostgreSQL database server """
        try:
            # connecting to the PostgreSQL server
            with psycopg2.connect(**config) as conn:
                print('Connected to the PostgreSQL server.')
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def load_config(self,filename='database.ini', section='postgresql'):
        """ Load database configuration from file """
        parser = ConfigParser()
        parser.read(filename)
        with open(filename) as f:
            print(f.read())
        # get section, default to postgresql
        config = {}
        
        if parser.has_section(section):
            params = parser.items(section)
            print(params)
            for param in params:
                config[param[0]] = param[1]
        else:
            print(f'Section {section} not found in the {filename} file')
            return None
            #raise Exception(f'Section {section} not found in the {filename} file')

        return config
if __name__ == '__main__':
    config = pconnect().load_config()
    pconnect().connect(config)