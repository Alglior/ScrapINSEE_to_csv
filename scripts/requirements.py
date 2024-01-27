import subprocess
import sys
import venv
import os

def create_virtual_environment(env_name):
    venv.create(env_name, with_pip=True)
    print(f"Virtual environment '{env_name}' created.")

def install(package, env_name):
    python_executable = os.path.join(env_name, 'bin', 'python') if os.name != 'nt' else os.path.join(env_name, 'Scripts', 'python.exe')
    subprocess.check_call([python_executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    env_name = "shovel_insee"  # You can customize this environment name
    create_virtual_environment(env_name)

    packages = ["requests", "beautifulsoup4", "pandas", "openpyxl"]
    for package in packages:
        install(package, env_name)

    print("All required packages have been installed in the virtual environment.")
