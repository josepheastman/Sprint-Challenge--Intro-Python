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
# Put a comment noting which class is the base class

# Base Class: Vehicle


class Vehicle:
    pass

# Class: Vehicle => FlightVehicle


class FlightVehicle(Vehicle):
    pass

# Class: Vehicle => FlightVehicle => Starship


class Starship(FlightVehicle):
    pass

# Class Vehicle => FlightVehicle => Airplane


class Airplane(FlightVehicle):
    pass

# Class Vehicle => GroundVehicle


class GroundVehicle(Vehicle):
    pass

# Class Vehicle => GroundVehicle => Car


class Car(GroundVehicle):
    pass

# Class Vehicle => GroundVehicle => Motorcycle


class Motorcycle(GroundVehicle):
    pass
