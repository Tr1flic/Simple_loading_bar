import threading
import time
import math
process = None
updatex = 0
updatey = 0

def display_progress():
    global updatex, updatey
    cachex = updatex
    cachey = updatey
    while True:
        while updatex == cachex and cachey == updatey:
            time.sleep(0.2)
        if updatex >= updatey:
            updatex = updatey-1
        hashtags = math.floor((updatey-updatex)/(updatey/100))-1
        print(f"[{'#' * (100-hashtags)}{' ' * hashtags}]{' ' * (3-len(str(100-hashtags)))}{100-hashtags}/100% {('Done! Waiting for main process...' if updatex == updatey-1 else '')}", end="\r")
        if updatex == updatey-1:
            exit()
        time.sleep(0.1)

def progress(x, y): #x=progress   y=out of   for example progress(70,100)=70% done
    global updatex,updatey,process
    if process == None:
        process = threading.Thread(target=display_progress)
        process.start()
    updatex = x
    updatey = y
    return
    
