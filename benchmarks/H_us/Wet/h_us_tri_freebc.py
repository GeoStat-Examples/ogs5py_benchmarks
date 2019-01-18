# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='h_us_tri_freebc_root',
    task_id='h_us_tri_freebc',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('h_us_tri_freebc.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', -21500],
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
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.38],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 4.46e-13],
    PERMEABILITY_SATURATION=[
        [0, 2],
        [0, 2],
    ],
    CAPILLARY_PRESSURE=[0, 1],
)
model.msh.read_file('h_us_tri_freebc.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 100, 0.0],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=[
        [0.01],
        [0.1],
        [1.0],
        [180.0],
        [1800.0],
        [3600.0],
        [7200.0],
        [32400.0],
        [61200.0],
    ],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.01],
        [0.1],
        [1.0],
        [180.0],
        [1800.0],
        [3600.0],
        [7200.0],
        [32400.0],
        [61200.0],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.read_file('h_us_tri_freebc.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE='SYSTEM_DEPENDENT',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_STEPS=[620, 1000.0],
    TIME_END=61200.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
