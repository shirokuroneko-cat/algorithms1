def least_common_multiple(a):
    """
    複数の最小公倍数を求める関数。
    それぞれの倍数を比較し、一致した値を返す
    
    @param a (list)
    @return 最小公倍数
    """
    copy_a = a[:]
    calc_list = a[:]
    while(min(calc_list) != max(calc_list)):
        for i in range(len(copy_a)):
            if(calc_list[i] == max(calc_list)):
                continue
            calc_list[i] += copy_a[i]

    return calc_list[0]

def greatest_common_divisor(a): 
    """
    複数の最大公約数を求める関数。
    ユークリッド互除法により求める。

    @param a　(list)
    @return 最大公約数
    """
    copy_a = a[:]

    while(min(copy_a) != max(copy_a)):
        copy_a = [i if i == min(copy_a) else i - min(copy_a) for i in copy_a]
    return copy_a[0]


print(least_common_multiple([4, 8, 3]))
print(greatest_common_divisor([8, 16, 32, 4, 64]))