# TMULE PROGRAMMING "LANGUAGE"
# Coded by @RoyalCoder51651
# BASIC SYNTAX:
"""Tmule (the most useless language ever) is an esoteric language not meant to be used seriously. 
Because I wanted to make it hard, Tmule programs do not use whitespace, with lines being seperated by a period.
This means that all Tmule programs are always one line long. For future reference, these periods are going to be called newlines
Tmule works by using two major keywords, being start, and stop. These two keywords are modified by adding letters at the beginning or end to 
differentiate eachother. These modified keywords are known as markers.
NOTE: Due to the limitations of the compiler, you must end every program with a newline, even if you have no more code to run
The list of markers, and their syntax, is as follows:
starto/stopo:
    Outputs whatever is contained inside to the console once the program is finished running. Words are seperated by newlines. You cannot use periods, because they are the default newline character
starti/stopi:
    Prompt the user for input, and creates a variable equal to said input. Variable will take the name of whatever the user inputs in the headers. 
    Multiple statements will create multiple variables
startv/stopv:
    Creates a variable, and assigns it the value of the item after it. An example is shown below
    startv.var1.hello.stopv
    This line will create a variable called var1, and assign it the value of hello. Data types dont really exist, and are handled as the program goes on. For generel reference,
    if you use starto/stopo, the data will be treated as a string. Multiple variables can be assigned with the same headers.
starta/stopa:
    Assigns a variable a different value. First word is a variable name, followed by the value it will be reasigned to. Can reasign multiple variables in the same line.
startp/stopp:
    Works the same as starto/stopo, but outputs right away. 
startm/stopm:
    Starts math mode. All code inside of these two headers must be numbers, variables, or math headers.
    Math in Tmule is a little funky. It works by having a total value, that starts at 0 when math mode is started. Certain headers inside of startm/stopm
    will change said value. However, this total is reset to 0 after using the stopm header.    
mstarta/mstopa:
    Math headers that add the values inside to the current total 
mstarts/mstops:
    Math headers that subtract the values inside from the current total
mstartm/mstopm:
    Math headers that multiply the values inside by the current total
mstartd/mstopd:
    Math headers that divide the total by the values inside. Might crash the program because I forgot to refer to floats correctly but idk
mstartv/mstopv:
    Math headers that turn inside values to variables, and assign them the current total
startl/stopl:
    Starts logic mode. For all logic statements, you should include two items to compare. For example, a variable and a number, or two variables.
lstartiee/lstopiee:
    Logic header that uses an if-else statment that compares if the two values given are equal
lstartiege/lstopiege:
    Logic header that uses an If-else statement that compares if the value on the left is greater than or equal to the other
lstartiele/lstopiele:
    Logic header that uses an If-else statement that compares if the value on the left is less than or equal to the other
lstartieg/lstopieg:
    Logic header that uses an If-else statement that compares if the value on the left is greater thanto the other
lstartiel/lstopiel:
    Logic header that uses an If-else statement that compares if the value on the left is less thanto the other
startri/stopri:
    Any code inside these headers will run if the related if-else statement returns true.
startre/stopre:
    Any code inside these header will run if the related if-else statement returns false
startw/stopw:
    Starts while-loop mode.
wstartlie/wstoplie:
    loop header that checks to see if the two condtions inside are equal
wstartline/wstopline:
    loop header that checks to see if the two condtions inside are not equal
wstartlige/wstoplige:
    loop header that checks to see if the condtion on the left is greater than or equal to the condition on the left
wstartlile/wstoplile:
    loop header that checks to see if the condtion on the left is less than or equal to the condition on the left
wstartlil/wstoplil:
    loop header that checks to see if the condtion on the left is less than the condition on the left
wstartlig/wstoplig:
    loop header that checks to see if the condtion on the left is greater than the condition on the left
startli/stopli:
    if the related while-loop is true, runs the code inside multiple times. If not, runs the code inside once.
startf/stopf:
    code inside these headers will be added to a function. start by typing the name of the function, followed by the code you want to run
    startf.greeting.startp.hello.world.stopp.stopf.
    the example above creates a function called greeting, which when called, will print hello world.
startc/stopc:
    calls a function. idk if it crashes or not, so try to use seperate statements if calling multiple functions at the same time.
    startc.greeting.stopc.
    the above example will call the function greeting
DEV COMMANDS:
Dev commands affect items in the compiler itself. Only run if you need or want to accsess or modify these values.
d/printstorage:
prints the lists containing all variables and values
d/startc and d/stopc:
the name of lists inside these headers will be cleared. 
d/startcomment and d/stopcomment:
self explanatory. All code inside these headers will be treated as a comment, and wont do anything
d/terminate:
Stops the current programming from running any further. Will not print any items stored with starto/stopo.
EXAMPLE:
    A simple Hello World program
    starto.Hello,.World!.stopo
    A program that creates a variable, sets it to 5, adds it to 3, stores the total to a total variable, and prints the total
    startv.var1.5.stopv.startm.mstarta.var1.3.mstopa.mstartv.total.mstopv.stopm.starto.total.stopo.
    A program that creates two variables, var1, and var2, checks if var1 is less than var2, prints less than if it is, and greater than if it isn't. Finally, the program prints finished
    startv.var1.3.var2.4.stopv.startl.lstartiel.var1.var2.lstopiel.startri.starto.less.than.stopo.stopri.startre.starto.greater.than.stopo.stopre.stopl.starto.finished.stopo.'"""
