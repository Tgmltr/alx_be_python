while True :
    task = str(input("Enter your task:"))
    priority = str(input("Priority (high/medium/low):"))
    time_bound = str(input("Is it time-bound? (yes/no):"))
    message = ""
    match priority :
        case "high":
            message = f"reminder:'{task}'is a high priority "
        case "medium":
            message = f"reminder:'{task}'is a medium priority "
        case "low":
            message = f"reminder:'{task}'is a low priority "
        case _: message = f"priority not defined "
    if time_bound =="yes":
        message += "that requires immediate attention today!"
    elif time_bound =="no":
        message += "Consider completing it when you have free time."
    print(message)
