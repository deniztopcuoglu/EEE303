print("Hello, we are going to ask you some questions about yourself.")
print("Please answer them correctly.")
ua = input("Do you agree?: ").strip().lower()

if ua in ("yes", "y"):
    name = input("What is your name?: ")
    sex = input("What is your sex?: ").strip().lower()
    age = input("How old are you?: ")
    height = input("How tall are you? Use centimeters: ")
    weight = input("How much do you weigh?: ")
    hobbies = input("Tell me about your hobbies: ")
    if sex in ("male", "m"):
        sex = "male"
    elif sex in ("female", "f"):
        sex = "female"
    print("\nHello {}, you are a {} and you are {} years old.".format(name, sex, age))
    print("You weigh {} and you are {} cm tall.".format(weight, height))
    print("Your hobbies are: " + hobbies)
else:
    print("Okay.")
