task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that requires attention soon!")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task that requires attention soon!")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}'is a low priority task. Consider completing it when you have free time. ")
        else:
            print(f"Note: '{task}'is a low priority task. Consider completing it when anytime today.")
    case _:
        print(f"Enter the right priority")
