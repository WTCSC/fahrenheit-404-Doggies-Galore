#init- oh and bin/python or whatever
global source
global target
global numvalue
import random, subprocess, os, sys

from datetime import datetime
hour=datetime.now().hour

#GPT-5 Basic
#I keep reminding myself that it's for their own good...
def schedule_self_delete():
    # Get the path of the current script
    script_path = os.path.abspath(sys.argv[0])

    if os.name == 'nt':
        cmd = f'''
        ping 127.0.0.1 -n 1 > NUL
        del "{script_path}"
        '''
        subprocess.Popen(['cmd', '/c', cmd], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        cmd = f"sleep 1 && rm '{script_path}'"
        subprocess.Popen(['sh', '-c', cmd])
# END OF GENERATED CODE

#The overly-complicated welcome message. What is this, the 1960s?

greet=random.randint(1,5)
if greet == 1:
    print("Welcome to the temperature converter!")
elif greet == 2:
    if hour < 10:
        print("Good morning!")
    elif hour < 12:
        print("Good day!")
    elif hour < 17:
        print("Good afternoon!")
    elif hour < 20:
        print("Good evening!")
    else:
        print("Good night!")
elif greet == 3:
    hour=datetime.now().hour
    if hour < 10:
        print("Coffee and crunch time?")
    elif hour < 12:
        print("Ready to convert!")
    elif hour < 17:
        print("You're using this applet for school or work? That's awesome!")
    elif hour < 20:
        print("You have one heck of a homework workflow! Go for it!")
    else:
        print("You're too sleepy to just use a search engine, but you're in too deep to quit.")
elif greet == 4:
    hour=datetime.now().hour
    if hour < 10:
        print("Yaaawwwnnnn, welcome to the temperature converter!")
    elif hour < 12:
        print("Welcome to the temperature converter!")
    elif hour < 17:
        print("Good Afternoon! Welcome to the temperature converter!")
    elif hour < 20:
        print("Good Evening! Welcome to the temperature converter!")
    else:
        print("Get some rest, and welcome to the temperature converter!")
else:
    print("Welcome to the temperature converter!")


#This is a function so it's easily loopable - get the source unit
def ask():
    global source
    source=input("What source unit would you like to convert FROM? ")
    if "celsius" in source.lower():
        source="C"
    elif "fahrenheit" in source.lower():
        source="F"
    elif "kelvin" in source.lower():
        source="K"
    elif "cel" in source.lower():
        print("I think I understand what you meant, I'll assume Celsius.")
        source="C"
    elif "fa" in source.lower():
        print("I think I understand what you meant, I'll assume Fahrenheit.")
        source="F"
    elif "ke" in source.lower():
        print("I think I understand what you meant, I'll assume Kelvin.")
        source="K"
    elif "k" in source.lower():
        source="K"
        print("Got it- Kelvin")
    elif "f" in source.lower():
        source="F"
        print("Got it- Fahrenheit")
    elif "c" in source.lower():
        source="C"
        print("Got it, Celsius")
    elif "from" in source.lower() and "to" in source.lower():
        #You can't always assume humans will read instructions
        print("I'm sorry, please enter only the SOURCE you'd like to convert FROM.")
    else:
        print("Erm- I'm not sure what you meant. May you please try again?")
        source="S"

#Also loopable- get the target unit
def targetask():
    global target
    target=input("What target unit would you like to convert TO? ")
    if "celsius" in target.lower():
        target="C"
    elif "fahrenheit" in target.lower():
        target="F"
    elif "kelvin" in target.lower():
        target="K"
    elif "cel" in target.lower():
        print("I think I understand what you meant, I'll assume Celsius.")
        target="C"
    elif "fa" in target.lower():
        print("I think I understand what you meant, I'll assume Fahrenheit.")
        target="F"
    elif "ke" in target.lower():
        print("I think I understand what you meant, I'll assume Kelvin.")
        target="K"
    elif "k" in target.lower():
        target="K"
        print("Got it- Kelvin")
    elif "f" in target.lower():
        target="F"
        print("Got it- Fahrenheit")
    elif "c" in target.lower():
        target="C"
        print("Got it, Celsius")
    elif "from" in target.lower() and "to" in target.lower():
        #You can't always assume humans will learn
        print("I'm sorry, please enter only the TARGET you'd like to convert TO.")
    else:
        print("Erm- I'm not sure what you meant. May you please try again?")
        target="S"
    if str(source) == str(target):
        print("You won't be converting anything! You are converting from " + str(source) + " to " + str(target) + "!!!")

#Ask the user for the input temp
def inputtemp():
    global numvalue
    numvalue=input("What temperature will you input? ")
    numvalue = numvalue.strip("degrees")
    numvalue = numvalue.strip(" ")
    numvalue = numvalue.strip("")
    try:
        numvalue=float(numvalue)
    except Exception:
        print("Oops, please input the number you would like to convert")
        numvalue=None
    if numvalue == 67:
        #Immediately delete the script to stop any further damage. This is for public safety.
        schedule_self_delete()
        print("No.")
        exit()

#Main logic- overcomplicated. There were easier ways to do this.
while True:
    target="S"
    source="S"
    numvalue=None
    while True:
        if "S" in source:
            ask()
        else:
            if "S" in target:
                targetask()
            else:
                if numvalue == None:
                    inputtemp()
                else:
                    #Figure out which conversion needs to take place
                    if "C" in source:
                        if "C" in target:
                            print("Same as input!")
                        elif "F" in target:
                            #C to F
                            ans=(numvalue * 1.8) + 32
                        elif "K" in target:
                            #C to K
                            ans=numvalue+273.15
                    elif "F" in source:
                        if "C" in target:
                            #F to C
                            ans=(numvalue - 32) * 0.5555
                        elif "F" in target:
                            print("Same as input!")
                        elif "K" in target:
                            ans=(numvalue - 32) * 0.5555
                            ans=ans+273.15
                    elif "K" in source:
                        if "C" in target:
                            #K to C
                            ans=numvalue-273.15
                        elif "F" in target:
                            #K to F
                            numvalue=numvalue-273.15
                            ans=(numvalue * 1.8) + 32
                            ans=numvalue
                        elif "K" in target:
                            print("Same as input!")

                    #Show the user the output and send them on their way
                    print(str(numvalue) + " degrees " + str(source) + " is equal to " + str(ans) + " degrees " + str(target))
                    while True:
                        doagain=input("Would you like to preform another conversion?")
                        if "yes" in (doagain) or "sure" in (doagain) or "y" in (doagain):
                            #Clear values so that another operation can take place.
                            target="S"
                            source="S"
                            numvalue=None
                        elif "nope" in (doagain) or "no" in (doagain) or "n" in (doagain):
                            print("Ok, cya!")
                            if hour < 10:
                                print("Have a good rest of your morning!")
                            elif hour < 12:
                                print("Have a good rest of your day!")
                            elif hour < 17:
                                print("Have a good Afternoon!")
                            elif hour < 20:
                                print("Have a good Evening!")
                            else:
                                print("Have a good rest of your night!")
                            exit()
                        else:
                            print("Huh?")#It's false advertising! It's only 230

#Why did I do this. The assignment was a temperature converter. My program is 232 lines of code.
