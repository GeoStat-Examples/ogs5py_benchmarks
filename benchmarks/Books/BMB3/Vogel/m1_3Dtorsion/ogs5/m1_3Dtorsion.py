# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='m1_3Dtorsion_root',
    task_id='m1_3Dtorsion',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE1'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [0, 0.0],
        [1, 0.0],
        [2, 0.0],
        [3, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE2'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [4, 0.0],
        [5, 0.0],
        [6, 0.0],
        [7, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE3'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [8, 0.0],
        [9, 0.0],
        [10, 0.0],
        [11, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.gli.read_file('m1_3Dtorsion.gli')
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
)
model.msh.read_file('m1_3Dtorsion.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.25],
        ['YOUNGS_MODULUS'],
        [1, 25000000000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 1, 1e-10, 10000, 1.0, 101, 4],
)
model.out.add_block(
    main_key='OUTPUT',
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
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NUM_TYPE='NEW',
)
model.rfd.read_file('m1_3Dtorsion.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE4'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [12, 0.0],
        [13, 0.0],
        [14, 0.0],
        [15, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE5'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [16, -1000000000.0],
        [17, -1000000000.0],
        [18, 1000000000.0],
        [19, 1000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE6'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [20, 1000000000.0],
        [21, -1000000000.0],
        [22, -1000000000.0],
        [23, 1000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE7'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [24, 0.0],
        [25, 0.0],
        [26, 0.0],
        [27, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE8'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [28, 1000000000.0],
        [29, 1000000000.0],
        [30, -1000000000.0],
        [31, -1000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE9'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [32, -1000000000.0],
        [33, 1000000000.0],
        [34, 1000000000.0],
        [35, -1000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE10'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [36, 1000000000.0],
        [37, 1000000000.0],
        [38, -1000000000.0],
        [39, -1000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE11'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [40, 0.0],
        [41, 0.0],
        [42, 0.0],
        [43, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE12'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [44, 0.0],
        [45, 0.0],
        [46, 0.0],
        [47, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE13'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [48, -1000000000.0],
        [49, -1000000000.0],
        [50, 1000000000.0],
        [51, 1000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE14'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [52, 0.0],
        [53, 0.0],
        [54, 0.0],
        [55, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE15'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [56, 0.0],
        [57, 0.0],
        [58, 0.0],
        [59, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE16'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [60, -1000000000.0],
        [61, -1000000000.0],
        [62, 1000000000.0],
        [63, 1000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE17'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [64, 0.0],
        [65, 0.0],
        [66, 0.0],
        [67, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE18'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [68, 0.0],
        [69, 0.0],
        [70, 0.0],
        [71, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE19'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [72, 1000000000.0],
        [73, 1000000000.0],
        [74, -1000000000.0],
        [75, -1000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE20'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [76, 0.0],
        [77, 0.0],
        [78, 0.0],
        [79, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE21'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [80, 0.0],
        [81, 0.0],
        [82, 0.0],
        [83, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_UNIT='SECOND',
    TIME_STEPS=[1, 1],
    TIME_END=1.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
