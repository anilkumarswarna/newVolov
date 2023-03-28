import subprocess

class adbLibrary():
    def screenSwipeADB(self):
        subprocess.call("adb shell input swipe 400 1200 100 200")

    def userNameInput(self):
        subprocess.run("adb shell input text anilswarna19952023")

    def passwordInput(self):
        subprocess.run("adb shell input text anil@155")
###########################################
#insta Language change

    def swipeScreen(self):
        subprocess.call("adb shell input swipe 400 1200 100 200")

    def langInputADB(self):
        subprocess.run("adb shell input text Telugu")

    def languageEnglishADB(self):
        subprocess.run("adb shell input text English")

    def SeacrchFriendInput(self):
        subprocess.run("adb shell input text 'Ella Vinay kumar'")

