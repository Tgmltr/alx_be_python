while True :
    task = input("Enter your task:")
    priority = input("Priority (high/medium/low):").lower()
    time_bound = input("Is it time-bound? (yes/no):").lower()
    reminder=""
    match priority :
        case "high":
            reminder = "reminder:"+task+" is a high priority "
        case "medium":
            reminder = "reminder:"+task+" is a medium priority "
        case "low":
            reminder = "reminder:"+task+" is a low priority "
        case _: message = f"priority not defined "
    if time_bound =="yes":
        reminder += "that requires immediate attention today!"
    elif time_bound =="no":
        reminder += "Consider completing it when you have free time."
    print(reminder)
