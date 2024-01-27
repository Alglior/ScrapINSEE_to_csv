import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    packages = ["requests", "beautifulsoup4", "pandas", "openpyxl"]
    for package in packages:
        install(package)

    print("All required packages have been installed.")
