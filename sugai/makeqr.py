#パッケージをインポート
import qrcode
import os #osインポート
 
#qrコードを生成
img = qrcode.make("https://www.google.co.jp/")

#パスで保存場所を指定、
path = os.path.join("..","../../../A5","qrcode-google.png")
 
#作成
img.save(path)
