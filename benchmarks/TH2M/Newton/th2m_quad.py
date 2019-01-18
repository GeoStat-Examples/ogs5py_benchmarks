# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='th2m_quad_root',
    task_id='th2m_quad',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_H2',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_H2',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_H2',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_H2',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('th2m_quad.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION_H2',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 50.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION_H2',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4280.0],
    HEAT_CONDUCTIVITY=[1, 0.6],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='PRESSURE2',
    DENSITY=7,
    VISCOSITY=[1, 1.8e-05],
    SPECIFIC_HEAT_CAPACITY=[1, 1010.0],
    HEAT_CONDUCTIVITY=[1, 0.026],
    PHASE_DIFFUSION=[1, 2.13e-06],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 0.8],
    DIFFUSION=373,
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-14],
    PERMEABILITY_SATURATION=[
        [0, 4],
        [0, 5],
    ],
    CAPILLARY_PRESSURE=[0, 3],
)
model.msh.read_file('th2m_quad.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, -2000.0],
    ELASTICITY=[
        ['POISSION', 0.4],
        ['YOUNGS_MODULUS:'],
        [1, 30000000.0],
    ],
    BIOT_CONSTANT=1.0,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION_H2',
    ELE_GAUSS_POINTS=3,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 0, 1e-10, 3000, 1.0, 100, 4],
    NON_LINEAR_ITERATION=['NEWTON', 'BNORM', 30, 0.0, 1e-05],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION_H2',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
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
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION_H2',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
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
    GEO_TYPE=['POINT', 'POINT6'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION_H2',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
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
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION_H2',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.read_file('th2m_quad.rfd')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION_H2',
    TIME_STEPS=[10, 5.0],
    TIME_END=100.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
