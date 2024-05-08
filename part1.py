# 文字列の長さを取得
print ( len("hello") )
print ( len("あ") )
print ( len("日本") )
print ( len("") )


# 文字列操作
print ( "hello", "python" )   # hello python
print ( "hello" + "python" )  # hellopython
print ( "hello" + "python", "です" )


# 大文字・小文字変換
# Webサイトでユーザーが入力するIDなどを管理するときなどに使用する
print ( "hello".upper() )
print ( "HELLO".lower() )


# 文字列を指定の基準で区切る
# メールアドレスの @ の左側を取得したいときなどに使用する
# CSV file で値を整理するとき
print( "hello".split("e") )
print( "hello world".split(" ") )
print( "hello,python,foo,bar".split(",") )
print( "hello+python+foo+bar".split("+") )


# エスケープ文字
# 改行
print("hello \nworld")

# # タブ
print( "hello \tpython" )

# # "" (ダブルクォーテーション) も出力したい
print("\"hello\"")

# # '' (シングルクォーテーション)
print("\'hello\'")


# 変数
# 変数には、文字、数字、オブジェクトなどが代入可能
# 変数の値は、いつでも変更可能
tmp = 100
print ( tmp )

tmp = 5
tmp2 = 3
print ( tmp * tmp2 )

tmp2 = tmp2 + tmp
print ( tmp2 )


# if文(条件分岐)
a = 2

if a > 1:
    print( "条件はTure" ) 
else:
    print( "条件はFlase" )

if a < 1:
    print( "条件はTure" ) 
else:
    print( "条件はFlase" )

# elif (else if)
a = 10
b = 3

if a > b:
    print( "aはbより大きい" )
elif a == b:
    print( "aとbは同じ" )
else:
    print( "上の二つの条件に当てはまらない" )


# リスト(配列)
list1 = [1, 2, 3, 4, 5]
print ( list1 )

list2 = ["hello", "world", "foo", "bar"]
print ( list2 )
print ( list2[0] )
print ( list2[4] )  # err!  range = 範囲


# append リスト追加
list4 = ["hello", "world"]
print( list4 )

list4.append("apple")
print( list4 )

list4.append("banana")
print( list4 )

list4.append("orange")
print( list4 )


# insert 要素を指定して追加
list5 = ["hello", "world", "foo", "bar" ]
print( list5 )

list5.insert(1, "apple")
print( list5 )

list5.insert(3, "banana")
print( list5 )


# pop 指定した要素を取り出して削除
list6 = ["hello", "world", "foo", "bar"]
print( list6.pop() )  # indexを指定しないと、最後の要素がpopされる
print( list6 )

print( list6.pop(1) )
print( list6 )


# remove 指定した要素と同じものがあれば削除
list8 = ["hello", "world", "foo", "bar"]
list8.remove("foo")
print( list8 ) 

list8.remove("apple")  # err!
