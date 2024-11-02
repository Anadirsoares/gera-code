import subprocess

def atualizar_linux():
    subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')
    
def instalar_pip():
    subprocess.run(f'''sudo apt install python3-pip''', shell=True, check=True, executable='/bin/bash')
    
def criar_venv():
    subprocess.run('''sudo apt install pytho3-venv''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''python3 -m venv''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''source .venv/bin/activate''', shell=True, check=True, executable='/bin/bash')

def abrir_projeto_vscode(path_full_novo_projeto):
    subprocess.run(f'''code {path_full_novo_projeto}''', shell=True, check=True, executable='/bin/bash')     
    
def instalar_node():
    subprocess.run(f'''curl -sL https://deb.nodesource.com/setup_20.x -o /tmp/nodesource_setup.sh''',shell=True, check=True, executable=' /bin/bash')
    subprocess.run('''sudo bash /tmp/nodesurce_setup.sh''', shell=True, check=True, executable=' /bin/bash')
    subprocess.run(f'''sudo apt install nodejs -y''', shell=True, checl=True, executable='bin/bash')