#!/usr/bin/python
import time
import sys

import message_defs as md

# Python version conditional import.
# Not necessary if targeting single version of Python
if sys.version_info[0] == 3 and sys.version_info[1] == 7:
    # Python 3.7
    import PyDragonfly3 as df
    from PyDragonfly3 import copy_to_msg

elif sys.version_info[0] == 2 and sys.version_info[1] == 7:
    # Python 2.7
    import PyDragonfly2 as df
    from PyDragonfly2 import copy_to_msg

else:
	raise ImportError("Producer only supports Python 2.7 and 3.7")


MID_PRODUCER = 10

if __name__ == "__main__":
    mod = df.Dragonfly_Module(MID_PRODUCER, 0)
    mod.ConnectToMMM("localhost:7111")
    
    print("Producer running...\n")

    a = 0
    run = True
    while run:
        out_msg = df.CMessage(md.MT_TEST_DATA)

        data = md.MDF_TEST_DATA()
        data.a = a
        data.b = -3
        data.x = 1.234
        copy_to_msg(data, out_msg)
        mod.SendMessage(out_msg)

        print("Sent message ", out_msg.GetHeader().msg_type)
        print("  Data = [a: %d, b: %d, x: %f]" % (data.a, data.b, data.x))

        a += 1
        
        time.sleep(1)
