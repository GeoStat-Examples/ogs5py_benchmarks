# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='TCE_10C_new_root',
    task_id='TCE_10C_new',
    output_dir='out',
)
model.msh.read_file('TCE_10C_new.msh')
model.gli.read_file('TCE_10C_new.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='PS_GLOBAL',
    NUM_TYPE='NEW',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 98100.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-15],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 283.15],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 283.15],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 98067],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE=['POLYLINE', 'NAPL_SOURCE_ZONE'],
    DIS_TYPE=['CONSTANT', 0.05],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION1',
    GEO_TYPE=['POLYLINE', 'NAPL_SOURCE_ZONE'],
    DIS_TYPE=['CONSTANT', 0.95],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-15],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_TCE',
    GEO_TYPE=['POLYLINE', 'NAPL_SOURCE_ZONE'],
    DIS_TYPE=['CONSTANT', 194.44425],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE',
    GEO_TYPE=['POLYLINE', 'NAPL_SOURCE_ZONE'],
    DIS_TYPE=['CONSTANT', 12.065],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_TCE',
    GEO_TYPE=['POLYLINE', 'CLEAN2'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_TCE',
    GEO_TYPE=['POLYLINE', 'CLEAN'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'Modellgebiet'],
    DIS_TYPE=['CONSTANT', 283.15],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT_NEUMANN', -9.54861e-07],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.35],
    VOL_BIO=[1, 0.0],
    VOL_MAT=[1, 0.65],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.54249e-11],
    PERMEABILITY_SATURATION=[
        [61, 0.2, 1.0, 3.86],
        [66, 0.2, 1.0, 3.86, 0.0],
    ],
    CAPILLARY_PRESSURE=[6, 0.0],
    MASS_DISPERSION=[1, 0.1],
    DENSITY=[1, 2650.0],
    HEAT_DISPERSION=[1, 1.0, 1.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650],
    THERMAL=[
        ['EXPANSION'],
        [1, 0.0],
        ['CAPACITY'],
        [1, 2500],
        ['CONDUCTIVITY'],
        [1, 2.4],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 999.7],
    VISCOSITY=[1, 0.001307],
    PHASE_DIFFUSION=[2, -1.4642, -1055.1],
    THERMAL=[
        ['CAPACITY'],
        [1, 4192.0],
        ['CONDUCTIVITY'],
        [1, 0.587],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='SATURATION2',
    DENSITY=[1, 1464.0],
    VISCOSITY=[1, 0.00055],
    PHASE_DIFFUSION=[1, 6.45e-10],
    THERMAL=[
        ['CAPACITY'],
        [1, 4192.0],
        ['CONDUCTIVITY'],
        [1, 0.587],
    ],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TCE',
    MOBILE=1,
    DIFFUSION=[1, 3.5e-08],
    TRANSPORT_PHASE=0,
    MOLAR_DENSITY=11111.1,
    MOLAR_WEIGHT=0.13139,
    MAXIMUM_AQUEOUS_SOLUBILITY=120.065,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='NAPL_TCE',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=3,
    MOLAR_DENSITY=11111.1,
    MOLAR_WEIGHT=0.13139,
    MAXIMUM_AQUEOUS_SOLUBILITY=120.065,
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=1,
    RELATIVE_ERROR=1e-06,
    MIN_TIMESTEP=1.0,
    INITIAL_TIMESTEP=1000.0,
    NO_REACTIONS=[
        ['POLYLINE', 'CLEAN'],
        ['POLYLINE', 'CLEAN2'],
    ],
)
model.krc.add_block(
    main_key='BLOB_PROPERTIES',
    NAME='blob1',
    D50=0.001,
    CALC_SHERWOOD=[1.15, 0.654, 0.486],
    GEOMETRY=0.66,
    INTERFACIAL_AREA=[
        ['DOMAIN', 0],
        ['POLYLINE', 'NAPL_SOURCE_ZONE', 636.3636],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='TCE-dissolution',
    TYPE='NAPLdissolution',
    EQUATION=['NAPL_TCE', '=', '-', 'TCE'],
    NAPL_PROPERTIES=['blob1', 120.065, 11111.1],
)
model.rei.add_block(
    main_key='REACTION_INTERFACE',
    TEMPERATURE='VARIABLE',
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='PS_GLOBAL',
    ELE_MASS_LUMPING=1,
    ELE_UPWINDING=[0, 1.0],
    LINEAR_SOLVER=[2, 1, 1e-10, 2000, 1.0, 1, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-10, 1000, 1.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 1, 1e-10, 1000, 1.0, 1, 4],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='PS_GLOBAL',
    TIME_STEPS=[2000, 43200.0],
    TIME_END=8.64e+24,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[2000, 43200.0],
    TIME_END=2.16e+21,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[2000, 43200.0],
    TIME_END=8.64e+24,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
        ['TCE'],
        ['NAPL_TCE'],
        ['TEMPERATURE1'],
    ],
    GEO_TYPE=['POLYLINE', 'Modellgebiet'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 200],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='TCE',
    GEO_TYPE=['POINT', 'POINT6'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 200],
)
model.write_input()
model.run_model()