# EXPLANATION OF LOGIC AT THE BOTTOM
# PARSER OR SOMETHING IDK I HAVENT DONE THIS BEFORE, AND I DONT KNOW HOW LANGUAGE COMPILERS WORK
print("TMULE v.5.0")
print("What Do You Want To Run?")
text = input()
temp = ''
printline = ""
printer = False
total = 0
inc = False
mathvar = False
single = True
sub = False
stop = False
mult = False
div = False
add = False
skipper = False
var = False
whilev = False
previous = ''
ifv = False
elsev = False
operation = ''
overall = []
comment = False
placeholder = ''
locate = 0
lout = False
vnstorage = []
dprintline = ''
import time
var1 = ''
var2 = ''
lbool = False
oloop = False
switch = False
inputv = False
logic = False
looper = ''
math = False
locatefunc = False
lostorage1 = []
directprint = False
vassign = False
nstorage = []
vstorage = []
lstorage = []
fstorage = []
breakv = True
istorage = []
value = []
devc = False
function = False
funccall = ''
idk = False
lostorage = []
listorage = []
test = ''
locater = 0
valid = True
current = ''
goal = 0
dinc = False
iterator = 0
def devclear(list):
    global value
    global vstorage
    global vnstorage
    global lstorage
    global nstorage
    global lostorage
    global listorage
    global overall
    if (list == "value"):
        value.clear()
    elif (list == "istorage"):
        istorage.clear()
    elif (list == "vnstorage"):
        vnstorage.clear()
    elif (list == "vstorage"):
        vstorage.clear()
    elif (list == "lstorage"):
        lstorage.clear()
    elif (list == "listorage"):
        listorage.clear()
    elif (list == "lostorage"):
        lostorage.clear()
    elif (list == "overall"):
        overall.clear()
def clean():
    global lstorage
    global lostorage
    global placeholder
    try:
        lstorage.remove("startl")
    except:
        placeholder = ''
    try:
        lstorage.remove("lstartiele")
    except:
        placeholder = ''
    try:
        lstorage.remove("lstartiege")
    except:
        placeholder = ''
    try:
        lstorage.remove("lstartiel")
    except:
        placeholder = ''
    try:
        lstorage.remove("lstartieg")
    except:
        placeholder = ''
    try:
        lstorage.remove("lstartiee")
    except:
        placeholder = ''
    try:
        lostorage.remove("startw")
    except:
        placeholder = ''
