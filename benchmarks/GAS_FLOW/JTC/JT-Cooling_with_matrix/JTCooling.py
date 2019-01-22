# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='JTCooling_root',
    task_id='JTCooling',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='AIR_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 7000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 120],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CH4',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='N2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.gli.read_file('JTCooling.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='AIR_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 4000000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 120],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CH4',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='N2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO2',
    TRANSPORT_PHASE=0,
    FLUID_PHASE=0,
    MOL_MASS=44.0,
    CRITICAL_PRESSURE=7382000.0,
    CRITICAL_TEMPERATURE=304.2,
    CRITICAL_VOLUME=92.28,
    CRITICAL_DENSITY=467.6,
    ACENTRIC_FACTOR=0.228,
    COMP_CAPACITY=1750.0,
    COMP_CONDUCTIVITY=0.0255,
    MOBILE=1,
    DIFFUSION=[1, 9.65e-06],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CH4',
    TRANSPORT_PHASE=0,
    FLUID_PHASE=0,
    MOL_MASS=16.0,
    CRITICAL_PRESSURE=4604000.0,
    CRITICAL_TEMPERATURE=190.6,
    CRITICAL_VOLUME=97.56,
    CRITICAL_DENSITY=162.66,
    ACENTRIC_FACTOR=0.011,
    COMP_CAPACITY=2600.0,
    COMP_CONDUCTIVITY=0.0255,
    MOBILE=1,
    DIFFUSION=[1, 2e-05],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='N2',
    TRANSPORT_PHASE=0,
    FLUID_PHASE=0,
    MOL_MASS=46.0,
    CRITICAL_PRESSURE=3394000.0,
    CRITICAL_TEMPERATURE=126.1,
    CRITICAL_VOLUME=249.14,
    CRITICAL_DENSITY=313.3,
    ACENTRIC_FACTOR=0.04,
    COMP_CAPACITY=1100.0,
    COMP_CONDUCTIVITY=0.048,
    MOBILE=1,
    DIFFUSION=[1, 1.78e-05],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=14,
    VISCOSITY=[1, 1.9836e-05],
    SPECIFIC_HEAT_CAPACITY=[1, 1067.0],
    HEAT_CONDUCTIVITY=[1, 0.0255],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.225],
    TORTUOSITY=[1, 0.6082],
    DIFFUSION=273,
    PERMEABILITY_TENSOR=['ISOTROPIC', 9.748e-14],
    MASS_DISPERSION=[1, 10, 1],
)
model.msh.read_file('JTCooling.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2460.0],
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
    PCS_TYPE='AIR_FLOW',
    LINEAR_SOLVER=[2, 6, 1e-15, 100, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 10, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-15, 100, 1, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 10, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-15, 100, 1, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 10, 0.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['CO2'],
        ['CH4'],
        ['N2'],
    ],
    MFP_VALUES=[
        ['DENSITY1'],
        ['VISCOSITY1'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['CO2'],
        ['CH4'],
        ['N2'],
    ],
    TIM_TYPE='TIME',
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='AIR_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='AIR_FLOW',
    TIME_STEPS=[
        [1, 1],
        [1, 59],
        [1, 3540],
        [1, 82800],
        [1, 2505600],
        [5, 28944000],
    ],
    TIME_END=1000000000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[
        [1, 1],
        [1, 59],
        [1, 3540],
        [1, 82800],
        [1, 2505600],
        [5, 28944000],
    ],
    TIME_END=1000000000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[
        [1, 1],
        [1, 59],
        [1, 3540],
        [1, 82800],
        [1, 2505600],
        [5, 28944000],
    ],
    TIME_END=1000000000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
