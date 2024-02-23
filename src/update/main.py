from typing import Literal
from functools import singledispatch

MODE = Literal[
    "left",     # update mutable
    "right",    # update all
    True,       # replace all
    False,      # no replace
]


@singledispatch
def deepupdate(this, other, replace: MODE = True):
    if replace is True or replace == "right":
        return other
    return this


@deepupdate.register
def _(this: dict, other: dict, replace: MODE = "right") -> dict:
    for k, v in other.items():
        if replace is True or k not in this:
            this[k] = v
        elif replace == "right":
            this[k] = deepupdate(this[k], v, replace=replace)
        elif replace == "left":
            deepupdate(this[k], v, replace=replace)
        else:  # replace == False
            pass
    return this


@deepupdate.register
def _(this: list, other: list, replace: MODE = False) -> list:
    if replace is True:
        this.clear()
    this.extend(other)
    return this
