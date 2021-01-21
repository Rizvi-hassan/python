"""
This is a program which is a kind of a "bahi- khata"(if you don`t know its meaning please google it).
It is useful for shopkeepers who run khata system for their regular customers.
This program gives you the following features:
    * Activate new customers khata
    * Stores the debt along with the date when it was taken
    * Stores the paid amount along with the date when it was given
    * You can see the remaining debt of all the customers along with the last paid amount with its date
    * You can see the detailed debts and paid amounts with their dates of each customers
    """
# ----------------------------------------PROGRAM----------------------------------------------------------


import time
c_name = []  # this is a global variable which stores the name of all the current customers

def inp_dept():
    """It is a function which takes debt as input.
       It takes the current date and returns a steing in which
        date and debt amount is concatenated.
        The string is stored in the text file for further use

        :return:    string
    """
    cur_time = time.strftime("%a, %d %b, %Y", time.localtime())
    inp = input("Enter the dept amount: ")
    return f"{cur_time} == debt- {inp}\n"


def inp_pay():
    """
    It is a function which takes paid amount as input.
    It takes the current date and returns a steing in which
        date and debt amount is concatenated.
        The string is stored in the text file for further use

    :return: string
    """
    cur_time = time.strftime("%a, %d %b, %Y", time.localtime())
    inp = input("Enter the paid amount: ")
    return f"{cur_time} == paid- {inp}\n"


def cust_inp_debt(index):
    """
    This function appends the string returned by inp_dept() in the text file of a user
    :param index: It is a provided index number of the c_name list which denotes the name of user
                  in whose text file the string is appended
    :return: none
    """
    with open(f"Bahi_data/{c_name[index]}.txt", "a") as F:
        content = inp_dept()
        F.write(content)


def cust_inp_pay(index):
    """
    This function appends the string returned by inp_pay() in the text file of a user
    :param index: It is a provided index number of the c_name list which denotes the name of user
                  in whose text file the string is appended
    :return: none
    """
    with open(f"Bahi_data/{c_name[index]}.txt", "a") as F:
        content = inp_pay()
        F.write(content)


def new_customer():
    """
    This is a function to create a new customer`s text file. It
    creates a new customer whose Bahi Khata is made.
    It takes the name from cust_strp() function and creates its khata
    :return: none
    """
    name = cust_strp()
    with open("Bahi_data/name_customer.txt", "a") as f:
        f.write(name+"\n")
    with open(f"Bahi_data/{name}.txt", "w")as F:
        F.write(inp_dept())


def cust_strp():
    """
    This is a function which takes new user`s name as input and converts it into upper case after replacing all the
    " " with "_".
    :return: r_name: It is the processed name whose txt file is going to be made by new_customer() function
    """
    name = input("Enter the name of customer: ")
    r_name = name.strip()
    r_name = r_name.upper()
    r_name = r_name.replace(" ", "_")
    return r_name


def cust_name_disp():
    """
    This function is used to display the name of all the existing customers so that the for the shopkeeper to choose
    from name_customer.txt file, stored in c_name list
    :return: c_index: It is the index no. of the selected name of list- c_name
    """
    with open("Bahi_data/name_customer.txt", "r") as f:
        global c_name
        c_name = f.read().split("\n")
        print("NO.\t\tNAME")
        for i in range(len(c_name)-1):
            print(i, "\t-\t", c_name[i])
        print("-1\t-\t to go back\n-----------------------------")
        c_index = int(input("Enter the no. of a customer whose data is to be used: "))
        return c_index

def debt_count(customer_name):
    """
    This function counts the total debt and paid amount of the given customer.
    :param customer_name: name of the customer whose debt is to be counted
    :return: a list which contains the remaining debt of the customer and the date when last amount was paid
    """
    debt_sum = 0
    paid_sum = 0
    l_paid = ""
    with open(f"Bahi_data/{customer_name}.txt", "r") as f:
        cust_data = f.read().split("\n")
        for item in cust_data:
            if item[21:25] == "debt":
                debt_sum += int(item[27:])
            elif item[21:25] == "paid":
                l_paid = item
                paid_sum += int(item[27:])

    return [debt_sum-paid_sum, l_paid]


