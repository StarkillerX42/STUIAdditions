import gc
import pprint

class ScriptClass(object,):
    def __init__(self, sr,):
        print('Garbage:')
        pprint.pprint(gc.garbage)
    
    def run(self, sr):
        n = gc.collect()
        pprint.pprint(gc.garbage)

