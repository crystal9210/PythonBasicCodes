# Pythonのinput関数は、ユーザからの入力を文字列として受け取るため、関数呼び出しの際に、空白を考慮して特別な処理を付す必要はない！
# →文字列をinput関数で受け取った後、それを媒介変数に代入し、それを他の変数に、list(map(int, input_str.split()))として渡すことで、リスト化可能。
def get_numbers_from_user():
    # 入力を受け取る
    input_str = input("整数をスペース区切りで入力してください: ")

    # スペースで分割し、整数のリストに変換
    numbers = list(map(int, input_str.split()))
    return numbers

print("プログラム開始")

# ユーザーからの入力を受け取る
numbers = get_numbers_from_user()

print("受け取った整数のリスト:", numbers)

print("プログラム終了")
