# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='h2_Liako_root',
    task_id='h2_Liako',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT', 101325],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 101325],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0],
)
model.gli.read_file('h2_Liako.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
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
    PCS_TYPE='PRESSURE1',
    DENSITY=7,
    VISCOSITY=[1, 1.8e-05],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.2975],
    PERMEABILITY_TENSOR=['ISOTROPIC', 4.5e-13],
    PERMEABILITY_SATURATION=[
        [0, 2],
        [66, 0.2, 1.0, 3.0, 0.0001],
    ],
    CAPILLARY_PRESSURE=[0, 1],
)
model.msh.read_file('h2_Liako.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 6, 1e-12, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 50, 1.0],
    ELE_GAUSS_POINTS=2,
)
model.out.add_block(
    main_key='OUTPUT',
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
    TIM_TYPE=[
        [0.001],
        [5],
        [10],
        [20],
        [30],
        [60],
        [120],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
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
    GEO_TYPE=['POLYLINE', 'left'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.001],
        [5],
        [10],
        [20],
        [30],
        [60],
        [120],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
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
    GEO_TYPE=['POINT', 'POINT0'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.add_block(
    PROJECT=['BENCHMARK:', 'Simulate', 'Liakoloulos', 'exp.', 'with', 'p-p', 'H2', 'scheme.', '17.06.2008', 'WW'],
)
model.rfd.add_block(
    CURVE=[
        [0.900000007, 9938.064],
        [0.910000009, 9516.018],
        [0.920000003, 9065.393],
        [0.929821599, 8589.271],
        [0.939999996, 8052.432],
        [0.950000006, 7469.886],
        [0.960000005, 6813.948],
        [0.97, 6052.562],
        [0.980000004, 5121.663],
        [0.982500005, 4847.584],
        [0.984999999, 4549.372],
        [0.9875, 4220.252],
        [0.989999997, 3849.668],
        [0.9925, 3419.508],
        [0.995000002, 2893.579],
        [0.997499999, 2174.942],
        [0.99962099, 1000],
        [1.0, 0.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.575, 0.0],
        [0.6, 0.12693],
        [0.625, 0.18214],
        [0.65, 0.2373],
        [0.675, 0.29242],
        [0.7, 0.34748],
        [0.725, 0.40248],
        [0.75, 0.45743],
        [0.775, 0.51231],
        [0.8, 0.56711],
        [0.825, 0.62184],
        [0.85, 0.67646],
        [0.875, 0.73098],
        [0.9, 0.78536],
        [0.925, 0.83958],
        [0.95, 0.89358],
        [0.975, 0.94723],
        [1.0, 1.0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_STEPS=[
        [10, 0.001],
        [9, 0.01],
        [9, 0.1],
        [120, 1.0],
    ],
    TIME_END=120.0,
    TIME_UNIT='MINUTE',
    TIME_START=0.0,
)
model.write_input()
model.run_model()
