# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='bhp_root',
    task_id='bhp',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 318.15],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='CARBON1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('bhp.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 6200000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 318.15],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='CARBON1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    COMPONENTS=[2, 'CARBON1', 'WATER1'],
    EOS_TYPE='VTPR',
    COMPRESSIBILITY=[
        [15],
        [15],
        [15],
    ],
    JTC='OFF',
    DENSITY=15,
    VISCOSITY=15,
    SPECIFIC_HEAT_CAPACITY=[1, 1000],
    HEAT_CONDUCTIVITY=[1, 0.6],
    ISOTHERM=[1, 0, 0],
    DECAY=[1, 0, 0],
    DIFFUSION=[15, 0, 0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=17,
    POROSITY=[1, 0.25],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 4.6e-14],
    STORAGE=[1, 0.0],
    MASS_DISPERSION=[1, 0, 0],
)
model.msh.read_file('bhp.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1200.0],
        ['CONDUCTIVITY:'],
        [1, 2.5],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 0, 1e-15, 2500, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 25, 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['CARBON1'],
        ['WATER1'],
    ],
    MFP_VALUES=[
        ['DENSITY1'],
        ['VISCOSITY1'],
        ['SPESIFIC_HEAT_CAPACITY1'],
        ['HEAT_CONDUCTIVITY1'],
    ],
    TIM_TYPE='TIME',
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TEMPERATURE_UNIT='KELVIN',
)
model.rfd.read_file('bhp.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TIME_STEPS=[1917, 36000],
    TIME_END=10000000000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
