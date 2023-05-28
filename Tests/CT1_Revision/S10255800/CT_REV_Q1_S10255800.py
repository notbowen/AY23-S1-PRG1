# Hu Bowen (S10255800) - CSF02

times = input('Enter time taken of 2 laps separated by semi-colon (seconds): ')  # Closed input bracket

times_list = times.split(';')

firstlap_time = float(times_list[0])    # Changed data type to float
secondlap_time = float(times_list[1])   # Changed data type to float

if firstlap_time < secondlap_time:      # Changed > to <
    best = firstlap_time                # Fixed indentation
else:
    best = secondlap_time               # Fixed indentation

total = firstlap_time + secondlap_time

print('Tom\'s best time is {:.1f} s and average time is {} s'.format(best, total / 2))  # Moved total into format and calculated average
