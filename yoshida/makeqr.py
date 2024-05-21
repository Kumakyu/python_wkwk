#パッケージをインポート
import qrcode
import os #osインポート

#qrコードを生成
img = qrcode.make("https://sugushinu-anime.jp/")

#パスで保存場所を指定
#ローカル→SSH先、リモート→リモートリポジトリ
#..→二階層戻る、matcha_trainingに入れる
path = os.path.join("..","../../A5,"qrcode-94.png")

#作成
img.save(path)



