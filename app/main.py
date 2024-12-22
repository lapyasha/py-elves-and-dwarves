from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from typing import List

from app.players.player import Player


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        if isinstance(elf, Elf):
            elf.play_elf_song()
        else:
            raise ValueError(f"{elf.nickname} is not an Elf")


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
        else:
            raise ValueError(f"{dwarf.nickname} is not a Dwarf")
