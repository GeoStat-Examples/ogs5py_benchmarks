# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='h2t_line_root',
    task_id='h2t_line',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 5495000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'OUT'],
    DIS_TYPE=[
        ['LINEAR', 2],
        [0, 380],
        [1, 420],
    ],
)
model.gli.read_file('h2t_line.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 5495000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.99],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 420],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    FLUID_NAME='CO2',
    COMPRESSIBILITY=[
        [3, 1],
        [0],
        [0],
    ],
    DENSITY=12,
    VISCOSITY=9,
    SPECIFIC_HEAT_CAPACITY=[1, 1000],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    FLUID_NAME='METHANE',
    COMPRESSIBILITY=[
        [3, 1],
        [0],
        [0],
    ],
    DENSITY=12,
    VISCOSITY=9,
    SPECIFIC_HEAT_CAPACITY=[1, 1000],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    POROSITY=[1, 0.03],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-12],
    PERMEABILITY_SATURATION=[
        [6, 0.0, 1.0, 2.0],
        [66, 0.0, 1.0, 2.0, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 5000],
)
model.msh.read_file('h2t_line.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION'],
        [1, 0],
        ['CAPACITY'],
        [1, 100],
        ['CONDUCTIVITY'],
        [1, 1],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='PS_GLOBAL',
    ELE_UPWINDING=[0.0, 1],
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[805, 6, 1e-10, 1000, 0, 1, 2],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 50, 0.0],
    ELE_GAUSS_POINTS=2,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[805, 0, 1e-12, 1000, 0.0, 1, 4],
    ELE_GAUSS_POINTS=2,
    NON_LINEAR_SOLVER=['PICARD', 0.001, 50, 0.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['SATURATION2'],
        ['TEMPERATURE1'],
    ],
    MFP_VALUES=[
        ['DENSITY1'],
        ['VISCOSITY1'],
        ['DENSITY2'],
        ['VISCOSITY2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1],
        [1000],
        [2000],
        [3000],
        [4000],
        [5000],
        [6000],
        [7000],
        [8000],
        [9000],
        [10000],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='PS_GLOBAL',
    NUM_TYPE='dPcdSwGradSnw',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
)
model.rfd.read_file('h2t_line.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='PS_GLOBAL',
    TIME_STEPS=[
        [50, 0.1],
        [45, 1],
        [50, 2],
        [70, 5],
        [150, 10],
        [100, 20],
        [60, 100],
    ],
    TIME_END=10001,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[
        [50, 0.1],
        [45, 1],
        [50, 2],
        [70, 5],
        [150, 10],
        [100, 20],
        [60, 100],
    ],
    TIME_END=10001,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
