from collections import defaultdict

######################## case: 1

# counter = defaultdict(int)
# my_dict = {1,2,1,2,1,3,4,5}
# for element in my_dict:
#     counter[element] += 1
# print(counter)     # output: defaultdict(<class 'int'>, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1})

############### case: 2

# words = ["apple", "banana", "carrot", "avocado", "brocoli", "orange"]
# grouped_words = defaultdict(list)
# for word in words:
#     grouped_words[word[0]].append(word)
# print(grouped_words) #output: {'a': ['apple', 'avocado'], 'b': ['banana', 'brocoli'], 'c': ['carrot'], 'o': ['orange']})

################ case: 3

tuple_list = [("A", 10), ("B", 4), ("A", 5), ("C", 7), ("B", 1)]
grouped_data = defaultdict(list)
for key, value in tuple_list:
    grouped_data[key].append(value)
print(grouped_data)   #output: {'A': [10, 5], 'B': [4, 1], 'C': [7]})