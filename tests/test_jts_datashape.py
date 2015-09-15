#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jts_datashape import *
from datashape import dshape

SCHEMA = {
    'fields': [
        {
            'name': 'foo',
            'type': 'integer' # 0
        },
        {
            'name': 'bar',
            'type': 'string' # 1
        },
        {
            'name': 'field2',
            'type': 'number' # 2
        },
        {
            'name': 'field3',
            'type': 'boolean' # 3
        }
    ]
}

# ===

def test_jts_to_datashape():
    expected = dshape("var * {'foo':int,'bar':string,'field2':float64,'field3':bool}")
    result = jts_to_datashape(SCHEMA)
    print(expected)
    print(result)
    assert result == expected

    expected = dshape("var * {'foo':?int,'bar':?string,'field2':?float64,'field3':?bool}")
    result = jts_to_datashape(SCHEMA, missing=True)
    assert result == expected

# ===

def test_jts_field_to_dtype_string():
    assert jts_field_to_dtype(SCHEMA['fields'][1]) == 'string'

def test_jts_field_to_dtype_number():
    assert jts_field_to_dtype(SCHEMA['fields'][2]) == 'float64'

def test_jts_field_to_dtype_integer():
    assert jts_field_to_dtype(SCHEMA['fields'][0]) == 'int'

def test_jts_field_to_dtype_boolean():
    assert jts_field_to_dtype(SCHEMA['fields'][3]) == 'bool'

def test_jts_field_to_dtype_null():
    assert jts_field_to_dtype({'type': 'null'}) == 'void'

def test_jts_field_to_dtype_object():
    pass

def test_jts_field_to_dtype_array():
    pass

def test_jts_field_to_dtype_datetime():
    pass

def test_jts_field_to_dtype_date():
    pass

def test_jts_field_to_dtype_time():
    pass

def test_jts_field_to_dtype_geopoint():
    pass

def test_jts_field_to_dtype_geojson():
    pass

def test_jts_field_to_dtype_any():
    pass

# ===

def test_datashape_to_jts():
    pass

# ===

def test_dtype_to_jts_fieldtype_string():
    pass
