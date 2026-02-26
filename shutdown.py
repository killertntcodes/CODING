import os
import time
def shutdown():
    print("Shutting down in 5 seconds...")
    time.sleep(5)
    os.system("shutdown /s /t 1")
shutdown()