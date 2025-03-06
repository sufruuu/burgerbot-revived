import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sufruuu/burgerbot-revived/dev_ws/install/burgerbot_rev1'
