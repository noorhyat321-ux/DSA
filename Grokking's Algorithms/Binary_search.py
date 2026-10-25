#- input : sorted list of elements  - output : index of item 
# halves number of steps taken to reach item by starting in the middle and eliminating accordingly 
# big- O : (log n)
def Binary_search(item , sorted_list):
  low = 0 #first index position 
  high = len(list) - 1 
  while low <= high :
    mid = (low + high) // 2 # return integer 
    guess = list[mid]
    if guess == item :
      return mid
    if guess > item :
      high = mid - 1 
    else :
      low = mid + 1 
  return None
  
      

