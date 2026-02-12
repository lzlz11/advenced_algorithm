def polynomial_evaluation(arr, x):
    result = 0
    for i in range(1,len(arr)+1):
        result = result*x + arr[-i]
    return result

print(polynomial_evaluation([3.8, -2, 0, 5], 2.48))
print(polynomial_evaluation([3.8, -2, 0, 5,8,5,74,5,7,1,-84558468,854,794,6,76,46,7497,649,949,49,494,94,8614,84848,48448494984,6484684,8948494,94], 2.48))
