py-update
=========

This package provides a module `update` for deep update operations with multiple strategies on nested structures.

```python
update.deepupdate(x, y[, replace: update.MODE])
"""Perform a deep update (in place) of `x` with `y` using the specified strategy."""
```

Use `update.MODE` to specify the strategy for merging fields from `y` into `x`:
- `"right"` : merge fields and update values, default
- `"left"`  : merge fields and keep values
- `True`    : replace fields
- `False`   : append fields

> **Note**: fields values are mutable objects (e.g. `dict.values`, `list`, `set`)
