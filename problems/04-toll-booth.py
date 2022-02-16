# Design a toll booth Application of Padma bridge. At booth, it will collect the amount of toll from
# all the vehicles passing through based on the vehicle types (.e. motorcycle, Buss, Truck, Car,
# Train etc.) and categories (Govt, Personal, carriage of Goods, Public etc.) and weight of the
# vehicles etc.
# Let's assume that Govt wants to encourage its citizen for paying tax regularly. So, it has
# categorized the taxpayer and provided a card (Platinum, Gold, Silver) to get discount on various
# public and non-public services. Let's consider that Govt has declared (Platinum->10%, discounts,
# Gold->8%, Silver->5%) in Tolls Fees, and for Govt vehicles (No Tool fees), for Personal Vehicles->
# Govt Official (2%).
# Design the model and implement the program from OOD and OOP (Inheritance, polymorphism)
# concept. Also implement a method ie. calculate Toll Vehicle) which is taking and returning the
# tollAmount to be paid at toll booth.

class Vehicle:
  def __init__(self, weight: int) -> None:
    self.weight = weight


class Motorcycle(Vehicle):
  def __init__(self, weight: int) -> None:
    super().__init__(weight)


class Bus(Vehicle):
  def __init__(self, weight: int) -> None:
    super().__init__(weight)


class Truck(Vehicle):
  def __init__(self, weight: int) -> None:
    super().__init__(weight)


class Car(Vehicle):
  def __init__(self, weight: int) -> None:
      super().__init__(weight)


class Train(Vehicle):
  def __init__(self, weight: int) -> None:
    super().__init__(weight)


class Card:
  def __init__(self, discount: str) -> None:
    self.discount = discount

class PlatiumCard(Card):
  def __init__(self) -> None:
    super().__init__(0.1)


class GoldCard(Card):
  def __init__(self) -> None:
    super().__init__(0.08)


class SilverCard(Card):
  def __init__(self) -> None:
    super().__init__(0.05)


class Citizen:
  _categoryDiscount = 0.98
  def __init__(self, card: Card, vehicle: Vehicle) -> None:
    self.card = card
    self.vehicle = vehicle


class GovtCitizen(Citizen):
  def __init__(self, card: Card, vehicle: Vehicle) -> None:
    super().__init__(card, vehicle)
    self._categoryDiscount = 0

class CivilianCitizen(Citizen):
  def __init__(self, card: Card, vehicle: Vehicle) -> None:
    super().__init__(card, vehicle)


class Toll:
  @classmethod
  def calculateToll(self, citizen: Citizen) -> int:
    tollFee = int(citizen.vehicle.weight * citizen.card.discount * citizen._categoryDiscount)
    return tollFee


motorcycle = Motorcycle(275)
truck = Truck(2722)


platiumCard = PlatiumCard()
goldCard = GoldCard()
silverCard = SilverCard()


govtCitizen_1 = GovtCitizen(platiumCard, motorcycle)
govtCitizen_2 = GovtCitizen(goldCard, truck)
civilianCitizen_1 = CivilianCitizen(goldCard, motorcycle)
civilianCitizen_2 = CivilianCitizen(silverCard, truck)


print (Toll.calculateToll(govtCitizen_1))
print (Toll.calculateToll(govtCitizen_2))
print (Toll.calculateToll(civilianCitizen_1))
print (Toll.calculateToll(civilianCitizen_2))