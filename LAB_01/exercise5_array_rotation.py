
# Method a
def rotate_temp_array(vect, k):

    n = len(vect)
    if n == 0 or k == 0:
        return vect
    k = k % n
    temp = vect[-k:]
    for i in range(n-1, k-1, -1):
        vect[i] = vect[i - k]
    for i in range(k):
        vect[i] = temp[i]
    return vect

# Method b
def rotate_one_by_one(vect, k):
  
    n = len(vect)
    if n == 0 or k == 0:
        return vect
    k = k % n
    for _ in range(k):
        last = vect[-1] 
        for i in range(n-1, 0, -1):
            vect[i] = vect[i-1]
        vect[0] = last
    return vect
# Aid function
def reverse_segment(vect, start, end):
    while start < end:
        vect[start], vect[end] = vect[end], vect[start]
        start += 1
        end -= 1

# Method c
def rotate_reverse(vect, k):

    n = len(vect)
    if n == 0 or k == 0:
        return vect
    k = k % n
    reverse_segment(vect, 0, n-1)
    reverse_segment(vect, 0, k-1)
    reverse_segment(vect, k, n-1)
    return vect

# test
if __name__ == "__main__":
    v1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 10
    print("Original array：", v1, "k =", k1)
    print("Results of Method a：", rotate_temp_array(v1.copy(), k1))
    print("Results of Method b：", rotate_one_by_one(v1.copy(), k1))
    print("Results of Method c：", rotate_reverse(v1.copy(), k1))

    v2 = [1]
    k2 = 5
    print("\nOriginal array：", v2, "k =", k2)
    print("Results of Method a：", rotate_temp_array(v2.copy(), k2))
    print("Results of Method b：", rotate_one_by_one(v2.copy(), k2))
    print("Results of Method c：", rotate_reverse(v2.copy(), k2)) 