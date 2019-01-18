# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS, RFR

model = OGS(
    task_root='Transient_root',
    task_id='Transient',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', -31800],
)
model.gli.read_file('Transient.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['RESTART', 'Transient.rfr'],
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
    NAME=['Bretsch', 'Oberboden', 'lS'],
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.406],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 8.36e-14],
    PERMEABILITY_SATURATION=[0, 9],
    CAPILLARY_PRESSURE=[0, 8],
    MASS_DISPERSION=[1, 0.1, 0.01],
)
model.msh.read_file('Transient.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 50, 0.0],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=['STEPS', 48],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POINT', 'POINT10'],
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POINT', 'POINT8'],
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POINT', 'POINT6'],
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POINT', 'POINT4'],
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POINT', 'POINT0'],
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.read_file('Transient.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT10'],
    DIS_TYPE=['CONSTANT', 1],
    TIM_TYPE=['CURVE', 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_UNIT='HOUR',
    TIME_START=0.0,
    TIME_END=2880,
    TIME_STEPS=[
        [2880, 0.5],
        [3000, 1],
    ],
)
rfr_file = RFR(
    file_name='Transient',
    file_ext='.rfr',
)
rfr_file.read_file('Transient.rfr')
model.add_rfr(rfr_file)
model.write_input()
model.run_model()
