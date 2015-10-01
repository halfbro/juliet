import os

class loader:
    modules = {};

    def __init__(self):
        self.load_modules();

    def load_modules(self, path="./modules/"): # Consider adding recursive sorting at some point in the future
        names = os.listdir(path);
        pwd = os.getcwd();
        os.chdir(path);
        for name in names:
            print("Importing module {0}".format(name));
            name = name.split('.')[0];
            try:
                new_module = __import__(name);
                self.modules[name] = new_module;
            except ImportError:
                print("Error importing module {0}".format(name));
                continue;
            print("Success");
        os.chdir(pwd);
