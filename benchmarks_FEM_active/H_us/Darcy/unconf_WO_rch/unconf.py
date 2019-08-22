# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='unconf_root',
    task_id='unconf',
    output_dir='out',
)
model.msh.read_file('unconf.msh')
model.gli.read_file('unconf.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'right'],
    DIS_TYPE=[
        ['FUNCTION'],
        ['49050+-9810*z'],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'left'],
    DIS_TYPE=['CONSTANT', 8],
    PRESSURE_AS_HEAD=0,
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['GRADIENT', 6.5, 0, 9810],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    TORTUOSITY=[1, 1],
    POROSITY=[1, 0.3],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
    PERMEABILITY_SATURATION=10,
    CAPILLARY_PRESSURE=[10, 0.0001, 3000],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DENSITY=[1, 1000],
    VISCOSITY=[1, 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    LINEAR_SOLVER=[2, 1, 1e-12, 5000, 1, 100, 4],
    NON_LINEAR_ITERATION=['PICARD', 'ERNORM', 15, 0, 1e-08],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_END=1e+35,
    TIME_START=0.0,
    TIME_STEPS=[2, 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['SATURATION1'],
    ],
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'bottom'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
