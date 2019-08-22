# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='govin_line_root',
    task_id='govin_line',
    output_dir='out',
)
model.msh.read_file('govin_line.msh')
model.gli.read_file('govin_line.gli')
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
    GEO_TYPE=['POLYLINE', 'CHANNEL'],
    DIS_TYPE=['CONSTANT_NEUMANN', 0.004],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=[
        ['NORMALDEPTH', 1],
        [0.01, 0.0],
    ],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    SURFACE_FRICTION=[18.25, 0.5, 0.67],
    RILL=[0.0, 0.0],
    WIDTH=1.0,
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='OVERLAND_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-06, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['NEWTON', 1e-06, 1e-08, 100, 0.0],
    ELE_GAUSS_POINTS=2,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='OVERLAND_FLOW',
    TIME_STEPS=[240, 1],
    TIME_END=240,
    TIME_START=0.0,
    TIME_CONTROL=[],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['WDEPTH'],
        ['FLUX'],
    ],
    GEO_TYPE=['POINT', 'POINT0'],
    PCS_TYPE='OVERLAND_FLOW',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['WDEPTH'],
    ],
    PCS_TYPE='OVERLAND_FLOW',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.write_input()
model.run_model()
