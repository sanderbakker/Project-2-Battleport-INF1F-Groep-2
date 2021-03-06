"""

Play the game by running this file.

"""

# Import the required modules 
import pygame, sys, pymysql, time

# Import all files stated in the __all__ variable in modules/__init__.py
from modules import *

from view import *
import game
from modules import ships
from modules import settings

"""Sets window title"""
pygame.display.set_caption("Battleport")

"""Sets player names"""
Player1 = player.Player(1, login.PlayerName().get_name(), 'red')
Player2 = player.Player(2, login.PlayerName2().get_name(), 'blue')
Players = {1: Player1, 2: Player2}


""" display menu screen """
menu_screen = menu.Menu(20, 800, 575)
menu_screen.show()
sidebar_screen = ''
Game = game.Game(800, 575)
Game.set_menu(menu_screen)

Turn = player.Turn(Player1)
press = pygame.key.get_pressed()

field_size = 400

"""Start save logic for ship movement"""
ship_list_player1 = []
ship_list_player2 = []
count = 0
p1_count, p2_count, count = 0, 0, 0

"""Instantiate ships player 1"""
Furgo = ships.Saltire("Furgo Saltire", 0, 0, 'red')
Silver = ships.Windsurf("Silver Whisper", 0, 'red')
Windsurf = ships.Windsurf("Windsurf", 0, 0, 'red')
Merapi = ships.Amadea("Merapi", 0, 0, 'red')
ship_list_player1.extend([Furgo, Silver, Windsurf, Merapi])
ship_list_player1[0].y, ship_list_player1[1].y, ship_list_player1[2].y, ship_list_player1[3].y = 19, 18, 18, 17

"""Instantiate ships player 2"""
Santa = ships.Saltire("Santa Bettina", 0, 0, 'blue')
Sea = ships.Windsurf("Sea Spirit", 0, 0, 'blue')
Intensity = ships.Windsurf("Intensity", 0, 0, 'blue')
Amadea = ships.Amadea("Amadea", 0, 0, 'blue')

ship_list_player2.extend([Santa, Sea, Intensity, Amadea])
ship_list_player2[0].y, ship_list_player2[1].y, ship_list_player2[2].y, ship_list_player2[3].y = 2, 3, 3, 4


""" Mines """
mine_list_player1 = []
mine_list_player2 = []

Player1.set_ships(ship_list_player1)
Player2.set_ships(ship_list_player2)

Player1.set_mines(mine_list_player1)
Player1.set_mines(mine_list_player2)

#remove_ship()

