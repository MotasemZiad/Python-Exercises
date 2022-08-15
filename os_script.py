import os

while (True):
    print("1) List Directories")
    print("2) Create a file")
    print("3) Create a directory/folder")
    print("4) Ping a server")
    print("5) Neofetch")
    print("6) Check Python Version")
    print("7) Check Java Version")
    print("8) Exit")

    ch = int(input("Enter Your Choice : "))

    if ch == 1:
        os.system('lsd')
    elif ch == 2:
        f_name = input("Enter file name : ")
        e_name = input("Enter file extension : ")

        os.system('touch ' + f_name + '.' + e_name)
    elif ch == 3:
        name = input("Enter folder name : ")
        os.system('mkdir ' + name)

    elif ch == 4:
        s = input("Enter address(Press enter for default - google.com) : ")
        p = input("Enter number of packer(press enter for default - 10 : )")
        o = input("Do you want the output in a txt file -- y | n -- :")

        # p = int(p)

        if (s == ''):
            s = 'google.com'
        if (p == ''):
            p = '10'

        if (o == 'y'):
            os.system('ping ' + s + ' -c ' + p + ' > ping-output.txt')
        else:
            os.system('ping ' + s + ' -c ' + p)

    elif ch == 5:
        os.system('neofetch')

    elif ch == 6:
        os.system('python --version')

    elif ch == 7:
        os.system('java --version')

    elif ch == 8:
        break
    else:
        print("Invalid Choice")