def cust_debt_disp():
    """
    This function displays the name, last paid amount and remaining debt of all all the customers in an order from old customer to new customer
    :return: none
    """
    with open("Bahi_data/name_customer.txt", "r") as f:
        cust_name = f.read().split("\n")
        cust_name.pop(len(cust_name)-1)
        for item in cust_name:
            c_ret = debt_count(item)
            print(f"Customer name: {item}\nLast Paid: {c_ret[1]}\nDebt Amount: {c_ret[0]}\n")
            print("\n----------------------------------------------")


def detail_disp(ind):
    """
    This program displays all the debt and paid amount of a given customer along with the dates
    when the debt was taken.
    :param ind: it is the index no. of the name form the c_name list whose detailed info is to be printed.
    :return:
    """
    name = c_name[ind]
    dep_str = debt_count(name)
    with open(f"Bahi_data/{name}.txt", "r") as f:
        det = f.read().split("\n")
        for item in det:
            print(item)
        print(f"Remaining debt: {dep_str[0]}\nLast paid : {dep_str[1]}")
        print("\n----------------------------------------------\n")


def short_hand_disp(ind):
    """
    This program displays the debt and last paid amount of a given customer
    :param ind: it is the index no. of the name form the c_name list whose short-hand info is to be printed.
    :return:
    """
    name = c_name[ind]
    dep_str = debt_count(name)
    with open(f"Bahi_data/{name}.txt", "r") as f:
        det = f.read().split("\n")
        # for item in det:
        #     print(item)
        print(f"Remaining debt: {dep_str[0]}\nLast paid : {dep_str[1]}")
        print("\n----------------------------------------------\n")

if __name__ == '__main__':
    while True:
        e_data = int(input("Enter 1 to Enter data\nEnter 2 to See data\nEnter 0 to exit: "))
        if e_data == 1:
            # user selected to Enter data
            while True:
                e_cust = int(input("Enter 1 to Add a new customer\nEnter 2 to input data of existing customer\nEnter 0 to go back: "))
                if e_cust == 1:
                    # user selected to add a new customer
                    new_customer()
                elif e_cust == 2:
                    # user selected to input data of existing customer
                    inx = cust_name_disp()
                    if inx == -1:
                        continue
                    else:
                        while True:
                            e_inp = int(input("Enter 1 to input debt amount\nEnter 2 to input paid amount\nEnter 3 to display his debt\nEnter 0 to go back: "))
                            if e_inp == 1:
                                # user selected to enter debt amount
                                cust_inp_debt(inx)
                                print("Debt amount added")
                            elif e_inp == 2:
                                # user selected to enter paid amount
                                cust_inp_pay(inx)
                                print("Paid amount added")
                            elif e_inp == 3:
                                # user selected to display the remaining debt and last paid amount of a customer
                                short_hand_disp(inx)
                            elif e_inp == 0:
                                # user selected to go back
                                break
                            else :
                                # if wrong input is being input then it asks again to input
                                continue

                elif e_cust == 0:
                    # user selected to go back
                    break

                else:
                    # if wrong input is being input then it asks again to input
                    continue

        elif e_data == 2:
            # user selected to display data
            while True:
                e_disp_op = int(input("Enter 1 to display the debt of all customers\nEnter 2 to display the detailed debt of a single customer\nEnter 0 to exit"))
                if e_disp_op == 1:
                    # user selected to display debt of all customers
                    cust_debt_disp()
                elif e_disp_op == 2:
                    # user selected to display the detailed debt of a single user
                    d_inx = cust_name_disp()
                    if d_inx == -1:
                        continue
                    else:
                        detail_disp(d_inx)
                elif e_disp_op == 0:
                    break
                else:
                    # user entered wrong no. so program will ask again
                    continue
        elif e_data == 0:
            # user decided to stop the program
            break

        else:
            # user entered wrong no. so it will ask again
            continue
