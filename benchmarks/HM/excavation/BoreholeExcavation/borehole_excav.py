# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='borehole_excav_root',
    task_id='borehole_excav',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'upper'],
    DIS_TYPE=['CONSTANT', 5000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'right'],
    DIS_TYPE=['CONSTANT', 5000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'back'],
    DIS_TYPE=['CONSTANT', 5000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'bottom'],
    DIS_TYPE=['CONSTANT', 5000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'left'],
    DIS_TYPE=['CONSTANT', 5000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'front'],
    DIS_TYPE=['CONSTANT', 5000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    DIS_TYPE=['CONSTANT', 1],
    TIM_TYPE=['CURVE', 4],
    EXCAVATION=[1, 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'left'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'right'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'back'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'front'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'bottom'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'upper'],
    DIS_TYPE=['CONSTANT', 0],
)
model.gli.read_file('borehole_excav.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_XX',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [2],
        [0, -9000000.0],
        [1, -9000000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_YY',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [2],
        [0, -9000000.0],
        [1, -9000000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_ZZ',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [2],
        [0, -9000000.0],
        [1, -9000000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 5000000.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    NON_GRAVITY=[],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    PERMEABILITY_TENSOR=['A', 1e-19, 0.0, 0.0, 0.0, 1e-19, 0.0, 0.0, 0.0, 1e-20],
    POROSITY=[1, 0.156],
    PERMEABILITY_SATURATION=[4, 0, 1, 0.5],
    CAPILLARY_PRESSURE=[4, 0.00049],
    STORAGE=[1, 5e-10],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    PERMEABILITY_TENSOR=['A', 1e-19, 0.0, 0.0, 0.0, 1e-19, 0.0, 0.0, 0.0, 1e-20],
    POROSITY=[1, 0.156],
    PERMEABILITY_SATURATION=[4, 0, 1, 0.5],
    CAPILLARY_PRESSURE=[4, 0.00049],
    STORAGE=[1, 5e-10],
)
model.msh.read_file('borehole_excav.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0],
    ELASTICITY=[
        ['POISSION', 0.25],
        ['YOUNGS_MODULUS'],
        [1, 5600000000.0],
    ],
    GRAVITY_CONSTANT=0,
    BIOT_CONSTANT=0.6,
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0],
    ELASTICITY=[
        ['POISSION', 0.25],
        ['YOUNGS_MODULUS'],
        [1, 5600000000.0],
    ],
    GRAVITY_CONSTANT=0,
    BIOT_CONSTANT=0.6,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_MASS_LUMPING=1,
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 100, 1],
    LINEAR_SOLVER=[2, 2, 1e-12, 20000, 1, 100, 4],
    COUPLING_CONTROL=['LMAX', 100000000.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 5, 1e-10, 10000, 1.0, 100, 4],
    COUPLING_CONTROL=['LMAX', 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 1],
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
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
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
    GEO_TYPE=['POLYLINE', 'horizon'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['PRESSURE1'],
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
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
    GEO_TYPE=['POLYLINE', 'vertikal'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    BOUNDARY_CONDITION_OUTPUT=[],
    TIME_CONTROLLED_EXCAVATION=[1, 1, 0, 1],
    NEGLECT_H_INI_EFFECT=1,
    UPDATE_INI_STATE=1,
    ELEMENT_MATRIX_OUTPUT=0,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NUM_TYPE='NEW',
    BOUNDARY_CONDITION_OUTPUT=[],
    TIME_CONTROLLED_EXCAVATION=[1, 1, 0, 1],
    NEGLECT_H_INI_EFFECT=1,
    UPDATE_INI_STATE=1,
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.add_block(
    main_key='PROJECT',
)
model.rfd.add_block(
    CURVE=[
        [0, 0],
        [1800, 0.5],
        [3600, 1],
        [5400, 1.5],
        [7200, 2],
        [9000, 2.5],
        [10800, 3],
        [12600, 3.5],
        [14400, 4],
        [16200, 4.5],
        [18000, 5],
        [19800, 5.5],
        [21600, 6],
        [23400, 6.5],
        [25200, 7],
        [27000, 7.5],
        [28800, 8],
        [30600, 8.5],
        [32400, 9],
        [34200, 9.5],
        [36000, 10],
        [86400, 10],
    ],
)
model.rfd.add_block(
    CURVE=[
        [-1, 1],
        [0, 1],
        [5e-05, 1.258925412],
        [0.0001, 1.584893192],
        [0.00015, 1.995262315],
        [0.0002, 2.511886432],
        [0.00025, 3.16227766],
        [0.0003, 3.981071706],
        [0.00035, 5.011872336],
        [0.0004, 6.309573445],
        [0.00045, 7.943282347],
        [0.0005, 10],
        [0.00055, 12.58925412],
        [0.0006, 15.84893192],
        [0.00065, 19.95262315],
        [0.0007, 25.11886432],
        [0.00075, 31.6227766],
        [0.0008, 39.81071706],
        [0.00085, 50.11872336],
        [0.0009, 63.09573445],
        [0.00095, 79.43282347],
        [0.001, 100],
        [0.00105, 125.8925412],
        [0.0011, 158.4893192],
        [0.00115, 199.5262315],
        [0.0012, 251.1886432],
        [0.00125, 316.227766],
        [0.0013, 398.1071706],
        [0.00135, 501.1872336],
        [0.0014, 630.9573445],
        [0.00145, 794.3282347],
        [0.0015, 1000],
        [1, 1000],
    ],
)
model.rfd.add_block(
    CURVE=[
        [-1, 1],
        [0, 1],
        [0.004, 1],
        [0.005, 2.718281828],
        [0.006, 3.320116923],
        [0.007, 4.055199967],
        [0.008, 4.953032424],
        [0.009, 6.049647464],
        [0.01, 7.389056099],
        [0.011, 9.025013499],
        [0.012, 11.02317638],
        [0.013, 13.46373804],
        [0.014, 16.44464677],
        [0.015, 20.08553692],
        [0.016, 24.5325302],
        [0.017, 29.96410005],
        [0.018, 36.59823444],
        [0.019, 44.70118449],
        [0.02, 54.59815003],
        [0.021, 66.68633104],
        [0.022, 81.45086866],
        [0.023, 99.48431564],
        [0.024, 121.5104175],
        [0.025, 148.4131591],
        [0.026, 181.2722419],
        [0.027, 221.4064162],
        [0.028, 270.4264074],
        [0.029, 330.2995599],
        [0.03, 403.4287935],
        [0.031, 492.7490411],
        [0.032, 601.8450379],
        [0.033, 735.0951892],
        [0.034, 897.8472917],
        [0.035, 1096.633158],
        [100.0, 1096.633158],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0, 100000],
        [86400, 100000],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[1, 3600],
    TIME_END=43200,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_STEPS=[1, 3600],
    TIME_END=43200,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
