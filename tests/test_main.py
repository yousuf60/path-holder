from .. import File

f = File("tests/","data/","fl.txt")

def test_exists():
    assert f.file.exists() and f.ok()

def test_remove():
    assert f.remove() 

def test_remake():
    f.new("f2.txt")
    assert f.ok()
    assert f.file == File("tests/data/f2.txt").file

