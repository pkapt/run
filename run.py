
import os

def run():
    for filename in os.listdir("."):
        if filename.lower() == "runfile":
            f = open(filename, "r")
            cmd = f.read()
            if cmd == '':
                print("Invalid runfile")
                return
            os.system(cmd)
            return
    print("No runfile found")

if __name__ == "__main__":
    run()