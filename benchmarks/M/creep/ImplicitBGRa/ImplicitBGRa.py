# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='ImplicitBGRa_root',
    task_id='ImplicitBGRa',
    output_dir='out',
)
model.msh.read_file('ImplicitBGRa.msh')
model.gli.read_file('ImplicitBGRa.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.rfd.read_file('ImplicitBGRa.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'PLY_2'],
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'PLY_3'],
    DIS_TYPE=['CONSTANT_NEUMANN', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    THERMAL=[
        ['EXPANSION', 4e-05],
        ['CAPACITY:'],
        [1, 1.0],
        ['CONDUCTIVITY:'],
        [1, 100.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.27],
        ['YOUNGS_MODULUS'],
        [1, 25000.0],
    ],
    CREEP=[0.18, 5.0, 1.0, 54000.0, 373.15, 1e-10, 300],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    NON_LINEAR_SOLVER=['NEWTON', 1e-10, 1e-12, 100, 0.0],
    LINEAR_SOLVER=[2, 5, 1e-12, 2000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[100, 1.0],
    TIME_END=100,
    TIME_START=0.0,
    TIME_UNIT='DAY',
    INDEPENDENT=0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['TEMPERATURE1'],
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_YY'],
        ['STRAIN_XY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 100],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['TEMPERATURE1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
