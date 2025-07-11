Gym_ID=int(input("Entert the ID_no: "))
Name=input("Enter Your name: ")
Calories_burned=float(input("Enter Calories burned today: "))
Activities=list(input("Activities done today ").split())
Workout_Time=tuple(input("Enter the workout_time(HH:MM) and end_time(HH:MM): ").split())
Equipment_used=set(input("Equipment used today: ").split())
Fitness_goal=eval(input(("Enter fitness goal: ")))
Gym_membership={
    "Duration":"3 months",
    "Amount_paid":"6000"
}
print()
print("Gym_ID, Name: ",end="")
print(Gym_ID,Name,sep=",")
print(f"Caloried_Burned ;{Calories_burned} kcal")
print("Workout Start Time: %s" % Workout_Time[0])
print("Workout End Time: %s" % Workout_Time[1])
print("Daily Goals : Steps Goal - {Steps_Goal}, Calories Goal - {Calories_Goal}".format(**Fitness_goal))
print("Duration: {Duration}, Amount_paid: {Amount_paid}".format_map(Gym_membership))


# Enter the ID_no: 007
# Enter Your name: James Bond
# Enter Calories burned today: 300.25
# Activities done today Running Yoga Cycling
# Enter the workout_time(HH:MM) and end_time(HH:MM): 06:30 07:30
# Equipment used today: TreadMills Dumbbell YogaMat
# Enter fitness goal: {"Steps_Goal": 8000,"Calories_Goal" :500.00}  

# Gym_ID, Name: 7,James Bond
# Caloried_Burned ;300.25 kcal
# Workout Start Time: 06:30
# Workout End Time: 07:30
# Daily Goals : Steps Goal - 8000, Calories Goal - 500.0
# Duration: 3 months, Amount_paid: 6000
