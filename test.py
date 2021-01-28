# def convert(e):
#     for i in range(len(e)):
#         for j in e[i]:
#             print(j)
    
# [print(i) for i in convert([1234, 1234])]
def minimumMoves(arr1, arr2):
    # Write your code here
    counter = 0
    
    x = 0
    for i in arr1:
        e = list(str(arr2[x]))
        print(e)
        y = 0
        for j in list(str(i)):
            diff = abs(int(j) - int(e[y]))
            print(diff, j, y)
            if diff != 0:
                counter += diff
            y += 1
        x += 1
    return counter
arr1 = [1234, 4321]
arr2 = [2345, 3214]
cnt = minimumMoves(arr1, arr2)
# if __main__
print(cnt)