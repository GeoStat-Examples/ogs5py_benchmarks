# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='reaction_heat_root',
    task_id='reaction_heat',
    output_dir='out',
)
model.gli.read_file('reaction_heat.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='TNEQ',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='TNEQ',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 400.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='TNEQ',
    PRIMARY_VARIABLE='TEMPERATURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 400.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='TNEQ',
    PRIMARY_VARIABLE='CONCENTRATION1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.5],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='N2',
    TRANSPORT_PHASE=0,
    FLUID_PHASE=0,
    MOBILE=1,
    DIFFUSION=[1, 9.65e-05],
    MOL_MASS=0.028,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='H2O',
    TRANSPORT_PHASE=0,
    FLUID_PHASE=0,
    MOBILE=1,
    DIFFUSION=[1, 9.65e-05],
    MOL_MASS=0.018,
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='TNEQ',
    DENSITY=26,
    VISCOSITY=26,
    SPECIFIC_HEAT_CAPACITY=[1, 1000],
    HEAT_CONDUCTIVITY=11,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=0.0314,
    POROSITY=[1, 0.7],
    TORTUOSITY=[1, 1.0],
    MASS_DISPERSION=[1, 0.1, 0.01],
    PERMEABILITY_TENSOR=['ISOTROPIC', 6.94e-14],
    HEAT_TRANSFER=[2, 1, 1000.0],
    PARTICLE_DIAMETER=[1, 5e-05],
    INTERPHASE_FRICTION='FLUID',
)
model.msh.read_file('reaction_heat.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[
        [1, 1.0],
        ['CAPACITY:'],
        [1, 620.573],
        ['CONDUCTIVITY:'],
        [1, 0.4],
    ],
    REACTIVE_SYSTEM=[
        ['SINUSOIDAL'],
        [-500000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='TNEQ',
    REACTION_SCALING=1,
    LOCAL_PICARD1=[200, 1e-10],
    LINEAR_SOLVER=[2, 6, 1e-15, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 200, 1.0],
    NON_LINEAR_UPDATE_VELOCITY=1,
    ELE_GAUSS_POINTS=2,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['TEMPERATURE2'],
        ['CONCENTRATION1'],
    ],
    MFP_VALUES='DENSITY',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='TNEQ',
    TEMPERATURE_UNIT='KELVIN',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.read_file('reaction_heat.rfd')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='TNEQ',
    TIME_STEPS=[10000000, 0.001],
    TIME_END=1.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
