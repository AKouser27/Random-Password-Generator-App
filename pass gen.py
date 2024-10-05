import random
import string
import PySimpleGUI as sg


upper = random.sample(string.ascii_uppercase, 2) #,2 if u want u can add any number of random letters
lower = random.sample(string.ascii_lowercase, 2)
digits = random.sample(string.digits, 2)
symbols = random.sample(string.punctuation, 2)
#print(upper, lower, digits,symbols)
#concatination

total= upper+lower+digits+symbols
total = random.sample(total, len(total))#it gives the length of total random letters
total=''.join(total)
print (total)


sg.theme('neonyellow1')
sg.set_options(font='verdana 15')

layout = [
    
    [sg.Text(' Enter Uppercase Characters : '), sg.Push(), sg.Input(size=15, key='-UP-')],
    [sg.Text('Enter Lowercase Characters : '), sg.Push(), sg.Input(size=15, key='-LOW-')],
    [sg.Text(' Enter Digits : '),sg.Push(), sg.Input(size=15, key='-DIG-')],
    [sg.Text('Enter Symbols :'),sg.Push(), sg.Input(size=15, key='-SYM-')],
    [sg.Button('OK'), sg.Button('Cancel')],
    [sg.Text("Your Password is : "), sg.Push(),sg.Multiline(size=25, no_scrollbar=True,
    disabled=True, key='-PASS-')]
]

#creating a window variable
window = sg.Window('Password Generator', layout)



while True:
    event, values = window.read()
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
    
    if event == 'OK':
        try:
            u_upper = int(values['-UP-'])
            upper = random.sample(string.ascii_uppercase, u_upper ) #,2 if u want u can add any number of random letters
            u_lower = int(values['-LOW-'])
            lower= random.sample(string.ascii_uppercase, u_lower )
            u_digits = int(values['-DIG-'])
            digits =random.sample(string.digits, u_digits )
            u_symbols = int(values['-SYM-'])
            symbols =random.sample(string.punctuation, u_symbols )
        #print(letters, digits,symbols)
        #concatination
            total= upper+lower+digits+symbols
            total = random.sample(total, len(total))#it gives the length of total random letters
            total=''.join(total)
            window['-PASS-'].update(total)
        except ValueError:
            window['-PASS-'].update("Please Enter a Valid Number")


window.close()