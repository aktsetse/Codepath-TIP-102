def find_cruise_length(cruise_lengths, vacation_length, low, high):
    
    low , high = 0, len(cruise_lengths) - 1

    mid = (low + high) // 2
    
    if cruise_lengths is None:
        return False
    
    if cruise_lengths[mid] == vacation_length:
        return True, 
    
    
    if cruise_lengths[mid] < vacation_length:
        low = mid + 1
        return find_cruise_length(cruise_lengths, vacation_length, low, high)
    elif cruise_lengths[mid] > vacation_length:
        high = mid - 1
        return find_cruise_length(cruise_lengths, vacation_length, low, high)
        
print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
  
    

# def find_cruise_length(cruise_lengths, vacation_length):
#     if cruise_lengths is None:
#         return False

#     low, high = 0, len(cruise_lengths) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if cruise_lengths[mid] == vacation_length:
#             return True
#         elif cruise_lengths[mid] < vacation_length:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return False



# def find_cabin_index(cabins, preferred_deck):
    


# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))