for i in text:
    while (single == True):
        if(i == "." or oloop == True or idk == True):
            if (comment == True and temp == "d/stopcomment"):
                comment = False
            elif (comment == True):
                temp = ''
            if (stop == True):
                break
            if (idk == True):
                if (locater == 0):
                    locater = fstorage.index(funccall) + 1
                    funccall = ''
                temp = fstorage[locater]
                locater += 1
                if (temp == "stopf"):
                    idk = False
                    locater = 0
                    locatefunc = False
                    breakv = True
            if (function == True):
                fstorage.append(temp)
                if (temp != "stopf"):
                    temp = ''
            single = True
            if (oloop == True):
                if (goal == 0):
                    goal = len(lostorage)
                if (iterator != goal):
                    temp = lostorage[iterator - 1]
                    iterator += 1
                else:
                    iterator = 0
            if (ifv == True):
                if (temp == "stopri"):
                    skipper = False
                    ifv = False
                elif (skipper == True):
                    temp = ''
            if (elsev == True):
                if (temp == "stopre"):
                    skipper = False
                    elsev = False
                elif (skipper == True):
                    temp = ''
            if (temp == "starto"):
                printer = True
            elif (temp == "stopo"):
                printer = False
                overall.append(printline)
                printline = ''
            elif (temp == "d/startc"):
                devc = True
            elif (temp == "d/stopc"):
                devc = False
            elif (temp == "d/startcomment"):
                comment = True
            elif (temp == "startf"):
                function = True
            elif (temp == "stopf"):
                function = False
            elif (temp == "startc"):
                locatefunc = True
            elif (temp == "stopc"):
                idk = False
                locatefunc = False
                breakv = True
            elif (temp == "startv"):
                var = True
            elif (temp == "stopv"):
                var = False
                switch = False
            elif (temp == "start+"):
                inc = True
            elif (temp == "stop+"):
                inc = False
            elif (temp == "start-"):
                dinc = True
            elif (temp == "stop-"):
                dinc = False
            elif (temp == "startw"):
                whilev = True
            elif (temp == "stopw"):
                lostorage.append("stopw")
                if (lbool == True):
                    oloop = True
                    breakv = False
                else:
                    oloop = False
                    breakv = True
                    whilev = False
                    lostorage = []
            elif (temp == "starti"):
                inputv = True
            elif (temp == "stopi"):
                inputv = False
            elif (temp == "startp"):
                directprint = True
            elif (temp == "stopp"):
                print(dprintline)
                directprint = False
                dprintline = ''
            elif (temp == "d/terminate"):
                stop = True
                continue
            elif (temp == "d/printstorage"):
                print("istorage:", istorage)
                print("value:", value)
                print("vstorage:", vstorage)
                print("vnstorage:", vnstorage)
                print("lstorage:", lstorage)
                print("nstorage:", nstorage)
                print("lostorage:", lostorage)
                print("listorage:", listorage)
                print("overall:", overall)
                print("fstorage:", fstorage)
            elif (temp == "starta"):
                vassign = True
            elif (temp == "stopa"):
                vassign = False
                switch = 0
            elif (temp == "startri" and lout == True):
                ifv = True
            elif (temp == "startri" and lout == False):
                skipper = True
                ifv = True
            elif (temp == "startre" and lout == False):
                elsev = True
            elif (temp == "startre" and lout == True):
                skipper = True
                elsev = True
            elif (temp == "startl"):
                logic = True
            elif (temp == "stopl"):
                logic = False
                ifv = False
                elsev = False
                lstorage = []
                operation = ""
            elif (temp == "startm"):
                math = True
            elif (temp == "stopm"):
                math = False
                total = 0
                nstorage = []
    # Last Level Items (Only Run If Key-Words Are Not Found In The Item)
            elif (inc == True):
                if (temp in istorage):
                    locate = istorage.index(temp)
                    value[locate] = int(value[locate]) + 1
                elif (temp in vstorage):
                    locate = vstorage.index(temp)
                    vnstorage[locate] = int(vnstorage[locate]) + 1
            elif (dinc == True):
                if (temp in istorage):
                    locate = istorage.index(temp)
                    value[locate] = int(value[locate]) - 1
                elif (temp in vstorage):
                    locate = vstorage.index(temp)
                    vnstorage[locate] = int(vnstorage[locate]) - 1
            elif (locatefunc == True):
                funccall = temp
                idk = True
                locatefunc = False
                breakv = False
            elif (directprint == True):
                if (temp in vstorage):
                    locate = vstorage.index(temp)
                    dprintline = dprintline + str(vnstorage[locate]) + ' '
                elif (temp in istorage):
                    locate = istorage.index(temp)
                    dprintline = dprintline + str(value[locate]) + ' '
                else:
                    dprintline = dprintline + temp + ' '
            elif (printer == True):
                if (temp in vstorage):
                    locate = vstorage.index(temp)
                    printline = printline + str(vnstorage[locate]) + ' '
                elif (temp in istorage):
                    locate = istorage.index(temp)
                    printline = printline + str(value[locate]) + ' '
                else:
                    printline = printline + temp + ' '
            elif (var == True and switch == False):
                vstorage.append(temp)
                switch = True
            elif (var == True and switch == True):
                vnstorage.append(temp)
                switch = False
            elif (devc == True):
                devclear(temp)
            
            elif (vassign == True and switch == False):
                locate = vstorage.index(temp)
                switch = True
            elif (vassign == True and switch == True):
                vnstorage[locate] = temp
                switch = False
            elif (inputv == True):
                if (temp in istorage):
                    locate = istorage.index(temp)
                    value[locate] = input()
                elif (temp in vstorage):
                    locate = vstorage.index(temp)
                    vnstorage[locate] = input()
                else:
                    istorage.append(temp)
                    temp = input()
                    value.append(temp)
    # MATH
            elif (math == True):
                if (temp == "mstarta"):
                    add = True
                elif (temp == "mstopa" and add == True):
                    add = False
                    for num in nstorage:
                        try:
                            if (num in vstorage):
                                locate = vstorage.index(num)
                                total += int(vnstorage[locate])
                            elif (num in istorage):
                                locate = istorage.index(num)
                                total += int(value[locate])
                            else:
                                total += int(num)
                        except:
                            placeholder = ''
                    nstorage = []
                elif (temp == "mstarts"):
                    sub = True
                elif (temp == "mstops" and sub == True):
                    sub = False
                    for num in nstorage:
                        try:
                            if (num in vstorage):
                                locate = vstorage.index(num)
                                total -= int(vnstorage[locate])
                            elif (num in istorage):
                                locate = istorage.index(num)
                                total -= int(value[locate])
                            else:
                                total -= int(num)
                        except:
                            placeholder = ''
                    nstorage = []
                elif (temp == "mstartd"):
                    div = True
                elif (temp == "mstopd" and div == True):
                    div = False
                    for num in nstorage:
                        try:
                            if (num in vstorage):
                                locate = vstorage.index(num)
                                total /= int(vnstorage[locate])
                            elif (num in istorage):
                                locate = istorage.index(num)
                                total /= int(value[locate])
                            else:
                                total /= int(num)
                        except:
                            placeholder = ''
                    nstorage = []
                elif (temp == "mstartm"):
                    mul = True
                elif (temp == "mstopm" and mul == True):
                    mul = False
                    for num in nstorage:
                        try:
                            if (num in vstorage):
                                locate = vstorage.index(num)
                                total *= int(vnstorage[locate])
                            elif (num in istorage):
                                locate = istorage.index(num)
                                total *= int(value[locate])
                            else:
                                total *= int(num)
                        except:
                            placeholder = ''
                    nstorage = []
                elif (temp == "mstartv"):
                    mathvar = True
                elif (temp == "mstopv"):
                    mathvar = False
                elif (mathvar == True):
                    if (temp in vstorage):
                        locate = vstorage.index(temp)
                        vnstorage[locate] = total
                    elif (temp in istorage):
                        locate = istorage.index(temp)
                        value[locate] = total
                    else:
                        vstorage.append(temp)
                        vnstorage.append(total)
                if (math == True):
                    nstorage.append(temp)
                    
