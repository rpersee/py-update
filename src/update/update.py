from functools import singledispatch
from typing import Literal


ReplaceStrategy = Literal[
    "left",
    "right",
    True,
    False,
]


class UpdateConflict:
    strict = True

    @classmethod
    def resolve(cls, this, that, *, replace: ReplaceStrategy):
        if replace is True:
            return that
        if replace is False:
            return this
        if cls.strict:
            raise ValueError(f"expected {type(this)}, got {type(that)}")
        if replace == "right":
            return that
        if replace == "left":
            return this


@singledispatch
def deepupdate(this, that, *, replace: ReplaceStrategy = "right"):
    """Update nested structures in place.

    :param this: The structure to update.
    :param that: The structure to update with.
    """
    if replace in (True, "right"):
        return that
    return this


@deepupdate.register
def _(this: dict, that: dict, *, replace: ReplaceStrategy = "right") -> dict:
    if not isinstance(that, dict):
        return UpdateConflict.resolve(this, that, replace=replace)

    for k, v in that.items():
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
def _(this: list, that: list, *, replace: ReplaceStrategy = "right") -> list:
    if not isinstance(that, list):
        return UpdateConflict.resolve(this, that, replace=replace)

    if replace is True:
        this.clear()
    this.extend(that)

    return this
