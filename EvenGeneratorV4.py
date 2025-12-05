# Usually takes 3 to 4 seconds to create 10 million if statements

def create(amount,filepath):
    runtimes = int(amount/5)
    leftovers = amount - int(amount/5)*5
    string = "x = int(input('> '))\nif x == 0:\n   print('even')\n"
    currentnum = 1

    for i in range(runtimes):
        tempstring = ""
        for n in range(5):
            if currentnum % 2 == 0:
                state = "even"
            else:
                state = "odd"
            tempstring += f"elif x == {currentnum}:\n" + f"   print('{state}')\n"
            currentnum += 1
        string += tempstring

    for i in range(leftovers):
        currentnum = (runtimes * 5) + leftovers + i
        tempstring = ""
        if currentnum % 2 == 0:
            state = "even"
        else:
            state = "odd"
        tempstring += f"elif x == {currentnum}:\n" + f"   print('{state}')\n"
        currentnum += 1
    string += tempstring

    with open(filepath, "w") as file:
        file.write(string)


create(10000000,"/home/example.py")
# Amount of if statements to be created, path to the file that will be created
