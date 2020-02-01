#other program timer
from datetime import datetime
from sys import argv
from importlib import import_module


start_time=datetime.now()
module_to_test = argv[2].strip(".py")
imported=import_module(module_to_test)

if hasattr(imported,"main"):
    imported.main()
else:
    print("The specified file has no entry method named \"main\"")





test.main()
end_time=datetime.now()
time_taken = end_time-start_time
print('python waited'+ str(time_taken)+'seconds')