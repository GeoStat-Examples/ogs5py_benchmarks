# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='2pf_2pt_root',
    task_id='2pf_2pt',
    output_dir='out',
)
model.msh.read_file('2pf_2pt.msh')
model.gli.read_file('2pf_2pt.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
    USE_PRECALCULATED_FILES=[],
    SAVE_ECLIPSE_DATA_FILES=[],
    SIMULATOR='ECLIPSE',
    SIMULATOR_PATH='C:\ecl\2012.1\bin\pc_x86_64\eclipse.exe',
    SIMULATOR_MODEL_PATH='./eclipse/ECL.DATA',
    ELEMENT_MATRIX_OUTPUT=0,
    ST_RHS=1,
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
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'PLY_Outflow_6'],
    DIS_TYPE=['CONSTANT', 24822500],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_Outflow_6'],
    DIS_TYPE=['CONSTANT', 5000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'PLY_Outflow_1'],
    DIS_TYPE=['CONSTANT', 24616490],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_Outflow_1'],
    DIS_TYPE=['CONSTANT', 5000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2tracer',
    GEO_TYPE=['POLYLINE', 'PLY_Injection_1'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2tracer',
    GEO_TYPE=['POLYLINE', 'PLY_Injection_2'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 5000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 24616490],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Wassertracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Wassertracer',
    GEO_TYPE=['POLYLINE', 'PLY_Tracer'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2tracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2tracer',
    GEO_TYPE=['POLYLINE', 'PLY_Tracer'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'PLY_Injection_1'],
    EPSILON=1e-08,
    DIS_TYPE=['CONSTANT', 1.90476e-07],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'PLY_Injection_2'],
    EPSILON=1e-08,
    DIS_TYPE=['CONSTANT', 1.90476e-07],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT0'],
    EPSILON=1e-08,
    DIS_TYPE=['CONSTANT', -9.52381e-08],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT5'],
    EPSILON=1e-08,
    DIS_TYPE=['CONSTANT', -9.52381e-08],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT6'],
    EPSILON=1e-08,
    DIS_TYPE=['CONSTANT', -9.52381e-08],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT11'],
    EPSILON=1e-08,
    DIS_TYPE=['CONSTANT', -9.52381e-08],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ORTHOTROPIC', 2e-13, 2e-13, 2e-14],
    PERMEABILITY_SATURATION=[
        [6, 0.25, 0.975, 2.0],
        [66, 0.025, 0.75, 2.0, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 5000],
    MASS_DISPERSION=[1, 0.5, 0.5],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650.0],
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
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Wassertracer',
    MOBILE=1,
    TRANSPORT_PHASE=0,
    DIFFUSION=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO2tracer',
    MOBILE=1,
    TRANSPORT_PHASE=10,
    DIFFUSION=[1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 6, 1e-10, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 25, 1.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-15, 2000, 1.0, 1, 2],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_STEPS=[100, 43200],
    TIME_END=4320000,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100, 43200],
    TIME_END=4320000,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['SATURATION2'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
        ['Wassertracer'],
        ['CO2tracer'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['SATURATION2'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
        ['Wassertracer'],
        ['CO2tracer'],
    ],
    GEO_TYPE=['POINT', 'POINT16'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['SATURATION2'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
        ['Wassertracer'],
        ['CO2tracer'],
    ],
    GEO_TYPE=['POINT', 'POINT17'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.asc.add(
    name='2pf_2pt_MASS_TRANSPORT_BC_ST',
    file_ext='.asc',
)
model.asc.read_file('2pf_2pt_MASS_TRANSPORT_BC_ST.asc')
model.write_input()
model.run_model()
