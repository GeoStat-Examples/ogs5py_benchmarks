# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='Wool_quad_root',
    task_id='Wool_quad',
    output_dir='out',
)
model.msh.read_file('Wool_quad.msh')
model.gli.read_file('Wool_quad.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='OVERLAND_FLOW',
    NUM_TYPE='NEW',
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-06],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'UP'],
    DIS_TYPE=['CONSTANT_NEUMANN', 6.944e-05],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'EAST'],
    DIS_TYPE=[
        ['CRITICALDEPTH', 1],
        [0.001],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'UP'],
    DIS_TYPE=[
        ['GREEN_AMPT', 1],
        [0.13, 2.3e-05, 6.944e-05, 0.344],
    ],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    SURFACE_FRICTION=[430000, 1.0, 2.0],
    RILL=[0.001, 0.0001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 756.0],
    VISCOSITY=[1, 0.00147],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='OVERLAND_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['NEWTON', 1e-05, 1e-08, 100, 0.0],
    ELE_GAUSS_POINTS=2,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='OVERLAND_FLOW',
    TIME_STEPS=[450, 2],
    TIME_END=900,
    TIME_START=0.0,
    TIME_CONTROL=[],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES='FLUX',
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.gli_ext.add(
    name='TIN_UP',
    file_ext='.tin',
)
model.gli_ext.read_file('TIN_UP.tin')
model.write_input()
model.run_model()
