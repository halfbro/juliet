import os
import imp

modules = {}

def load_modules(path="./modules/"): # Consider adding recursive sorting at some point in the future
    names = os.listdir(path)
    for name in names:
        if not name.endswith(".py"): continue
        print("Importing module {0}".format(name))
        name = name.split('.')[0]
        try:
            new_module = imp.load_source(name, path)
            modules[name] = new_module
        except ImportError as e:
            print("Error importing module {0} from directory {1}".format(name,os.getcwd()))
            print(e)
            continue
        print("Success")

load_modules()
