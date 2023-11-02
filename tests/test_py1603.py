from py1603 import ParkingSystem


def test_1():
    obj = ParkingSystem(1, 1, 0)
    assert obj.addCar(1) is True
    assert obj.addCar(2) is True
    assert obj.addCar(3) is False
    assert obj.addCar(1) is False
