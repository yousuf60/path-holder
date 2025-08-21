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
    assert f.remove()
    f.new("f1.txt")
    assert f.ok()


def test_process_file():
    text1 = "blah blah test"
    text2 = "2blah blah test"
    f.write(text1)
    f.add(text2)
    assert f.text() == text1+text2
    assert next(f.lines())== text1+text2
    f.clear()
    assert f.text() == ""
    


