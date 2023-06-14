my_list = [1, 6, 3, 5, 1, 5, 3, 10]
# print(my_list)
# my_list = list(set(my_list))
# print(my_list)

my_dict = {}

for i in range(len(my_list)):
    my_dict[my_list[i]] = my_dict.get(my_list[i], 0) + 1
new_list = [x[0] for x in my_dict.items() if x[1] == 1]
# new_list = []
# for key, value in my_dict.items():
#     if value == 1:
#         new_list.append(key)
print(new_list)

# new_list = list(filter(lambda x: my_list.count(x) == 1, my_list))
# print([x for x in my_list if my_list.count(x) == 1])
