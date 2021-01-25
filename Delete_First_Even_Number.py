delete_starting_evens = ([4, 8, 10, 11, 12, 15])
lst = [4, 8, 10, 11, 12, 15]

# def delete_starting_evens(lst):
#   for numbers in lst:
#     if numbers % 2 == 0:
#       lst = lst[1:]
#     else:
#         return lst
      
# def delete_starting_evens (lst):
#     new_lst = []
#     for num in lst:
#         if num % 2 == 0:
#             continue
#         else:
#             i = lst.index(num)
#             new_lst = lst[i:]
#             break
#     return new_lst

def delete_starting_evens(lst):
  for index in range(len(lst)):
    while lst[index] % 2 == 0:
      lst = lst[index+1:]
      if lst[index] % 2 != 0:
        break
    return lst

# def delete_starting_evens(lst):
#   while lst[0] % 2 == 0 :
#     del lst[0]  
#     if lst == 0:
#       break
#   return lst

print(delete_starting_evens(lst))
