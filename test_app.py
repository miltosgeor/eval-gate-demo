from app import classify

def test_urgent():
    assert classify("Court filing due today") == "urgent"

def test_normal():
    assert classify("Lunch next week?") == "normal"