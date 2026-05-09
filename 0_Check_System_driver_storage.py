import shutil
import platform

def check_system():
    print(f"--- System Report for {platform.system()}---")

    # Check Disk Space
    total, used, free = shutil.disk_usage("/")

    # Convert bytes to Gigabytes 
    print(f"Total Disk: {total // (2**30)} GB")
    print(f"Used Disk: {used // (2**30)} GB")
    print(f"Free Disk: {free // (2**30)} GB")

if __name__ == "__main__":
    check_system()