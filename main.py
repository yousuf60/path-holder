import pathlib
from pathlib import Path
import os


class File:
    file: pathlib.PosixPath
    def __init__(self, *paths: str):
        self.hold(*paths)
            
    def make(self):
        if self.ok():
            return True
        self.file.touch()

    def remove(self):
        os.remove(self.file)
        return not self.ok()
        
    def ok(self):
        return self.file.exists()

    def hold(self, *paths: str):  
        self.file = Path(os.path.join(*paths))    
        self.make()

    #hold new file in the same dir
    def new(self, one_file: str):
        splitted_path = os.path.split(self.file)
        self.hold(splitted_path[0], one_file)
    
        

