class ParkingSystem(object):


  def __init__(self, big, medium, small):
    self.parkingSpace = {
      1: big,
      2: medium,
      3: small
    }
    

  def addCar(self, carType):
    if self.parkingSpace[carType] > 0:
      self.parkingSpace[carType] -= 1
      return True
    else:
      return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)