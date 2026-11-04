def largest_num(num):
    for n in num:
        largestnum = n
        for i in num:
            if i > n:
                largestnum = i
        break
    print(largestnum)


largest_num([70,10,20,5,30,20,30,6,-35])