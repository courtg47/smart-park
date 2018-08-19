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
    bulletin_board.append(_visitor_bulletin())
    bulletin_choice = random.choice(bulletin_board)
    return bulletin_choice


def _read_arduino_visitors():
    with open('arduino/output.txt') as f:
        peeps = f.readline().strip()
        doggos = f.readline().strip()
    # leaving as strings. We aren't crunching this!
    num_peeps = peeps.split(':')[1].strip()
    num_doggos = doggos.split(':')[1].strip()
    return (num_peeps, num_doggos)

def _visitor_bulletin():
    visitors = _read_arduino_visitors()
    peeps = visitors[0]
    doggos = visitors[1]
    # This is a terrible way to write strings #sorrynotsorry
    bulletin = "We've had " + peeps + " visitors and " + doggos + " canine visitors today!"
    return bulletin
