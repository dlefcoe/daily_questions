"""
math_gcse.py

This module provides a collection of mathematical utilities and formulas 
commonly used in GCSE-level mathematics. It includes functions and classes 
for calculations involving geometry, algebra, physics, and general mathematics.

Features:
- Functions for calculating the circumference of a circle, solving quadratic equations, 
    and applying Pythagoras' theorem.
- The `Area` class for calculating the area of various shapes such as squares, circles, 
    triangles, rectangles, and trapeziums.
- The `Volume` class for calculating the volume of 3D shapes such as cylinders, spheres, 
    and cones.
- The `SpeedDistanceTime` class for solving problems involving speed, distance, and time.
- The `DensityMassVolume` class for solving problems involving density, mass, and volume.
Constants:
- `C`: Speed of light in vacuum (300,000,000 m/s).
- `VERY_LARGE_NUMBER`: A placeholder for extremely large numbers (1e308).


This module is designed to be a utility for educational purposes and basic mathematical 
calculations.
"""


import math


# speed of light in vacuum
C = 300_000_000  # m/s

# a very large number
VERY_LARGE_NUMBER = 1e308


# Circumference of a circle
def circumference_of_circle(radius: float) -> float:
    return 2 * math.pi * radius


# Pythagoras' theorem
def pythagoras(a: float, b: float) -> float:
    return math.sqrt(a**2 + b**2)


# Quadratic formula
def quadratic_formula(a: float, b: float, c: float) -> tuple[float, float] | None:
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None  # No real roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2


class Area:
    """Utility class for area calculations."""

    @staticmethod
    def square(side: float) -> float:
        """Calculate the area of a square."""
        if side < 0:
            print("Side cannot be negative")
            return 0
        return side**2

    @staticmethod
    def circle(radius: float) -> float:
        """Calculate the area of a circle."""
        if radius < 0:
            print("Radius cannot be negative")
            return 0
        return math.pi * radius**2

    @staticmethod
    def triangle(base: float, height: float) -> float:
        """Calculate the area of a triangle."""
        return 0.5 * base * height

    @staticmethod
    def rectangle(length: float, width: float) -> float:
        """Calculate the area of a rectangle."""
        return length * width

    @staticmethod
    def trapezium(base1: float, base2: float, height: float) -> float:
        """Calculate the area of a trapezium."""
        return 0.5 * (base1 + base2) * height


class Volume:
    """Utility class for volume calculations."""

    @staticmethod
    def cylinder(radius: float, height: float) -> float:
        """Calculate the volume of a cylinder."""
        return math.pi * radius**2 * height

    @staticmethod
    def sphere(radius: float) -> float:
        """Calculate the volume of a sphere."""
        return (4 / 3) * math.pi * radius**3

    @staticmethod
    def cone(radius: float, height: float) -> float:
        """Calculate the volume of a cone."""
        return (1 / 3) * math.pi * radius**2 * height


class SpeedDistanceTime:
    """Utility class for speed, distance, and time calculations."""

    @staticmethod
    def speed(distance: float, time: float) -> float:
        """Calculate speed given distance and time."""
        if time == 0:
            print("Time cannot be zero")
            return C

        return distance / time

    @staticmethod
    def distance(speed: float, time: float) -> float:
        """Calculate distance given speed and time."""
        if time < 0:
            print("Time cannot be negative")
            return 0

        return speed * time

    @staticmethod
    def time(distance: float, speed: float) -> float:
        """Calculate time given distance and speed."""
        if speed == 0:
            print("Speed cannot be zero")
            return VERY_LARGE_NUMBER
        return distance / speed


class DensityMassVolume:
    """Utility class for density, mass, and volume calculations."""

    @staticmethod
    def density(mass: float, volume: float) -> float:
        """Calculate density given mass and volume."""
        return mass / volume

    @staticmethod
    def mass(density: float, volume: float) -> float:
        """Calculate mass given density and volume."""
        return density * volume

    @staticmethod
    def volume(mass: float, density: float) -> float:
        """Calculate volume given mass and density."""
        return mass / density