sounds.Sounds().background_sound()
while not Game.events():
    # get the current player
    Player = Turn.player
    if(Player.get_id() == 1):
        Other_player = Player2
    else:
        Other_player = Player1



    Turn.set_ships(ship_list_player1, ship_list_player2)

    Game.get_screen().fill((235, 235, 235))

    help_img = pygame.image.load("assets/table_back2.png")
    Game.get_screen().blit(help_img, (0, 0))

    #grid_bg = pygame.image.load("assets/grid_field2.png")
    #Game.get_screen().blit(grid_bg, (50, 50))

    bar = pygame.image.load("assets/bar.png")
    Game.get_screen().blit(bar, (100, 0))

    # show the current player stats ( name and score )
    player_turn.Show(Game, Player)

    # show sidebar
    sidebar_screen = sidebar.Show(Game, Players, Turn, menu_screen)

    # show deck of current player
    deck.Show(Game, Player, Turn, sidebar_screen)

    main_grid = grid.Grid({
        'screen': Game.get_screen(),
        'x_blocks': 20,
        'y_blocks': 20,
        'opacity_grid': field_size,
        'move_grid': 50,
        #'background_color': (0, 255, 0)
    })

    for mine in player.Turn(Other_player).get_mines():
        main_grid.Place_Mine(mine[0], mine[1])

    Game.set_grid(main_grid)
    click = Game.get_grid_click()

    """"Loads ships from array (WIP)"""
    for i in range(0, len(ship_list_player2)):
        for x in range(0, ship_list_player2[i].size):
            main_grid.Place_Player_2(i, ship_list_player2[i])
    main_grid.reset_ship_counts()
    for i in range(0, len(ship_list_player1)):
        for x in range(0, ship_list_player1[i].size):
            main_grid.Place_Player_1(i, ship_list_player1[i])

    chk = sounds.sounds.check_sound()
    chkgame = sounds.sounds.check_gamesound()

    """Start ship placement/game logic (WIP)"""
    if click:
        count += 1


        if count == 1:
            if chkgame == True:
                sounds.Sounds().place_ship()
            Turn = player.Turn(Player1)
            Turn.add_normal_card(cards.normal_card().get_random())
            Turn.add_normal_card(cards.normal_card().get_random())
        if count == 2:

            if chkgame == True:
                sounds.Sounds().place_ship()
            Turn = player.Turn(Player2)
            Turn.add_normal_card(cards.normal_card().get_random())
            Turn.add_normal_card(cards.normal_card().get_random())
        if count % 2 != 0 and count < 9:
            if click[0] == ship_list_player1[0].x:

                if chkgame == True:
                    sounds.Sounds().error()
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player1[1].x:

                if chkgame == True:
                    sounds.Sounds().error()
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player1[2].x:

                if chkgame == True:
                    sounds.Sounds().error()
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player1[3].x:

                if chkgame == True:
                    sounds.Sounds().error()
                print("Invalid placement, try again.")
                count -= 1
            else:

                if chkgame == True:
                    sounds.Sounds().place_ship()
                ship_list_player1[p1_count].x = click[0]
                p1_count += 1

            Turn = player.Turn(Player2)

        elif count % 2 == 0 and count < 9:
            if click[0] == ship_list_player2[0].x:

                if chkgame == True:
                    sounds.Sounds().error()
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player2[1].x:

                if chkgame == True:
                    sounds.Sounds().error()
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player2[2].x:

                if chkgame == True:
                    sounds.Sounds().error()
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player2[3].x:

                if chkgame == True:
                    sounds.Sounds().error()
                print("Invalid placement, try again.")
                count -= 1
            else:

                if chkgame == True:
                    sounds.Sounds().place_ship()
                ship_list_player2[p2_count].x = click[0]
                ship_list_player2[p2_count].y = 1
                p2_count += 1

            Turn = player.Turn(Player1)

        elif count >= 9:
            """Ship movement logic"""
            for ship in Turn.get_ships():
                if (set([click]).intersection(set(ship.get_ship()))):
                    for ship_unselect in Turn.get_ships():
                        ship_unselect.unset_select()

                    ship.set_select()
                    time.sleep(0.15)

    try:
        if count % 2 != 0 and count < 9:
            sidebar_screen.set_placing_ship(ship_list_player2[p2_count])
        elif count % 2 == 0 and count < 9:
            sidebar_screen.set_placing_ship(ship_list_player1[p1_count])
    except IndexError:
        sidebar_screen.set_placing_ship(None)

    for ship in Turn.get_ships():
        if ship.get_select():
            sidebar_screen.set_ship(ship)
            ship.movement(Game.get_event(), Player, Other_player, player.Turn(Other_player))
            ships_in_range = ship.locate_enemy_ships(Turn, Other_player)
            sidebar_screen.draw_attackable_ships(ships_in_range)


    #def remove_ship():
    #        for i in range(3):
    #            if len(ship_list_player1) > 0:
    #                ship_list_player1.remove(ship_list_player1[i - 1])

    """ check if player won """
    won = True
    for ship in Other_player.get_saved_ships():
        if not ship.check_if_dead():
            won = False

    if(won):
        win.win_screen(800, 575, Player, Other_player)

    """Save and load hooks"""
    """Writes player 1 data"""
    #for i in range(0, len(ship_list_player1)):
    #    save(ship_list_player1[i].name, ship_list_player1[i].x, ship_list_player1[i].y, "1337",  "placeholder", "placeholder", 22, "placeholder", 22, Game.get_event()).sendsave(Game.get_event())
    #
    """Writes player 1 data"""
    #for i in range(0, len(ship_list_player2)):
    #    save(ship_list_player2[i].name, ship_list_player2[i].x, ship_list_player2[i].y, "1337", "placeholder", "placeholder", 22, "placeholder", 22, Game.get_event()).sendsave(Game.get_event())

    """Load hook"""

    #remove_ship()
    sidebar_screen.show_instructions()
    #animation.Animation(Game).add_animation()
    Game.update()

# Turn = player.Turn(Player1)