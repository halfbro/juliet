import os
import imp

modules = {}

def load_modules(path="./modules/"):
    try:
        modules['juliet_module'] = imp.load_source('juliet_module', path + "juliet_module.py")
    except ImportError as e:
            print("Error importing module {0} from directory {1}".format(name,os.getcwd()))
            print(e)

    for root, dirs, files in os.walk(path):
        for name in files:
            if not name.endswith(".py"): continue
            print("Importing module {0}".format(name))
            try:
                modules[name.split('.')[0]] = imp.load_source(name.split('.')[0], root + '/' + name)
            except ImportError as e:
                print("Error importing module {0} from directory {1}".format(name,os.getcwd()))
                print(e)
                continue
            print("Success")

load_modules()
