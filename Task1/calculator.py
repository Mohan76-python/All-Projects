import sys
while(True):
    print("="*60)
    print("\t\tMenu Application")
    print("="*60)
    print("\t\t1.Addition")
    print("\t\t2.Subtraction")
    print("\t\t3.Multiplication")
    print("\t\t4.Division")
    print("\t\t5.Exit")
    print("="*60)
    user=input("Enter the choice number below:")
    if user.isdigit():
        user=int(user)
        match(user):
            case 1:
                def Add():
                    a=int(input("Enter First value:"))
                    b=int(input("Enter second value:"))
                    c=a+b
                    print("({}+{})={}".format(a,b,c))
                Add()
            case 2:
                def sub():
                    a=int(input("Enter First value:"))
                    b=int(input("Enter Second value:"))
                    c=a-b
                    print("({}-{})={}".format(a,b,c))
                sub()
            case 3:
                def mul():
                    a=int(input("Enter First value:"))
                    b=int(input("Enter Second value:"))
                    c=a*b
                    print("({}*{})={}".format(a,b,c))
                mul()
            case 4:
                def div():
                    a=int(input("Enter First value:"))
                    b=int(input("Enter Second value:"))
                    c=a/b
                    print("({}/{})={}".format(a,b,c))
                div()
            case 5:
                print("Thanks for using operation")
                sys.exit()
            case _:
                print("UR-SELECTION OF OPERATION IS WRONG ------TRY AGINE")
    else:
        print("UR-SELECTION OF OPERATION IS WRONG ------TRY AGINE")
