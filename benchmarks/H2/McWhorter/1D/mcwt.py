# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='mcwt_root',
    task_id='mcwt',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 5000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 200000.0],
)
model.gli.read_file('mcwt.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 50000.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.3],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
    PERMEABILITY_SATURATION=[
        [6, 0.0, 1.0, 2],
        [66, 0.0, 1.0, 2, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 5000],
)
model.msh.read_file('mcwt.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    ELE_UPWINDING=[0, 1.0],
    LINEAR_SOLVER=[2, 1, 1e-12, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 1000, 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE=['POLYLINE', 'Profile'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [500],
        [1000],
        [2000],
        [4000],
        [7000],
        [10000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [500],
        [1000],
        [2000],
        [4000],
        [7000],
        [10000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE=['POINT', 'POINT0'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.add_block(
    PROJECT=['Buckley-Leverett', 'benchmark', 'one.', 'Prepared', 'by', 'WW'],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 50990.2],
        [0.025, 36055.51],
        [0.05, 29439.2],
        [0.075, 25495.1],
        [0.1, 22803.51],
        [0.125, 20816.66],
        [0.15, 19272.48],
        [0.175, 18027.76],
        [0.2, 16996.73],
        [0.225, 16124.52],
        [0.25, 15374.12],
        [0.275, 14719.6],
        [0.3, 14142.14],
        [0.325, 13627.7],
        [0.35, 13165.61],
        [0.375, 12747.55],
        [0.4, 12366.94],
        [0.425, 12018.5],
        [0.45, 11697.95],
        [0.475, 11401.75],
        [0.5, 11126.97],
        [0.525, 10871.15],
        [0.55, 10632.19],
        [0.575, 10408.33],
        [0.6, 10408.33],
        [0.625, 10408.33],
        [0.65, 10408.33],
        [0.675, 10408.33],
        [0.7, 10408.33],
        [0.725, 10408.33],
        [0.75, 10408.33],
        [0.775, 10408.33],
        [0.8, 10000.0],
        [0.825, 10000.0],
        [0.85, 10000.0],
        [0.875, 10000.0],
        [0.9, 10000.0],
        [0.925, 10000.0],
        [0.95, 10000.0],
        [0.975, 10000.0],
        [1.0, 10000.0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_CONTROL=[
        ['PI_AUTO_STEP_SIZE'],
        [1, 0.0001, 1e-10, 10],
    ],
    TIME_END=10000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
