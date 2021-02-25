###   A simple calculator on python using the module 'tkinter'
###   Uses a GUI interface and interactive buttons

from tkinter import *



# Variables
numbers = [] # Stores our numbers we press
num = 0      # Stores the integer version of screen
count = 0    # Sees if it is the first time minus has been pressed
screen = 0   # The numbers that will be displayed are stored in this
op = ''      # What tells the program to add or minus
answer = 0   # The final sum

#  Making the window and setting it's attributes 
window = Tk()
window.geometry('207x290')
window.configure(background= '#D1FFF2')
window.title('Calculator')

#   Define functions to each button
#   Add n to numbers when pressed, where n is the button pressed
def btn0():
    global numbers
    numbers.append('0')
    addscreen()
def btn1():
    global numbers
    numbers.append('1')
    addscreen()
def btn2():
    global numbers
    numbers.append('2')
    addscreen()
def btn3():
    global numbers
    numbers.append('3')
    addscreen()
def btn4():
    global numbers
    numbers.append('4')
    addscreen()
def btn5():
    global numbers
    numbers.append('5')
    addscreen()
def btn6():
    global numbers
    numbers.append('6')
    addscreen()
def btn7():
    global numbers
    numbers.append('7')
    addscreen()
def btn8():
    global numbers
    numbers.append('8')
    addscreen()
def btn9():
    global numbers
    numbers.append('9')
    addscreen()
    
# Other button functions

# This will clear all variable and set them back to the starting point,
# so this will be just like opening the calculator again.
def clear():
    global numbers, screen, count, op, answer
    op = ''
    numbers = []
    screen = 0
    count = 0
    answer = 0
    disp()  # calls the function to display variables on screen.
    
# This is where the function to add ( + ) is made, this allows us to make the add button able to do it's job.    
def add():
    global screen, numbers, count, num, answer, op
    # This creates a screen variable which is an integer, so we can do addition to it
    num = int(screen)
    # checking the last operation done
    # if this is not the first time we are using an operation we will need to work out the last operation done.
    if op == '-':
        answer -= num
    # if this is the first time or we are using addition continuously we will just add the the last answer.
    else:
        answer += num
        count = 1

    # we have to set the numbers back to zero so we can input more in a minute.
    numbers = []
    screen,op = '+','+'
    disp()
    
def minus():
    global count, num, screen, answer, numbers, op
    # This creates a screen variable which is an integer, so we can do subtraction to it
    num = int(screen)
    # checking the last operation done
    # if this is not the first time we are using an operation we will need to work out the last operation done.
    if op == '+':
        answer += num
    
    else:
    # if we are just running the program for the first time then we need to set the number to the answer( variable ) so we can minus it,
    # this stops it from going into negative number at the beginning of the program.
        if count == 0:
            answer = num
            count = 1 # let the program know that our first time is up and we can subtract normally now.
        # this is where we subtract like normal now
        elif count == 1:
            answer -= num

    # we have to set the numbers back to zero so we can input more in a minute.
    numbers = []
    screen,op = '-', '-'
    disp()

# displaying the final answer on screen for us to see.
def equal():
    global screen, answer, count, num, op

    # making sure that we have done all of the operations
    num = int(screen)
    # if the last one pressed was add then do this
    if op == '+':
        answer += num
    # if the last one pressed was minus then do this
    elif op == '-':
        answer -= num
        
    screen = answer
    disp()

    
#   Updates the screen
def addscreen():
    global numbers, screen
#   Join the numbers we have pressed together into a variable
    screen = ''.join(numbers)
    disp()
    
def disp():
    global screen
#   Show the variable, we stored are numbers on, on the display
    display.configure(text= screen)
    

#  Make the number buttons and giving them a position
#  Arrange them into 'grid like' fassion
#  1  2  3
#  4  5  6
#  7  8  9

##############################################################################################################

btn0 = Button(window, text = '0', command = btn0, height= 2, width= 11, bg= '#E0FFF5' ).place(x= 10, y= 240)
btn1 = Button(window, text = '1', command = btn1, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 10, y= 90)  
btn2 = Button(window, text = '2', command = btn2, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 60, y= 90)  
btn3 = Button(window, text = '3', command = btn3, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 110, y= 90) 
btn4 = Button(window, text = '4', command = btn4, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 10, y= 140) 
btn5 = Button(window, text = '5', command = btn5, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 60, y= 140) 
btn6 = Button(window, text = '6', command = btn6, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 110, y= 140)
btn7 = Button(window, text = '7', command = btn7, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 10, y= 190) 
btn8 = Button(window, text = '8', command = btn8, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 60, y= 190) 
btn9 = Button(window, text = '9', command = btn9, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 110, y= 190)

##############################################################################################################

#  Creating the other buttons on the calculator
#  For example, ones that arent numbers like:
#  Add, minus, equals and the clear button

################################################################################################################

equal = Button(window, text= '=', command= equal, height= 2, width= 11, bg= '#E0FFF5' ).place(x= 110, y= 240) 
add = Button(window, text = '+', command = add, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 160, y= 190)    
minus = Button(window, text = '-', command = minus, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 160, y= 140)
ac = Button(window, text = 'AC', command = clear, height= 2, width= 4, bg= '#E0FFF5' ).place(x= 160, y= 90)

################################################################################################################

#  Making the display screen and the position at the top

display = Label(window, text= screen, height= 3, width= 20, anchor=W, font= 20, bg= '#FFFFC2')
display.place(x=10, y=10 )

# making the main loop so it will continuously run.
window.mainloop()
















