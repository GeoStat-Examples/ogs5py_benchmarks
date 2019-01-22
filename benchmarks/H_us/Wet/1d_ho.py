# -*- coding: utf-8 -*-
from ogs5py import OGS, RFR

model = OGS(
    task_root='1d_ho_root',
    task_id='1d_ho',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('1d_ho.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['RESTART', '1d_ho.rfr'],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DAT_TYPE='LIQUID',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4680.0],
    SPECIFIC_HEAT_CONDUCTIVITY=[1, 0.6],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='DEFAULT',
    GEO_TYPE=['POLYLINE', 'BANTNITE'],
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.41],
    TORTUOSITY=[1, 0.8],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2e-21],
    PERMEABILITY_SATURATION=[0, 2],
    CAPILLARY_PRESSURE=[0, 1],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='DEFAULT',
    GEO_TYPE=['POLYLINE', 'GRATNATE'],
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.01],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-17],
    PERMEABILITY_SATURATION=[4, 0.0, 1.0, 0.6],
    CAPILLARY_PRESSURE=[4, 0.006673469387755102],
)
model.msh.read_file('1d_ho.msh')
model.num.add_block(
    main_key='NUMERICS',
    METHOD=[],
    PCS_TYPE='PRESSURE1',
    NON_LINEAR_SOLVER=['PICARD', 0.001, 10, 0.0],
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    ELE_GAUSS_POINTS=3,
    ELE_MASS_LUMPING=1,
    ELE_UPWINDING=0.5,
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
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [8],
        [9],
        [10],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
    CPL_TYPE='PARTITIONED',
    TIM_TYPE='TRANSIENT',
)
model.rfd.read_file('1d_ho.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE='SYSTEM_DEPENDENT',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_UNIT='YEAR',
    TIME_START=0.0,
    TIME_END=10,
    TIME_CONTROL=[
        ['PI_AUTO_STEP_SIZE'],
        [1, 0.001, 1e-09, 0.01],
    ],
)
rfr_file = RFR(
    file_name='1d_ho',
    file_ext='.rfr',
)
rfr_file.read_file('1d_ho.rfr')
model.add_rfr(rfr_file)
model.write_input()
model.run_model()
