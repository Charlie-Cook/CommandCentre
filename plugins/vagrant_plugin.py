import subprocess

hook = 'Vagrant'


def run_command(command):
    if command == "up":
        p = subprocess.Popen(['powershell.exe',
                              'C:\\Users\\Digital4357\\Documents\\PowershellScripts\\VagrantCommands -command up'])
        p.communicate()
    elif command == "halt":
        p = subprocess.Popen(['powershell.exe',
                              'C:\\Users\\Digital4357\\Documents\\PowershellScripts\\VagrantCommands -command halt'])
        p.communicate()
