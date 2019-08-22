# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='Lauwerier_root',
    task_id='Lauwerier',
    output_dir='out',
)
model.msh.read_file('Lauwerier.msh')
model.gli.read_file('Lauwerier.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
    TIM_TYPE='STEADY',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    NUM_TYPE='NEW',
    MEMORY_TYPE=1,
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT4'],
    DIS_TYPE=['CONSTANT', 100000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-07],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=0.001,
    POROSITY=[1, 1],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-15],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 1],
        ['CONDUCTIVITY_TENSOR:'],
        ['ORTHOTROPIC', 3, 0, 0, 1],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 1],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4000],
    HEAT_CONDUCTIVITY=[1, 1e-08],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 2, 1e-16, 5000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 0, 1e-12, 1000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=2,
    NON_LINEAR_SOLVER=['PICARD', 0.001, 1, 0.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[250, 2000000.0],
    TIME_END=1e+99,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    GEO_TYPE=['POLYLINE', 'V2'],
    TIM_TYPE=[
        [50000000.0],
        [100000000.0],
        [150000000.0],
        [200000000.0],
        [250000000.0],
        [300000000.0],
        [350000000.0],
        [400000000.0],
        [450000000.0],
        [500000000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    GEO_TYPE=['POLYLINE', 'FRACTURE'],
    TIM_TYPE=[
        [50000000.0],
        [100000000.0],
        [150000000.0],
        [200000000.0],
        [250000000.0],
        [300000000.0],
        [350000000.0],
        [400000000.0],
        [450000000.0],
        [500000000.0],
    ],
)
model.write_input()
model.run_model()
