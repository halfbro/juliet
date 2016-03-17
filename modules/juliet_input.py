from threading import Thread

class Juliet_Input (Thread):
    def __init(self):
        Thread.__init(self)
    
    def run(self):
        while True:
            char = raw_input()
            if char == 'q':
                break

