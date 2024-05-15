# forループ
# for 変数 in 要素: 処理文
list1 = [1, 2, 3, 4]
for elm in list1:  # list1をループする
    print( elm )

list2 = ["apple", "google", "ms"]
for elm in list2:
    print( elm )

# ループ処理を使用しない場合
print(list2[0])
print(list2[1])
print(list2[2])


# break ループを途中で抜ける
list3 = ["apple", "google", "ms"]
for elm in list3:
    # print( elm )
    if elm == "google":
        print( elm )
        break


# whileループ
# while 条件:  処理文
# 条件がtrueなら永遠にループされる
# 無限ループにならないように注意する  ctrl + C で終了させる
num = 0
while num < 3:
    print( "num =",  num )
    num = num + 1  # 最後に num には 3 が入っているので、下記の print には 3 が入る

print( "End", num )


num = 0
while num < 10:
    print( "num =",  num )
    num = num + 1

    if num == 5:
        break
print( "End", num )
