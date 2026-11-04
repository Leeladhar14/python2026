

def frequnecy_num(num=list):
    set_num = set(num)
    print(set_num)
    dict = {}
    for i in set_num:
        count = 0
        for j in num:
            if i == j:
                count +=1
        dict[i] = count
    return dict

final_dict = frequnecy_num([1,2,2,2,3,3,3,4,4])
print(final_dict)

