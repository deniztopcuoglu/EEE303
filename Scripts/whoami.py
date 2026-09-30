print("Hello, we are going to ask you some questions about yourself.")
print("Please answer them correctly.")
ua = input("Do you agree?: ").strip().lower()

if ua in ("yes", "y"):
    name = input("What is your name?: ")
    while True:
        sex = input("What is your sex?: ").strip().lower()
        if sex in ("male", "m"):
            sex = "male"
            break
        elif sex in ("female", "f"):
            sex = "female"
            break
        else:
            print("Please enter only male/m or female/f.")
    while True:
        while True:
            age = input("How old are you? Please enter an integer: ")
            try:
                age = int(age)
                break
            except ValueError:
                print("I said an integer!: ")
        if age <= 0:
            print("ugucubugubugucubugugu")
        elif age >= 127:
            print("Liar.")
        else:
            break
    while True:
        while True:
            height = input("How tall are you? Please enter an integer: ")
            try:
                height = int(height)
                break
            except ValueError:
                print("I said an integer!: ")
        if height <= 100:
            print("what?")
        elif height >= 251:
            print("Go to Guinness immediately.")
        else:
            break
    while True:
        while True:
            weight = input("How much do you weigh? Please enter an integer: ")
            try:
                weight = int(weight)
                break
            except ValueError:
                print("I said an integer!: ")
        if weight <= 35:
            print("Oh no.")
        elif weight >= 180:
            print("Go to a doctor.")
        else:
            break
    hobbies = input("Tell me about your hobbies: ")

    print("\nHello {}, you are a {} and you are {} years old.".format(name, sex, age))
    print("You weigh {} kg and you are {} cm tall.".format(weight, height))
    print("Your hobbies are: " + hobbies)
else:
    print("Okay.")
