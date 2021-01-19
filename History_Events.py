# this is a program in which you can store, retrieve, edit or delete an historical event
import sys
try:
    file = open('database.txt', "r+")
except Exception as e_try:
    print("Run the program again!!")
    file = open('database.txt', "w")
    file.close()
    sys.exit(0)

c = file.readlines()

dic = {20200110: "This script was developed\n"}   # this is a dictionary ( to know more about it feel free to google)

for item in c:
    dic[int(item[:8])] = item[8:]


op = -1

def func1():
    inp = input("Enter the date(eg- 2020/03/01 as yyyy/mm/dd):\n")
    year = int(inp.replace("/", ""))
    event = input("Enter the event: ")+"\n"
    dic[year] = event


def func2():
    inp = input("Enter the date of which event is to be changed(eg- 2020/03/01 as yyyy/mm/dd):\n")
    year = int(inp.replace("/", ""))
    event = input("Enter the new event: ")+"\n"
    dic[year] = event

def func3():
    inp = input("Enter the date to be deleted(eg- 2020/03/01 as yyyy/mm/dd):\n")
    year = int(inp.replace("/", ""))
    del dic[year]


def func4():

    print("Enter 1 to print history of a given century else enter any other number to print the whole history")
    print("\n\n")
    choice = input()
    if int(choice) == 1:
        cent = int(input("Enter the century: "))
        counter = 0
        for key, value, in sorted(dic.items()):

            day =str(key)[6: 8]+ "/"+ str(key)[4:6]+ "/"+ str(key)[0:4]
            if key // 10000 >= cent and key // 10000 < (cent+100):
                print(f"{day} - {value}")
                counter += 1
        if counter == 0:
            print("No event in this century")


    else:
        for key, value, in sorted(dic.items()):

            day =str(key)[6: 8]+ "/"+ str(key)[4:6]+ "/"+ str(key)[0:4]
            print(f"{day} - {value}")

    print("\n\n")



while op != 0:
    print("Option\tAction")
    print("1\t\tTo enter data.")
    print("2\t\tTo edit existing data.")
    print("3\t\tTo delete data.")
    print("4\t\tTo display data.")
    print("0\t\tTo terminate program.")
    op = int(input("Enter your option: "))
    if op == 1:
        func1()
    elif op == 2:
        func2()
    elif op == 3:
        func3()
    elif op == 4:
        func4()
file.truncate(0)
file.close()
new_data = ""
for i, j in dic.items():
    new_data += str(i)+j

file = open('database.txt', "w")
co = file.write(new_data)
print(co)
file.close()
