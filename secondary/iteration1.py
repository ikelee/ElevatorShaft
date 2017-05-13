import json
import sys
def abs(e):
    return e if e >= 0 else -e

# read as json
def read_file(filename):
    with open(filename) as data:
        return json.load(data)

# returns int, int, list of objects
def get_data():
    data = read_file("elevator_practice.json")
    return data["elevators"], data["floors"], data["events"]

a = open("output1.txt", "w")

def naive_solve(elevators, floors, events):
    answer_sequence = [1]  # sequence of floors to visit
    def place_one_person(events, position):
        if len(events) == 0:
            return events, position, 0
        else:
            # find nearest start
            acc_min = events[0]
            for e in events:
                if e["start"] - position < acc_min["start"] - position:
                    acc_min = e
            time_taken = abs(acc_min["start"] - answer_sequence[-1]) * 3 + 10
            answer_sequence.append(acc_min["start"])
            time_taken += abs(acc_min["end"] - answer_sequence[-1]) * 3 + 10
            answer_sequence.append(acc_min["end"])
            events.remove(acc_min)
            return events, position, time_taken
    event_times = [[] for _ in range(1001)]
    for e in events:
        event_times[e["time"]].append(e)
    events_so_far, current_position, next_avail_time = [], 1, 0
    dropoff_sum, sum_starts = 0, 0
    time = 0
    while True:
        a.write(str(time) + "(1, 0)" + "\n")

        if time < 1001:
            events_so_far += event_times[time]
        if time >= next_avail_time:
            events_so_far, current_position, time_taken = place_one_person(events_so_far, current_position)
            next_avail_time += time_taken
            dropoff_sum += next_avail_time
        if time > 1000 and len(events_so_far) == 0:
            break
        time += 1
    print "sequence of moves:", answer_sequence
    sum_starts = sum(map(lambda e: e["time"], events))
    total_wait = dropoff_sum - sum_starts
    print "total wait time:", total_wait
    print "total start time:", sum_starts
    print "total dropoff time:", dropoff_sum


elevators, floors, events = get_data()
naive_solve(elevators, floors, events)