# logic                    
                    
            if (logic == True):
                clean()
                lstorage.append(temp)
                if (temp == "lstartiee"):
                    operation = "if-else-equals"
                elif (temp == "lstopiee" and operation == "if-else-equals"):
                    clean()
                    if (lstorage[0] in istorage):
                        locate = istorage.index(lstorage[0])
                        var1 = str(value[locate])
                    elif (lstorage[0] in vstorage):
                        locate = vstorage.index(lstorage[0])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lstorage[0])
                    if (lstorage[1] in istorage):
                        locate = istorage.index(lstorage[1])
                        var2 = str(value[locate])
                    elif (lstorage[1] in vstorage):
                        locate = vstorage.index(lstorage[1])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lstorage[1])
                    if (var1 == var2):
                        lout = True
                elif (temp == "lstartiege"):
                    operation = "if-else-greater-equal"
                elif (temp == "lstopiege" and operation == "if-else-greater-equal"):
                    clean()
                    if (lstorage[0] in istorage):
                        locate = istorage.index(lstorage[0])
                        var1 = str(value[locate])
                    elif (lstorage[0] in vstorage):
                        locate = vstorage.index(lstorage[0])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lstorage[0])
                    if (lstorage[1] in istorage):
                        locate = istorage.index(lstorage[1])
                        var2 = str(value[locate])
                    elif (lstorage[1] in vstorage):
                        locate = vstorage.index(lstorage[1])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lstorage[1])
                    if (int(var1) >= int(var2)):
                        lout = True
                elif (temp == "lstartiele"):
                    operation = "if-else-less-equal"
                elif (temp == "lstopiele" and operation == "if-else-less-equal"):
                    clean()
                    if (lstorage[0] in istorage):
                        locate = istorage.index(lstorage[0])
                        var1 = str(value[locate])
                    elif (lstorage[0] in vstorage):
                        locate = vstorage.index(lstorage[0])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lstorage[0])
                    if (lstorage[1] in istorage):
                        locate = istorage.index(lstorage[1])
                        var2 = str(value[locate])
                    elif (lstorage[1] in vstorage):
                        locate = vstorage.index(lstorage[1])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lstorage[1])
                    if (int(var1) <= int(var2)):
                        lout = True
                elif (temp == "lstartiel"):
                    operation = "if-else-less"
                elif (temp == "lstopiel" and operation == "if-else-less"):
                    clean()
                    if (lstorage[0] in istorage):
                        locate = istorage.index(lstorage[0])
                        var1 = str(value[locate])
                    elif (lstorage[0] in vstorage):
                        locate = vstorage.index(lstorage[0])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lstorage[0])
                    if (lstorage[1] in istorage):
                        locate = istorage.index(lstorage[1])
                        var2 = str(value[locate])
                    elif (lstorage[1] in vstorage):
                        locate = vstorage.index(lstorage[1])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lstorage[1])
                    if (int(var1) < int(var2)):
                        lout = True
                elif (temp == "lstartieg"):
                    operation = "if-else-greater"
                elif (temp == "lstopiel" and operation == "if-else-greater"):
                    clean()
                    if (lstorage[0] in istorage):
                        locate = istorage.index(lstorage[0])
                        var1 = str(value[locate])
                    elif (lstorage[0] in vstorage):
                        locate = vstorage.index(lstorage[0])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lstorage[0])
                    if (lstorage[1] in istorage):
                        locate = istorage.index(lstorage[1])
                        var2 = str(value[locate])
                    elif (lstorage[1] in vstorage):
                        locate = vstorage.index(lstorage[1])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lstorage[1])
                    if (int(var1) > int(var2)):
                        lout = True
            if (whilev == True):
                if (oloop == False):
                    lostorage.append(temp)
                if (temp == "wstartlie"):
                    looper = "loop-if-equal"
                elif (temp == "wstoplie" and looper == "loop-if-equal"):
                    clean()
                    if (lostorage[1] in istorage):
                        locate = istorage.index(lostorage[1])
                        var1 = str(value[locate])
                    elif (lostorage[1] in vstorage):
                        locate = vstorage.index(lostorage[1])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lostorage[1])
                    if (lostorage[2] in istorage):
                        locate = istorage.index(lostorage[2])
                        var2 = str(value[locate])
                    elif (lostorage[2] in vstorage):
                        locate = vstorage.index(lostorage[2])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lostorage[2])
                    if (var1 == var2):
                        lbool = True
                    else:
                        lbool = False
                elif (temp == "wstartline"):
                    looper = "loop-if-not-equal"
                elif (temp == "wstopline" and looper == "loop-if-not-equal"):
                    clean()
                    if (lostorage[1] in istorage):
                        locate = istorage.index(lostorage[1])
                        var1 = str(value[locate])
                    elif (lostorage[1] in vstorage):
                        locate = vstorage.index(lostorage[1])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lostorage[1])
                    if (lostorage[2] in istorage):
                        locate = istorage.index(lostorage[2])
                        var2 = str(value[locate])
                    elif (lostorage[2] in vstorage):
                        locate = vstorage.index(lostorage[2])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lostorage[2])
                    if (var1 != var2):
                        lbool = True
                    else:
                        lbool = False
                elif (temp == "wstartlile"):
                    looper = "loop-if-less-equal"
                elif (temp == "wstoplile" and looper == "loop-if-less-equal"):
                    clean()
                    if (lostorage[1] in istorage):
                        locate = istorage.index(lostorage[1])
                        var1 = str(value[locate])
                    elif (lostorage[1] in vstorage):
                        locate = vstorage.index(lostorage[1])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lostorage[1])
                    if (lostorage[2] in istorage):
                        locate = istorage.index(lostorage[2])
                        var2 = str(value[locate])
                    elif (lostorage[2] in vstorage):
                        locate = vstorage.index(lostorage[2])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lostorage[2])
                    if (var1 <= var2):
                        lbool = True
                    else:
                        lbool = False
                elif (temp == "wstartlige"):
                    looper = "loop-if-greater-equal"
                elif (temp == "wstoplige" and looper == "loop-if-greater-equal"):
                    clean()
                    if (lostorage[1] in istorage):
                        locate = istorage.index(lostorage[1])
                        var1 = str(value[locate])
                    elif (lostorage[1] in vstorage):
                        locate = vstorage.index(lostorage[1])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lostorage[1])
                    if (lostorage[2] in istorage):
                        locate = istorage.index(lostorage[2])
                        var2 = str(value[locate])
                    elif (lostorage[2] in vstorage):
                        locate = vstorage.index(lostorage[2])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lostorage[2])
                    if (var1 >= var2):
                        lbool = True
                    else:
                        lbool = False
                elif (temp == "wstartlig"):
                    looper = "loop-if-greater"
                elif (temp == "wstoplig" and looper == "loop-if-greater"):
                    clean()
                    if (lostorage[1] in istorage):
                        locate = istorage.index(lostorage[1])
                        var1 = str(value[locate])
                    elif (lostorage[1] in vstorage):
                        locate = vstorage.index(lostorage[1])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lostorage[1])
                    if (lostorage[2] in istorage):
                        locate = istorage.index(lostorage[2])
                        var2 = str(value[locate])
                    elif (lostorage[2] in vstorage):
                        locate = vstorage.index(lostorage[2])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lostorage[2])
                    if (var1 > var2):
                        lbool = True
                    else:
                        lbool = False
                elif (temp == "wstartlil"):
                    looper = "loop-if-less"
                elif (temp == "wstoplil" and looper == "loop-if-less"):
                    clean()
                    if (lostorage[1] in istorage):
                        locate = istorage.index(lostorage[1])
                        var1 = str(value[locate])
                    elif (lostorage[1] in vstorage):
                        locate = vstorage.index(lostorage[1])
                        var1 = str(vnstorage[locate])
                    else:
                        var1 = str(lostorage[1])
                    if (lostorage[2] in istorage):
                        locate = istorage.index(lostorage[2])
                        var2 = str(value[locate])
                    elif (lostorage[2] in vstorage):
                        locate = vstorage.index(lostorage[2])
                        var2 = str(vnstorage[locate])
                    else:
                        var2 = str(lostorage[2])
                    if (var1 < var2):
                        lbool = True
                    else:
                        lbool = False
            temp = ""
        else:
            if (i == " "):
                print("You Trying To Make This Easier On Yourself??? NAHHHH")
                stop = True
                break
            temp += i
        if (breakv == True):
            break
    if (stop == True):
        break
