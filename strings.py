"""
to start the script open CMD -> filepath -> py [filename]
"\033[x;yH"         -set curser to position x,y  (dont ask)
w = str()           -sets specific datatype manually (casting)
print(type(w))      -outputs variable datatype
print(x + y , z)    -"+" adds directly after "," adds with a space
def string_func():  -defines a method with the name "string_func"
string_func()       -call function "string_func" ()=parameters
\n \t               -\n next line -\t add tabulator
print(x[0])         -outputs character on pos0 in str x
print(x[0:4])       -outputs range of chars in str (not including high#)
print(len(w))       -outputs length of string
print(w.lower())    -outputs string in lowercases upper-for upper case
print(x.replace('H','J')) -replaces characters in output hello->jello
print(w.split('l')) -outputs string comma seperated if it finds instances of seperator (l)

string_tmp = 'First word: {}. Second word: {}. Third word: {}.'
print(string_tmp.format(x,y,z))
                    -lets u combine str and int and others in output
"""
import os

def string_func():
    print("\033[2;45H",x)
    print("\033[2;25H",y)
    print("\033[2;5H",z,'\n')
    print(x + y , z)
    print("\033[6;15HHello World!!! Fuckers\n") 
    print('\n<-------------------------0\n')  

def show_w():    
    print('This is w: \t\t' + w)
    print('\n<-------------------------1\n')
    
def change_w():
    w = z + ' ' + y + ' '  + x
    print('This is changed w: \t' + w)
    print('\n<-------------------------2\n')
    
def global_w():
    global w
    w = y + ' ' + x + ' '  + z
    print('This is global w: \t' + w)
    print('\n<-------------------------4\n')
    
x , y , z = 'Hello' , 'World!!!' , 'Fuckers'
w = str(x + ' ' + y + ' '  + z)
os.system('cls')

string_func()
show_w()
change_w()

print('This is first w again: \t' + w)
print('\n<-------------------------3\n')

global_w()
print('This is global w again: ' + w)
print('\n<-------------------------5\n')

print(x[0] + x[1] + x[2] + y[3] + y[1])
print(y[7] + y[7] + y[7] + y[0] + x[4] + y[2] + x[3] + y[4])
print()
print(x[0:4])
print(y[1:5])
print('\n<-------------------------6\n')

print('Datatype of w is:')
print(type(w))
print()
print('Length of w is:')
print(len(w))                       
print()
print(w.lower())
print(w.upper())
print(x.replace('H','J'),y,z)
print(w.split('l'))
print()

string_tmp = 'First word: {}. Second word: {}. Third word: {}.'
print(string_tmp.format(x,y,z))
print('\n<-------------------------7\n')

print('And now...a cat:')
print(",_     _,\n|\\\___//|\n|=6   6=|\n\=._Y_.=/")
print(" )  `  (    ,\n/       \\  ((\n|       |   ))")
print("/| |   | |\\_//\n\\| |._.| |/-`\n '\"'   '\"'")





