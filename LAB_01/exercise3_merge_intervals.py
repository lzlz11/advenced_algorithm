def overlapping_interval(arr):
    sorted_arr = sorted(arr)
    i = 0
    while i < len(sorted_arr)-1:
        if sorted_arr[i][1] >= sorted_arr[i+1][0]:
            if sorted_arr[i][1] < sorted_arr[i+1][1]:
                sorted_arr[i][1] = sorted_arr[i+1][1]
            sorted_arr.pop(i+1)
            i -= 1
        i += 1
    return sorted_arr

print(overlapping_interval([[1,3], [2,6], [15,18], [8,10]]))
print(overlapping_interval([[1,4], [4,5]]))
print(overlapping_interval([[1,4], [0,4]]))
print(overlapping_interval([]))