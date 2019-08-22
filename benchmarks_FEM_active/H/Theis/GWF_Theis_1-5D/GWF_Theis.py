# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='GWF_Theis_root',
    task_id='GWF_Theis',
    output_dir='out',
)
model.msh.read_file('GWF_Theis.msh')
model.gli.read_file('GWF_Theis.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
    PRIMARY_VARIABLE='HEAD',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'INIFINIT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'WELL'],
    DIS_TYPE=['CONSTANT_NEUMANN', -194.69],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1,
    STORAGE=[1, 0.001],
    PERMEABILITY_SATURATION=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.000929036],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 1.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-14, 1000, 1.0, 100, 4],
    RENUMBER=[2, -1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[
        [10, 1e-05],
        [10, 9e-05],
        [10, 0.0009],
        [10, 0.009],
        [10, 0.09],
        [10, 0.9],
    ],
    TIME_END=10,
    TIME_START=0.0,
    TIME_UNIT='DAY',
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='GROUNDWATER_FLOW',
    NOD_VALUES='HEAD',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='GROUNDWATER_FLOW',
    NOD_VALUES='HEAD',
    GEO_TYPE=['POINT', 'OBS'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
