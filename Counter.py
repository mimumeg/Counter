class Counter:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1

    def increase2(self):
        self.value += 3

    def increase3(self):
        self.value += 5

if __name__ == "__main__":
    counter_1 = Counter(0)
    print(counter_1.value)  # 0 が出力される

    counter_1.increase()
    print(counter_1.value)  # 1 が出力される  <-- 1だけ増えてる!

    counter_1.increase()
    print(counter_1.value)  # 2 が出力される  <-- さらに1だけ増えてる!


    counter_2 = Counter(15)
    print(counter_2.value)  # 15 が出力される

    counter_2.increase2()
    print(counter_2.value)

    counter_2.increase2()
    print(counter_2.value)

    counter_3 = Counter(-5)
    print(counter_3.value)  # -5 が出力される

    counter_3.increase3()
    print(counter_3.value)  # 0 が出力される

    counter_3.increase3()
    print(counter_3.value)  # 5 が出力される
