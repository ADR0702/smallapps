trainspeeda=70
trainspeedb=30
starting_hour=9
starting_minute=45
total_speed=trainspeeda+trainspeedb
distance_a=45/60 * 70

time_to_meet=distance_a/total_speed
minutes_to_meet=time_to_meet*60
print(minutes_to_meet)
crash_hour= starting_hour+(starting_minute +minutes_to_meet) // 60
crash_hour=int(crash_hour)
crash_minutes=(starting_minute+minutes_to_meet) % 60
crash_minutes=int(crash_minutes)
print(f"The trains will crash each other at {crash_hour}:{crash_minutes}")