import pyautogui, time, os, signal, datetime, random

# Config
File_Name = "Spam_Meme.txt"      # File To Read From
Time_Before = 10                 # Time Before Spamming

class Spammy():

	def Memeify(text):
		Memeified_Text = []
		for i in text:
			r = random.randint(0,1)
			if r:
				Memeified_Text.append(i.upper())
			else:
				Memeified_Text.append(i.lower())
		return ''.join(Memeified_Text)

	def Count_Down():
		n = -1
		while n <= Time_Before -1:
			print(f"\033[97m[\033[01;96mHades\033[97m/\033[01;96mSpammer\033[97m] Starting Spam In\033[01;96m: {str(datetime.timedelta(seconds=Time_Before -1 - n))}", end="\r")
			time.sleep(1)
			n+= 1

	def Clear():
		os.system('cls' if os.name == 'nt' else 'clear')

	def Quit_Program(sig, frame):
		print('\n\033[97m[\033[01;96mHades\033[97m/\033[01;96mSpammer\033[97m] Program Terminated \033[01;96m@ \033[97mRequest Of User')
		os._exit(0)

	def Read_File():
		try:
			f = open(File_Name, "r")
			return f
		except Exception as e:
			print(str(e))

	def Main():
		Spammy.Clear()
		Spammy.Count_Down()
		Total = 0
		for _ in Spammy.Read_File():
			pyautogui.typewrite(Spammy.Memeify(_))
			pyautogui.press("enter")
			Total += 1
		print("\n\033[97m[\033[01;96mHades\033[97m/\033[01;96mSpammer\033[97m] Finished Spamming\033[01;96m, \033[97mSent \033[01;96m" + str(Total) + " \033[97mMessages\033[01;96m!") 

signal.signal(signal.SIGINT, Spammy.Quit_Program)
Spammy.Main()
