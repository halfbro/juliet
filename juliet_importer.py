import os
import imp

modules = {}

def load_modules(path="./modules/"): # Consider adding recursive searching at some point in the future
    modules['juliet_module'] = imp.load_source('juliet_module', path + "juliet_module.py")
    names = os.listdir(path)
    for name in names:
        if not name.endswith(".py"): continue
        print("Importing module {0}".format(name))
        try:
            modules[name.split('.')[0]] = imp.load_source(name.split('.')[0], path + name)
        except ImportError as e:
            print("Error importing module {0} from directory {1}".format(name,os.getcwd()))
            print(e)
            continue
        print("Success")

load_modules()
