def bubble_sort(sort_lst, reverse=False):
    """
    バブルソートを使ったソート。
    reverse = True -> 降順
    reverse = False -> 昇順

    @param sort_lst (list) ソートするリスト
    @param reverse (bool) ソート順
    @return ソート後リスト
    """

    ans_lst = sort_lst[:]

    for i in range(len(ans_lst)-1):
        for j in range(len(ans_lst) - 1, i, -1):
            if (ans_lst[j] <= ans_lst[j-1]):
                tmp = ans_lst[j]
                ans_lst[j] = ans_lst[j-1]
                ans_lst[j-1] = tmp
    
    return ans_lst
