# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='t_tri_root',
    task_id='t_tri',
    output_dir='out',
)
model.gli.read_file('t_tri.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
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
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.msh.read_file('t_tri.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[
        [1, 1.0],
        ['CAPACITY'],
        [1, 1.0],
        ['CONDUCTIVITY'],
        [1, 1.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=['petsc', 'bcgs', 'bjacobi', 1e-07, 2000, 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    NUM_TYPE='NEW',
)
model.rfd.read_file('t_tri.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'T'],
    DIS_TYPE=['CONSTANT_NEUMANN', 1.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[200, 0.005],
    TIME_END=1.0,
    TIME_START=0.0,
    TIME_UNIT='SECOND',
)
model.write_input()
model.run_model()
