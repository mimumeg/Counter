class Counter:
    pass


if __name__ == "__main__":
    counter_1 = Counter(0)
    print(counter_1.value)  # 0 が出力される

    counter_1.increase()
    print(counter_1.value)  # 1 が出力される

    counter_1.increase()
    print(counter_1.value)  # 2 が出力される

    counter_2 = Counter(15)
    print(counter_2.value)  # 15 が出力される

    counter_2 = Counter()
    print(counter_2.value)  # 16 が出力される

    counter_2 = Counter()
    print(counter_2.value)  # 17 が出力される
