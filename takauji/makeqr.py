import qrcode
import os
img = qrcode.make("https://www.triples-official.jp/")


path = os.path.join("..","../../../../A5_takauji","qrcode-test.png")
img.save (path)