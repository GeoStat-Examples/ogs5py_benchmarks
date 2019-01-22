# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='m1_3Dwings_root',
    task_id='m1_3Dwings',
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
model.gli.read_file('m1_3Dwings.gli')
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
)
model.msh.read_file('m1_3Dwings.msh')
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
    LINEAR_SOLVER=[2, 1, 1e-10, 20000, 1.0, 101, 4],
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
model.rfd.read_file('m1_3Dwings.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE4'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [12, -10000000000.0],
        [13, -10000000000.0],
        [14, 10000000000.0],
        [15, 10000000000.0],
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
        [16, -20000000000.0],
        [17, 20000000000.0],
        [18, 20000000000.0],
        [19, -20000000000.0],
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
        [20, 0.0],
        [21, 0.0],
        [22, 0.0],
        [23, 0.0],
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
        [24, 10000000000.0],
        [25, 10000000000.0],
        [26, -10000000000.0],
        [27, -10000000000.0],
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
        [28, 20000000000.0],
        [29, -20000000000.0],
        [30, -20000000000.0],
        [31, 20000000000.0],
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
        [32, 0.0],
        [33, 0.0],
        [34, 0.0],
        [35, 0.0],
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
        [36, 0.0],
        [37, 0.0],
        [38, 0.0],
        [39, 0.0],
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
        [40, -500000000.0],
        [41, -500000000.0],
        [42, 500000000.0],
        [43, 500000000.0],
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
        [45, 10000000000.0],
        [46, 10000000000.0],
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
        [48, 0.0],
        [49, 0.0],
        [50, 0.0],
        [51, 0.0],
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
        [52, 500000000.0],
        [53, 500000000.0],
        [54, -500000000.0],
        [55, -500000000.0],
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
        [57, -10000000000.0],
        [58, -10000000000.0],
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
        [60, -500000000.0],
        [61, -500000000.0],
        [62, 500000000.0],
        [63, 500000000.0],
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
        [69, 20000000000.0],
        [70, 20000000000.0],
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
        [72, 500000000.0],
        [73, 500000000.0],
        [74, -500000000.0],
        [75, -500000000.0],
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
        [81, -20000000000.0],
        [82, -20000000000.0],
        [83, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE22'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [84, 0.0],
        [85, 0.0],
        [86, 0.0],
        [87, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE23'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [88, -500000000.0],
        [89, -500000000.0],
        [90, 500000000.0],
        [91, 500000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE24'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [92, -10000000000.0],
        [93, 0.0],
        [94, 0.0],
        [95, -10000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE25'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [96, 0.0],
        [97, 0.0],
        [98, 0.0],
        [99, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE26'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [100, 500000000.0],
        [101, 500000000.0],
        [102, -500000000.0],
        [103, -500000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE27'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [104, 10000000000.0],
        [105, 0.0],
        [106, 0.0],
        [107, 10000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE28'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [108, -500000000.0],
        [109, -500000000.0],
        [110, 500000000.0],
        [111, 500000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE29'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [112, 0.0],
        [113, 0.0],
        [114, 0.0],
        [115, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE30'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [116, -20000000000.0],
        [117, 0.0],
        [118, 0.0],
        [119, -20000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE31'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [120, 500000000.0],
        [121, 500000000.0],
        [122, -500000000.0],
        [123, -500000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE32'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [124, 0.0],
        [125, 0.0],
        [126, 0.0],
        [127, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE33'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [128, 20000000000.0],
        [129, 0.0],
        [130, 0.0],
        [131, 20000000000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_UNIT='SECOND',
    TIME_STEPS=[2, 1.0],
    TIME_END=1.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
