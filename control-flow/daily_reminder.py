while True:
    task = input("Enter your task:")
    priority = input("Priority (high/medium/low):").lower()
    time_bound = input("Is it time-bound? (yes/no):").lower()
    Reminder=""

    match priority :
        case "high":
            Reminder = "reminder:" + task + " is a high priority task "
        case "medium":
            Reminder = "reminder: "+task+" is a medium priority task "
        case "low":
            Reminder = "reminder: " + task + " is a low priority task "
        case _: message = f"priority not defined "
        
    if time_bound =="yes":
        Reminder += "that requires immediate attention today!"
    elif time_bound =="no":
        Reminder += ". Consider completing it when you have free time."
        
    print("\n" + Reminder)
