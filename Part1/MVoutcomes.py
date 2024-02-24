# date 2/24/2024
# Name LIA Perera
# part 1 Main Version
# A outcomes

import time

pCredit = 0
dCredit = 0
fCredit = 0
totMarks = 0
condition = False


while True:
    pCredit = int(input("Enter credits at PASS : "))
    if pCredit == 120:
        print("PASS", "=", pCredit)
        print("Successfully entred !!")
        break
    dCredit = int(input("Enter credits at DEFFER : "))
    if dCredit+pCredit == 120:
        print("PASS", "=", pCredit)
        print("DEFFER", "=", dCredit)
        print("Successfully entred !!")
        break
    fCredit = int(input("Enter credits at FAIL : "))
    if pCredit + fCredit +dCredit == 120:
        print("PASS", "=", pCredit)
        print("DEFFER", "=", dCredit)
        print("FAIL", "=", fCredit)
        print("Successfully entred !!")
        break
def progress(pCredit, dCredit, fCredit):
    if pCredit == 120:
        print("... PROGRESS ...")
    elif pCredit == 100 and (dCredit == 20 or fCredit == 20):
        print("... PROGRESS - MODULE TRAILER ...")
    elif fCredit >= 80:
        print("... EXCLUDE ...")
    elif (dCredit + fCredit >= 40):
        print("... DO NOT PROGRESS – MODULE RETRIEVET ...")


result = "........."
print("Result pending", end="")
for letters in result:
    print(letters, end="")
    time.sleep(0.3)

time.sleep(0.3)
print()
print()

outcome = progress(pCredit, dCredit, fCredit)
time.sleep(5)