def sequential_search(search_num, num_list):
    """
    指定した数値を指定した数値配列から探します。
    指定数値がない場合は、-1　ある場合はindex番号を返す。

    @param search_num (int) 数値
    @param num_list (list)　数値配列
    @return index or -1
    """
    ans = -1

    ans_lst = num_list[:]
    ans_lst.append(search_num): # 番兵をセット
    for i in range(len(ans_lst)):
        if(ans_lst[i] == search_num and i != len(num_list)):
            ans = i

    return ans