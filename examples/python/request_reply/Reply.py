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


MID_REPLY = 10

# Note: Reply must be started first

if __name__ == "__main__":
    mod = df.Dragonfly_Module(MID_REPLY, 0)
    mod.ConnectToMMM()
    mod.Subscribe(md.MT_REQUEST_TEST_DATA)
    
    print("Reply running...\n")
    
    run = True
    while run:
        in_msg = df.CMessage()
        print("Waiting for message")
        rcv = mod.ReadMessage(in_msg, 1.0)
        if rcv == 1:
            print("Received message", in_msg.GetHeader().msg_type)
            out_msg = df.CMessage(md.MT_TEST_DATA)
            data = md.MDF_TEST_DATA()
            if in_msg.GetHeader().msg_type == md.MT_REQUEST_TEST_DATA:
                data.a = -20
                data.b = 47
                data.x = 123.456
                copy_to_msg(data, out_msg)
                mod.SendMessage(out_msg)
                print("Sent message", out_msg.GetHeader().msg_type)
            elif in_msg.GetHeader().msg_type in (MT_EXIT, MT_KILL):
               run = False        
