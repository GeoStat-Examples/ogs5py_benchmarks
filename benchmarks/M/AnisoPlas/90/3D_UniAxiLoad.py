# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='3D_UniAxiLoad_root',
    task_id='3D_UniAxiLoad',
    output_dir='out',
)
model.msh.read_file('3D_UniAxiLoad.msh')
model.gli.read_file('3D_UniAxiLoad.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.rfd.read_file('3D_UniAxiLoad.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', -5e-07],
    TIM_TYPE=['CURVE', 2],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.27],
        ['YOUNGS_MODULUS'],
        [10, 10500000000.0, 5000000000.0, 0.27, 2479920000.0, 1, 0, 0],
    ],
    PLASTICITY=[
        ['MOHR-COULOMB'],
        [2000000.0],
        [20],
        [0],
        [6670000.0],
        [-1],
        [-1],
    ],
    MICRO_STRUCTURE_PLAS=[
        ['MICRO_STRUCTURE_TENSOR', 1, 1, 0.5],
        ['BEDDING_NORM', 1, 0, 0],
        ['UNIAXI_COMP_CURVE', 2, 70820400, -171383200, 113588800],
        ['TENSION_CURVE', 1, 0, 2000000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    NON_LINEAR_SOLVER=['NEWTON', 0.001, 2e-10, 100, 0.0],
    LINEAR_SOLVER=[2, 5, 1e-12, 2000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[20, 50],
    TIME_END=1000,
    TIME_START=0.0,
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
        ['STRESS_YZ'],
        ['STRESS_XZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_Z1'],
        ['STRESS_ZZ'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
