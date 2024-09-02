# Topics:
# 2. Hashmap
#3. Tree/Graph
# 4. Heap/Queue
# 5. String

# 1. Array/List
int_List = [10, 20, 30, 40, 50, 60]

#Q Print last index value
print(int_List[-1]) #this is called slicing

#Q Print index 2 to last index value
print(int_List[2 : -1])

#Q Print first five index value
print(int_List[:5]) # No need to put 1st index no

#Q Print 3rd to last index value
print(int_List[3:]) # No need to put last index no

#Q Print Maximum value of the list
Max_Value = max(int_List)
print(Max_Value)

#Q Print Maximum value using manual process
Max_value = int_List[0] # Let the 1st index value is the max value
for i in int_List:
    if i > Max_value:
        Max_value = i
print(Max_value)

#Q Print Minimum value of the list
Min_Value = min(int_List)
print(Min_Value)

#Q #Q Print Minimum value using manual process
Min_value = int_List[0]
for i in int_List:
    if i < Min_value:
        Min_value = i
print(Min_value)        

#Q Print sum value of the list
print(sum(int_List)) # This is built-in method