# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:27:36 2010

@author: Jonas
"""

from __future__ import print_function
import numpy as np
import struct

lecroy_format = { 'descriptor_name':   [0, '16s'],  # 16-character string
                  'template_name':     [16, '16s'],
                  'comm_type':         [32, 'h'],   # short (2-byte signed integer)
                  'comm_order':        [34, 'h'],
                  'wave_descriptor':   [36, 'i'],   # int (4-byte signed integer)
                  'user_text':         [40, 'i'],
                  'res_desc1':         [44, 'i'],
                  'trig_time_array':   [48, 'i'],
                  'ris_time_array':    [52, 'i'],
                  'res_array1':        [56, 'i'],
                  'wave_array1':       [60, 'i'],
                  'wave_array2':       [64, 'i'],
                  'res_array2':        [68, 'i'],
                  'res_array3':        [72, 'i'],
                  'instrument_name':   [76, '16s'],
                  'instrument_number': [92, 'i'],
                  'trace_label':       [96, '16s'],
                  'reserved1':         [112, 'h'],
                  'reserved2':         [114, 'h'],
                  'wave_array_count':  [116, 'i'],
                  'points_per_screen': [120, 'i'],
                  'first_valid_point': [124, 'i'],
                  'last_valid_point':  [128, 'i'],
                  'first_point':       [132, 'i'],
                  'sparsing_factor':   [136, 'i'],
                  'segment_index':     [140, 'i'],
                  'subarray_count':    [144, 'i'],
                  'sweeps_per_acq':    [148, 'i'],
                  'points_per_pair':   [152, 'h'],
                  'pair_offset':       [154, 'h'],
                  'vertical_gain':     [156, 'f'],   # float (4-byte real number)
                  'vertical_offset':   [160, 'f'],
                  'max_value':         [164, 'f'],
                  'min_value':         [168, 'f'],
                  'nominal_bits':      [172, 'h'],
                  'nom_subarray_count':[174, 'h'],
                  'horiz_interval':    [176, 'f'],
                  'horiz_offset':      [180, 'd'],   # double (8-byte real number)
                  'pixel_offset':      [188, 'd'],
                  'vert_unit':         [196, '48s'],
                  'horiz_unit':        [244, '48s'],
                  'horiz_uncertainty': [292, 'f'],
                  'trigger_time':      [296, 'dbbbbhh'],
                  'acq_duration':      [312, 'f'],
                  'record_type':       [316, 'h'],
                  'processing_done':   [318, 'h'],
                  'reserved5':         [320, 'h'],
                  'ris_sweeps':        [322, 'h'],
                  'time_base':         [324, 'h'],
                  'vert_coupling':     [326, 'h'],
                  'probe_att':         [328, 'f'],
                  'fixed_vert_gain':   [332, 'h'],
                  'bandwidth_limit':   [334, 'h'],
                  'vertical_vernier':  [336, 'f'],
                  'acq_vert_offset':   [340, 'f'],
                  'wave_source':       [344, 'h']                  
                }
                
    
def read(fn, readdata=True, scale=True, fn_is_raw_string=False):    
    if fn_is_raw_string:
        raw = fn
    else:
        raw = open(fn, 'rb').read()
    
    startpos = raw.find(b'WAVEDESC')
    
    # read raw binary strings into metadata dictionary
    metadata = {}
    for field, val in lecroy_format.items():
        fieldlen = struct.Struct(val[1]).size
        metadata[field] = raw[startpos + val[0] : startpos + val[0] + fieldlen] 
            
    # byte order character, read from COMM_ORDER
    if struct.unpack('h', metadata['comm_order']) == 0:
        boc = '>'
    else:
        boc = '<'
    
    # unpack the binary values according to data types in lecroy_format
    for field, rawval in metadata.items():
        val = struct.unpack(boc + lecroy_format[field][1], rawval)
        if field != 'trigger_time':
            val = val[0]
        if lecroy_format[field][1][-1] == 's':
            val = val.strip(b'\x00')        
        metadata[field] = val
    
    # pretty format various metadata
    metadata['trigger_time'] = list(metadata['trigger_time'])[:-1]
    metadata['trigger_time'].reverse()
    metadata['record_type'] = (['single sweep',
                                'interleaved',
                                'histogram',
                                'graph',
                                'filter coefficient',
                                'complex',
                                'extrema',
                                'sequence obsolete',
                                'centered RIS',
                                'peak detect']
                               [metadata['record_type']])
    metadata['processing_done'] = (['no processing',
                                    'fir filter',
                                    'interpolated',
                                    'sparsed',
                                    'autoscaled',
                                    'no result',
                                    'rolling',
                                    'cumulative']
                                   [metadata['processing_done']])
    metadata['vert_coupling'] = (['DC 50 Ohm',
                                  'ground',
                                  'DC 1 MOhm',
                                  'ground',
                                  'AC 1 MOhm']
                                 [metadata['vert_coupling']])
    tb = metadata['time_base']
    if tb == 100:
        metadata['time_base'] = 'external'
    else:
        metadata['time_base'] = (str([1,2,5,10,20,50,100,200,500][tb%9]) + ' '
                                 + ['p','n','u','m','','k'][tb//9] + 's/div')
    fvt = metadata['fixed_vert_gain']
    metadata['fixed_vert_gain'] = (str([1,2,5,10,20,50,100,200,500][fvt%9]) + ' '
                                   + ['u','m','','k'][fvt//9] + 'V/div')
    
    
    if readdata:
        # read the trigger times into a NumPy array
        trigtimes_startpos = (startpos + metadata['wave_descriptor'] +
            metadata['user_text'])
        trigtimes = np.fromstring(raw[trigtimes_startpos:], dtype=np.float64, 
                                  count=int(metadata['trig_time_array']/8))
        trigtimes = trigtimes.reshape(2, -1, order='F')
        
        # number format for data. COMM_TYPE: 0 -> byte, 1 -> short
        number_type = np.int16 if metadata['comm_type'] else np.int8

        # read the binary data into a NumPy array
        data_startpos = trigtimes_startpos + metadata['trig_time_array']
        data = np.fromstring(raw[data_startpos:],
                             dtype=number_type,
                             count=metadata['wave_array_count'])
        
        # scale, offset and reshaping into segments
        if scale:
            data = data * metadata['vertical_gain'] + metadata['vertical_offset']
        
        data = data.reshape(metadata['subarray_count'], -1)
        
        return metadata, trigtimes, data
    else:
        return metadata
        
        
def pretty_metadata(metadata, filter=[]):
    """
    pretty_metadata(metadata, filter=[])
    ------------------------------------
    Pretty print a metadata dictionary.
    filter:  List of keys to print. If empty, all keys are printed.
             If 'main', selected useful entries are printed.
    """
    if filter == []:
        keys = metadata.keys()
    elif filter == 'main':
        keys = ['trigger_time', 'vert_coupling',
                'time_base', 'horiz_interval', 'horiz_offset',
                'fixed_vert_gain', 'vertical_gain', 'vertical_offset',
                'wave_array1', 'subarray_count']
    else:
        keys = filter
    
    for key in keys:
        print(key, (20-len(key))*' ', metadata[key])
    
    
