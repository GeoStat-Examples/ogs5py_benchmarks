# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='exp1_root',
    task_id='exp1',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT_RIGHT'],
    DIS_TYPE=['CONSTANT', 1000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'PLY_0'],
    DIS_TYPE=['CONSTANT', 1],
    TIM_TYPE=['CURVE', 1],
)
model.gli.read_file('exp1.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1000000.0],
)
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
    DENSITY=[6, 1000.0, 1000000.0, 4.6e-10, 25, -0.0002],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4280.0],
    HEAT_CONDUCTIVITY=[1, 0.6],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-15],
    TORTUOSITY=[1, 1.0],
)
model.msh.read_file('exp1.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2600],
    THERMAL=[
        ['EXPANSION', 1e-06],
        ['CAPACITY:'],
        [1, 860],
        ['CONDUCTIVITY:'],
        [1, 3],
    ],
    ELASTICITY=[
        ['POISSION', 0.35],
        ['YOUNGS_MODULUS:'],
        [1, 317000000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    ELE_GAUSS_POINTS=2,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 0, 2],
    COUPLING_CONTROL=['LMAX', 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    ELE_GAUSS_POINTS=2,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 0, 4],
    COUPLING_CONTROL=['LMAX', 0.001],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
    ],
    GEO_TYPE=['POINT', 'POINT_LEFT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
    ],
    GEO_TYPE=['POINT', 'POINT_RIGHT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
)
model.rfd.read_file('exp1.rfd')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[10, 86400],
    TIME_END=1e+99,
    TIME_START=0,
)
model.write_input()
model.run_model()
