#!/usr/bin/python
import time
import sys

import message_defs as md

# Python version conditional import.
# Not necessary if targeting single version of Python
if sys.version_info[0] == 3 and sys.version_info[1] == 7:
    # Python 3.7
	import PyDragonfly3 as df
	from PyDragonfly3 import copy_from_msg

elif sys.version_info[0] == 2 and sys.version_info[1] == 7:
    # Python 2.7
	import PyDragonfly2 as df
	from PyDragonfly2 import copy_from_msg

else:
	raise ImportError("Consumer only supports Python 2.7 and 3.7")


MID_CONSUMER = 11

if __name__ == "__main__":
    mod = df.Dragonfly_Module(MID_CONSUMER, 0)
    mod.ConnectToMMM("localhost:7111")
    mod.Subscribe(md.MT_TEST_DATA)
    
    print("Consumer running...\n")
    
    while (1):
        msg = df.CMessage()
        mod.ReadMessage(msg)    # blocking read
        print("Received message ", msg.GetHeader().msg_type)

        if msg.GetHeader().msg_type == md.MT_TEST_DATA:
            msg_data = md.MDF_TEST_DATA()
            copy_from_msg(msg_data, msg)
            print("  Data = [a: %d, b: %d, x: %f]" % (msg_data.a, msg_data.b, msg_data.x))
        
    mod.DisconnectFromMMM()
        
