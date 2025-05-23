import random
import math
'''mine clearance
    First,user can input x and y as map's rows and columns 
    and the value should between 5 to 20
    
    Second, people should input a number to inform the system 
    how many mines should be created and 
    the system will create the mines randomly.(The number of the mine is limited)(rows*columns/10-rows*columns/3)
    After the system create the map, the game will start
    And people try to find the mine.

    If the user touch a mine, it will lose.
    If the user find all the mine, it will win. 
'''
'''To build Two 
x rows * y colums empty maps
one for show, one for function requirement  
'''

#1.introduce rules to player
def rules_and_start():
    welcome_message = '''
Welcome to Xudong's mine clearance Game!

Rules:
1. Cell Symbols:
   - '#' represents an unopened cell.
   - ' ' (space) represents a cell with no mines around.
   - A number (like '3') shows the number of mines in the surrounding 8 cells.
   - '*' marks a mine.
   - 'F' indicates a flagged cell.

2. Game Setup:
   - Enter two numbers, e.g., '4 5':
     - First number: The number of rows of the game map.
     - Second number: The number of columns of the game map.
   - Then, enter a single number to specify the number of mines.

3. Gameplay:
   - Once the map is created, the game begins.
   - Enter commands in the format: <command> x y
     - 'L' (Left-click): Reveal the cell at position (x, y).
     - 'R' (Right-click): Flag or unflag the cell at (x, y).
   - Coordinates (x, y) are 0-based (e.g., x=0, y=0 is the top-left cell).

4. Win/Lose Conditions:
   - Win: Reveal all non-mine cells (numbers and spaces).
   - Lose: Reveal any mine, ending the game.
   - Interrupt: Input 'END' to terminate the game

Example:
   Enter board rows and columns: 6 10
   Enter number of mines: 10
   Enter command: L 0 0
   Enter command: END

Enjoy the game and good luck!
'''
    print(welcome_message)
#create show_map for player
def create_show_map(x: int,y: int) -> list[list[str]]:
    show_map = []
    for i in range(x):
        #To build each row for the map 
        each_row = []
        for j in range(y):
            each_row.append('#')
        #add the built row to the map
        show_map.append(each_row)
    return show_map

#create function_map for operating
def create_function_map(x: int,y: int) -> list[list[int]]:
    function_map = []
    for i in range(x):
        #To build each row for the map 
        each_row = []
        for j in range(y):
            each_row.append(0)
        #add the built row to the map
        function_map.append(each_row)
    return function_map
#display the map
def display_map(map: list[list[str]]):
    #use 2D nested interation
    row=0
    column=len(map[0])
    for each_column in range(column):
        print(f"{each_column:3} ",end='')
    print("")
    for each_row in map:
        #to build the start'|'
        print("|",end='')
        for each_element in each_row:
            print(f" {each_element} |",end='')
        print(f" {row}")
        row+=1
'''
Create mines for this map:
mine_number: how many mines should the function create
map:function map
'''
def create_mine(map: list[list[int]], mine_number:int):
    while mine_number!=0:
        #which columns
        mine_x=random.randint(0,len(map[0])-1)
        #which rows
        mine_y=random.randint(0,len(map)-1)
        #if the cell is mine already
        if map[mine_y][mine_x]==9:
            continue
        else :
        #if the cell is not mine
            map[mine_y][mine_x]=9
            mine_number-=1
#find the number of mines around for a cell
def find_mine_around(map: list[list[int]],x:int ,y:int)->int:
    count=0
    if map[y][x]==9:
        return 9
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx==0 and dy==0:
                continue
            if (x+dx) in range(0,len(map[0])) and (y+dy) in range(0,len(map)) and map[y+dy][x+dx]==9:
                count+=1
    return count
#update all the cells in the map
def update_map(map: list[list[int]]):
    for y in range(0,len(map)):
        for x in range(0,len(map[0])):
            map[y][x]=find_mine_around(map,x,y)

