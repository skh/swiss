#!/usr/bin/env python
#
# Command line tool to interactively run a tournament

from tournament import *

# helper methods for interactive loop

def complain(allowed, entered):
    print "Unknown command: " + entered
    printHelp(allowed)

def printHelp(allowed):
    printLine()
    print "Available commands:"
    for key in allowed.keys():
        print "  " + key + ": " + allowed[key]
    printLine()

def getCommand(allowed):
    while True:
        # prompt the user for input
        command = raw_input("(h for help) > ")
        if allowed.has_key(command):
            return command
        else:
            complain(allowed, command)

def printLine():
    print "----------------------------------------------------------------------------"

# add a new player to the systm
def addPlayer():
    name = raw_input("Please enter the player's full name: ")
    registerPlayer(name)

# list all players in the system
def listPlayers():
    numPlayers = countPlayers()
    players = playerStandings()
    print "%d players are registered: " % (numPlayers)
    printLine()
    print "id\tName\t\t\t\tMatches won\tMatches played"
    printLine()
    for player in players:
        print "%d\t%s\t%d\t\t%d" % (player[0], player[1].ljust(24), player[2], player[3])
    printLine()

# show pairings for the next round
def showNextRound():
    pairings = swissPairings()
    print "id\tName\t\t\t\tid\tName"
    printLine()
    for pair in pairings:
        print "%d\t%s\t%d\t%s" % (pair[0], pair[1].ljust(24), pair[2], pair[3])        
    printLine()

# enter the result of a match
def enterMatchResult():
    winner = int(raw_input("Please enter the id of the winner: "))
    loser = int(raw_input("Please enter the id of the loser: "))
    reportMatch(winner, loser)

# main interactive loop

done = False
while not done:
    commands = {'p': "Add a new player to the system",
                'l': "List all players in the system",
                'r': "Show pairings for the next round",
                'm': "Enter the result of a match",
                'q': "Quit the program",
                'h': "Print this help"}

    c = getCommand(commands)

    if c == 'h':
        printHelp(commands)
    elif c == 'q':
        done = True
    elif c == 'p':
        addPlayer()
    elif c == 'l':
        listPlayers()
    elif c == 'r':
        showNextRound()
    elif c == 'm':
        enterMatchResult()

