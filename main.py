from __future__ import annotations

from dataclasses import dataclass
import dataclasses
from typing import List, Type





@dataclass
class Server:
    id: str
    name: str
    rank: str

    @classmethod
    def from_dict(cls: Type[Server], data: dict[str, str]) -> Server:
        """Creates a new Server instance from dict"""


@dataclass
class Class:
    id: str
    name: str

    @classmethod
    def from_dict(cls: Type[Class], data: dict[str, str]) -> Class:
        """Creates a new Class instance from dict"""

        _id = data.get("id")
        _name = data.get("name")

        return cls(id=_id, name=_name)


@dataclass
class Player:
    id: str
    power: str
    global_rank: str
    name: str
    tao_res: str
    alliance_id: str
    _class: Class

    @property
    def player_class(self):
        return self._class

    @classmethod
    def from_dict(cls: Type[Player], data: dict[str, str]) -> Player:
        """Creats a new Player instance from dict"""
        _id = data.get("id")
        _power = data.get("power")
        _global_rank = data.get("global_rank")
        _name = data.get("name")
        _tao_res = data.get("tao_res")
        _alliance_id = data.get("alliance_id")
        _class = Class.from_dict(data.get("class"))

        return cls(
            id=_id,
            power=_power,
            global_rank=_global_rank,
            name=_name,
            tao_res=_tao_res,
            alliance_id=_alliance_id,
            _class=_class,
        )


@dataclass
class Guild:
    id: str
    characters: str
    power: str
    global_rank: str
    warriors: str
    sorcerers: str
    taoists: str
    arbalists: str
    lancers: str
    name: str
    server: Server
    roster: List[Player]

    @classmethod
    def from_dict(cls: Type[Guild], data: dict[str, str]) -> Guild:
        """Creates a new Guild instance from dict"""

        _id = data.get("id")
        _characters = data.get("characters")
        _power = data.get("power")
        _global_rank = data.get("global_rank")
        _warriors = data.get("warriors")
        _sorcerers = data.get("sorcerers")
        _taoists = data.get("taoists")
        _arbalists = data.get("arbalists")
        _lancers = data.get("lancers")
        _name = data.get("name")
        server = Server.from_dict(data.get("server"))
        roster = [Player.from_dict(v) for k, v in data.get("roster").items()]

        return cls(
            id=_id,
            characters=_characters,
            power=_power,
            global_rank=_global_rank,
            warriors=_warriors,
            sorcerers=_sorcerers,
            taoists=_taoists,
            arbalists=_arbalists,
            lancers=_lancers,
            name=_name,
            server=server,
            roster=roster,
        )


if __name__ == '__main__':


   # guild = Guild.from_dict(data)
    print(guild.name)  # UNFORGIVEN 乡
    print(guild.power) # 8603001
    print(guild.roster[1]) # Player(id='1229507', power='200253', global_rank='2136', name='eoDigs', tao_res=None, alliance_id='0', _class=Class(id='2', name='Sorcerer'))
