# Bailey Thompson, Charles Lei, Gordon Winchester, Ike Lee
# Elevator Shaft (0.1.0)
# 12 May 2017
# Simulates an elevator shaft.

from src.fileio import get_data


def main():
    data = get_data()
    check_data(data)
    print(data)


def check_data(data):
    elevators = data[0]
    assert is_integer(elevators)
    assert elevators >= 1
    floors = data[1]
    assert is_integer(floors)
    assert floors >= 1
    people = data[2]
    for person in people:
        time = person["time"]
        assert is_integer(time)
        assert time >= 0
        start_floor = person["start"]
        assert is_integer(start_floor)
        assert 0 <= start_floor < floors
        end_floor = person["end"]
        assert is_integer(end_floor)
        assert 0 <= end_floor < floors


def is_integer(input_num):
    while input_num > 0:
        input_num -= 1
    return input_num == 0

if __name__ == "__main__":
    main()
