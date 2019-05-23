
# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class.


class Vehicle:
    # Vehicle
    # This is the base class for all vehicles
    pass


class GroundVehicle(Vehicle):
    # Vehicle => GroundVehicle
    pass


class Car(GroundVehicle):
    # Vehicle => GroundVehicle => Car
    pass


class Motorcycle(GroundVehicle):
    # Vehicle => Ground Vehicle => Motorcycle
    pass


class FlightVehicle(Vehicle):
    # Vehicle => FlightVehicle
    pass


class Starship(FlightVehicle):
    # Vehicle => FlightVehicle => Starship
    pass


class Airplane(FlightVehicle):
    # Vehicle => FlightVehicle => Airplane
    pass
