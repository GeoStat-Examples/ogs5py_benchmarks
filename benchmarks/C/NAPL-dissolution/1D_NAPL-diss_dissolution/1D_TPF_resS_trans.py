# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='1D_TPF_resS_trans_root',
    task_id='1D_TPF_resS_trans',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='PCE',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCM',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.gli.read_file('1D_TPF_resS_trans.gli')
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
    PRIMARY_VARIABLE='SATURATION1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION1',
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT', 0.899997748],
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
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT', 0.100002252],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'LEFTPLINE'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='PCE',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='PCE',
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT', 0.532],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE',
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT', 4.478],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCM',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCM',
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT', 8.545],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_PCE',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_PCE',
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT', 122.14],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_TCE',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_TCE',
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT', 111.11],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_TCM',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='NAPL_TCM',
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT', 30.99],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=1,
    RELATIVE_ERROR=1e-06,
    MIN_TIMESTEP=1,
    INITIAL_TIMESTEP=1000,
    NO_REACTIONS=[
        ['POINT', 'POINT1'],
        ['POLYLINE', 'NOSOURCE'],
    ],
)
model.krc.add_block(
    main_key='BLOB_PROPERTIES',
    NAME='blob1',
    D50=0.001,
    CALC_SHERWOOD=[1.15, 0.654, 0.486],
    GEOMETRY=0.0,
    INTERFACIAL_AREA=[
        ['DOMAIN', 0],
        ['POINT', 'POINT17', 5000],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='PCE-dissolution',
    TYPE='NAPLdissolution',
    EQUATION=['NAPL_PCE', '=', '-', 'PCE'],
    NAPL_PROPERTIES=['blob1', 1.15, 9770.8],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='TCE-dissolution',
    TYPE='NAPLdissolution',
    EQUATION=['NAPL_TCE', '=', '-', 'TCE'],
    NAPL_PROPERTIES=['blob1', 10.65, 11111.1],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='TCM-dissolution',
    TYPE='NAPLdissolution',
    EQUATION=['NAPL_TCM', '=', '-', 'TCM'],
    NAPL_PROPERTIES=['blob1', 72.86, 12395.3],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='PCE',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
    MOLAR_DENSITY=9770.8,
    MOLAR_WEIGHT=0.16583,
    MAXIMUM_AQUEOUS_SOLUBILITY=1.15,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TCE',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
    MOLAR_DENSITY=11111.1,
    MOLAR_WEIGHT=0.13139,
    MAXIMUM_AQUEOUS_SOLUBILITY=10.65,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TCM',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
    MOLAR_DENSITY=12395.3,
    MOLAR_WEIGHT=0.1538227,
    MAXIMUM_AQUEOUS_SOLUBILITY=72.86,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='NAPL_PCE',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=3,
    MOLAR_DENSITY=9770.8,
    MOLAR_WEIGHT=0.16583,
    MAXIMUM_AQUEOUS_SOLUBILITY=1.15,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='NAPL_TCE',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=3,
    MOLAR_DENSITY=11111.1,
    MOLAR_WEIGHT=0.13139,
    MAXIMUM_AQUEOUS_SOLUBILITY=10.65,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='NAPL_TCM',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=3,
    MOLAR_DENSITY=12395.3,
    MOLAR_WEIGHT=0.1538227,
    MAXIMUM_AQUEOUS_SOLUBILITY=72.86,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Tracer',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 999.7],
    VISCOSITY=[1, 0.001307],
    PHASE_DIFFUSION=[1, 7.66e-10],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='SATURATION2',
    DENSITY=[1, 999.7],
    VISCOSITY=[1, 0.001307],
    PHASE_DIFFUSION=[1, 7.66e-10],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.25],
    VOL_BIO=[1, 0.0],
    VOL_MAT=[1, 0.75],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.54249e-11],
    PERMEABILITY_SATURATION=[
        [61, 0.2, 1.0, 3.86],
        [66, 0.2, 1.0, 3.86, 0.0],
    ],
    CAPILLARY_PRESSURE=[6, 0.0],
    MASS_DISPERSION=[1, 0.09, 1e-10],
    DENSITY=[1, 2650.0],
)
model.msh.read_file('1D_TPF_resS_trans.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='PS_GLOBAL',
    ELE_MASS_LUMPING=1,
    ELE_UPWINDING=[0, 1.0],
    LINEAR_SOLVER=[2, 1, 1e-10, 2000, 1.0, 1, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 15, 1.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['NAPL_PCE'],
        ['NAPL_TCE'],
        ['NAPL_TCM'],
        ['PCE'],
        ['TCE'],
        ['TCM'],
    ],
    GEO_TYPE=['POINT', 'POINT17'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='PS_GLOBAL',
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
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT4'],
    DIS_TYPE=['CONSTANT', -1.157405e-06],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.157405e-06],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='PS_GLOBAL',
    TIME_STEPS=[800, 43200.0],
    TIME_END=8.64e+22,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[3200, 10800.0],
    TIME_END=8.64e+22,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
