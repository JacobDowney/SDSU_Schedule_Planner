import GetListOfSchedules

def test_get_schedules():
    abc = ['a', 'b', 'c']
    xyz = ['x', 'y', 'z']
    expected = [
        ['a', 'x'], ['a', 'y'], ['a', 'z'],
        ['b', 'x'], ['b', 'y'], ['b', 'z'],
        ['c', 'x'], ['c', 'y'], ['c', 'z']]
    schedules = GetListOfSchedules.get_schedules([], [], [abc, xyz])
    print(schedules)
    assert (schedules == expected), "Not expected output"

if __name__ == '__main__':
    test_get_schedules()
    print("all tests passed")
else:
    print("Not Supported")
