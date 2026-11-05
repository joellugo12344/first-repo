import getpass
from checker import analyze, estimate
from generator import generate

GREEN="\033[92m"
RED="\033[91m"
YELLOW="\033[93m"
CYAN="\033[96m"
RESET="\033[0m"

while True:

    print(CYAN)
    print("="*45)
    print("      PASSWORD SECURITY CHECKER")
    print("="*45)
    print(RESET)

    print("1. Check Password")
    print("2. Generate Password")
    print("3. Exit")

    choice=input("\nSelect: ")

    if choice=="1":

        password=getpass.getpass("\nEnter password: ")

        score,tips=analyze(password)

        filled=score//5

        print()

        print("Strength")

        print("["+"█"*filled+"░"*(20-filled)+"]")

        print(f"{score}/100")

        print()

        if score>=90:
            print(GREEN+"Excellent"+RESET)
        elif score>=75:
            print(GREEN+"Strong"+RESET)
        elif score>=50:
            print(YELLOW+"Medium"+RESET)
        else:
            print(RED+"Weak"+RESET)

        print()

        print("Estimated Security")

        print(estimate(score))

        print()

        if tips:
            print("Suggestions")

            for t in tips:
                print("-",t)

        else:
            print("No improvements needed.")

        input("\nPress Enter...")

    elif choice=="2":

        print()

        print(GREEN+"Generated Password"+RESET)

        print(generate())

        input("\nPress Enter...")

    elif choice=="3":

        break

    else:

        print("Invalid option.")