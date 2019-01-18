# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='m_brick_l_root',
    task_id='m_brick_l',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'V_EDGE'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'V_EDGE'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'X0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'X1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('m_brick_l.gli')
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
)
model.msh.read_file('m_brick_l.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.4],
        ['YOUNGS_MODULUS'],
        [1, 20000000.0],
    ],
    PLASTICITY=[
        ['DRUCKER-PRAGER'],
        [29692.5],
        [8165.0],
        [-0.233345],
        [-0.141421],
        [0.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    NON_LINEAR_SOLVER=['NEWTON', 0.0001, 1e-10, 100, 0.0],
    LINEAR_SOLVER=[2, 0, 1e-10, 10000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['DISPLACEMENT_Z1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRESS_XZ'],
        ['STRESS_YZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 2],
    AMPLIFIER=100.0,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['DISPLACEMENT_Z1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRESS_XZ'],
        ['STRESS_YZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT9'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.rfd.read_file('m_brick_l.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [4, 0.0],
        [5, 0.0],
        [6, 1.0],
        [7, 1.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[36, 0.5],
    TIME_END=10.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
