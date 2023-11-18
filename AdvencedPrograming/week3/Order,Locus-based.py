def func(order_based):
    locus_based = [0] * len(order_based)  # locus_list 생성

    for i in range(len(order_based)):  # i: 0, 1, 2, 3 ... 9
        if (order_based.index(i)+1 < len(order_based)):
            locus_based[i] = order_based[order_based.index(i)+1]
        else:
            locus_based[i] = order_based[0]

    print("Order-based:", order_based)
    print("Locus-based:", locus_based)
    return locus_based


order_based = [3, 6, 1, 7, 2, 5, 8, 4, 0, 9]
locus_based = func(order_based)
