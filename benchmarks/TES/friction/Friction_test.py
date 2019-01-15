# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='Friction_test_root',
    task_id='Friction_test',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=[
        ['LINEAR', 2],
        [3, 150000.0],
        [0, 200000.0],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=[
        ['LINEAR', 2],
        [0, 200000.0],
        [1, 150000.0],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=[
        ['LINEAR', 2],
        [2, 100000.0],
        [3, 150000.0],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'RIGHT'],
    DIS_TYPE=[
        ['LINEAR', 2],
        [1, 150000.0],
        [2, 100000.0],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 573.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 573.0],
)
model.gli.read_file('Friction_test.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 573.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='CONCENTRATION1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
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
    PCS_TYPE='PRESSURE1',
    DENSITY=26,
    VISCOSITY=[1, 1e-05],
    SPECIFIC_HEAT_CAPACITY=[1, 1000],
    HEAT_CONDUCTIVITY=[1, 10.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.8],
    TORTUOSITY=[1, 1.0],
    MASS_DISPERSION=[1, 0.1, 0.01],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    HEAT_TRANSFER=[2, 1, 8000],
    PARTICLE_DIAMETER=[1, 5e-05],
    INTERPHASE_FRICTION='SOLID',
)
model.msh.read_file('Friction_test.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1.0],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1200],
        ['CONDUCTIVITY:'],
        [1, 0.4],
    ],
    REACTIVE_SYSTEM='INERT',
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='TES',
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
        ['CONCENTRATION1'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 10],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='TES',
    TEMPERATURE_UNIT='KELVIN',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='TES',
    TIME_STEPS=[
        [100, 1],
        [100, 10],
    ],
    TIME_END=500,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
