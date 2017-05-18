import subprocess
class cmd:
    def __init__(self):
        self.command = 'cmd'
        self.description = 'shell command execution\n'
        self.args = True
    def main(self,data):
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        return stdout_value
