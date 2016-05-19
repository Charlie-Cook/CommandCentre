import subprocess

hook = 'Vagrant'


def run_command(command):
    if command == "up":
        p = subprocess.Popen(['powershell.exe',
                              'C:\\Users\\MyUser\\Documents\\PowershellScripts\\VagrantCommands -command up'])
        p.communicate()
    elif command == "halt":
        p = subprocess.Popen(['powershell.exe',
                              'C:\\Users\\MyUser\\Documents\\PowershellScripts\\VagrantCommands -command halt'])
        p.communicate()

# Create powershell script to start or stop vagrant then update the above path
