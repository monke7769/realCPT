import time
import random

def displayInstructions():
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
    N = '' # initialize N
    while N == '': # go as long as N hasn't been defined as an integer
        userchoice = input('Enter the number of pigeons you would like to shoot: ')
        try: # see if it's possible to convert input to integer
            test = int(userchoice)
            if 1 <= test <= 10:
                N = test
                return N # if converted to integer between 1 and 10, return it
            else:
                print('Please an integer between 1 and 10 inclusive.')
        except ValueError: # in the case that the user entered a non-integer
            print('Please an integer between 1 and 10 inclusive.')
            
def generatepigeons(num):
    # we will generate the coordinates of the pigeons
    # we use a set first to ensure that all coordinates are distinct, then convert back to list
    pigeons = set()
    while len(pigeons) < num: # generate as long as there are not enough pigeons
        x = random.randint(1,20)
        y = random.randint(1,20)
        pigeons.add((x,y)) # try to add new coordinates to the set
    return list(pigeons)

def shootpigeon(list): # shootpigen takes list of remaining coordaintes as argument
    K = len(list) # pigeons left before shot
    xy = [] # initialize coordinates as list
    coordnames = ['x','y'] # for interaction in terminal (print is different for x and y coordinates)
    for i in range(2): # repeat for x and y coordinates per shot
        coord = 0 # initialize coordinate as 0 (needs to be between 1 to 20)
        while coord == 0: 
            userchoice = input('Enter the '+coordnames[i]+' coordinate you want to shoot: ') # one for x, one for y
            try: # see if it's possible to convert input to integer
                test = int(userchoice)
                if 1 <= test <= 20:
                    coord = test
                    xy.append(coord)
                else:
                    print('Please an integer between 1 and 20 inclusive.')
            except ValueError: # in the case that the user entered a non-integer
                print('Please an integer between 1 and 20 inclusive.')
    # xy contains user input coordinates now
    # now test if there is pigeon there & calculate distances
    mindis = 99999 # initialize minimum distance variable
    for i in range(K): # go through all elements of list, check for minimum distance
        distance = ((list[i][0]-xy[0])**2+(list[i][1]-xy[1])**2)**(0.5) # calculate distances to pigeons using distance formula
        mindis = min(mindis, distance) # take new minimum distance if needed
        if int(distance) == 0: # if distance is 0, guaranteed a pigeon is there
            print('HIT!')
            list.pop(i) # remove the dead pigeon
            break
    if len(list) != K: # if a pigeon died, the list should now be one element shorter
        print('There are '+str(K-1)+' pigeons remaining.')
        return list
    else: # missed the shot
        mindis = round(mindis, 2) # truncate distance
        print('The closest pigeon is '+str(mindis)+' units away.')
        return list

def game(): # driver code
    print('Welcome to the game where you put holes in pigeons!')
    time.sleep(1)
    print('If you would like to view the instructions, enter "yes". If not, enter anything else.')
    if input().lower() == 'yes':
        displayInstructions()
    time.sleep(0.5)
    N = chooseN() # N will now represent how many pigeons there are at the beginning
    print('There are now '+str(N)+' pigeons to shoot!')
    pigeons = generatepigeons(N)
    count = 0 # initialize shot count
    # print(pigeons)
    while len(pigeons) != 0:
        print("Shot number "+str(count+1))
        time.sleep(0.2)
        pigeons = shootpigeon(pigeons)
        count += 1
    # after the loop, no pigeons are left and the game is over
    print('YOU WIN')
    time.sleep(0.5)
    print('You wasted '+str(count)+' bullets in destroying all the pigeons.')

# run the game
game()
            