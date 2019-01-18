# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='LF_Theis_root',
    task_id='LF_Theis',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'INIFINIT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('LF_Theis.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DENSITY=[1, 999.7026],
    VISCOSITY=[1, 0.001308],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    STORAGE=[1, 1.02e-07],
    PERMEABILITY_SATURATION=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.2391e-10],
)
model.msh.read_file('LF_Theis.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-14, 1000, 1.0, 100, 4],
    RENUMBER=[2, -1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='LIQUID_FLOW',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='LIQUID_FLOW',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POINT', 'OBS'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'WELL'],
    DIS_TYPE=['CONSTANT_NEUMANN', -0.002253],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[
        [10, 0.864],
        [10, 7.776],
        [10, 77.76],
        [10, 777.6],
        [10, 7776],
        [10, 77760],
    ],
    TIME_END=864000,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
