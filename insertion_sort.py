def insertion_sort(sort_lst, reverse=False):
    """
    挿入法を使って数値配列をソートする。
    reverse = False ->　昇順
    reverse = True  ->　降順

    @param sort_lst (list) ソートする配列
    @param reverse(=False) (bool) ソード順を決める
    @return ソート後の配列
    """

    ans_lst = sort_lst[:]

    for i in range(1, len(ans_lst)):
        tmp = ans_lst[i]
        for j in range(i-1, -1, -1):
            if(ans_lst[j] >= tmp):
                ans_lst[j+1] = ans_lst[j]
            else:
                ans_lst[j+1] = tmp
                break
        ans_lst[j+1] = tmp
    
    return ans_lst