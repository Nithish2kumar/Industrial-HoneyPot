from pymodbus.server import StartTcpServer
from pymodbus.datastore import (ModbusSequentialDataBlock,ModbusSlaveContext,ModbusServerContext)

from plc.simulator import (reg,startSimulator)

import threading
import time

holdingReg=ModbusSequentialDataBlock(0,[0]*10)
store=ModbusSlaveContext(hr=holdingReg)
context=ModbusServerContext(slaves=store,single=True)

def sync_reg():
    while True:
        for adr, val in enumerate(reg):
            holdingReg.setValues(adr,[val])
        time.sleep(1)

def startrealPLC():
    print("Starting simulator...")
    startSimulator()
    print("Starting Reg synchronizatiom...")
    threading.Thread(target=sync_reg,daemon=True).start()
    print("Starting TCP server...")
    StartTcpServer(context=context,address=("0.0.0.0",502))

if __name__ =="__main__":
    startrealPLC()