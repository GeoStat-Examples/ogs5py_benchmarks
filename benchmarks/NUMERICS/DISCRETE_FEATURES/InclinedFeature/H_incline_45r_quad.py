# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='H_incline_45r_quad_root',
    task_id='H_incline_45r_quad',
    output_dir='out',
)
model.msh.read_file('H_incline_45r_quad.msh')
model.gli.read_file('H_incline_45r_quad.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 2000000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT_NEUMANN', 0.0002],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.1,
    POROSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.0003],
    SPECIFIC_HEAT_CAPACITY=[1, 4000],
    HEAT_CONDUCTIVITY=[1, 0.6],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 1, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-10, 1000, 0.0],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_END=630720000,
    TIME_START=0,
    TIME_STEPS=[1, 5184000],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    GEO_TYPE=['POLYLINE', 'PLY_1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
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
model.write_input()
model.run_model()
