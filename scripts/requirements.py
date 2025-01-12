import subprocess
import sys
import venv
import os

def create_virtual_environment(env_name):
    # Obtenir le chemin du dossier parent
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(parent_dir, env_name)
    
    # Créer l'environnement virtuel dans le dossier parent
    venv.create(env_path, with_pip=True)
    print(f"Virtual environment '{env_name}' created in {parent_dir}")
    return env_path

def install(package, env_path):
    python_executable = os.path.join(env_path, 'bin', 'python') if os.name != 'nt' else os.path.join(env_path, 'Scripts', 'python.exe')
    subprocess.check_call([python_executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    env_name = "shovel_insee"
    env_path = create_virtual_environment(env_name)

    packages = ["requests", "beautifulsoup4", "pandas", "openpyxl", "lxml", "xlrd", "tk", "tkinter", "_tkinter","tqdm"]
    for package in packages:
        print(f"Installing {package}...")
        install(package, env_path)

    print("All required packages have been installed in the virtual environment.")
