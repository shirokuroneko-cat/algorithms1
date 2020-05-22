def binary_search(search_num, search_lst):
    """
    ソート済配列（昇順）から指定数値を探索する二分探索。
    indexを返す。

    @param search_num 検索する数値
    @param search_lst 検索するソート済配列（昇順）
    @return ソート済配列におけるindex
    """

    ans_lst = sorted(search_lst)

    left = 0
    right = len(ans_lst) - 1
    middle = -1
    ans_index = -1

    while(search_num != ans_lst[middle] and left <= right):

        middle = (left + right) // 2

        if (ans_lst[middle] == search_num):

            ans_index = middle
            break

        elif(ans_lst[middle] > search_num):

            right = middle - 1

        elif(ans_lst[middle] < search_num):

            left = middle + 1


    return ans_index