import logging 

class Test():
    def __init__(self, name: str="") -> None:
        self.name = name
        pass
    
    def run(self):
        print(f"Running {self.name}:", sep= ' ', end=" ", flush=True)
        logging.info(f"Running {self.name}")
        self._run()
        pass
    
    def success(self):
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
        pass
    
    def fail(self):
        print('\x1b[6;30;41m' + 'Failed!' + '\x1b[0m')
        pass