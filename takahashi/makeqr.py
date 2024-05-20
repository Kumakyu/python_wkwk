#QRコード生成プログラム

# pipパッケージ
import qrcode
import os

# 引数のためのモジュール
import sys
args = sys.argv

#引数の入力
input_url = str(args[1])
input_filename = str(args[2])

#QRコードの作成
img = qrcode.make(input_url)

# 保存
path = os.path.join("..","../.././A5","input_filename.png")

img.save(path)