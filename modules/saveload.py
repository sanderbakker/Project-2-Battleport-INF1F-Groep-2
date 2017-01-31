"""Module containing save and load classes"""
from modules import mysql
from datetime import datetime
import time
import pygame
pygame.init()



class Save:
    """Main save class containing the needed logic to write savestates to the DB"""
    def __init__(self, name, x, y, card_id, player_name, password, player_score, saved_card_name, score, event):
        """Collects needed data to read to DB"""

        """saved_ships table"""
        self.name = name
        self.x = x
        self.y = y
        self.card_id = card_id

        """players table"""
        self.player_name = player_name
        self.password = password
        self.player_score = player_score

        """saved_cards table"""
        self.saved_card_name = saved_card_name

        """saved_score table"""
        self.score = score

        """Catches keypresses"""
        self.event = event

    def sendsave(self, event):
        """Writes data into the DB"""
        mysql_con = mysql.mysql()
        loop = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                """Write to saved_ships table"""
                mysql_con.update(
                    "INSERT INTO `saved_ships` (`ship_name`,"
                    " `x`, `y`, `card_id`) VALUES (' {}, {}, {}' + "'32'.format(self.name, self.x, self.y))

                """Write to players table"""
                mysql_con.update("INSERT INTO `players` (`player_name`, `password`, `player_score`) VALUES ('{}, {}, {}'".format(self.name, self.x, self.y))

                """Write to saved_cards table"""
                mysql_con.update(
                    "INSERT INTO `saved_cards` (`saved_card_name`) VALUES ('{}'".format(self.saved_card_name))

                """Write to saved_score table"""
                mysql_con.update(
                    "INSERT INTO `score` (`score`) VALUES ('{}'".format(self.score))

                print("Saved.")

    def showsave(self, event):
        mysql_con = mysql.mysql()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print(mysql_con.select("SELECT * FROM players ORDER BY score DESC LIMIT 6"))
                time.sleep(1)

class Load:
    """Main load class containing the needed logic to read savestates to the DB"""
    def __init__(self):
        mysql_con = mysql.mysql()

        """Read saved_ships table"""
        self.ship_name = mysql_con.select("SELECT ship_name FROM saved_ships")
        self.x = mysql_con.select("SELECT x FROM saved_ships")
        self.y = mysql_con.select("")
        self.card_id = mysql_con.select("SELECT card_id FROM saved_ships")

        """Read players table"""
        self.player_name = mysql_con.select("SELECT player_name FROM players")
        self.password = mysql_con.select("SELECT password FROM players")
        self.player_score = mysql_con.select("SELECT player_score FROM players")

        """Read saved_cards table"""
        self.saved_card_name = mysql_con.select("SELECT saved_card_name FROM saved_cards")

        """Read saved_score table"""
        self.score = mysql_con.select("SELECT score FROM saved_score")

    def getsave(self, event):
        mysql_con = mysql.mysql()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_MINUS:
                print(mysql_con.select("SELECT * FROM saved_ships"))
                time.sleep(1)