import numpy as numpy
from numba import jitclass
from numba import types, typed

obj_meta = (types.string, types.string)
obj_vars = (types.string, types.int64)

spec = [
    ('bld_meta', types.DictType(*obj_meta)),
    ('bld_vars', types.DictType(*obj_vars)),
    ('end_uses', types.ListType(types.string))
]

@jitclass(spec)
class BuildingNumba(object):
    def __init__(self):
        self.bld_meta = typed.Dict.empty(*obj_meta)
        self.bld_vars = typed.Dict.empty(*obj_vars)
        self.end_uses = typed.List.empty_list(types.string)

def parse_building_meta(bld_obj, bld_numba):
    """Parse string type meta fields into numba class"""
    # will assume that all string type fields are meta data
    for key, val in bld_obj.items():
        if isinstance(val, str):
            bld_numba.bld_meta[key] = val

    return bld_numba

def parse_building_vars(bld_obj, bld_numba):
    """Parse numeric variables used for building calculation"""
    # will assume that all string type fields are meta data
    for key, val in bld_obj.items():
        if isinstance(val, int):
            bld_numba.bld_vars[key] = val

    return bld_numba

def parse_end_uses(bld_obj, bld_numba):
    """Parse end uses into numba attributes"""
    # will assume that all string type fields are meta data
    for i in bld_obj['EndUses'].keys():
        bld_numba.end_uses.append(i)
    return bld_numba

