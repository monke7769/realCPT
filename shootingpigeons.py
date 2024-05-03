'''
Shooting Pigeons Text-based game.
All code is original and written by me.
To be run within a terminal.
'''
# we will be using the time package to space out terminal output
# the random package will be used to generate random pigeons every time
import time
import random

def displayInstructions():
    '''
    display instructions for the game
    '''
    time.sleep(0.8)
    print('There are N pigeons, located on a coordinate grid. Each pigeon will be represented by a coordinate pair (x,y).')
    time.sleep(0.8)
    print('x and y will always be positive integers, between 1 and 20 inclusive. You will choose the value of N, but must be at most 10. It is guaranteed that all pigeons have distinct coordinates.')
    time.sleep(0.8)
    print('Your job is to shoot down all the pigeons with as few bullets as possible. Each shot will be made by entering a coordinate pair (x,y) that you would like to shoot at.')
    time.sleep(0.8)
    print('After every shot, the distance to the nearest pigeon will be provided. If a pigeon is shot, it is a "HIT" and there will be no pigeon there anymore. You may then enter your next target.')
    time.sleep(0.8)
    print('You win the game when all the pigeons are dead!')

def chooseN():
    '''
    in this function, the user is allowed to choose an integer.
    the function handles user error cases with try/except.
    it returns the user-selected value of N at the end
    '''
    N = '' # initialize N
    while N == '': # go as long as N hasn't been defined as an integer
        userchoice = input('Enter the number of pigeons you would like to shoot: ')
        try: # see if it's possible to convert user input to integer
            test = int(userchoice)
            if 1 <= test <= 10:
                N = test
                return N # if converted to integer between 1 and 10, return it
            else:
                print('Please an integer between 1 and 10 inclusive.')
        except ValueError: # in the case that the user entered a non-integer
            print('Please an integer between 1 and 10 inclusive.')
            
def generatepigeons(num):
    '''
    this function will generate the coordinates of the pigeons
    it uses a set first to ensure that all inserted coordinates are distinct, then converts this back to a list to return as output
    '''
    pigeons = set()
    while len(pigeons) < num: # generate as long as there are not enough pigeons to satisfy user desires
        x = random.randint(1,20)
        y = random.randint(1,20)
        pigeons.add((x,y)) # try to add new random coordinates to the set
    return list(pigeons)

def shootpigeon(pigeons): # shootpigeon takes list of remaining coordaintes as argument
    '''
    this function will take user input for the coordinate they want to shoot.
    x and y coordinates will be provided by the user separately.
    after the coordinates are input, a for loop will iterate through the all the remaining pigeons in the "pigeons" list in the argument.
    the distance to each pigeon will be calculated, and a minimum distance is kept in the "mindis" variable.
    if at any point, the distance to some pigeon is 0, then that pigeon is hit and will be removed from the pigeons list, and the loop breaks.
    if the user hit a pigeon, an output message will be "there are X pigeons remaining"
    if the user didn't hit anything, an output message will inform the user of the minimum distance to a pigeon
    this function returns the list "pigeons" provided in the argument (modified or not modified) as the current coordinates of the pigeons
    '''
    K = len(pigeons) # pigeons left before shot
    xy = [] # initialize new coordinate pair as list
    coordnames = ['x','y'] # for interaction in terminal (print is different for x and y coordinates)
    for i in range(2): # repeat for x and y coordinates per shot
        coord = 0 # initialize coordinate as 0 (needs to be between 1 to 20)
        while coord == 0: 
            userchoice = input('Enter the '+coordnames[i]+' coordinate you want to shoot: ') # one for x, one for y
            try: # see if it's possible to convert input to integer
                test = int(userchoice)
                if 1 <= test <= 20:
                    coord = test
                    xy.append(coord) # insert x or y value into coordinate pair
                else:
                    print('Please an integer between 1 and 20 inclusive.')
            except ValueError: # in the case that the user entered a non-integer
                print('Please an integer between 1 and 20 inclusive.')
                # if this doesn't work, coord will still be 0 and the while loop is run again
                # the user will be prompted to enter a proper coordinate again
    
    # xy contains user input coordinates now
    # now test if there is pigeon there & calculate distances
    mindis = 99999 # initialize minimum distance variable
    for i in range(K): # iterate through all elements of list, check for minimum distance
        distance = ((pigeons[i][0]-xy[0])**2+(pigeons[i][1]-xy[1])**2)**(0.5) # calculate distances to pigeons using distance formula
        mindis = min(mindis, distance) # take new minimum distance if needed
        if int(distance) == 0: # if distance is 0, guaranteed a pigeon is there
            # note that this works because distance between integer coordinates cannot be between 0 and 1 exclusive (by the Pythagorean Theorem)
            print('HIT!')
            pigeons.pop(i) # remove the dead pigeon from the list
            break
    if len(pigeons) == K-1: # if a pigeon died, the list should now be one element shorter
        print('There are '+str(K-1)+' pigeons remaining.')
        return pigeons
    else: # if user missed the shot
        mindis = round(mindis, 2) # truncate distance
        print('The closest pigeon is '+str(mindis)+' units away.')
        return pigeons

def game(): # driver code
    print('Welcome to the game where you put holes in pigeons!')
    time.sleep(1)
    print('If you would like to view the instructions, enter "yes". If not, enter anything else.')
    if input().lower() == 'yes':
        displayInstructions()
    time.sleep(0.5)
    N = chooseN() # N will now represent how many pigeons there are initially to shoot
    print('There are now '+str(N)+' pigeons to shoot!')
    pigeons = generatepigeons(N)
    '''
    "pigeons" is the list that will contain the coordinates of the remaining pigeons.
    this list is updated in real time whenever the user hits a pigeon, via the "shootpigeon" function.
    each time the shootpigeons(pigeons) function is called, the "pigeons" list is redefined as whatever the output of shootpigeon() is.
    '''
    count = 0 # initialize shot count to output when all pigeons are gone
    while len(pigeons) != 0: # run as long as "pigeons" is not empty
        print("Shot number "+str(count+1)) # tell user how much they've guessed
        time.sleep(0.2)
        pigeons = shootpigeon(pigeons)
        count += 1 # update shot count
    # after the loop finishes, no pigeons are left and the game is over
    print('YOU WIN')
    time.sleep(0.5)
    print('You wasted '+str(count)+' bullets in destroying all the pigeons.')

# run the game
game()