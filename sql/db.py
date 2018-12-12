import sqlite3
from sqlite3 import Error
import logging as log


class FlowerDB():
    __database_location__ = "./sql/database/flowers.db"

    def create_connection(self):
        """ 
        Connect to the flowers database
        """
        try:
            conn = sqlite3.connect(self.__database_location__)
            log.info("Successfully connected to flower database. (sqlite3 version " + sqlite3.version + ")")
            return conn
        except Error as e:
            log.error(e)

    def get_flowers_list(self, conn):
        """
        Pull a list of all flowers
        """
        c = conn.cursor()
        c.execute("SELECT comname FROM flowers ORDER BY comname")

        rows = c.fetchall()
        c.close()

        return rows

    def get_flower_details(self, conn, flower):
        """
        Pull details for a specific flower
        """
        c = conn.cursor()
        c.execute(f"SELECT * FROM flowers WHERE comname=?", (flower,))

        rows = c.fetchall()
        c.close()

        return rows

    def get_n_recent_sightings(self, conn, flower, limit):
        """
        Pull n most recent sightings of a flower
        """
        c = conn.cursor()
        c.execute(f"SELECT * FROM sightings WHERE name=? ORDER BY sighted DESC LIMIT ?", (flower, limit))

        rows = c.fetchall()
        c.close()

        return rows

    def update_flowers(self, conn, flower, genus, species):
        """
        Update flower information
        """
        c = conn.cursor()
        c.execute(f"UPDATE flowers SET genus=?, species=? WHERE comname=?", (genus, species, flower))
        result = c.rowcount
        c.close()

        return result

    def insert_new_sighting(self, conn, flower, person, location, sighted):
        """
        Insert new sighting
        """
        c = conn.cursor()
        c.execute(f"INSERT INTO sightings VALUES (?, ?, ?, ?)", (flower, person, location, sighted))
        result = c.rowcount
        c.close()

        return result

