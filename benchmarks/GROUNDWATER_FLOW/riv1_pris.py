# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='riv1_pris_root',
    task_id='riv1_pris',
    output_dir='out',
)
model.msh.read_file('riv1_pris.msh')
model.gli.read_file('riv1_pris.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'BCoben'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'BCunten'],
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'Channel'],
    DIS_TYPE=[
        ['RIVER', 2],
        [0, 4, 1e-06, 20.0, 1.0, 0.7],
        [3, 4, 1e-06, 20.0, 1.0, 0.7],
    ],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    GEO_TYPE='DOMAIN',
    POROSITY=[1, 0.2],
    STORAGE=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.025],
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
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 1, 1e-10, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-10, 100, 0.0],
    ELE_GAUSS_POINTS=2,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[30, 60],
    TIME_END=1800,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='HEAD',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='HEAD',
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.write_input()
model.run_model()
