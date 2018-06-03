#!/usr/bin/python3

import sys

f = open("stores.txt")
stores = f.readlines()
f.close()

KNOWN_STORES = [s.strip() for s in stores if s.strip() != ""]

#print("\t[debug] known stores: {}".format(KNOWN_STORES))

def query(options):
    if len(options) <= 1:
        print("[Error] Uh, what did you want us to do? Choose from {}, you say!?".format(options), file=sys.stderr)
        return 0
    print("\tPlease select an option:")
    for i in range(0, len(options)):
        print("\t{}: {}".format(i+1, options[i]))
    print()
    selection = -1
    while selection not in range(0, len(options)):
        try:
            selection = int(input("\tYour selection [1-{}]: ".format(len(options)))) - 1
        except:
            print("\tThat was not an integer from [1-{}]. Please try again.".format(len(options)))
    return (selection, options[selection])

def receiptEntry():
    qu = KNOWN_STORES
    qu.append("Enter New Store")
    n,storeName = query(qu)
    if n == len(KNOWN_STORES) - 1:
        print()
        storeName = input("\tEnter name of the store: ")
    print()
    items = []
    done = False
    while not done:
        action,_ = query(["Enter line item", "Finish"])
        if action == 0:
            print()
            item = input("\tItem Name: ")
            price = -1.0
            while price <= 0:
                try:
                    price = float(input("\tPrice: $ "))
                except:
                    print("\tNo $ signs, please. Also, positive numbers greater than 0, only")
            quantity = 0
            while quantity <= 0:
                try:
                    quantity = int(input("\tQuantity: "))
                except:
                    print("\tEnter a whole number greater than zero, please")
            items.append((item, price, quantity))
            print()
        elif action == 1:
            done = True
        print()
    subtotal = -1.1
    while subtotal <= 0 and subtotal != -1.0:
        try:
            print("\tTo skip entering the subtotal, enter `-1`")
            subtotal = float(input("\t{:9s} $ ".format("Subtotal:")))
        except:
            print("\tNo $ signs, please. Also, positive numbers greater than 0, only, except for when skipping (specify -1)")
    total = -1.1
    while total <= 0:
        try:
            total = float(input("\t{:9s} $ ".format("Total:")))
        except:
            print("\tNo $ signs, please. Also, positive numbers greater than 0, only")
    print("\n")

    # print verification
    print("\t== Summary ==")
    print()
    print("\tItems:")
    longest = 0
    for item in items:
        if len(item[0]) > longest:
            longest = len(item[0])
    for item in items:
        qstr = ""
        if item[2] > 1:
            qstr = "(x{})".format(item[2])
        print(("\t  {:" + str(longest) + "s} $ {:.2f} {}").format(item[0], item[1], qstr))
    print()
    if subtotal > 0:
        print("\t{:9s} $ {:.2f}".format("Subtotal:",subtotal))
        print("\t{:9s} $ {:.2f}".format("Total:",total))
    else:
        print("\t{:6s} $ {:.2f}".format("Total:",total))
    print()
    print("\tIs this correct?")
    ans,_ = query(["Yes", "No"])
    print()
    if ans == 0:
        # TODO: Date validation
        date = input("\tEnter the date on the reciept:\n\t  mm-dd-yy_hh:mm\n\t> ")
        #print("\t" + date)
        print()
        print("\tSaving reciept..")
        fname = "receipts/{}_{}.txt".format(date, storeName.replace(" ","_"))
        f = open(fname, "w")
        f.write("date: {}\n".format(date))
        f.write("store name: {}\n".format(storeName))
        f.write("total: {:.2f}\n".format(total))
        if subtotal > 0:
            f.write("subtotal: {:.2f}\n".format(subtotal))
        f.write("==========\n")
        for item in items:
            f.write("{}_{:.2f}_{}\n".format(item[0], item[1], item[2]))
        f.close()
        print("\tReciept saved as {}".format(fname))
        print()

    else:
        # TODO: implement editing functionality
        print("\tOh well, please start again (TODO: implement editing functionality)")
        print()

print("\tWelcome to the receipt data cruncher")
print()
leave = False
while not leave:
    print("\tWhat would you like to do?")
    action,_ = query(["Enter a receipt", "Exit"])
    print()
    if action == 0:
        receiptEntry()
    else:
        leave = True
