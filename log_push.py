import os
import shutil
import datetime
import subprocess

REPO_PATH = "/home/damusja357/aao-core-vm"
LOG_PATH = "/home/damusja357/aao/status.json"

def push_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    temp_log = f"{REPO_PATH}/logs/status_{timestamp}.json"
    os.makedirs(f"{REPO_PATH}/logs", exist_ok=True)
    shutil.copy(LOG_PATH, temp_log)

    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"log push {timestamp}"], check=True)
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    push_log()
