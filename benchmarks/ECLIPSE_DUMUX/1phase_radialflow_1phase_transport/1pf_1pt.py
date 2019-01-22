# -*- coding: utf-8 -*-
from ogs5py import OGS, ASC

model = OGS(
    task_root='1pf_1pt_root',
    task_id='1pf_1pt',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_LEFT_HIGH'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 480690],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_LEFT_LOW'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 490500],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_RIGHT_HIGH'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 480690],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_RIGHT_LOW'],
    EPSILON=1e-05,
    DIS_TYPE=['CONSTANT', 490500],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_UP_HIGH'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 480690],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_UP_LOW'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 490500],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_LOW_HIGH'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 480690],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_LOW_LOW'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 490500],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POINT', 'POINT4'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POINT', 'POINT10'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POINT', 'POINT12'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POINT', 'POINT13'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POINT', 'POINT14'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POINT', 'POINT15'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POINT', 'POINT16'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POINT', 'POINT17'],
    EPSILON=0.0002,
    DIS_TYPE=['CONSTANT', 1.0],
)
model.gli.read_file('1pf_1pt.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 480690],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='ConsTracer',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.3],
    VOL_BIO=[1, 0.01],
    VOL_MAT=[1, 0.69],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.17982e-11],
    MASS_DISPERSION=[1, 10, 10],
    DENSITY=[1, 2000.0],
)
model.msh.read_file('1pf_1pt.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 1, 1e-15, 20000, 1.0, 100, 4],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-15, 2000, 1.0, 1, 2],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['ConsTracer'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 20],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['ConsTracer'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
    ],
    GEO_TYPE=['POLYLINE', 'PLY_OUTPUT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 20],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
    TIM_TYPE='STEADY',
    USE_PRECALCULATED_FILES=[],
    SAVE_ECLIPSE_DATA_FILES=[],
    SIMULATOR='ECLIPSE',
    SIMULATOR_PATH='C:\ecl\2012.1\bin\pc_x86_64\eclipse.exe',
    SIMULATOR_MODEL_PATH='./eclipse/ECL.DATA',
    ST_RHS=1,
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    MEMORY_TYPE=1,
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT4'],
    DIS_TYPE=['CONSTANT_GEO', 0.000144676],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT10'],
    DIS_TYPE=['CONSTANT_GEO', 0.000144676],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT12'],
    DIS_TYPE=['CONSTANT_GEO', 0.000144676],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT15'],
    DIS_TYPE=['CONSTANT_GEO', 0.000144676],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT13'],
    DIS_TYPE=['CONSTANT_GEO', 0.000144676],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT16'],
    DIS_TYPE=['CONSTANT_GEO', 0.000144676],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT14'],
    DIS_TYPE=['CONSTANT_GEO', 0.000144676],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT17'],
    DIS_TYPE=['CONSTANT_GEO', 0.000144676],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[100, 2333],
    TIME_END=233300.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100, 2333],
    TIME_END=233300.0,
    TIME_START=0.0,
)
asc_file = ASC(
    file_name='1pf_1pt_LIQUID_FLOW_ST_RHS',
    file_ext='.asc',
)
asc_file.read_file('1pf_1pt_LIQUID_FLOW_ST_RHS.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='1pf_1pt_LIQUID_FLOW_BC_ST',
    file_ext='.asc',
)
asc_file.read_file('1pf_1pt_LIQUID_FLOW_BC_ST.asc')
model.add_asc(asc_file)
model.write_input()
model.run_model()
