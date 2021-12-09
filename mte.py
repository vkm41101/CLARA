import os
os.system('python3 plotter.py')
while True:
    try:
        f=open('h.dll','r')
        f.close()
        os.remove('h.dll')
        break
    except:
        continue
os.system('python3 PH_GUI.py')
