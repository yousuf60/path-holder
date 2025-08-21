import pathlib
from pathlib import Path
import os


class File:
    file: pathlib.PosixPath
    def __init__(self, *paths: str):
        self.hold(*paths)
            
    def make(self):
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
    
        
    def _open(self, *args, **kwargs):
        return open(self.file, *args, **kwargs)

        
    def write(self, text: str, *args, **kwargs):
        with  self._open("w" ,*args, **kwargs) as f:
            f.write(str(text))

    def add(self, text: str, *args, **kwargs):
        with self._open("a", *args, **kwargs) as f:
            f.write(text)
            
    def clear(self):
        self.write("")
        
    def lines(self):
        with self._open("r") as f:
            yield f.readline()

    def text(self):
        with self._open("r") as f:
            return f.read()
