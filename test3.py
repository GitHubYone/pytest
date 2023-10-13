def get_price(a, b):
    # 仮引数、値が代入された変数 → ローカル変数
    # 値が代入されていない変数 → 外のスコープを探す
    total = (a + b) * rate
    return total

rate = 1.1
print(get_price(300, 700))
