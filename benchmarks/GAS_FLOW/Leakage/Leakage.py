# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='Leakage_root',
    task_id='Leakage',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=[
        ['LINEAR', 2],
        [5, 29114118],
        [0, 30754350],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'RIGHT'],
    DIS_TYPE=[
        ['LINEAR', 2],
        [4, 29114118],
        [1, 30754350],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT12'],
    DIS_TYPE=['CONSTANT', 318.15],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='CARBON1',
    GEO_TYPE=['POINT', 'POINT12'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE=['POINT', 'POINT12'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='CARBON1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='CARBON1',
    GEO_TYPE=['POLYLINE', 'RIGHT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='WATER1',
    GEO_TYPE=['POLYLINE', 'RIGHT'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.gli.read_file('Leakage.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['GRADIENT', 2840, 0, 10251.45],
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
    EOS_TYPE='CONSTANT',
    COMPRESSIBILITY=[
        [15, 0, 0],
        [15, 0, 0],
        [15, 0, 0],
    ],
    JTC='OFF',
    DENSITY=[15, 479, 1045],
    VISCOSITY=[15, 3.95e-05, 0.0002535],
    SPECIFIC_HEAT_CAPACITY=[15, 1000, 1000],
    HEAT_CONDUCTIVITY=[15, 0.025, 0.6],
    ISOTHERM=[1, 0, 0],
    DECAY=[1, 0, 0],
    DIFFUSION=[15, 0, 0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=30,
    POROSITY=[1, 0.15],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.9738466e-14],
    STORAGE=[1, 0.0],
    MASS_DISPERSION=[1, 5, 0.5],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=30,
    POROSITY=[1, 0.15],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.9738466e-14],
    STORAGE=[1, 0.0],
    MASS_DISPERSION=[1, 5, 0.5],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=0.0624561615,
    GEOMETRY_INCLINATION=90,
    POROSITY=[1, 0.15],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 9.869233e-13],
    STORAGE=[1, 0.0],
    MASS_DISPERSION=[1, 5, 0.5],
)
model.msh.read_file('Leakage.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 750],
        ['CONDUCTIVITY:'],
        [1, 3.5],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 750],
        ['CONDUCTIVITY:'],
        [1, 3.5],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 750],
        ['CONDUCTIVITY:'],
        [1, 3.5],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 0, 1e-15, 2500, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 25, 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['CARBON1'],
        ['WATER1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    MFP_VALUES=[
        ['DENSITY1'],
        ['VISCOSITY1'],
    ],
#    TIM_TYPE='TIME',
    GEO_TYPE=['POINT', 'OB'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TEMPERATURE_UNIT='KELVIN',
)
model.rfd.read_file('Leakage.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT12'],
    DIS_TYPE=['CONSTANT', 0.2956666666666667],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TIME_STEPS=[22, 579000],
    TIME_END=3110400,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
