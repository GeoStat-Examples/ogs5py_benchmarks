# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='conv_2D_axi_root',
    task_id='conv_2D_axi',
    output_dir='out',
)
model.gli.read_file('conv_2D_axi.gli')
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
    DIS_TYPE=['CONSTANT', 293],
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
    DENSITY=[1, 1.0],
    VISCOSITY=[1, 3e-05],
    SPECIFIC_HEAT_CAPACITY=[1, 1000.0],
    HEAT_CONDUCTIVITY=[1, 10.0],
    SPECIFIC_HEAT_SOURCE=500.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.01,
    POROSITY=[1, 0.8],
    TORTUOSITY=[1, 1.0],
    MASS_DISPERSION=[1, 0.1, 0.01],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    HEAT_TRANSFER=[2, 1, 0],
    PARTICLE_DIAMETER=[1, 5e-05],
    INTERPHASE_FRICTION='SOLID',
)
model.msh.read_file('conv_2D_axi.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 50],
        ['CONDUCTIVITY:'],
        [1, 0.2],
    ],
    REACTIVE_SYSTEM='INERT',
    SPECIFIC_HEAT_SOURCE=10.0,
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
    TIM_TYPE=['STEPS', 1000],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='TES',
    TEMPERATURE_UNIT='KELVIN',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.add_block(
    CURVE=[
        [0.0, 0.0],
        [5.0, 1.0],
        [100000, 1.0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='TES',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'WALL'],
    DIS_TYPE=['TRANSFER_SURROUNDING', 1.0, 293.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='TES',
    TIME_STEPS=[
        [2000, 0.02],
        [2000, 0.05],
        [1000, 0.1],
        [3000, 0.2],
        [1000, 0.5],
        [2000, 1.0],
        [2000, 2.0],
    ],
    TIME_END=5000,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
