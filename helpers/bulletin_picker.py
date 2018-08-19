import random, datetime
from datetime import datetime


def bulletin_picker():

    text = bulletins()
    month = datetime.now().month
    
    
    if month == 1:
        color = 'red'
    if month == 2:
        color = 'purple'
    if month == 3:
        color = 'aqua'
    if month == 4:
        color = 'yellow'
    if month == 5:
        color = 'green'
    if month == 6:
        color = 'navy'
    if month == 7:
        color = 'red'
    if month == 8:
        color = 'orange'
    if month == 9:
        color = 'blue'
    if month == 10:
        color = 'brown'
    if month == 11:
        color = 'violet'
    if month == 12:
        color = 'garnet'
    
    return (text, color)

    
def bulletins():
    bulletin_board = ['Sidewalk Film Festival: Aug. 2-6', 'Concert Tonight: Carrie Underwood', 'Hot Dog Eating Contest: Five Points',
                      'Sloss Furnace Music Festival', ' Pepper Place Market: Every Saturday', 'Play: Wonderland Wives', 'Birmingham Restaurant Week',
                      'Barons Game: Tonight', 'Magic City Brewfest', 'Birimingham Innovation Week', 'Rock and Roll Bingo: Tonight',
                      'The Three Musketeers Live Show: Brookwood Village', 'Free Art Friday: July 13th', 'McWayne Science Center Celebration',
                      'Birmingham TACO FEST: Avondale', 'Cooking Class at Railroad Park: Sunday', 'Sloss Furnace: Metal Casting Class']
    bulletin_choice = random.choice(bulletin_board);
    return bulletin_choice



print(bulletin_picker())

