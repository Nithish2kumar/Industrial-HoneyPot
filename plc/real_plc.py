from pymodbus.server import StartTcpServer
from pymodbus.datastore import (ModbusSequentialDatablock,ModbusDeviceContext,ModbusServerContext)

from plc.simulator import (reg,startSimulator)

import threading
import time

store=ModbusSequentialDatablock(address=0,values=[0]*10)
plcdevice=ModbusDeviceContext(hr=store)
context=ModbusServerContext(devices=plcdevice,single=True)\

def sync_reg():
    while True:
        for adr, val in enumerate(reg):
            store.setValues(adr,[val])
        time.sleep(1)

def startrealPLC():
    print("Starting simulator...")
    startSimulator()
    print("Starting Reg synchronizatiom...")
    threading.Thread(target=sync_reg,daemon=True).start()
    print("Starting TCP server...")
    StartTcpServer(context=context,address=("0.0.0.0",5020))

if __name__ =="__main__":
    startrealPLC()