import sys
from os import getcwd
print(f"running from {getcwd()}")
print(sys.argv)
if "--port" in sys.argv:
    try:
        port = int(sys.argv[sys.argv.index("--port")+1])
    except ValueError:
        print("ivalid port number")
        exit()
else:
    print("no port argument")
    exit()

file= open("python-server/default_htaccess","r")
default = file.read()
file.close()

replace = default.replace("0000",str(port))

file = open("public_html/.htaccess","w")
file.write(replace)
file.close()