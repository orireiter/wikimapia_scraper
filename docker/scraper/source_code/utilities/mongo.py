from pymongo import MongoClient
import pymongo


def db_connect(connection_string: str, db: str, collection: str):
    try:
        # creating a client
        db_client = MongoClient(connection_string)

        # returning a connection to db so you only need to query/insert afterwards
        return db_client[db][collection]

    except:
        print('Error: db related')
        raise Exception('Error: db related')


def create_ttl_in_collections(index_name: str, ttl_interval_in_seconds: int, *collections):
    '''
        takes a ttl index name, and a ttl integer, and mongo collections.
        creates this index in those collections.
    '''
    for collection in collections:
        collection.create_index(
            index_name, expireAfterSeconds=ttl_interval_in_seconds)


def is_collection(connection_string: str, db: str, collection: str):
    '''
        connects to a mongo server and checks if 
        said collection exists in that db.
    '''
    
    connection = MongoClient(connection_string)[db]

    if collection in connection.list_collection_names():
        return True
    else:
        return False
                                        