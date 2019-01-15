# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='3D_UniAxiLoad_root',
    task_id='3D_UniAxiLoad',
    output_dir='out',
)
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
model.gli.read_file('3D_UniAxiLoad.gli')
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
)
model.msh.read_file('3D_UniAxiLoad.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.27],
        ['YOUNGS_MODULUS'],
        [10, 10500000000.0, 5000000000.0, 0.27, 2479920000.0, 0.70710678118654, 0, 0.70710678118654],
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
        ['BEDDING_NORM', 0.70710678118654, 0, 0.70710678118654],
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
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.rfd.add_block(
    PROJECT=['BENCHMARK:', 'PLASTIC', 'DEFORMATION:', 'CAM-CLAY', 'MODEL'],
)
model.rfd.add_block(
    CURVE=[
        [0.0, -50.0],
        [110.0, -200.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 0.0],
        [400.0, 400],
        [500, 500],
        [600, 600],
        [2000, 2000],
    ],
)
model.rfd.add_block(
    CURVE=[
        [-100, 20],
        [0, 20],
        [100, 20],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.5, 14200000.0],
        [0.55, 12200000.0],
        [0.6, 10100000.0],
        [0.65, 8080000.0],
        [0.7, 6510000.0],
        [0.75, 5560000.0],
        [0.8, 5360000.0],
        [0.85, 6000000.0],
        [0.9, 7510000.0],
        [0.95, 9860000.0],
        [1, 13000000.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [-100, 6670000.0],
        [100, 6670000.0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[20, 50],
    TIME_END=1000,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
