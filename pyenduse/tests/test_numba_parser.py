import sys
sys.path.append('/mnt/c/Users/johnr/Documents/py-enduse/pyenduse')
from pyenduse import numba_parser as nbp

faf = {
    1: (0.75, 5000, 15), 
    2: (0.20, 3000, 20), 
    3: (0.05, 2000, 25),
}

faf_action = {
    2025: [[1, 2, 3], [0.1, 0.65, 0.25]],
    2030: [[1, 2, 3], [0, 0.25, 0.75]],
}

end_use = {
    'faf': (faf, faf_action), 
    'faf2': (faf, faf_action), 
    'faf3': (faf, )
    }

building_obj = {
    'CustomerClass': 'Residential',
    'Segment': 'Single Family',
    'ConstructionVintage': 'Existing',
    'PrimaryFuelType': 'Electric',
    'EfficiencyLevel': 'Low',
    'Floorspace': 2000,
    'NumberBuildings': 1000,
    'StartYear': 2020,
    'EndYear': 2040,
    'EndUses': end_use,
}

def test_parse_building_meta():
    """Test if Numba meta field matches test meta data"""
    # get list of all string type fields
    vals = [val for key, val in building_obj.items() if isinstance(val, str)]
    # all numba meta fields should be strings
    bld_numba = nbp.parse_building_meta(building_obj, nbp.BuildingNumba())
    numba_vals = bld_numba.bld_meta.values()
    assert all(a == b for a, b in zip(vals, numba_vals))

def test_parse_building_vars():
    """Test if Numba variable fields"""
    # get list of all string type fields
    vals = [val for key, val in building_obj.items() if isinstance(val, int)]
    # all numba meta fields should be strings
    bld_numba = nbp.parse_building_vars(building_obj, nbp.BuildingNumba())
    numba_vals = bld_numba.bld_vars.values()
    assert all(a == b for a, b in zip(vals, numba_vals))

def test_parse_end_uses():
    """Test if Numba variable fields"""
    # get list of all string type fields
    end_uses = end_use.keys()
    # all numba meta fields should be strings
    bld_numba = nbp.parse_end_uses(building_obj, nbp.BuildingNumba())
    numba_vals = bld_numba.end_uses
    assert all(a == b for a, b in zip(end_uses, numba_vals))

