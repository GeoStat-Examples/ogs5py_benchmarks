# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='TDiff-Wall_root',
    task_id='TDiff-Wall',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 25.0],
)
model.gli.read_file('TDiff-Wall.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 25],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.0],
    SPECIFIC_HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='DEFAULT',
    GEO_TYPE='DOMAIN',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
)
model.msh.read_file('TDiff-Wall.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[
        [1, 2000.0],
        ['CAPACITY'],
        [1, 900],
        ['CONDUCTIVITY'],
        [1, 5.5],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='HEAT_TRANSPORT',
    NOD_VALUES='TEMPERATURE1',
    ELE_VALUES=[],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=['STEPS', 50],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 30.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[
        [600, 1000],
        [1000, 100000],
    ],
    TIME_END=1e+99,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
