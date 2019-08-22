# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='advdiffsorption_root',
    task_id='advdiffsorption',
    output_dir='out',
)
model.msh.read_file('advdiffsorption.msh')
model.gli.read_file('advdiffsorption.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TEMPERATURE_UNIT='KELVIN',
)
model.rfd.read_file('advdiffsorption.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT_NUEMANN', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 1],
)
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
    DIS_TYPE=['CONSTANT', 318.15],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 2],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-14],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 960],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    COMPONENTS=[1, 'WATER1'],
    EOS_TYPE='CONSTANT',
    COMPRESSIBILITY=[
        [1, 0],
        [1, 0],
        [1, 0],
    ],
    JTC='OFF',
    DENSITY=[1, 30],
    VISCOSITY=[1, 1e-05],
    SPECIFIC_HEAT_CAPACITY=[1, 1000],
    HEAT_CONDUCTIVITY=[1, 0.6],
    ISOTHERM=[1, 0.0001],
    DECAY=[1, 0.0],
    DIFFUSION=[1, 1e-06],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 0, 1e-15, 2000, 1, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 25, 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TIME_STEPS=[360, 86400],
    TIME_END=248832000,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    NOD_VALUES=[
        ['WATER1'],
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    TIM_TYPE='TIME',
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    NOD_VALUES=[
        ['WATER1'],
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    TIM_TYPE='TIME',
    GEO_TYPE=['POINT', 'POINT3'],
    DAT_TYPE='TECPLOT',
)
model.write_input()
model.run_model()
