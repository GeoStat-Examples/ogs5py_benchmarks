# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='m_drift_init_root',
    task_id='m_drift_init',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'PLY_4'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'PLY_5'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'PLY_8'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'PLY_6'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'PLY_7'],
    DIS_TYPE=['CONSTANT', 0],
)
model.gli.read_file('m_drift_init.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_XX',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [4],
        [0, '23.75+0.2*y'],
        [1, '24.75+0.5*y'],
        [2, '26.75+12.*y+10*x'],
        [3, '27.75+14.0*y+10*x'],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_YY',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [4],
        [0, '23.75+0.2*y'],
        [1, '24.75+1.3*y'],
        [2, '26.75+16.*y+20*x'],
        [3, '27.75+18.0*y+20*x'],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_ZZ',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [4],
        [0, '23.75+0.2*y'],
        [1, '24.75+0.5*y'],
        [2, '26.75+12.*y+10*x'],
        [3, '27.75+14.0*y+10*x'],
    ],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.0],
)
model.msh.read_file('m_drift_init.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0025],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 25000],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0025],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 26000],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0025],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 30000],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0025],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 28000],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 0, 1e-20, 5000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
    ],
    GEO_TYPE=['POLYLINE', 'PLY_11'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
    ],
    GEO_TYPE=['POLYLINE', 'PLY_13'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
    ],
    GEO_TYPE=['POLYLINE', 'PLY_14'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
    ],
    GEO_TYPE=['POLYLINE', 'PLY_15'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NUM_TYPE='EXCAVATION',
)
model.rfd.read_file('m_drift_init.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'PLY_12'],
    DIS_TYPE=['CONSTANT_NEUMANN', -23.75],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='EXCAVATION',
    GEO_TYPE=[
        ['NULL', 'NULL'],
        ['EXCAVATION_DOMAIN', 2],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='EXCAVATION',
    GEO_TYPE=[
        ['POLYLINE', 'ARC'],
        ['EXCAVATION_DOMAIN', 3],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[1, 1],
    TIME_END=1,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
