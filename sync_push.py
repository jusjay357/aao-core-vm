import os
import shutil
from datetime import datetime

SOURCE_DIR = "/home/damusja357/aao"
DEST_DIR = "/home/damusja357/aao-core-vm/log_sync"

def sync_logs():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest_folder = os.path.join(DEST_DIR, f"sync_{now}")
    os.makedirs(dest_folder, exist_ok=True)
    
    for fname in ["status.json"]:
        full_path = os.path.join(SOURCE_DIR, fname)
        if os.path.exists(full_path):
            shutil.copy(full_path, dest_folder)

if __name__ == "__main__":
    sync_logs()
