import os
import subprocess
import datetime
import shutil

timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
log_path = f"log_sync/sync_{timestamp}/status.json"

# Create folder if needed
os.makedirs(os.path.dirname(log_path), exist_ok=True)
shutil.copyfile("/home/damusja357/aao/status.json", log_path)

# GitHub push
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", f"log push {timestamp}"], check=True)
subprocess.run(["git", "push"], check=True)
