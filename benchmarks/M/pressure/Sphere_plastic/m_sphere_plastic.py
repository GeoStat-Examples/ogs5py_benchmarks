# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='m_sphere_plastic_root',
    task_id='m_sphere_plastic',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'oben'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'mitte'],
    DIS_TYPE=['CONSTANT', 0],
)
model.gli.read_file('m_sphere_plastic.gli')
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
model.msh.read_file('m_sphere_plastic.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.35],
        ['YOUNGS_MODULUS:'],
        [1, 125000.0],
    ],
    PLASTICITY=[
        ['DRUCKER-PRAGER'],
        [200.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 1, 1e-11, 5000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
    NON_LINEAR_SOLVER=['NEWTON', 0.001, 1e-09, 20, 0.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_1'],
        ['STRESS_2'],
        ['STRESS_3'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['NORM_STRESS_1_X'],
        ['NORM_STRESS_1_Y'],
        ['NORM_STRESS_1_Z'],
        ['NORM_STRESS_2_X'],
        ['NORM_STRESS_2_Y'],
        ['NORM_STRESS_2_Z'],
        ['NORM_STRESS_3_X'],
        ['NORM_STRESS_3_Y'],
        ['NORM_STRESS_3_Z'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=2,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.rfd.add_block(
    CURVE=[
        [0, 0],
        [1, 1],
        [2, 0],
        [10, 0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_N',
    GEO_TYPE=['POLYLINE', 'innen'],
    DIS_TYPE=['CONSTANT_NEUMANN', -93.101629],
    TIM_TYPE=['CURVE', 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[
        [1, 0.1],
        [40, 0.05],
    ],
    TIME_END=2.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
