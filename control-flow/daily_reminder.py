task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no)")

match priority:
    case high:
        if time_bound == "yes":
            print("You have to do this as before the schedule")
        else:
            print("You need to do this as soon as possible")
