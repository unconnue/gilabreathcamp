from database.database_functions import *


class Camper:
    """
    a class that represent camper which is responsible for validating data before commiting to the database
    """
    def __init__(self, camper_id, first_name = '', last_name = '', birth_date = '', gender = '', address = ''):
        """
        initialize a camper object, you can only define a camper id
        """
        self.__camper_id__ = camper_id
        self.__first_name__ = first_name
        self.__last_name__ = last_name
        self.__birth_date__ = birth_date
        self.__gender__ = gender
        self.__address__ = address

    def insert_camper(self):
        """
        insert a camper record into the db after validating
        """
        insert_camper_into_db(self.__first_name__, self.__last_name__, self.__birth_date__, self.__gender__, self.__address__)

    def update_camper(self):
        """
        update a camper record to the db after validating
        """
        update_camper_to_db(self.__camper_id__, self.__first_name__, self.__last_name__, self.__birth_date__, self.__gender__, self.__address__)

    def select_camper(self):
        """
        select a camper record from the db after validating
        returns a camper object
        """
        return select_camper_by_id(self.__camper_id__)

    def delete_camper(self):
        """
        delete a camper record from the db after validating
        """
        return delete_camper_by_id(self.__camper_id__)

    @staticmethod
    def get_all_ids():
        return get_all_campers_ids()

    def __str__(self):
        return self.__camper_id__, self.__first_name__, self.__last_name__, self.__birth_date__, self.__gender__, self.__address__
     
    @staticmethod
    def get_all_ids_assigned_camp():
        return get_all_ids_assigned_camp_db()
