import re

while 1:
    print("#", end = "") #this is the prompt
    line = input().strip() #reads in the input, trims whitespace at beginning and end
    if len(line) == 0: #empty line; ignore
        continue

    matches = re.split(" +", line) #parses input by space into a list
    
    #parsing command
    command = matches.pop(0) #getting command, first word in input
    command_match = re.match("^[a-zA-Z]+$", command) #checking if command is letters only
    if not command_match: #illegal characters
        print("Error: Command should consist of only a-z, A-Z")
        continue

    #parsing arg
    arg = None

    if len(matches) > 0:
        arg = matches.pop() # getting arg, we'll deal with arg merged with flag issue later
        if not re.match("[a-zA-Z0-9]*$", str(arg)):
            print("Error: Argument should consist of alphanumeric characters")
            continue

    #parsing flags
    flags = list() #now we're getting the flags
    flagError = False;
    for x in matches:
        if not re.match("^-[a-zA-Z]$", x): #invalid flag format
            flagError = True

        flags.append(x)

    if(flagError):
        print("Error: Flags must start with '-' followed by exactly one letter")
        continue

    #dealing with situation where flag and arg are merged (accepted syntax)
    #e.g.: -ofile instead of -o file
    if arg != None and arg[0] == "-": #only single hyphen flags allowed to merge with arg
        flags.append(arg[0:2])
        arg = arg[2:]

    print("Command: " + str(command))
    print("Flags: " + ("None" if len(flags) == 0 else str(flags)))
    print("Argument: " + str(arg))
