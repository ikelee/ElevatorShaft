def print_stats(floor, elevator_direction, people_entering, people_travelling, people_exiting, time_people_exiting,
                waiting_at_floor, waiting_total, total_wait_time):
    i = 0
    print("We are at floor " + floor + ".")
    for elevator in elevator_direction:
        i += 1
        direction = "not moving."
        if elevator < 0:
            direction = "going down."
        elif elevator > 0:
            direction = "going up."
        print("Elevator " + str(i) + "is " + direction)
    print(people_entering + "are entering the elevator.")
    print(people_travelling + "are travelling in the elevator")
    print(people_exiting + "are exiting the elevator.")
    i = 0
    for time in time_people_exiting:
        i += 1
        print("Person " + str(i) + " is exiting. It took him/her " + time + " time.")
    i = 0
    for people in waiting_at_floor:
        i += 1
        print(people + " people are waiting at floor " + str(i) + ".")
    print(waiting_total + " are waiting in total.")
    print("The cumulative waiting time at the current time is " + total_wait_time + ".")
