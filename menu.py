from workouts import generate_workout
import random


def print_ascii():
    print("""
██████╗ ██╗   ██╗███╗   ███╗██████╗     ██████╗ ██╗      █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██║   ██║████╗ ████║██╔══██╗    ██╔══██╗██║     ██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝    ██████╔╝██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██║╚██╔╝██║██╔═══╝     ██╔═══╝ ██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║ ╚═╝ ██║██║         ██║     ███████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝     ╚═╝╚═╝         ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
""")
    

def welcome():
    print("Welcome to Pump Planner, Your personal workout generator!")
    print("Getting fit has never been easier! With Pump Planner, you can generate customized workout routines at the touch of a button.")
    print("Here's how to get started:\n")
    print("\033[1m1: Choose Workout Type:\033[0m Select from upper body, lower body, full body, abs or random!")
    print("\033[1m2: Specify Exercise Count:\033[0m Decide how many exercises you'd like in your routine!")
    print("\033[1m3: Generate Routine:\033[0m Watch as your personalized workout is created instantly!")
    print("\033[1m4: Get Moving:\033[0m Perform the exercises at you own pace and enjoy your workout!\n")

    print("Choose a type below:")
    print("1: Upper Body")
    print("2: Lower Body")
    print("3: Full Body")
    print("4: Abs")
    workout_type = input(str())
    num_of_exercises = input("Enter number of exercises you'd like: ")
    workout = generate_workout(workout_type, num_of_exercises)
    print("\nYour Workout consists of: ")
    for exercise in workout:
        print(f"- {exercise} - {random.randint(2,5)}x{random.randint(8, 20)}")



print_ascii()
welcome()