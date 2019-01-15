# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='H2_Permeability_GasPressure_root',
    task_id='H2_Permeability_GasPressure',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'PLY_1'],
    DIS_TYPE=['CONSTANT', 101325],
    TIM_TYPE=['CURVE', 2],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'PLY_3'],
    DIS_TYPE=['CONSTANT', 101325],
)
model.gli.read_file('H2_Permeability_GasPressure.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1875000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 101325],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='PRESSURE2',
    DENSITY=[2, 1.2, 101325, 1.189e-05],
    VISCOSITY=[1, 1.6e-05],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.16],
    PERMEABILITY_TENSOR=['ORTHOTROPIC', 3e-17, 3e-18],
    PERMEABILITY_FUNCTION_PRESSURE=[10, 3],
    PERMEABILITY_SATURATION=[
        [4, 0.5, 1, 0.5],
        [44, 0, 0.5, 0.5],
    ],
    CAPILLARY_PRESSURE=[4, 0.003924],
)
model.msh.read_file('H2_Permeability_GasPressure.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    LINEAR_SOLVER=[2, 0, 1e-15, 10000, 1, 100, 4],
    ELE_UPWINDING=[0, 1.0],
    ELE_MASS_LUMPING=1,
    ELE_GAUSS_POINTS=3,
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 1000, 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.add_block(
    main_key='PROJECT',
)
model.rfd.add_block(
    CURVE=[
        [0.21, 199984374.4],
        [0.22, 99968745.12],
        [0.23, 66619775.18],
        [0.24, 49937460.89],
        [0.25, 39921798.56],
        [0.26, 33239451.13],
        [0.27, 28461843.42],
        [0.28, 24874685.93],
        [0.29, 22081149.44],
        [0.3, 19843134.83],
        [0.31, 18009123.03],
        [0.32, 16478099.94],
        [0.33, 15180131.44],
        [0.34, 14065263.33],
        [0.35, 13096861.37],
        [0.36, 12247448.71],
        [0.37, 11496012.55],
        [0.38, 10826208.48],
        [0.39, 10225131.98],
        [0.4, 9682458.366],
        [0.41, 9189828.499],
        [0.42, 8740402.056],
        [0.43, 8328527.285],
        [0.44, 7949493.345],
        [0.45, 7599342.077],
        [0.46, 7274723.2],
        [0.47, 6972781.69],
        [0.48, 6691069.284],
        [0.49, 6427474.285],
        [0.5, 6180165.406],
        [0.51, 5947546.473],
        [0.52, 5728219.619],
        [0.53, 5520955.155],
        [0.54, 5324666.762],
        [0.55, 5138390.918],
        [0.56, 4961269.75],
        [0.57, 4792536.656],
        [0.58, 4631504.186],
        [0.59, 4477553.778],
        [0.6, 4330127.019],
        [0.61, 4188718.17],
        [0.62, 4052867.745],
        [0.63, 3922156.971],
        [0.64, 3796202.975],
        [0.65, 3674654.599],
        [0.66, 3557188.733],
        [0.67, 3443507.087],
        [0.68, 3333333.333],
        [0.69, 3226410.562],
        [0.7, 3122498.999],
        [0.71, 3021373.942],
        [0.72, 2922823.876],
        [0.73, 2826648.73],
        [0.74, 2732658.252],
        [0.75, 2640670.463],
        [0.76, 2550510.153],
        [0.77, 2462007.404],
        [0.78, 2374996.089],
        [0.79, 2289312.315],
        [0.8, 2204792.759],
        [0.81, 2121272.835],
        [0.82, 2038584.623],
        [0.83, 1956554.45],
        [0.84, 1875000],
        [0.85, 1793726.741],
        [0.86, 1712523.417],
        [0.87, 1631156.194],
        [0.88, 1549360.846],
        [0.89, 1466832.064],
        [0.9, 1383208.338],
        [0.91, 1298049.901],
        [0.92, 1210805.262],
        [0.93, 1120758.094],
        [0.94, 1026938.118],
        [0.95, 927960.7271],
        [0.96, 821710.2629],
        [0.97, 704627.7407],
        [0.98, 569756.0524],
        [0.99, 399035.4498],
        [1, 0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0, 1.0],
        [1000, 10],
        [1001, 13],
        [2000, 13],
        [2001, 16],
        [3000, 16],
        [3001, 19],
        [4000, 19],
        [4001, 22],
        [5000, 22],
        [5001, 25],
        [6000, 25],
        [6001, 28],
        [7000, 28],
        [7001, 31],
        [8000, 31],
        [8001, 34],
        [9000, 34],
        [9001, 10],
        [10000, 10],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0, 1],
        [3200000.0, 1.4],
        [3500000.0, 47],
        [3600000.0, 47],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0, 10000000000.0],
        [0.001, 1],
        [1, 1],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0, 1],
        [8000000.0, 1],
        [9000000.0, 1],
        [10000000.0, 1],
        [11000000.0, 10.38],
        [12000000.0, 90.28],
        [13000000.0, 120.6],
    ],
)
model.rfd.add_block(
    REFERENCE_CONDITIONS=[9.81, 293, 101325],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_STEPS=[
        [1, 1000],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
    ],
    TIME_END=10000,
    TIME_START=0,
)
model.write_input()
model.run_model()
