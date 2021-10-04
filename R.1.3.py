def minmax(data):
    mini = data[0]
    maxi  = data[0]
    
    for item in data:
        if mini > item:
            mini = item
        elif maxi < item:
            maxi = item
    return mini, maxi


if __name__ == '__main__':
    print(minmax([123, 45,1, 4, 6, 0 , 34, 2344, 2, 3, -1, 45, -3]))
    print(minmax([0, 0, 0, 0, 0, 0, 0]))
    print(minmax([98787, 87987, 8878, 87879, 7898, 82787]))
    print(minmax([23, 2, 9, 0, 1, 2, 3 , 0 , 0, 0, 3434,3434, 3434]))


