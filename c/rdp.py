SUCCESS = True
FAILED = False

def E():
    global cursor
    print("{:16s} E -> T E'".format(cursor))
    if T():
        if Edash():
            return SUCCESS
        else:
            return FAILED
    else:
        return FAILED

def Edash():
    global cursor
    if cursor and cursor[0] == '+':
        cursor = cursor[1:]
        print("{:16s} E' -> + T E'".format(cursor))
        if T():
            if Edash():
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    else:
        print("{:16s} E' -> $".format(cursor))
        return SUCCESS

def T():
    global cursor
    print("{:16s} T -> F T'".format(cursor))
    if F():
        if Tdash():
            return SUCCESS
        else:
            return FAILED
    else:
        return FAILED

def Tdash():
    global cursor
    if cursor and cursor[0] == '*':
        cursor = cursor[1:]
        print("{:16s} T' -> * F T'".format(cursor))
        if F():
            if Tdash():
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    else:
        print("{:16s} T' -> $".format(cursor))
        return SUCCESS

def F():
    global cursor
    if cursor and cursor[0] == '(':
        cursor = cursor[1:]
        print("{:16s} F -> ( E )".format(cursor))
        if E():
            if cursor and cursor[0] == ')':
                cursor = cursor[1:]
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    elif cursor and cursor[0] == 'i':
        cursor = cursor[1:]
        print("{:16s} F -> i".format(cursor))
        return SUCCESS
    else:
        return FAILED

# Test the parser
cursor = ""
string = "i+(i+i)*i" #input
cursor = string
print("\nInput            Action")
print("--------------------------------")

if E() and cursor == "":
    print("--------------------------------")
    print("String is successfully parsed")
else:
    print("--------------------------------")
    print("Error in parsing string")
