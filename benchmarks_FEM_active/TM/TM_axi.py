# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='TM_axi_root',
    task_id='TM_axi',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'PLY_B'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'PLY_T'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'PLY_O'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'PLY_O'],
    DIS_TYPE=['CONSTANT', 25.0],
)
model.gli.read_file('TM_axi.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 2200.0],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 5.5],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
)
model.msh.read_file('TM_axi.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, -2000.0],
    THERMAL=[
        ['EXPANSION', 4.2e-05],
        ['CAPACITY'],
        [1, 0.0],
        ['CONDUCTIVITY'],
        [1, 5.5],
    ],
    ELASTICITY=[
        ['POISSION', 0.25],
        ['YOUNGS_MODULUS'],
        [1, 2500000000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 2, 1e-12, 2000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 2, 1e-13, 2000, 1.0, 100, 4],
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
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
    AMPLIFIER=10.0,
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
    GEO_TYPE=['POLYLINE', 'PLY_B'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NUM_TYPE='NEW',
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'PLY_I'],
    DIS_TYPE=['CONSTANT_NEUMANN', 30],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[1, 1],
    TIME_END=1,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[1, 1],
    TIME_END=1.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
