# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='tm_01_3Du_root',
    task_id='tm_01_3Du',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'top'],
    DIS_TYPE=['CONSTANT', 308],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'bottom'],
    DIS_TYPE=['CONSTANT', 308],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'front'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'back'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'right'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'left'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'top'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'bottom'],
    DIS_TYPE=['CONSTANT', 0],
)
model.ddc.read_file('tm_01_3Du.ddc')
model.gli.read_file('tm_01_3Du.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 298],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 2200.0],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 0.9],
    HEAT_CONDUCTIVITY=[1, 5.5],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
)
model.msh.read_file('tm_01_3Du.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, -2200.0],
    ELASTICITY=[
        ['POISSION', 0.27],
        ['YOUNGS_MODULUS'],
        [1, 25000000000.0],
    ],
    THERMAL=[
        ['EXPANSION', 6e-06],
        ['CAPACITY'],
        [1, 1],
        ['CONDUCTIVITY'],
        [1, 1],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 1, 1e-12, 1000, 0.5, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 1, 1e-12, 1000, 0.5, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['TEMPERATURE1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[1, 900],
    TIME_END=360000,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[1, 900],
    TIME_END=360000,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
