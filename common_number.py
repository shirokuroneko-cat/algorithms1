def least_common_multiple(a, b):
    """
    2数の最小公倍数を求める関数。
    それぞれの倍数を比較し、一致した値を返す
    
    @return 最小公倍数
    """
    a_mul = a
    b_mul = b
    while(a_mul != b_mul):
        if(a_mul > b_mul):
            b_mul += b
        else:
            a_mul += a
    
    return a_mul

def greatest_common_divisor(a, b):
    """
     2数の最大公約数を求める関数。
     ユークリッド互除法により求める。

     @return 最大公約数
    """
    a_div = a
    b_div = b

    while(a_div != b_div):
        if(a_div > b_div):
            a_div -= b_div
        else:
            b_div -= a_div

    return a_div
