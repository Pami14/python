import shutil

def check_specific_drive():
    
    #get input form user
    drive = input("Enter the drive letter to check (e.g., C:/ or D:/): ")
    
    try:
        # use 'try' block in case the drive doesn't exist or is emty
        total, used, free = shutil.disk_usage(drive)
        
        print(f"--- Report for {drive} ---")
        print(f"--- Free Space: {free // (2**30)} GB")
    except FileNotFoundError:
        print("Error: That drive was not found.")

if __name__ == "__main__":
    check_specific_drive()