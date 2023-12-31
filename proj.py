import serial
import pyautogui

arduino = serial.Serial('/dev/cu.usbserial-130', 115200, timeout=.1)

pyautogui.PAUSE = 0

keysDown = {}

# Element = key to be pressed
# leave empty to not map
keyMap = [
	'A',		# A
	'B',		# B
	'space',	# C
	'D',		# D
	'E',		# E
	'F',		# F
	'enter',			# JoyStick button
]

def keyDown(key):
	if key not in keysDown:
		keysDown[key] = True
		pyautogui.keyDown(key)
		# print('Down: ', key)


def keyUp(key):
	if key in keysDown:
		del(keysDown[key])
		pyautogui.keyUp(key)
		# print('Up: ', key)


def handleJoyStickAsArrowKeys(x, y):
	if x > 30:
		keyDown('d')
		keyUp('a')
	elif x < -30:
		keyDown('a')
		keyUp('d')
	else:
		keyUp('a')
		keyUp('d')

	if y > 30:
		keyDown('w')
		keyUp('s')
	elif y < -30:
		keyDown('s')
		keyUp('w')
	else:
		keyUp('s')
		keyUp('w')


def handleButtonState(state):
	for i in range(7):
		if not keyMap[i]:
			continue

		if buttonState >> i & 1:
			keyDown(keyMap[i])
		else:
			keyUp(keyMap[i])


while True:
	data = arduino.read().decode('utf-8')

	#print(data)
	if data == 'S':
		dx = int(arduino.read_until(b',')[:-1].decode('utf-8'))

		#print("ok")
		if abs(dx) < 10:
			dx = 0
		dy = int(arduino.read_until(b',')[:-1].decode('utf-8'))

		if abs(dy) < 10:
			dy = 0
		buttonState = int(arduino.readline()[:-2])
		handleJoyStickAsArrowKeys(dx, dy * -1)
		handleButtonState(buttonState)



