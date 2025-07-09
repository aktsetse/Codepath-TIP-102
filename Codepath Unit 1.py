# def sort_by_parity(nums):
#     lst = []
#     for i in nums:
#         if i % 2 == 0:
#             lst.append(i)
#         elif i % 2 != 0:
#             lst.append(i)
#     print(lst)

# nums = [3, 1, 2, 4]
# sort_by_parity(nums)

# def showpairs():
#     pairs = []
#     for i in range (5):
#         x = int(input("Enter your x - coordinate: "))
#         y = int(input("Enter your y - coordinate: "))
#         pair = (x, y)
#         pairs.append(pair)
#     print(pairs)
    
#     for i in range(4):
#         slope = calslope(pairs[i], pairs[i + 1])
#         print(f"Slope between {pairs[i]} and {pairs[i + 1]}: {slope}")


# def calslope(point1, point2):
#     x1, y1 = point1
#     x2, y2 = point2
    
#     if x2 - x1 == 0:
#         return "Slope doesn't exist"
#     else:
#         return (y2 - y1) / (x2 - x1)
        


# showpairs()

# print(dir(my_dictionary))
# print(help(my_dictionary))

def frequency(words):
    res = {}
    # go through words

    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res

print(frequency([]))