if (stop == False):
    print(*overall, sep='')
"""
Thanks For Using My Language! I Don't Know Why You Wanted To, But Hey, Hope It Was At Least Somewhat Understandable.
To begin, I have a for loop going through the user input. it will add each letter to a total word, which is called temp.
This item is called temp because it is a temporary input, and totally not because I just reused this algorithm from another project.
Once the program hits a newline character, it will check to see what this temp variable is, and act acccordingly.
If the program recognizes it as a header, it will run the associated header's function. If it isnt an applicable function,
the program either crashes, or treats it as a comment. I havent tested this too much, but I plan on adding a comment line header soon.
The basic idea behind storage centers around a series of lists. These lists come in pairs of two, representing the name of a stored variable,
and the argument stored inside said variable. These lists match eachother exactly, so a list that contains the name of 4 variables will always have
a list that contains 4 arguments associated with it. I used to have a central list storing both variable names, and arguments,
but this led to a large number of unforseen consquences (arguments were being treated as variables, which is bad).
It should be noted that for the starto/stopo headers, data isn't directly printed, but instead stored to an output list. This is
so you can have several different starto/stopo statements that all end up printing on the same line. This was because it looked
better, and fits with the single-line theme. One unfortunate downside of the current system for handling conditionals is that
evaluating multiple condtions is basically impossible without adding a lot more logic statements. This shouldn't be an issue, because
this language likely wont see the light of day. As far as the newline character goes, the default value is assigned to a period. There
is no real reason for this, but only a single line has to be changed to switch the character, so it's prolly fine.
List of lists and storage methods:
istorage and value: store variables created by user inputs and their arguments respectivly
vstorage and vnstorage: store variables created by startv/stopv and their arguments
lstorage: stores the text that needs to be looped through during while loops
nstorage: stores the items that are modified during math operations
overall: stores the text generated by starto/stopo
"""