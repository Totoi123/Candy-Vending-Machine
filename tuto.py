# program to mimic a candy vending machine
# suppose that there are five candies in the vending machine but the customer wants six
# display that the vending machine is short of 1 candy
# And if the customer wants the available candy, give it to the customer else ask for another number of candy.

av = 5
x = int(input("Enter the number of candies you want: "))
for i in range(x):
    if x > av:
        remain = x - av
        print("Total number of candies available is ", av)
        print("We are short of ", remain, 'candies')
        if remain != 0:
            total = x - remain
            print("Do you want", total, 'candies instead?')
            ans = input("Enter yes/no: ")
            if ans == 'yes':
                for j in range(total):
                    print("Candy")
            elif ans == 'no':
                print("Do you want to continue or quit?")
                choose = input("Enter 'C' to Continue or 'Q' to Quit: ")
                if choose == 'C':
                    ans1 = int(input("Enter the number of Candies you want: "))
                    for k in range(ans1):
                        print("Candy")
                else:
                    break
        break
    else:
        print("candy")

print("Thank you for shopping with us. :)")
