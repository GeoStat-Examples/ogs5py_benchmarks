# -*- coding: utf-8 -*-
from ogs5py import OGS, ASC

model = OGS(
    task_root='2pf_radialmodel_root',
    task_id='2pf_radialmodel',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.gli.read_file('2pf_radialmodel.gli')
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
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ORTHOTROPIC', 2e-13, 2e-13, 2e-14],
    PERMEABILITY_SATURATION=[
        [6, 0.25, 0.975, 2.0],
        [66, 0.025, 0.75, 2.0, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 5000],
)
model.msh.read_file('2pf_radialmodel.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 6, 1e-10, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 25, 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
    ],
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
    SIMULATOR_PATH='C:\ecl\2012.1\bin\pc_x86_64\eclipse.exe',
    SIMULATOR_MODEL_PATH='./eclipse/ECL.DATA',
    ELEMENT_MATRIX_OUTPUT=0,
    ST_RHS=1,
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_STEPS=[10, 86400.0],
    TIME_END=4320000,
    TIME_START=0.0,
)
asc_file = ASC(
    file_name='2pf_radialmodel_LIQUID_FLOW_ST_RHS',
    file_ext='.asc',
)
asc_file.read_file('2pf_radialmodel_LIQUID_FLOW_ST_RHS.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='2pf_radialmodel_MULTI_PHASE_FLOW_ST_RHS',
    file_ext='.asc',
)
asc_file.read_file('2pf_radialmodel_MULTI_PHASE_FLOW_ST_RHS.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='2pf_radialmodel_LIQUID_FLOW_BC_ST',
    file_ext='.asc',
)
asc_file.read_file('2pf_radialmodel_LIQUID_FLOW_BC_ST.asc')
model.add_asc(asc_file)
model.write_input()
model.run_model()
