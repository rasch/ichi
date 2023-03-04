#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ICHI - a simple CLI game for one player that plays similar to UNO
Copyright © 2012 Randy Schneck

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details.
"""

import random
import os

###################################
# credits                         #
###################################

credits = '\n\tThis Game was created by Randy Schneck on 30.03.2012 \
\n\tVisit www.randyschneck.com if you like this game.'


###################################
# create empty lists to manage    #
# all game pieces                 #
###################################

all_bugs = []  # populate by running build_all_bugs()
shuffle_bugs = []
bugs_nest = []
player_bugs = []
opponent_bugs = []

whos_turn_isit = []
your_opponent = []

test_ants = []
test_bees = []
test_flys = []
test_spys = []
test_zeros = []
test_ones = []
test_twos = []
test_threes = []
test_fours = []
test_fives = []
test_sixes = []
test_sevens = []
test_eights = []
test_nines = []
test_add2s = []
test_skips = []

opponent_can_play = []
opponent_cant_play = []


###################################
# define items that will be       #
# reused to make games            #
###################################

# standard user input prompt
def prompt():
    ans = input("\n\t\033[1;31mType an option or press ENTER to continue\n\n\t> ")
    if ans == '?':
        clear_screen()
        print(help_me)
        prompt()
        clear_screen()
        return()
    if ans == 'bugs':
        clear_screen()
        print(bugs_information)
        prompt()
        clear_screen()
        return()
    elif ans == 'meet':
        clear_screen()
        for bugs in player_bugs:
            show_bugs_ascii(bugs)
            input("\n\t\033[1;31mPress ENTER to continue")
            clear_screen()
        print("\n\t\033[1;34mThat's your Army. Good Luck Soldier!")
        prompt()
        clear_screen()
        return()
    elif ans == "cheat":
        clear_screen()
        if bugs_nest == []:
            print("\n\tYou can't cheat now.")
            prompt()
        else:
            print("\n\tYou Cheated!")
            print("\n\tThe top card is: %s" % bugs_nest[-1])
            show_bugs_ascii(bugs_nest[-1])
            prompt()
            clear_screen()
        return()
    elif ans == "quit":
        print(credits)
        quit(0)
    elif ans == "1" and whos_turn_isit != [] and player_bugs != [] \
            and len(bugs_nest) >= 1:
        clear_screen()
        if whos_turn_isit[-1] == 'your_turn':
            nest_a_bug()
        else:
            print('You can\'t go out of turn!')
            return()
    elif ans == "2" and whos_turn_isit != [] and player_bugs != [] \
            and len(bugs_nest) >= 1:
        clear_screen()
        if whos_turn_isit[-1] == 'your_turn':
            pick_up_bug()
        else:
            print('You can\'t go out of turn!')
            return()
    else:
        return()


# function for testing broken code
def broken():
    print('\nW\nh\ny\n \na\nr\ne\n \ny\no\nu\n \nb\nr\no\nk\ne\nn\n?')


# function to clear screen
def clear_screen():
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        print('\n' * 100)


# function to populate list: all_bugs
def build_all_bugs():
    bugs = ['ANT', 'BEE', 'FLY', 'SPY']
    ranks = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
             'ADD2', 'ADD2', 'SKIP', 'SKIP']
    for b in bugs:
        for r in ranks:
            bug = '%s-%s' % (r, b)
            all_bugs.append(bug)
    squash = '!SQUASH'
    n = 0
    while n < 8:
        all_bugs.append(squash)
        n = n + 1


# function to shuffle bugs and populate list: shuffle_bugs
# it also empties the list: all_bugs
def shuffle():
    for i in range(len(all_bugs)):
        bug = random.choice(all_bugs)
        all_bugs.remove(bug)
        shuffle_bugs.append(bug)


# function to deal bugs to players -- dealt 2,2,3,3,2,2.
def deal():
    for x in [2, 2, 5, 5, 5, 7, 7]:
        player_bugs.append(shuffle_bugs[x])
        shuffle_bugs.remove(shuffle_bugs[x])
    for y in [0, 0, 0, 0, 0, 0, 0]:
        opponent_bugs.append(shuffle_bugs[y])
        shuffle_bugs.remove(shuffle_bugs[y])


# function to show your bugs
def show_bugs():
    print("\n\t\033[1;34mYour Army of Bugs:")
    for i in player_bugs:
        print('\t\033[1;37m%s' % i)


# funtion to populate test lists for checking bugs
def build_test_groups():
    test_rank = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'ADD2', 'SKIP']
    test_bugs = ['ANT', 'BEE', 'FLY', 'SPY']
    for rank in test_rank:
        test_ants.append('%s-' % rank + 'ANT')
    test_rank = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'ADD2', 'SKIP']
    for rank in test_rank:
        test_bees.append('%s-' % rank + 'BEE')
    for rank in test_rank:
        test_flys.append('%s-' % rank + 'FLY')
    for rank in test_rank:
        test_spys.append('%s-' % rank + 'SPY')
    for bug in test_bugs:
        test_zeros.append('0-' + bug)
    for bug in test_bugs:
        test_ones.append('1-' + bug)
    for bug in test_bugs:
        test_twos.append('2-' + bug)
    for bug in test_bugs:
        test_threes.append('3-' + bug)
    for bug in test_bugs:
        test_fours.append('4-' + bug)
    for bug in test_bugs:
        test_fives.append('5-' + bug)
    for bug in test_bugs:
        test_sixes.append('6-' + bug)
    for bug in test_bugs:
        test_sevens.append('7-' + bug)
    for bug in test_bugs:
        test_eights.append('8-' + bug)
    for bug in test_bugs:
        test_nines.append('9-' + bug)
    for bug in test_bugs:
        test_add2s.append('ADD2-' + bug)
    for bug in test_bugs:
        test_skips.append('SKIP-' + bug)


# randomly choose an opponent and store in list: your_opponent
def choose_opponent():
    enemy = random.choice(range(1, 5))
    if enemy == 1:
        your_opponent.append('Admiral Arachnid')
    elif enemy == 2:
        your_opponent.append('Commander Cockroach')
    elif enemy == 3:
        your_opponent.append('Colonol Cricket')
    elif enemy == 4:
        your_opponent.append('General Dragonfly')

# function to decide which bug army goes first
# starts list: whos_turn_isit
def who_first():
    your_bug = random.choice(shuffle_bugs)
    comp_bug = random.choice(shuffle_bugs)
    print("\n\t\033[1;34mYour Bug is:")
    show_bugs_ascii(your_bug)
    print("\n\n\t\033[1;34m%s's Bug is:" % your_opponent[-1])
    show_bugs_ascii(comp_bug)
    if your_bug < comp_bug:
        print('\n\t\033[1;34mYou have the lowest ranking bug! \
                \n\tYou Start the Battle.')
        whos_turn_isit.append('your_turn')
    elif your_bug > comp_bug:
        print('\n\t\033[1;34mYour opponent has the lowest ranking bug!\
                \n\tThey will Start the Battle.')
        whos_turn_isit.append('opponents_turn')
    else:
        your_bug == comp_bug
        print("\n\t\033[1;34mThey are equal, let's try again.")
        prompt()
        clear_screen()
        who_first()


# function to start the bug nest with one from shuffle_bugs
def start_nest():
    top_bug = shuffle_bugs[0]
    while top_bug == '!SQUASH':
        shuffle_bugs.remove(top_bug)
        shuffle_bugs.append(top_bug)
        top_bug = shuffle_bugs[0]
    print("\n\t\033[1;34mThe first bug in the nest is:")
    show_bugs_ascii(top_bug)
    bugs_nest.append(top_bug)


# function to check whos turn it is and direct to appropriate function
def whos_turn():
    if whos_turn_isit[-1] == 'your_turn':
        your_play()
    elif whos_turn_isit[-1] == 'opponents_turn':
        opponents_play()
    else:
        broken()


# function to show your opponent
def show_opponent():
    if 'Admiral Arachnid' in your_opponent:
        ascii_arachnid(arachnid_info)
    elif 'Commander Cockroach' in your_opponent:
        ascii_cockroach(cockroach_info)
    elif 'Colonol Cricket' in your_opponent:
        ascii_cricket(cricket_info)
    elif 'General Dragonfly' in your_opponent:
        ascii_dragonfly(dragonfly_info)
    else:
        broken()


# function to show ascii art for bugs
def show_bugs_ascii(x):
    if x in test_ants:
        ascii_ant(x)
    elif x in test_bees:
        ascii_bee(x)
    elif x in test_flys:
        ascii_fly(x)
    elif x in test_spys:
        ascii_spy(x)
    elif x == '!SQUASH':
        ascii_squash(x)
    else:
        broken()


# function to define action bugs when played by player
def bug_action():
    z = bugs_nest[-1]
    if z in test_skips:
        show_bugs_ascii(bugs_nest[-1])
        print("\n\tYou just skipped %s! Good Move." % your_opponent[-1])
        if len(player_bugs) == 1:
            ascii_title("You only have 1 Bug left!")
        if len(player_bugs) == 0:
            clear_screen()
            ascii_winner(credits)
            score()
            quit(0)
        whos_turn_isit.append('your_turn')
        prompt()
        clear_screen()
        whos_turn()
    elif z in test_add2s:
        show_bugs_ascii(bugs_nest[-1])
        print("\n\tYou just skipped %s and they had to \
                \n\trecruit 2 more Bugs! Nice." % your_opponent[-1])
        opponent_bugs.append(shuffle_bugs[0])
        opponent_bugs.append(shuffle_bugs[1])
        shuffle_bugs.remove(shuffle_bugs[0])
        shuffle_bugs.remove(shuffle_bugs[0])
        whos_turn_isit.append('your_turn')
        if len(player_bugs) == 1:
            ascii_title("You only have 1 Bug left!")
        if len(player_bugs) == 0:
            clear_screen()
            ascii_winner(credits)
            score()
            quit(0)
        prompt()
        clear_screen()
        whos_turn()
    elif z == '!SQUASH':
        show_bugs_ascii(bugs_nest[-1])
        n = 1
        squash_value = random.choice(range(1, 5))
        while n <= squash_value:
            opponent_bugs.append(shuffle_bugs[0])
            shuffle_bugs.remove(shuffle_bugs[0])
            n = n + 1
        print("\n\tYou just skipped %s and they had to" % your_opponent[-1])
        print("\trecruit %d more Bugs! Nice." % squash_value)
        print("\tYou can now send any Bug from your Army into the nest!")
        whos_turn_isit.append('your_turn')
        if len(player_bugs) == 1:
            ascii_title("You only have 1 Bug left!")
        if len(player_bugs) == 0:
            clear_screen()
            ascii_winner(credits)
            score()
            quit(0)
        prompt()
        clear_screen()
        whos_turn()
    else:
        whos_turn_isit.append('opponents_turn')
        return()


# function to define action bugs when played by opponent
def bug_action_opponent():
    z = bugs_nest[-1]
    if z in test_skips:
        print("\n\t%s just skipped you! That Sucks." % your_opponent[-1])
        if len(opponent_bugs) == 1:
            ascii_title("Your opponent only has 1 Bug left!")
        if len(opponent_bugs) == 0:
            ascii_lost(credits)
            score()
            quit(0)
        whos_turn_isit.append('opponents_turn')
        return()
    elif z in test_add2s:
        print("\n\t%s just skipped you and you had to \
                \n\trecruit 2 more Bugs! Tough Luck." % your_opponent[-1])
        player_bugs.append(shuffle_bugs[0])
        player_bugs.append(shuffle_bugs[1])
        shuffle_bugs.remove(shuffle_bugs[0])
        shuffle_bugs.remove(shuffle_bugs[0])
        whos_turn_isit.append('opponents_turn')
        if len(opponent_bugs) == 1:
            ascii_title("Your opponent only has 1 Bug left!")
        if len(opponent_bugs) == 0:
            ascii_lost(credits)
            score()
            quit(0)
        return()
    elif z == '!SQUASH':
        n = 1
        squash_value = random.choice(range(1, 5))
        while n <= squash_value:
            player_bugs.append(shuffle_bugs[0])
            shuffle_bugs.remove(shuffle_bugs[0])
            n = n + 1
        print("\n\t%s just skipped you and you had to" % your_opponent[-1])
        print("\trecruit %d more Bugs! Ouch." % squash_value)
        print("\tThey can now send any Bug from their Army into the nest!")
        whos_turn_isit.append('opponents_turn')
        if len(opponent_bugs) == 1:
            ascii_title("Your opponent only has 1 Bug left!")
        if len(opponent_bugs) == 0:
            ascii_lost(credits)
            score()
            quit(0)
        return()
    else:
        if len(opponent_bugs) == 1:
            ascii_title("Your opponent only has 1 Bug left!")
        if len(opponent_bugs) == 0:
            ascii_lost(credits)
            score()
            quit(0)
        whos_turn_isit.append('your_turn')
        return()


# function to test play to make sure it is legal
def test_the_last_bug(x, y):
    if x in test_ants and y in test_ants:
        z = 'Good Move'
    elif x in test_bees and y in test_bees:
        z = 'Good Move'
    elif x in test_flys and y in test_flys:
        z = 'Good Move'
    elif x in test_spys and y in test_spys:
        z = 'Good Move'
    elif x in test_ones and y in test_ones:
        z = 'Good Move'
    elif x in test_twos and y in test_twos:
        z = 'Good Move'
    elif x in test_threes and y in test_threes:
        z = 'Good Move'
    elif x in test_fours and y in test_fours:
        z = 'Good Move'
    elif x in test_fives and y in test_fives:
        z = 'Good Move'
    elif x in test_sixes and y in test_sixes:
        z = 'Good Move'
    elif x in test_sevens and y in test_sevens:
        z = 'Good Move'
    elif x in test_eights and y in test_eights:
        z = 'Good Move'
    elif x in test_nines and y in test_nines:
        z = 'Good Move'
    elif x in test_zeros and y in test_zeros:
        z = 'Good Move'
    elif x in test_skips and y in test_skips:
        z = 'Good Move'
    elif x in test_add2s and y in test_add2s:
        z = 'Good Move'
    elif x == '!SQUASH':
        z = 'Good Move'
    elif y == '!SQUASH':
        z = 'Good Move'
    else:
        z = 'Bad Move'
    if z == 'Good Move' and whos_turn_isit[-1] == 'your_turn':
        bug_action()
    elif z == 'Good Move' and whos_turn_isit[-1] == 'opponents_turn':
        opponent_can_play.append(x)
    elif z == 'Bad Move' and whos_turn_isit[-1] == 'your_turn':
        bad_move()
    elif z == 'Bad Move' and whos_turn_isit[-1] == 'opponents_turn':
        opponent_cant_play.append(x)


# function to punish player for making illegal move
def bad_move():
    print("\n\t\033[1;37mYou can't send that bug in the nest! \
            \n\tNow you have to recruit 2 more bugs \
            \n\tand lose your turn.")
    player_bugs.append(bugs_nest[-1])
    bugs_nest.remove(bugs_nest[-1])
    player_bugs.append(shuffle_bugs[0])
    player_bugs.append(shuffle_bugs[1])
    shuffle_bugs.remove(shuffle_bugs[0])
    shuffle_bugs.remove(shuffle_bugs[0])
    prompt()
    clear_screen()
    whos_turn_isit.append('opponents_turn')


# function to define a play choice for putting bug in nest
def nest_a_bug():
    print("\n\t\033[1;34mWhich Bug would you like to try to infiltrate?\n")
    n = 1
    x = 0
    while n <= len(player_bugs):
        for bugs in player_bugs:
            print('\t\033[1;37m%s. %s' % (n, player_bugs[x]))
            n = n + 1
            x = x + 1
    ans = input('\n\t\033[1;31mChoose a number: 1-%s?\n\t> '
                % len(player_bugs))
    if ans.isdigit() is False:
        clear_screen()
        print("\n\tI didn't understand your response.\n\tTry Again.")
        nest_a_bug()
    elif int(ans) > len(player_bugs):
        clear_screen()
        print("\n\tThat is not one of the choices.\n\tTry Again.")
        nest_a_bug()
    elif int(ans) == 0:
        clear_screen()
        print("\n\tThat is not one of the choices.\n\tTry Again.")
        nest_a_bug()
    else:
        ans = player_bugs[int(ans)-1]
        clear_screen()
        print("\n\t\033[1;34mYou chose %s." % ans)
        player_bugs.remove(ans)
        bugs_nest.append(ans)
        test_the_last_bug(bugs_nest[-1], bugs_nest[-2])
        print("\tThe current last Bug in:")
        show_bugs_ascii(bugs_nest[-1])
        if len(player_bugs) == 1:
            ascii_title('You only have 1 Bug left!')
            input("\n\t\033[1;31mPress ENTER to continue\n\n\t> ")
            clear_screen()
        elif len(player_bugs) == 0:
            clear_screen()
            ascii_winner(credits)
            score()
            quit(0)
        else:
            input("\n\t\033[1;31mPress ENTER to continue\n\n\t> ")
            clear_screen()


# function to define a play choice for adding a bug to army
def pick_up_bug():
    drawn = shuffle_bugs[0]
    print("\n\t\033[1;34mYou picked up a:")
    show_bugs_ascii(drawn)
    shuffle_bugs.remove(drawn)
    player_bugs.append(drawn)
    ans = input("\n\t\033[1;31mCan your new bug infiltrate the nest? \
            \n\ty/n > ")
    clear_screen()
    if ans == "y":
        nest_a_bug()
    else:
        whos_turn_isit.append('opponents_turn')
        return()


# function to allow you to play your turn
def your_play():
    print("\n\t\033[1;34mIt's your turn.")
    show_bugs()
    print("\n\tYou have %d bugs left." % len(player_bugs))
    print("\n\t%s has %d bugs left." % (your_opponent[-1], len(opponent_bugs)))
    print("\n\t\033[1;31mWhat would you like to do?")
    print("\t\033[1;32m1 = Infiltrate Nest\n\t2 = Recruit Bug to Army")
    prompt()
    clear_screen()
    whos_turn()


# function to allow computer to play its turn
def opponents_play():
    print("\n\t\033[1;34mIt's %s's turn." % your_opponent[-1])
    del opponent_can_play[:]
    del opponent_cant_play[:]
    for i in opponent_bugs:
        test_the_last_bug(i, bugs_nest[-1])
    opponent_can_play.sort()
    if len(opponent_can_play) >= 1:
        bugs_nest.append(opponent_can_play[-1])
        opponent_bugs.remove(opponent_can_play[-1])
        print("\n\tYour opponent played a %s." % bugs_nest[-1])
        print("\n\tThe current last Bug in:")
        show_bugs_ascii(bugs_nest[-1])
        bug_action_opponent()
        prompt()
        clear_screen()
        whos_turn()
    elif len(opponent_can_play) < 1:
        opponent_bugs.append(shuffle_bugs[0])
        shuffle_bugs.remove(shuffle_bugs[0])
        print("\n\tYour opponent had to recruit a bug.")
        for i in opponent_bugs:
            test_the_last_bug(i, bugs_nest[-1])
        if len(opponent_can_play) >= 1:
            bugs_nest.append(opponent_can_play[-1])
            print("\n\tHowever, they were able to send in the new recruit.")
            opponent_bugs.remove(opponent_can_play[-1])
            print("\n\tYour opponent played a %s." % bugs_nest[-1])
            print("\n\tThe current last Bug in:")
            show_bugs_ascii(bugs_nest[-1])
            bug_action_opponent()
        elif len(opponent_can_play) < 1:
            print("\n\tBut even with the new recruit they still can't \
                    \n\tenter the nest.")
            whos_turn_isit.append('your_turn')
        prompt()
        clear_screen()
        whos_turn()
    else:
        broken()


# function to score game
def score():
    opponents_score = []
    players_score = []
    for i in opponent_bugs:
        if i in test_zeros:
            opponents_score.append(0)
        elif i in test_ones:
            opponents_score.append(1)
        elif i in test_twos:
            opponents_score.append(2)
        elif i in test_threes:
            opponents_score.append(3)
        elif i in test_fours:
            opponents_score.append(4)
        elif i in test_fives:
            opponents_score.append(5)
        elif i in test_sixes:
            opponents_score.append(6)
        elif i in test_sevens:
            opponents_score.append(7)
        elif i in test_eights:
            opponents_score.append(8)
        elif i in test_nines:
            opponents_score.append(9)
        elif i in test_skips:
            opponents_score.append(20)
        elif i in test_add2s:
            opponents_score.append(20)
        else:
            opponents_score.append(50)
    for i in player_bugs:
        if i in test_zeros:
            players_score.append(0)
        elif i in test_ones:
            players_score.append(1)
        elif i in test_twos:
            players_score.append(2)
        elif i in test_threes:
            players_score.append(3)
        elif i in test_fours:
            players_score.append(4)
        elif i in test_fives:
            players_score.append(5)
        elif i in test_sixes:
            players_score.append(6)
        elif i in test_sevens:
            players_score.append(7)
        elif i in test_eights:
            players_score.append(8)
        elif i in test_nines:
            players_score.append(9)
        elif i in test_skips:
            players_score.append(20)
        elif i in test_add2s:
            players_score.append(20)
        else:
            players_score.append(50)
    if opponents_score == []:
        score = sum(players_score)
        print("\n\tYour opponent, %s has defeated you!" % your_opponent[-1])
        print("\n\tThey scored \033[1;32m%d points." % score)
    else:
        score = sum(opponents_score)
        print("\n\tYou were victorious against %s!" % your_opponent[-1])
        print("\n\tYour score is \033[1;32m%d points." % score)


###################################
# graphics for game               #
###################################

# display title of game and to announce one bug left
def ascii_title(x):
    print("""
    \033[1;37m
    \t /$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$ /$$
    \t|_  $$_/ /$$__  $$| $$  | $$|_  $$_/| $$
    \t  | $$  | $$  \__/| $$  | $$  | $$  | $$
    \t  | $$  | $$      | $$$$$$$$  | $$  | $$
    \t  | $$  | $$      | $$__  $$  | $$  |__/
    \t  | $$  | $$    $$| $$  | $$  | $$
    \t /$$$$$$|  $$$$$$/| $$  | $$ /$$$$$$ /$$
    \t|______/ \______/ |__/  |__/|______/|__/
    \t%s
    """ % x)


# announce winner of game
def ascii_winner(x):
    print("""
    \033[1;34m
    \t /$$     /$$ /$$$$$$  /$$   /$$
    \t|  $$   /$$//$$__  $$| $$  | $$
    \t \  $$ /$$/| $$  \ $$| $$  | $$
    \t  \  $$$$/ | $$  | $$| $$  | $$
    \t   \  $$/  | $$  | $$| $$  | $$
    \t    | $$   | $$  | $$| $$  | $$
    \t    | $$   |  $$$$$$/|  $$$$$$/
    \t    |__/    \______/  \______/
    \t /$$      /$$  /$$$$$$  /$$   /$$ /$$
    \t| $$  /$ | $$ /$$__  $$| $$$ | $$| $$
    \t| $$ /$$$| $$| $$  \ $$| $$$$| $$| $$
    \t| $$/$$ $$ $$| $$  | $$| $$ $$ $$| $$
    \t| $$$$_  $$$$| $$  | $$| $$  $$$$|__/
    \t| $$$/ \  $$$| $$  | $$| $$\  $$$
    \t| $$/   \  $$|  $$$$$$/| $$ \  $$ /$$
    \t|__/     \__/ \______/ |__/  \__/|__/
    \t%s
    """ % x)


# announce if you lost
def ascii_lost(x):
    print("""
    \033[1;31m
    \t /$$     /$$ /$$$$$$  /$$   /$$
    \t|  $$   /$$//$$__  $$| $$  | $$
    \t \  $$ /$$/| $$  \ $$| $$  | $$
    \t  \  $$$$/ | $$  | $$| $$  | $$
    \t   \  $$/  | $$  | $$| $$  | $$
    \t    | $$   | $$  | $$| $$  | $$
    \t    | $$   |  $$$$$$/|  $$$$$$/
    \t    |__/    \______/  \______/
    \t /$$        /$$$$$$   /$$$$$$  /$$$$$$$$ /$$
    \t| $$       /$$__  $$ /$$__  $$|__  $$__/| $$
    \t| $$      | $$  \ $$| $$  \__/   | $$   | $$
    \t| $$      | $$  | $$|  $$$$$$    | $$   | $$
    \t| $$      | $$  | $$ \____  $$   | $$   |__/
    \t| $$      | $$  | $$ /$$  \ $$   | $$
    \t| $$$$$$$$|  $$$$$$/|  $$$$$$/   | $$    /$$
    \t|________/ \______/  \______/    |__/   |__/
    \t%s
    """ % x)


# image for opponent #1
def ascii_arachnid(x):
    print("""
    \t\033[1;37mAdmiral Arachnid
    \t
    \t    /             \\
    \t   |               |
    \t   |     _..._     |
    \t   |   .'  _  '.   |
    \t   \  /    V    \  /
    \t    \ |    A    | /
    \t     \\\\         //
    \t ___  ``\     /``  ___
    \t/   ``~=_\   /_=~``   \\
    \t        / /W\ \\
    \t      ~` /   \ `~
    \t     /  /     \  \\
    \t    `  /       \  `
    \t      `         `
    \t     `           `
    \t\033[1;34m%s
    """ % x)


# image for opponent #2
def ascii_cockroach(x):
    print("""
    \t\033[1;37mCommander Cockroach
    \t
    \t `;                         ;`
    \t   \           _           /
    \t   `\        .` `.        /`
    \t     \     .`     `.     /
    \t      \   :`       `:   /
    \t      `\  |         |  /`
    \t       `==|         |==`
    \t          |         |
    \t   \      |.        |      /
    \t    -\    : ;       :    /-
    \t      -   {  .      }   -
    \t       \  :  .;     :  /
    \t        -=: .  ..   :=-
    \t:         i.     ;  ;         :
    \t ;         \      ./         ;
    \t  ;       _=\     /=_       ;
    \t  `;     /   \._./   \     ;`
    \t   `;   /`   (   )   `\   ;`
    \t    `;  |    ;`-`i    |  ;`
    \t     `;     ;     i     ;`
    \t      `;   ;       i   ;`
    \t        ~_~         ~_~
    \t
    \t\033[1;34m%s
    """ % x)


# image for opponent #3
def ascii_cricket(x):
    print("""
    \t\033[1;37mColonol Cricket
    \t
    \t.``.           .``.
    \t   `;         ;`
    \t    `;       ;`
    \t     `;     ;`
    \t      `:   :`
    \t     `||   ||`
    \t     / |   | \\
    \t   ,/  :___:  \,
    \t   \  {_____}  /
    \t    `=|     |=`
    \t   .==|_____|==.
    \t  /   |     |   \\
    \t_/   /|     |\   \_
    \t    //|     |\\\\
    \t    i i     ; ;
    \t     \ i   ; /
    \t      \ i ; /
    \t      / /|\ \\
    \t     / | | | \\
    \t    `  ` | `  `
    \t         |
    \t         |
    \t         `
    \t\033[1;34m%s
    """ % x)


# image for opponent #4
def ascii_dragonfly(x):
    print("""
    \t\033[1;37mGeneral Dragonfly
    \t
    \t                 _     _
    \t.-----,,,.    `` / q|p \ ``    .,,,-----.
    \t`~=_      ``````.\_\ /_/.``````      _=~`
    \t    ```~=_       l _v_ l       _=~```
    \t.,-~`````~~~---,.. / \..,---~~~`````~-,.
    \t;._               .\ /.               _.;
    \t   ```~~~,,,......;{_};......,,,~~~```
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                   {_}
    \t                    V
    \t
    \t\033[1;34m%s
    """ % x)


# image for SPY soldiers
def ascii_spy(x):
    print("""
    \t\033[1;37m%s
    \t ||  ||
    \t \\\\()//
    \t//(__)\\\\
    \t||    ||
    """ % x)


# image for FLY soldiers
def ascii_fly(x):
    print("""
    \t\033[1;37m%s
    \t  `\  v  /`
    \t`\  \qop/  /`
    \t  \__( )__/
    \t   _/ v \_
    \t  //  A  \\\\
    \t`/ \_/V\_/ \`
    """ % x)


# image for ANT soldiers
def ascii_ant(x):
    print("""
    \t\033[1;37m%s
    \t  \/
    \t`\()/`
    \t--()--
    \t_//\\\\_
    \t  \/
    """ % x)


# image for BEE soldiers
def ascii_bee(x):
    print("""
    \t\033[1;37m%s
    \t      v
    \t{```\( )/```}
    \t {` :(_): `}
    \t  `` (_) ``
    \t      V
    """ % x)


# image for !SQUASH soldiers
def ascii_squash(x):
    print("""
    \t\033[1;37m%s
    \t+-++-++-++-++-++-++-+
    \t|S||Q||U||A||S||H||!|
    \t+-++-++-++-++-++-++-+
    """ % x)


###################################
# phrases to use in game          #
###################################

# game introduction
intro = '\n\t\033[1;34mWelcome Bug Commander! \
\n\tIt is your assignment to conquer the Bug\'s Nest \
\n\tby infiltrating until your entire army has entered. \
\n\tEach Bug in your Army can only enter the Nest if \
\n\tthe Bug that last entered was either the same Rank \
\n\tor the same Type of Bug. The first one to send in \
\n\ttheir entire army Wins!\n\n\tGood Luck. \
\n\n\t\033[1;31mType \'?\' for help.'


# help menu
help_me = ' \
\n\tOBJECT: To send your entire bug army into the Bug\'s Nest \
\n\tbefore your opponent does. \
\n\n\tSTARTING THE GAME: You will be given a random opponent to \
\n\tcompete against for the position of Bug Nest Leader. \
\n\tEach of you will be given a random bug soldier. Whoever has \
\n\tthe lowest ranking bug will be the one to make the first move. \
\n\tYou and your opponent will each be given an army of 7 random \
\n\tBugs to start out with and the first bug to enter the nest will \
\n\tbe chosen at random. The game will then begin with whoever won \
\n\tthe bug draw. \
\n\n\tHOW TO PLAY: Bugs can only enter the nest if they have\
\n\teither matching Ranks or if they are matching Bugs. \
\n\tFor Example: \
\n\tThe first bug to enter the nest was a 3-SPY and it\'s your turn. \
\n\tYou could send in a 3-FLY, 3-ANT, SKIP-SPY, 8-SPY, etc. \
\n\tas long as it is either a rank of \'3\' or a \'SPY\' in this example.\
\n\tWhen its your turn, you will be promted with 2 options. \
\n\t1 = Infiltrate Nest and 2 = Recruit Bug to Army \
\n\tIf you have a bug that can enter the Bug\'s Nest you should \
\n\tchoose \'1\' to Infiltrate Nest. You will then be prompted for \
\n\ta numerical value choice for each of the Bugs in your army. \
\n\tBe careful to only choose a Bug that is allowed to enter or \
\n\tyour Bug will be sent back to rejoin your army along with two \
\n\tadditional recruits. \
\n\tIf you can\'t Infiltrate the Nest, choose \'2\' to Recruit Bug. \
\n\tYou get the option to Infiltrate with the new recruit right away. \
\n\tThe game continues in this manner taking turns with you and your \
\n\topponent until one of you sends their entire army in first. \
\n\tWhen one of you wins the game will end and tell you your score.\
\n\n\tSCORING: The score is calculated from assigned values for each \
\n\tbug. If you run out of bugs before your opponent you are the \
\n\twinner and your score is the sum of the values of the Bugs left \
\n\tin your opponent\'s army. \
\n\n\tFor information about the Bug\'s values and about how the \
\n\tspecial Bugs (!SQUASH, ADD2-BUG, SKIP-BUG) work type \
\n\t\'bugs\' at the prompt.'


bugs_information = '\n\tThere are a total of 100 Bugs that the armies are \
\n\tbuilt from. 23 Bugs of Each ANT, BEE, FLY, SPY and 8 !SQUASH \
\n\tEach Group of Bugs Contains 2 of each rank (1-9, SKIP, ADD2) \
\n\tand 1 zero. \
\n\n\t0-9: These Don\'t do anything special. Their value is the same \
\n\tas their rank value. Example: 8-ANT is worth 8 pts. \
\n\n\tSKIP: These Skip the other player when used. \
\n\tADD2: These Skip the other player and adds 2 bugs to their army. \
\n\tBoth SKIP and ADD2 are worth 20 pts. \
\n\n\t!SQUASH: These Skip the other player and add a random number \
\n\tof bugs to their army (up to 4 Bugs!). They also allow anything to \
\n\tenter the nest behind them. Try not to get caught with these in \
\n\tyour army at the end if you lose because they are worth 50 pts. \
\n\tfor your opponent! \
\n\n\t\t\033[1;32mH\033[1;31mA\033[1;34mPP\033[1;37mY! \
\n\t\t\t\033[1;34mB\033[1;31mU\033[1;32mGG\033[1;31mI\033[1;34mN\033[1;37mG!'

###################################
# bug information - for fun       #
###################################

dragonfly_info = 'Your enemy is a Southern Giant Darner \
\n\n\tWatch out for the speed of this Austrailian dragonfly! \
\n\tIt has the ability to fly at speeds approaching sixty \
\n\tmiles per hour.'

cockroach_info = 'Your enemy is a Giant Cockroach \
\n\n\tIt is one of the largest of the species measuring \
\n\tover three inces in length. This cockroach makes \
\n\tits home in the caves of tropical environments.'

cricket_info = 'Your enemy is a Common Black Cricket \
\n\n\tThe cricket is a nocturnal insect known for its chirping. \
\n\tThey can usually be heard playing one of the four songs \
\n\tthat they know.'

arachnid_info = 'Your enemy is a Black Widow Spider \
\n\n\tThis spider is named for the fact that the females \
\n\tusually eat the males after mating. Although known \
\n\tfor its hourglass markings, adult females don\'t \
\n\talways have this characteristic.'


#######################################################################
#                                                                     #
#   START OF THE GAME!                                                #
#                                                                     #
#######################################################################

###################################
# set up game                     #
###################################

build_all_bugs()     # creates all game pieces
build_test_groups()  # builds test_groups lists to check bugs against
choose_opponent()    # randomly choose opponent
clear_screen()       # clears the screen for a fresh display
shuffle()            # shuffles all_bugs list into shuffle_bugs list

###################################
# show intro screen               #
###################################

ascii_title(intro)
prompt()
clear_screen()

###################################
# introduce opponent              #
###################################

print('\n\t\033[1;34mYou will be at battle against the great...')
show_opponent()
prompt()
clear_screen()

###################################
# decide who goes first           #
###################################

print('\n\t\033[1;34mWe need to decide which Bug Army makes the first move.\
    \n\tA random Bug will be chosen for you and %s. \
    \n\tWhoever has the lowest ranking bug will go first.' % your_opponent[-1])
prompt()
clear_screen()
who_first()
prompt()
clear_screen()

###################################
# deal the bug armies             #
###################################

deal()
show_bugs()
prompt()
clear_screen()

###################################
# put first bug in nest to start  #
###################################

start_nest()
print('\n\t\033[1;32mBe sure to always remember what the last \
        \n\tbug to enter to nest was as you will only be shown \
        \n\twhen it changes.')
prompt()
clear_screen()

###################################
# begin match                     #
###################################

whos_turn()
