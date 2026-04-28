my_list = []
my_tuple = ()
my_set = set()
my_dict = {}

while True:
    print("\n Menu")
    print("1.list operation")
    print("2.tuple operation")
    print("3.set operation")
    print("4.dict operation")
    print("5.exit")
   
    choice = int(input("enter choice: "))
   
    # list
    if choice == 1:
        while True:
            print("\n list operation")
            print("1.insert")
            print("2.update")
            print("3.display")
            print("4.sort")
            print("5.search")
            print("6.back")
           
            ch = int(input("enter choice: "))
           
            if ch == 1:
                val = int(input("enter value: "))
                my_list.append(val)
               
            elif ch == 2:
                pos = int(input("enter position: "))
                val = int(input("enter new value: "))
                if pos < len(my_list):
                    my_list[pos] = val
                   
            elif ch == 3:
                print("list:", my_list)
               
            elif ch == 4:
                my_list.sort()
                print("sorted list:", my_list)
               
            elif ch == 5:
                val = int(input("enter value to search: "))
                if val in my_list:
                    print("found")
                else:
                    print("not found")
                   
            elif ch == 6:
                break

    # tuple
    elif choice == 2:
        while True:
            print("\n tuple")
            print("1.insert")
            print("2.display")
            print("3.search")
            print("4.back")
           
            ch = int(input("enter choice: "))
           
            if ch == 1:
                val = int(input("enter value: "))
                my_tuple = my_tuple + (val,)
               
            elif ch == 2:
                print("tuple:", my_tuple)
               
            elif ch == 3:
                val = int(input("enter value to search: "))
                if val in my_tuple:
                    print("found")
                else:
                    print("not found")
                   
            elif ch == 4:
                break

    # set
    elif choice == 3:
        while True:
            print("\n set")
            print("1.insert")
            print("2.display")
            print("3.search")
            print("4.back")
           
            ch = int(input("enter choice: "))
           
            if ch == 1:
                val = int(input("enter value: "))
                my_set.add(val)
               
            elif ch == 2:
                print("set:", my_set)
               
            elif ch == 3:
                val = int(input("enter value search: "))
                if val in my_set:
                    print("found")
                else:
                    print("not found")
                   
            elif ch == 4:
                break

    # dict
    elif choice == 4:
        while True:
            print("\n dict")
            print("1.insert")
            print("2.update")
            print("3.display")
            print("4.search")
            print("5.back")
           
            ch = int(input("enter choice: "))
           
            if ch == 1:
                key = input("enter key: ")
                val = input("enter value: ")
                my_dict[key] = val
               
            elif ch == 2:
                key = input("enter the key to update: ")
                if key in my_dict:
                    val = input("enter new value: ")
                    my_dict[key] = val
                else:
                    print("key not found")
                   
            elif ch == 3:
                print("dict:", my_dict)
               
            elif ch == 4:
                key = input("enter key to search: ")
                if key in my_dict:
                    print("found", my_dict[key])
                else:
                    print("not found")
                   
            elif ch == 5:
                break

    elif choice == 5:
        print("exit")
        break
