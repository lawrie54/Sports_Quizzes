# Football quiz based on State Capitals quiz, to find 
# the nicknames of Premier League teams for 2013/14 season.


nicknames_dict = {
'City' : 'The Citizens',
'Liverpool' : 'The Reds',
'Chelsea' : 'The Blues',
'Arsenal' : 'The Gunners',
'Everton' : 'The Toffees',
'Tottenham' : 'Spurs',
'Man Utd' : 'The Red Devils',
'Southampton' : 'The Saints',
'Stoke' : 'The Potters',
'Newcastle' : 'The Magpies',
'Crystal Palace' : 'The Eagles',
'Swansea' : 'The Swans',
'West Ham' : 'The Hammers',
'Sunderland' : 'The Black Cats',
'Aston Villa' : 'The Villans',
'Hull' : 'The Tigers',
'West Brom' : 'The Baggies',
'Norwich' : 'The Canaries',
'Fulham' : 'The Cottagers',
'Cardiff' : 'The Bluebirds',
}

import random

teams = list(nicknames_dict.keys())
for i in [1,2,3,4,5]:
    team = random.choice(teams)
    nickname = nicknames_dict[team]
    nickname_guess = input("What is the nickname of " + team + "?")

    if nickname_guess == nickname:
       print("Correct! Nice job.")
    else:
         print("Incorrect. The nickname of " +team + " is " + nickname + ",")

print("All done")
