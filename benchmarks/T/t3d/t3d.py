# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='t3d_root',
    task_id='t3d',
    output_dir='out',
)
model.msh.read_file('t3d.msh')
model.gli.read_file('t3d.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'SURF_0'],
    DIS_TYPE=['CONSTANT', 308.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'SURF_1'],
    DIS_TYPE=['CONSTANT', 308.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'SURF_2'],
    DIS_TYPE=['CONSTANT', 308.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'SURF_3'],
    DIS_TYPE=['CONSTANT', 308.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 298.15],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1.0],
    ELASTICITY=[
        ['POISSION', 0.27],
        ['YOUNGS_MODULUS'],
        [1, 25000000000.0],
    ],
    THERMAL=[
        ['EXPANSION', 6e-06],
        ['CAPACITY'],
        [1, 1.0],
        ['CONDUCTIVITY'],
        [1, 1.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1.0],
    ELASTICITY=[
        ['POISSION', 0.27],
        ['YOUNGS_MODULUS'],
        [1, 25000000000.0],
    ],
    THERMAL=[
        ['EXPANSION', 6e-06],
        ['CAPACITY'],
        [1, 1.0],
        ['CONDUCTIVITY'],
        [1, 1.0],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 0.0],
    SPECIFIC_HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 1, 1e-10, 3000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=2,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[10, 0.1],
    TIME_END=10,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT12'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 2],
)
model.write_input()
model.run_model()
