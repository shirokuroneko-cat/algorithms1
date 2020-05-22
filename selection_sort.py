def selection_sort(sort_lst, reverse=False):
    """
    選択法を使って数値配列をソートする。
    reverse = True -> 降順
    reverse = False -> 昇順

    @param sort_lst (list) ソートする配列
    @param reverse (bool) ソート順
    @return 
    """

    ans_lst = sort_lst[:]

    for i in range(len(ans_lst) - 1):
        minimum_idx = -1
        minimum = float('inf')

        for j in range(i, len(ans_lst)):
            if (minimum >= ans_lst[j]):
                minimum_idx = j
                minimum = ans_lst[j]
        ans_lst[minimum_idx] = ans_lst[i]
        ans_lst[i] = minimum


    return ans_lst