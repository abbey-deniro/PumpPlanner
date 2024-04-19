workouts = {
    'upper body': [
        'Push-ups',
        'Pull-ups',
        'Shoulder Press',
        'Bench Press',
        'Bicep Curls',
        'Overhead Press',
        'Tricep Dips',
        'Lat Pull-Downs',
        'Chest Flys',
        'Shoulder Shrugs',
        'Bent-Over Rows'
    ],
    'lower body': [
        'Squats',
        'Deadlifts',
        'Lunges',
        'Hip Thrusts',
        'Calf Raises',
        'Bulgarian Split Squats',
        'Step-Ups',
        'Box Jumps'
    ],
    'full body': [
        'Burpees',
        'Mountain Climbers',
        'Kettlebell Swings',
        'Jumping Jacks',
        'Bear Crawls',
        'Clean and Press',
        'Deadlifts'
    ],
    'abs': [
        'Plank Saws',
        'Crunches',
        'Russian Twists',
        'Leg Raises',
        'Bicycle Crunches',
        'Hanging Leg Raises',
        'Mountain Climbers',
        'Reverse Crunches',
        'Dead Bugs',
        'Toe Taps',
        'Heel Taps',
        'Eagle Crunches',
        'Knee to Elbow (Both Sides)'
    ],
}

import random

def generate_workout(workout_type, num_exercises):
    if(workout_type == '1'):
        chosen_workout = workouts.get('upper body', [])
        return random.sample(chosen_workout, min(int(num_exercises), len(chosen_workout)))
    elif(workout_type == '2'):
        chosen_workout = workouts.get('lower body', [])
        return random.sample(chosen_workout, min(int(num_exercises), len(chosen_workout)))
    elif(workout_type == '3'):
        chosen_workout = workouts.get('full body', [])
        return random.sample(chosen_workout, min(int(num_exercises), len(chosen_workout)))
    elif(workout_type == '4'):
        chosen_workout = workouts.get('abs', [])
        return random.sample(chosen_workout, min(int(num_exercises), len(chosen_workout)))
    else:
        print("Workout type not recognized. Please try again")

if __name__ == "__main__":
    generate_workout(workout_type, num_exercises);