# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='w_exp_root',
    task_id='w_exp',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
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
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.gli.read_file('w_exp.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 84000000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_XX',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [1],
        [0, -100000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_YY',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [1],
        [0, -100000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_ZZ',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [1],
        [0, -100000.0],
    ],
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
    DENSITY=7,
    VISCOSITY=[1, 1.8e-05],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.4],
    PERMEABILITY_TENSOR=['ISOTROPIC', 6e-21],
    PERMEABILITY_SATURATION=[
        [0, 6],
        [0, 5],
    ],
    CAPILLARY_PRESSURE=[0, 7],
)
model.msh.read_file('w_exp.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2010.0],
    ELASTICITY=['POISSION', 0.4],
    PLASTICITY=[
        ['CAM-CLAY'],
        [1.5],
        [1.5],
        [0.1],
        [8000000.0],
        [0.7],
        [1.0],
        [0.0],
        [0.0],
        [0.0],
        [100000.0],
    ],
    SWELLING_PRESSURE_TYPE=[3, 0.01, -3e-09, 0.25, -0.1609, -3e-08, 100000.0],
    BIOT_CONSTANT=1.0,
    STRESS_INTEGRATION_TOLERANCE=[1e-09, 1e-08],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    LINEAR_SOLVER=[2, 2, 1e-16, 1000, 1.0, 100, 4],
    ELE_MASS_LUMPING=0,
    ELE_GAUSS_POINTS=2,
    NON_LINEAR_SOLVER=['PICARD', 1e-06, 100, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 0, 1e-11, 5000, 1.0, 100, 4],
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
    TIM_TYPE=[
        [0.001],
        [0.01],
        [0.1],
        [1.0],
        [5.0],
        [10.0],
        [50.0],
        [100.0],
        [500.0],
        [1000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION',
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
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.001],
        [0.01],
        [0.1],
        [1.0],
        [5.0],
        [10.0],
        [50.0],
        [100.0],
        [500.0],
        [1000.0],
    ],
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
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION',
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
    ],
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
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
    GEO_TYPE=['POINT', 'POINT5'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION',
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
    ],
    GEO_TYPE=['POINT', 'POINT5'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
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
    GEO_TYPE=['POINT', 'POINT6'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION',
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
    ],
    GEO_TYPE=['POINT', 'POINT6'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
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
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.01],
        [0.1],
        [1.0],
        [5.0],
        [10.0],
        [50.0],
        [100.0],
        [500.0],
        [1000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION',
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
    ],
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.01],
        [0.1],
        [1.0],
        [5.0],
        [10.0],
        [50.0],
        [100.0],
        [500.0],
        [1000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NEGLECT_H_INI_EFFECT=2,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NEGLECT_H_INI_EFFECT=2,
)
model.rfd.add_block(
    PROJECT=['BENCHMARK:', 'TH2M', '(M:', 'PLASTIC', 'DEFORMATION,', 'DRUCKER-PRAGER', 'MODEL)', 'WW'],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 0.0],
        [1000.0, -1.2],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 100000.0],
        [1200.0, 100000.0],
        [2400.0, 100000.0],
        [4800.0, 100000.0],
        [9600.0, 100000.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.743, 22700000.0],
        [0.8825, 500000.0],
        [0.9026, 300000.0],
        [0.9367, 100000.0],
        [0.9578, 50000.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.200000003, 1.0],
        [0.2399999946, 0.8899999857],
        [0.264772743, 0.8168712258],
        [0.3000000119, 0.7200000286],
        [0.400000006, 0.5],
        [0.4499999881, 0.400000006],
        [0.5, 0.3100000024],
        [0.6000000238, 0.1700000018],
        [0.6999999881, 0.0700000003],
        [0.8000000119, 0.01700000092],
        [0.8500000238, 0.01499999966],
        [0.8999999762, 0.01700000092],
        [0.9100000262, 0.01882802136],
        [0.9200000167, 0.02500000037],
        [0.9399999976, 0.05000000075],
        [0.9499999881, 0.1000000015],
        [0.9637847543, 0.1948159337],
        [0.9700000286, 0.3000000119],
        [0.9875695109, 0.5982720256],
        [0.9937847853, 0.8000000119],
        [1.0, 1.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.200000003, 0.99],
        [0.2399999946, 0.8899999857],
        [0.264772743, 0.8168712258],
        [0.3000000119, 0.7200000286],
        [0.400000006, 0.5],
        [0.4499999881, 0.400000006],
        [0.5, 0.3100000024],
        [0.6000000238, 0.1700000018],
        [0.7111498713, 0.08593542129],
        [0.8015800714, 0.04099307209],
        [0.8563649654, 0.02260014415],
        [0.9063808322, 0.01251126267],
        [0.9495475292, 0.007170357276],
        [1.001592875, 0.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.01, 1e-06],
        [0.02, 8e-06],
        [0.03, 2.7e-05],
        [0.04, 6.4e-05],
        [0.05, 0.000125],
        [0.06, 0.000216],
        [0.07, 0.000343],
        [0.08, 0.000512],
        [0.09, 0.000729],
        [0.1, 0.001],
        [0.11, 0.001331],
        [0.12, 0.001728],
        [0.13, 0.002197],
        [0.14, 0.002744],
        [0.15, 0.003375],
        [0.16, 0.004096],
        [0.17, 0.004913],
        [0.18, 0.005832],
        [0.19, 0.006859],
        [0.2, 0.008],
        [0.21, 0.009261],
        [0.22, 0.010648],
        [0.23, 0.012167],
        [0.24, 0.013824],
        [0.25, 0.015625],
        [0.26, 0.017576],
        [0.27, 0.019683],
        [0.28, 0.021952],
        [0.29, 0.024389],
        [0.3, 0.027],
        [0.31, 0.029791],
        [0.32, 0.032768],
        [0.33, 0.035937],
        [0.34, 0.039304],
        [0.35, 0.042875],
        [0.36, 0.046656],
        [0.37, 0.050653],
        [0.38, 0.054872],
        [0.39, 0.059319],
        [0.4, 0.064],
        [0.41, 0.068921],
        [0.42, 0.074088],
        [0.43, 0.079507],
        [0.44, 0.085184],
        [0.45, 0.091125],
        [0.46, 0.097336],
        [0.47, 0.103823],
        [0.48, 0.110592],
        [0.49, 0.117649],
        [0.5, 0.125],
        [0.51, 0.132651],
        [0.52, 0.140608],
        [0.53, 0.148877],
        [0.54, 0.157464],
        [0.55, 0.166375],
        [0.56, 0.175616],
        [0.57, 0.185193],
        [0.58, 0.195112],
        [0.59, 0.205379],
        [0.6, 0.216],
        [0.61, 0.226981],
        [0.62, 0.238328],
        [0.63, 0.250047],
        [0.64, 0.262144],
        [0.65, 0.274625],
        [0.66, 0.287496],
        [0.67, 0.300763],
        [0.68, 0.314432],
        [0.69, 0.328509],
        [0.7, 0.343],
        [0.71, 0.357911],
        [0.72, 0.373248],
        [0.73, 0.389017],
        [0.74, 0.405224],
        [0.75, 0.421875],
        [0.76, 0.438976],
        [0.77, 0.456533],
        [0.78, 0.474552],
        [0.79, 0.493039],
        [0.8, 0.512],
        [0.81, 0.531441],
        [0.82, 0.551368],
        [0.83, 0.571787],
        [0.84, 0.592704],
        [0.85, 0.614125],
        [0.86, 0.636056],
        [0.87, 0.658503],
        [0.88, 0.681472],
        [0.89, 0.704969],
        [0.9, 0.729],
        [0.91, 0.753571],
        [0.92, 0.778688],
        [0.93, 0.804357],
        [0.94, 0.830584],
        [0.95, 0.857375],
        [0.96, 0.884736],
        [0.97, 0.912673],
        [0.98, 0.941192],
        [0.99, 0.970299],
        [1, 1],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.01, 35833736280],
        [0.02, 13758328039],
        [0.03, 7858779486],
        [0.04, 5281557349],
        [0.05, 3880171563],
        [0.06, 3015754241],
        [0.07, 2436731787],
        [0.08, 2025608510],
        [0.09, 1720744425],
        [0.1, 1486942346],
        [0.11, 1302760671],
        [0.12, 1154452425],
        [0.13, 1032830975],
        [0.14, 931542944.8],
        [0.15, 846065673.1],
        [0.16, 773099336],
        [0.17, 710184490],
        [0.18, 655453656.9],
        [0.19, 607465445.6],
        [0.2, 565091060.3],
        [0.21, 527434963.8],
        [0.22, 493778340.5],
        [0.23, 463538108.7],
        [0.24, 436236739.1],
        [0.25, 411479715.3],
        [0.26, 388938484],
        [0.27, 368337404.1],
        [0.28, 349443649.6],
        [0.29, 332059318.9],
        [0.3, 316015210.9],
        [0.31, 301165874.5],
        [0.32, 287385638.8],
        [0.33, 274565406.5],
        [0.34, 262610045.8],
        [0.35, 251436254.3],
        [0.36, 240970800.5],
        [0.37, 231149065.7],
        [0.38, 221913830.9],
        [0.39, 213214259.6],
        [0.4, 205005043.3],
        [0.41, 197245678.5],
        [0.42, 189899853.6],
        [0.43, 182934925.4],
        [0.44, 176321472.5],
        [0.45, 170032910.2],
        [0.46, 164045159.7],
        [0.47, 158336361.3],
        [0.48, 152886625.8],
        [0.49, 147677817.9],
        [0.5, 142693367.1],
        [0.51, 137918102.3],
        [0.52, 133338106],
        [0.53, 128940586.4],
        [0.54, 124713764.2],
        [0.55, 120646772.5],
        [0.56, 116729567.5],
        [0.57, 112952849.7],
        [0.58, 109307992.7],
        [0.59, 105786980.7],
        [0.6, 102382350.7],
        [0.61, 99087142.41],
        [0.62, 95894851.37],
        [0.63, 92799387.52],
        [0.64, 89795037.12],
        [0.65, 86876428.13],
        [0.66, 84038498.44],
        [0.67, 81276466.58],
        [0.68, 78585804.7],
        [0.69, 75962213.2],
        [0.7, 73401597.06],
        [0.71, 70900043.24],
        [0.72, 68453799.08],
        [0.73, 66059251.33],
        [0.74, 63712905.48],
        [0.75, 61411365.08],
        [0.76, 59151310.64],
        [0.77, 56929477.72],
        [0.78, 54742633.6],
        [0.79, 52587552.05],
        [0.8, 50460985.12],
        [0.81, 48359631.23],
        [0.82, 46280097.82],
        [0.83, 44218857.06],
        [0.84, 42172191.76],
        [0.85, 40136128.13],
        [0.86, 38106350.04],
        [0.87, 36078087.52],
        [0.88, 34045967.86],
        [0.89, 32003812.07],
        [0.9, 29944348.28],
        [0.91, 27858795.44],
        [0.92, 25736235.68],
        [0.93, 23562625.44],
        [0.94, 21319150.51],
        [0.95, 18979295.39],
        [0.96, 16503124.73],
        [0.97, 13824610.01],
        [0.98, 10817505.44],
        [0.99, 7164594.883],
        [0.999, 1867812.074],
        [0.9999, 490851.0058],
        [0.99999, 129095.5759],
        [0.999999, 33955.29648],
        [1, 0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_STEPS=[
        [10, 0.001],
        [9, 0.01],
        [90, 0.01],
        [100, 0.05],
        [100, 0.1],
        [100, 0.5],
        [1000, 1.0],
    ],
    TIME_END=17.5,
    TIME_START=0.0,
    TIME_UNIT='HOUR',
)
model.write_input()
model.run_model()
