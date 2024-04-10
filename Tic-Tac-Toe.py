import random

username=input("Enter your name here: ") #Player name
print("""
Welcome to the game of Tic-Tac-Toe!

Instructions:

-> You need instructions in Tic-Tac-Toe? Seriously?
-> Just input the your markings by the given numberings and enjoy!
    
                        |     |
                     1  |  2  |  3
                   -----|-----|-----
                     4  |  5  |  6
                   -----|-----|-----
                     7  |  8  |  9
                        |     |
       """) #Extra Content

mark=input("Choose your Marker ('X' or 'O'): ").upper() #What marker you want to use
while mark not in ['X','O']: #Marker condition for input other than 'X' or 'O'
    print("Choose a valid marker.")
    mark=input("Choose your Marker ('X' or 'O'): ")
if mark=='X': #marker condition
    comp='O' 
elif mark=='O': #Marker condition
    comp='X'
print(f"\n{username} has chosen {mark} as their marker.\n") #Output

dict={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '} #The dict variable is used to store the initial values of the Tic-Tac-Toe grid.
grid={} #The grid variable is used to store the updated values as the game progresses.

keys=[] #The keys variable is used to store the keys of the dict variable, which are used to randomly select a cell for the computer's move.
for i in dict.keys():
    keys.append(i)

win_flag=False #The win_flag variable is used to track if a player has won the game.

class game: 
    def base(self): #Game grid
        print(f"""
                   |     |
                 {dict.get(1)} |  {dict.get(2)}  | {dict.get(3)}
              -----|-----|-----
                 {dict.get(4)} |  {dict.get(5)}  | {dict.get(6)}
              -----|-----|-----
                 {dict.get(7)} |  {dict.get(8)}  | {dict.get(9)}
                   |     | 
        """)

    def p1(self): #Player's turn
        player=int(input("Your turn: "))
        while player in dict and player not in grid:
            dict.update({player:mark})
            grid.update({player:mark})
            print(f"""\n{username} marked {mark} at {player}.\n
                   |     |
                 {dict.get(1)} |  {dict.get(2)}  | {dict.get(3)}
              -----|-----|-----
                 {dict.get(4)} |  {dict.get(5)}  | {dict.get(6)}
              -----|-----|-----
                 {dict.get(7)} |  {dict.get(8)}  | {dict.get(9)}
                   |    
        """)
            break
        else:
            print("Enter a valid input.")

    def p2(self): #Computer's turn
        val=random.choice(keys)
        while val not in grid: 
            dict.update({val:comp})
            grid.update({val:comp})
            print(f"""Computer has marked {comp} at {val}.\n
                   |     |
                 {dict.get(1)} |  {dict.get(2)}  | {dict.get(3)}
              -----|-----|-----
                 {dict.get(4)} |  {dict.get(5)}  | {dict.get(6)}
              -----|-----|-----
                 {dict.get(7)} |  {dict.get(8)}  | {dict.get(9)}
                   |     |  
            """)
            break

    def win(a,b,c):
        global win_flag
        if a==mark and b==mark and c==mark:
            win_flag=True
            print("You Win!\nComputer Lost!")
            
        elif a==comp and b==comp and c==comp:
            win_flag=True
            print("You Lost!\nComputer Won!")

    def conditions(self):
        while True:
            try:
                if game.win(dict.get(1),dict.get(2),dict.get(3)):
                    break
                if game.win(dict.get(4),dict.get(5),dict.get(6)):
                    break
                if game.win(dict.get(7),dict.get(8),dict.get(9)):
                    break
                if game.win(dict.get(1),dict.get(4),dict.get(7)):
                    break
                if game.win(dict.get(2),dict.get(5),dict.get(8)):
                    break
                if game.win(dict.get(3),dict.get(6),dict.get(9)):
                    break
                if game.win(dict.get(1),dict.get(5),dict.get(9)):
                    break
                if game.win(dict.get(3),dict.get(5),dict.get(7)):
                    break
            except:
                pass
            break

obj=game() #The obj variable is an object of the game class which is used to access the class's methods.

chances=[1,2] #The chances variable is used to randomly select the first player, and rand variable is used to store the random value.
rand=random.choice(chances) #The even and odd variables are used to alternate between the player and computer's turns.

if rand==1: #Condition
    even=obj.p1
    odd=obj.p2
else: #Condition
    even=obj.p2
    odd=obj.p1

obj.base() #Display grid

while len(grid)<=8 and not win_flag: #Game running condition
    if len(grid)%2==0:
        even()
        obj.conditions()
    else:
        odd()
        obj.conditions()
if win_flag:
    pass
else:
    print("Tie!\nGame Over!") #Game tie statement
