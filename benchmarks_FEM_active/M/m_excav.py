# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='m_excav_root',
    task_id='m_excav',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'RIGHT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.gli.read_file('m_excav.gli')
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.msh.read_file('m_excav.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 2.85388127854e-05],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 2.85388127854e-05],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 2.85388127854e-05],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 0, 1e-12, 5000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
    GRAVITY_PROFILE=1,
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [0.02],
        [1],
        [10],
        [100],
        [1000],
        [10000],
        [100000],
        [1000000],
    ],
    AMPLIFIER=0.0,
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POLYLINE', 'H_PROFILE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [1],
        [10],
        [100],
        [1000],
        [10000],
        [100000],
        [1000000],
    ],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [1],
        [10],
        [100],
        [1000],
        [10000],
        [100000],
        [1000000],
    ],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT15'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT7'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT8'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT9'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT10'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT11'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT12'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT13'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NUM_TYPE='EXCAVATION',
)
model.rfd.read_file('m_excav.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='EXCAVATION',
    GEO_TYPE=[
        ['NULL', 'NULL'],
        ['EXCAVATION_DOMAIN', 0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='EXCAVATION',
    GEO_TYPE=[
        ['POLYLINE', 'ARC2'],
        ['EXCAVATION_DOMAIN', 2],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[1, 0.02],
    TIME_END=0.02,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
