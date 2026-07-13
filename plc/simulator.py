import random
import time

reg={"Temperature":30,
     "Pressure":100,
     "Tank Level":70,
     "Pump state":1
    }

def updateRegister():
    while True:
        reg["Temperature"]+=random.randint(-1,1)
        reg["Pressure"]+=random.randint(-2,2)
        
        if reg["Pump state"]:
            reg["Tank Level"]+=random.randint(0,2)
        else:
            reg["Tank Level"]-=random.randint(0,2)
        reg["Tank Level"]=max(0,min(100, reg["Tank Level"]))

        if random.random() <0.1:
            reg["Pump state"]^=1
        print(reg)

        time.sleep(1)