# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='h2_line_root',
    task_id='h2_line',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 195000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('h2_line.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 195000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.99],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='SATURATION2',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    POROSITY=[1, 0.3],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
    PERMEABILITY_SATURATION=[
        [6, 0.0, 1.0, 2.0],
        [66, 0.0, 1.0, 2.0, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 5000],
)
model.msh.read_file('h2_line.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='PRESSURE1',
    ELE_UPWINDING=[0.0, 1],
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[805, 6, 1e-10, 1000, 1, 2],
    NON_LINEAR_ITERATION=['PICARD', 'LMAX', 100, 0.0, 10.0, 0.0001],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['SATURATION2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=[
        [1000],
        [4000],
        [7000],
        [10000],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='PS_GLOBAL',
    NUM_TYPE='dPcdSwGradSnw',
)
model.rfd.read_file('h2_line.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='PS_GLOBAL',
    TIME_CONTROL=[
        ['PI_AUTO_STEP_SIZE'],
        [1, 0.0001, 1e-10, '10s'],
    ],
    TIME_END=10000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
