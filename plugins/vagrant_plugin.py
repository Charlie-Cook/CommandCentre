import subprocess


def run_command(passed_cmd):
    if passed_cmd == "Vagrant up":
        p = subprocess.Popen(['powershell.exe',
                              'C:\\Users\\Digital4357\\Documents\\PowershellScripts\\VagrantCommands -command up'])
        p.communicate()
    elif passed_cmd == "Vagrant halt":
        p = subprocess.Popen(['powershell.exe',
                              'C:\\Users\\Digital4357\\Documents\\PowershellScripts\\VagrantCommands -command halt'])
        p.communicate()
