# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='CO2phase_gen_E100_root',
    task_id='CO2phase_gen_E100',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LINE_0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'LINE_0'],
    DIS_TYPE=['CONSTANT', 20702300],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LINE_1'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'LINE_1'],
    DIS_TYPE=['CONSTANT', 20706420.2],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LINE_2'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'LINE_2'],
    DIS_TYPE=['CONSTANT', 20710540.4],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LINE_3'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'LINE_3'],
    DIS_TYPE=['CONSTANT', 20714660.6],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LINE_4'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'LINE_4'],
    DIS_TYPE=['CONSTANT', 20718780.8],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LINE_5'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'LINE_5'],
    DIS_TYPE=['CONSTANT', 20722901],
)
model.gli.read_file('CO2phase_gen_E100.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Bac',
    GEO_TYPE=['POINT', 'POINT26'],
    DIS_TYPE=['CONSTANT', 1],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Bac',
    GEO_TYPE=['POINT', 'POINT27'],
    DIS_TYPE=['CONSTANT', 1],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='C(4)',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=1,
    REALATIVE_ERROR=1e-06,
    MIN_TIMESTEP=1e-14,
    MAX_TIMESTEP=1000.0,
    INITIAL_TIMESTEP=0.001,
    ALLOW_REACTIONS=[
        ['POINT', 'POINT26'],
        ['POINT', 'POINT27'],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='SimpleFirstOrder',
    TYPE='monod',
    BACTERIANAME='Bac',
    RATECONSTANT=[0.1, 1.0],
    GROWTH=0,
    MONODTERMS=['C(4)', 1e-10, 0.0],
    INHIBITIONTERMS=[],
    PRODUCTIONSTOCH=['C(4)', 1000.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Bac',
    MOBILE=0,
    TRANSPORT_PHASE=0,
    DIFFUSION=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='C(4)',
    MOBILE=0,
    TRANSPORT_PHASE=0,
    DIFFUSION=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='C(4)_gas',
    MOBILE=0,
    TRANSPORT_PHASE=3,
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[18, 0],
    VISCOSITY=[1, 0.00051],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='PRESSURE2',
    DENSITY=[18, 0],
    VISCOSITY=[1, 5.5e-05],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    VOL_BIO=[1, 0.0],
    VOL_MAT=[1, 0.5],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2e-13],
    PERMEABILITY_SATURATION=[
        [3, 0.3, 0.6, 1.0, 1.0],
        [33, 0.4, 0.7, 1.0, 1.0],
    ],
    CAPILLARY_PRESSURE=[0, 1],
    DENSITY=[1, 1800.0],
)
model.msh.read_file('CO2phase_gen_E100.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 25, 1.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 0.5, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['SATURATION2'],
        ['Bac'],
        ['C(4)'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    ELE_VALUES='VELOCITY1_X',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
    USE_PRECALCULATED_FILES=[],
    SAVE_ECLIPSE_DATA_FILES=[],
    SIMULATOR='ECLIPSE',
    SIMULATOR='C:\ecl\2012.1\bin\pc_x86_64\eclipse.exe',
    SIMULATOR='./eclipse/ECL.DATA',
    ELEMENT_MATRIX_OUTPUT=0,
    ST_RHS=1,
    BOUNDARY_CONDITION_OUTPUT=[],
    DISSOLVED_CO2_PCS_NAME='C(4)',
    DISSOLVED_CO2_INGAS_PCS_NAME='C(4)_gas',
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
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.rfd.add_block(
    PROJECT=['Buckley-Leverett', 'benchmark', 'one.', 'Prepared', 'by', 'WW'],
)
model.rfd.add_block(
    CURVE=[
        [0.3, 30000],
        [1, 0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_STEPS=[50, 1],
    TIME_END=50.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[50, 1],
    TIME_END=50.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
