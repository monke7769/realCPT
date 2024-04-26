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
    N = ''
    while N == '':
        userchoice = input('Enter the number of pigeons you would like to shoot: ')
        try:
            test = int(userchoice)
            if 1 <= test <= 10:
                N = test
                return N
            else:
                print('Please an integer between 1 and 10 inclusive.')
        except ValueError:
            print('Please an integer between 1 and 10 inclusive.')
            
def generatepigeons(num):
    pigeons = set()
    while len(pigeons) < num:
        x = random.randint(1,20)
        y = random.randint(1,20)
        pigeons.add((x,y))
    return list(pigeons)

def shootpigeon(list): 
    K = len(list) 
    xy = []
    coordnames = ['x','y']
    for i in range(2):
        coord = 0
        while coord == 0: 
            userchoice = input('Enter the '+coordnames[i]+' coordinate you want to shoot: ') # one for x, one for y
            try:
                test = int(userchoice)
                if 1 <= test <= 20:
                    coord = test
                    xy.append(coord)
                else:
                    print('Please an integer between 1 and 20 inclusive.')
            except ValueError:
                print('Please an integer between 1 and 20 inclusive.')
    mindis = 99999
    for i in range(K):
        distance = ((list[i][0]-xy[0])**2+(list[i][1]-xy[1])**2)**(0.5) 
        mindis = min(mindis, distance)
        if int(distance) == 0:
            print('HIT!')
            list.pop(i)
            break
    if len(list) != K: 
        print('There are '+str(K-1)+' pigeons remaining.')
        return list
    else: 
        mindis = round(mindis, 2)
        print('The closest pigeon is '+str(mindis)+' units away.')
        return list

def game():
    print('Welcome to the game where you put holes in pigeons!')
    time.sleep(1)
    print('If you would like to view the instructions, enter "yes". If not, enter anything else.')
    if input().lower() == 'yes':
        displayInstructions()
    time.sleep(0.5)
    N = chooseN()
    print('There are now '+str(N)+' pigeons to shoot!')
    pigeons = generatepigeons(N)
    count = 0
    while len(pigeons) != 0:
        print("Shot number "+str(count+1))
        time.sleep(0.2)
        pigeons = shootpigeon(pigeons)
        count += 1
    print('YOU WIN')
    time.sleep(0.5)
    print('You wasted '+str(count)+' bullets in destroying all the pigeons.')

game()

            