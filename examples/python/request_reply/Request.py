#!/usr/bin/python
import time
import sys

import message_defs as md

# Python version conditional import.
# Not necessary if targeting single version of Python
if sys.version_info[0] == 3 and sys.version_info[1] == 7:
    # Python 3.7
	import PyDragonfly3 as df
	from PyDragonfly3 import copy_from_msg, copy_to_msg, MT_EXIT, MT_KILL

elif sys.version_info[0] == 2 and sys.version_info[1] == 7:
    # Python 2.7
	import PyDragonfly2 as df
	from PyDragonfly2 import copy_from_msg, copy_to_msg, MT_EXIT, MT_KILL

else:
	raise ImportError("Consumer only supports Python 2.7 and 3.7")


MID_REQUEST = 11

# Note: Request must be started second

if __name__ == "__main__":
    mod = df.Dragonfly_Module(MID_REQUEST, 0)
    mod.ConnectToMMM()
    mod.Subscribe(md.MT_TEST_DATA)
    mod.Subscribe(MT_EXIT)
    
    print("Request running...\n")
    
    while ( 1):
        mod.SendSignal(md.MT_REQUEST_TEST_DATA)
        print("Sent request for data")
        msg = df.CMessage()
        mod.ReadMessage(msg)
        print("Received message", msg.GetHeader().msg_type)
        if msg.GetHeader().msg_type == md.MT_TEST_DATA:
            msg_data = md.MDF_TEST_DATA()
            copy_from_msg(msg_data, msg)
            print("Data = [a: %d, b: %d, x: %f]" % (msg_data.a, msg_data.b, msg_data.x))
        time.sleep(1)
        
    mod.DisconnectFromMMM()
        
