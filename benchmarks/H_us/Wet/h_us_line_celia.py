# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='h_us_line_celia_root',
    task_id='h_us_line_celia',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', -97893.474],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', -7342.0106],
)
model.gli.read_file('h_us_line_celia.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', -97893.474],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.368],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 9.35247e-12],
    PERMEABILITY_SATURATION=[4, 0.2772, 1.0, 0.5],
    CAPILLARY_PRESSURE=[4, 3.35],
)
model.msh.read_file('h_us_line_celia.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 10, 0.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=[
        [0.001],
        [0.01],
        [0.3],
        [0.35],
        [0.4],
        [1.0],
        [1800.0],
        [3600.0],
        [10800.0],
        [21600.0],
    ],
    DAT_TYPE='TECPLOT',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.read_file('h_us_line_celia.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_END=21600.0,
    TIME_START=0.0,
    TIME_STEPS=[
        [100, 0.001],
        [100, 0.01],
        [1000, 0.1],
        [1000, 1.0],
        [35000, 10.0],
        [100000, 20.0],
    ],
)
model.write_input()
model.run_model()
