# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Python code​​​​​​‌‌​‌‌‌​​​​‌‌‌‌‌‌‌​‌​​‌‌​‌ below
# Use print("messages...") to debug your solution.
list = [] 
def allPrimesUpTo(num):
    # Your code goes here.
    #already calculated
    if(len(list) > 0 and list[len(list) - 1] > num):
        # return the numbers less than num
        new_list = [item for item in list if item < num]
        return new_list;
    # calculate and add new items in list
    else:
        for current_item in range(2,num):
            # if list contains all the prime numbers till the square root of number
            if len(list) > 0 and (int(current_item ** 0.5) + 1) < list[len(list)- 1]:
                for x in (item for item in list if item < (int(current_item ** 0.5) + 1)):
                    if(current_item % x == 0):
                        break;
                else:
                    if current_item not in list:
                        list.append(current_item)
            else:
                for item in list:
                    if(current_item % item == 0):
                        break;
                for factor in range(2, int(current_item ** 0.5) + 1):
                    if(current_item % factor == 0):
                        break;
                else:
                    if current_item not in list:
                        list.append(current_item)
        return [item for item in list if item < num]





