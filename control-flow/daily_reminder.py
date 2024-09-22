task = input("Enter your task:")
Priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")


match Priority:
    case "high":
        if time_bound == "yes":
            print("Reminder:'",task,"' is a high priority task that requires immediate attention today!")
        else:
            print("note:'",task,"' is a high priority task. Consider completing it when you have free time.")

    case "medium":
        if time_bound == "yes":
            print("Reminder:'",task,"' is a medium priority task that requires immediate attention today!")
        else:
            print("note:'",task,"' is a medium priority task. Consider completing it when you have free time.")

    case "low":
        if time_bound == "yes":
            print("Reminder:'",task,"' is a low priority task that requires immediate attention today!")
        else:
            print("note:'",task,"' is a low priority task. Consider completing it when you have free time.")