initial_cost = {
        'Bergara B-14 HMR .308': 950,
        'Vortex Viper PST Gen II': 1000,
        'Nightforce REM 700 Short Action 20 MOA Base': 120,
        'Vortex 30mm rings - 0.97in height': 150,
        'Bulldog rifle case': 95,
}

up_front_cost = 0
for i in initial_cost.values():
    up_front_cost += i

print(f"Up front/'0 ammunition' cost = { up_front_cost }")

total_rounds_purchased = float( input("How much ammo are you going to buy? ") )
cost_of_total_rounds_purchased = float( input("How much will this ammo cost? ") )
shots_in_group = 5
groups_shot_per_range_trip = 10

groups_to_shoot = total_rounds_purchased // shots_in_group
trips_to_range = groups_to_shoot // groups_shot_per_range_trip

message = f'''
If you buy {total_rounds_purchased} total rounds, and,
If you shoot {shots_in_group} shots per group, and,
If you shoot {groups_shot_per_range_trip} groups per trip to the range,

You will have {groups_to_shoot} total groups to shoot, and,
You will have {trips_to_range} trips to the range before you need to buy more ammo.

The total "bullets downrange" cost is {up_front_cost + cost_of_total_rounds_purchased}.
'''

print(message)
