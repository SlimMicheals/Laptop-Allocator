from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple
from itertools import permutations


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def sadness(person: Person, laptop: Laptop) -> int:
    if laptop.operating_system in person.preferred_operating_system:
        return person.preferred_operating_system.index(laptop.operating_system)

    return 100


def allocate_laptops(
    people: List[Person],
    laptops: List[Laptop],
) -> List[Tuple[Person, Laptop]]:
    best_allocation = None
    lowest_sadness = None

    for laptop_order in permutations(laptops, len(people)):
        allocation = list(zip(people, laptop_order))

        total_sadness = 0
        for person, laptop in allocation:
            total_sadness += sadness(person, laptop)

        if lowest_sadness is None or total_sadness < lowest_sadness:
            lowest_sadness = total_sadness
            best_allocation = allocation

    return best_allocation


if __name__ == "__main__":
    people = [
        Person("Alice", 25, [OperatingSystem.UBUNTU, OperatingSystem.ARCH, OperatingSystem.MACOS]),
        Person("Bob", 30, [OperatingSystem.MACOS, OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
    ]

    laptops = [
        Laptop(1, "Dell", "XPS", 13.3, OperatingSystem.UBUNTU),
        Laptop(2, "Apple", "MacBook", 13.0, OperatingSystem.MACOS),
    ]

    result = allocate_laptops(people, laptops)

    for person, laptop in result:
        print(person.name, "->", laptop.operating_system)