#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
from datashape import dshape

D_TYPES_FIELD_TO_DTYPE =  {
    'string': 'string',
    'number': 'float64',
    'integer': 'int',
    'boolean': 'bool',
    'null': 'void',
    'object': 'json',
    'array': 'var',
    'datetime': "datetime[tz='UTC']",
    'date': 'date',
    'time': "time[tz='UTC']",
    'geopoint': 'string',
    'geojson': 'json',
    'any': 'var'
}

D_DTYPE_TO_TYPES_FIELD =  {
}

DTYPE_DEFAULT = 'string'
JTS_FIELD_TYPE_DEFAULT = 'string'

class DatashapeNoFormatter(object):
    LINE_FEED = ''
    INDENT = ''
    KEY_VAL_SEP = ''

class DatashapeNormalFormatter(DatashapeNoFormatter):
    LINE_FEED = '\n'
    INDENT = "  "
    KEY_VAL_SEP = ' '

DatashapeDefaultFormatter = DatashapeNormalFormatter

def jts_field_to_dtype(field, missing=False):
    """Converts a field of a JSON Table Schema to dtype"""
    if missing:
        s_missing = '?'
    else:
        s_missing = ''

    try:
        typ = field['type']
    except KeyError:
        return DTYPE_DEFAULT

    try:
        fmt = field['format']
    except KeyError:
        fmt = None

    try:
        constraint = field['constraint']
    except KeyError:
        constraint = None

    try:
        return s_missing + D_TYPES_FIELD_TO_DTYPE[typ]
    except KeyError:
        msg = "Can't find type %r - using %r" % (typ, DTYPE_DEFAULT)
        warnings.warn(msg)
        return s_missing + DTYPE_DEFAULT

def jts_to_datashape(schema, missing=False):
    """Converts a JSON Table Schema to a Datashape"""
    return dshape(_jts_to_string_datashape(schema, missing, datashape_formatter=DatashapeNoFormatter))

def _jts_to_string_datashape(schema, missing=False, datashape_formatter=DatashapeDefaultFormatter):
    """Converts a JSON Table Schema to a string that could be convert to Datashape"""
    line_feed = datashape_formatter.LINE_FEED
    indent = datashape_formatter.INDENT
    key_val_sep = datashape_formatter.KEY_VAL_SEP
    s = 'var * {' + line_feed
    for i, field in enumerate(schema['fields']):
        if i != 0:
            s += ',' + line_feed
        s += indent + "%r:%s%s" % (field['name'], key_val_sep, jts_field_to_dtype(field, missing=missing))
    s += line_feed + '}'
    return s

def dtype_to_jts_fieldtype(dtyp):
    """Converts a dtype to a type of a field of a JSON Table Schema"""
    raise NotImplementedError

def datashape_to_jts(ds):
    """Converts a Datashape to JSON Table Schema"""
    raise NotImplementedError
