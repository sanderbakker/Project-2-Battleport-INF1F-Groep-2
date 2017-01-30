"""Module containing save and load classes"""
from modules import mysql
from datetime import datetime
import pygame
pygame.init()
mysql_con = mysql.mysql()


class Save:
    """Main save class containing the needed logic to write savestates to the DB"""
    def __init__(self, name, x, y, card_id):
        self.save_id = datetime.now().time()
        self.saved_player_id = datetime.now().time()
        self.ship_name = name
        self.x = x
        self.y = y
        self.card_id = card_id

    def savestate(self):
        """Writes data into the DB"""
        mysql_con.update("INSERT INTO saved_ships (saved_ship_id, save_id, saved_player_id, ship_name, x, y, card_id)")


class Load:
    """Main load class containing the needed logic to read savestates to the DB"""
    def __init__(self):
        self.save_id = mysql_con.select("SELECT save_id FROM saved_ships")
        self.saved_player_id = mysql_con.select("SELECT saved_player_id FROM saved_ships")
        self.ship_name = mysql_con.select("SELECT ship_name FROM saved_ships")
        self.x = mysql_con.select("SELECT x FROM saved_ships")
        self.y = mysql_con.select("SELECT y FROM saved_ships")
        self.card_id = mysql_con.select("SELECT card_id FROM saved_ships")

