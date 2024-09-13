def activity_selection(start_times, finish_times):
    # Create array of start and finish times
    activities = list(zip(start_times, finish_times))
    # Sort activities by finish times
    activities.sort(key=lambda x: x[1])
    selected_activities = []
    last_finish_time = -1
    
    for start, finish in activities:
        if start >= last_finish_time:
            selected_activities.append((start, finish))
            last_finish_time = finish
    
    return selected_activities

def activity_selection_recursive(start_times, finish_times, last_finish_time, index = 0):
    if index == len(start_times):
        return []
    
    if start_times[index] >= last_finish_time:
        return (
            [(start_times[index], finish_times[index])] + 
            activity_selection_recursive(
                start_times, 
                finish_times, 
                finish_times[index], 
                index + 1)
            )
    else:
        return activity_selection_recursive(
            start_times, 
            finish_times, 
            last_finish_time, 
            index + 1
        )

start_times = [1, 3, 0, 5, 3, 5, 6, 7, 8, 2, 12]
finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

selected_activities = activity_selection(start_times, finish_times)
selected_activities_recursive = activity_selection_recursive(start_times, finish_times, 0)
assert selected_activities == selected_activities_recursive
print("Selected activities:", selected_activities)
