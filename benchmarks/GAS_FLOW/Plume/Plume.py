# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='Plume_root',
    task_id='Plume',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    DIS_TYPE=['CONSTANT', 101325],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT3'],
    DIS_TYPE=['CONSTANT', 101325],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE=['POINT', 'POINT4'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.gli.read_file('Plume.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 101325],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 313.15],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    COMPONENTS=[1, 'WATER1'],
    EOS_TYPE='CONSTANT',
    COMPRESSIBILITY=[
        [1, 0],
        [1, 0],
        [1, -0.01865],
    ],
    JTC='OFF',
    DENSITY=[14, 1019, 101325, 0, 0.0, -0.01865],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 1000],
    HEAT_CONDUCTIVITY=[1, 0.6],
    ISOTHERM=[1, 0],
    DECAY=[1, 0],
    DIFFUSION=[1, 1.477e-09],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.39],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.120795e-09],
    MASS_DISPERSION=[1, 0.0005, 5e-05],
)
model.msh.read_file('Plume.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 2.5],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 0, 1e-15, 2500, 1, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 25, 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['WATER1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
    ],
    MFP_VALUES='DENSITY',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [40],
        [68],
        [410],
        [726],
        [1426],
        [2672],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TEMPERATURE_UNIT='KELVIN',
)
model.rfd.read_file('Plume.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT4'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 2],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TIME_STEPS=[8, 10],
    TIME_END=30000,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
