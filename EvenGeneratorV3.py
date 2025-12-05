import time
def addcode(times,timespassed):
    msg1 = ""
    for i in range(int(times)):
        if i % 2 == 0:
            state = "odd"
        else:
            state = "even"
        msg1 = msg1 + f"elif x == {int(i+1 + timespassed * (times))}:\n" + f'    print("{state}")\n'
        print(f"[{timespassed + 1}] {int(i+1)}/{int(times)}")
    return msg1

def runner(times,splitfreq):
    msg2 = ""
    for i in range(splitfreq):
        msg2 += addcode(times/splitfreq,i)
    return msg2

def main():
    msg = "x = int(input('> '))\n" + f"if x == {0}:\n" + f'    print("even")\n'
    msg += runner(10000000, 500000) #input yo shid here cro (amounttocreate,splitamt)
    with open("oddeven.py","w") as file:
        file.write(msg)
time1 = time.time()
main()
time2 = time.time()

print(time2-time1)