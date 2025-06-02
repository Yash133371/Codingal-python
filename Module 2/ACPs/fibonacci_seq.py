num_list = [0, 1]
for i in range(10):
    print(num_list[1])
    num_list.append(sum(num_list))
    num_list.pop(0)