#Logical Function Control
class S_fmap:
    #- Win: Reveal all non-mine cells (numbers and spaces).
    #- Lose: Reveal any mine, ending the game.
    def __init__(self, show_map: list[list[str]], function_map: list[list[int]],mine_number:int):
        self.show_map=show_map
        self.function_map=function_map
        self.open_mine=False
        self.open_number=0
        self.flag_num=mine_number
        #all number minus mine number
        self.win_number=len(show_map)*len(show_map[0])-mine_number
    def update_flags(self,x:int,y:int):
        if x not in range(0,len(self.show_map[0])) or y not in range(0,len(self.show_map)):
            print("Invalid coordinates!")
            return
        if self.show_map[y][x] == '#':
            self.flag_num-=1
            self.show_map[y][x] = 'F'
        elif self.show_map[y][x] == 'F':
            self.flag_num+=1
            self.show_map[y][x] = '#'
        else:
            print(">>>>>>Cell already opened!>>>>>>>")

    def update_status(self,x:int,y:int):
        #base situation
        if x not in range(0,len(self.show_map[0])) or y not in range(0,len(self.show_map)) or self.show_map[y][x]!='#':
            return
        if self.function_map[y][x]==9:
            self.show_map[y][x]='*'
            self.open_mine=True
        else:
            self.open_number+=1
            self.show_map[y][x]=self.function_map[y][x]
            if self.function_map[y][x]==0:
                self.show_map[y][x]=' '
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if dx==0 and dy==0:
                            continue
                        self.update_status(x+dx,y+dy)

    def is_win(self)->bool:
        return self.open_number==self.win_number
    def is_lose(self)->bool:
        return self.open_mine

if __name__ == '__main__':
    #1.introduce rules to player
    rules_and_start()
    #2.Create empty map
    show_map=None
    function_map=None
    min_mines=0
    max_mines=400
    num_mines=10
    is_tester=False
    while True:
        try:
            check=input(">>>>>>>Are you a tester?>>>>>> Y/N:")
            if len(check)==1 and check[0].upper()=='Y':
                is_tester=True
                break
            elif len(check)==1 and check[0].upper()=='N':
                is_tester=False
                break
            else:
                raise Exception
        except Exception:
            print("Error: Please enter 'Y' or 'N'")
    while True:
        try:
            x_y = input("Enter x and y (both from 5 to 20, e.g., '5 10'): ").split()
            x=int(x_y[0])
            y=int(x_y[1])
            if x<5 or x>20 or y<5 or y>20:
                print("Error: Both x and y must be between 5 and 20 (inclusive).")
                continue
            show_map=create_show_map(x,y)
            function_map=create_function_map(x,y)
            min_mines = math.ceil(x * y / 10)
            max_mines = math.floor(x * y / 3)
            break
        except Exception:
            print("Error: Please enter two valid numbers separated by a space.")
    #input the numbers of mines(int) between (x * y / 10) and (x * y / 3)
    #First, create the mines in the function_map, second, update the numbers in the function map 
    while True:
            try:
                num_mines = int(input(f"Enter number of mines ({min_mines} to {max_mines}): "))
                if num_mines < min_mines or num_mines > max_mines:
                    print(f"Error: Number of mines must be between {min_mines} and {max_mines}!")
                    continue
                create_mine(function_map,num_mines)
                update_map(function_map)
                break
            except ValueError:
                print("Error: Please enter a valid number.")
    #game start and show the map
    print(">>>>>>>>>>>>>>>>MAP HAS BEEN CREATED, GAME START!>>>>>>>>>>>>")
    my_map=S_fmap(show_map,function_map,num_mines)
    #only tester can see the function code
    if is_tester:
        print(">>>>>>>>>>>>>>You can function map>>>>>>>>>>>>>>>>>>")
        display_map(function_map)
        print(">>>>>>>>>>>>>>Real game Start>>>>>>>>>>>>>>>>>>>>>>>>>")
    display_map(show_map)
    while True:
        try:
            action=input("Enter <command> x y (command must be 'L' or 'R') or Enter <command> (command must 'END')").split(' ')
            if len(action)==1 and action[0].upper()=='END':
                print("YOU TERMINATE THE GAME")
                break
            elif len(action) != 3:
                raise ValueError("Invalid format! Use '<command> x y'.")
            command=action[0].upper()
            x=int(action[1])
            y=int(action[2])
            if x not in range(0,len(show_map[0])) or y not in range(0,len(show_map)):
                    raise ValueError("Coordinates are out of bounds!")
            if command == 'L':
                if show_map[y][x] == 'F':
                    raise ValueError("You should unlock the flag first!")
                elif show_map[y][x] !='#':
                    raise ValueError("You should choose an unopened cell!")
                else:
                    my_map.update_status(x, y)
                    print("COMMAND EXECUTED")
                    display_map(show_map)
            elif command == 'R':
                my_map.update_flags(x, y)
                print(f"{my_map.flag_num} flags remain")
                display_map(show_map)
            else:
                raise ValueError("Invalid command! Use 'L' or 'R'.")
            if my_map.is_lose():
                print(f">>>>>>YOU LOSE AT ({x},{y})>>>>>>>>")
                break
            elif my_map.is_win():
                print(">>>>>>YOU WIN>>>>>>>>>")
                break
        except ValueError as e:
            print(f"Error: {e}")
        except IndexError:
                print("Error: Invalid input format!")


        