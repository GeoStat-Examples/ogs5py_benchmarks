# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='hm2_1Dcolumn2_root',
    task_id='hm2_1Dcolumn2',
    output_dir='out',
)
model.msh.read_file('hm2_1Dcolumn2.msh')
model.gli.read_file('hm2_1Dcolumn2.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE=[
        ['LIQUID_FLOW'],
        ['DEFORMATION'],
    ],
    NUM_TYPE='NEW',
)
model.rfd.read_file('hm2_1Dcolumn2.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE1'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [0, 0.0],
        [1, 0.0],
        [2, 0.0],
        [3, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE2'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [4, 0.0],
        [5, 0.0],
        [6, 0.0],
        [7, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE3'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [8, 0.0],
        [9, 0.0],
        [10, 0.0],
        [11, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE4'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [12, 0.0],
        [13, 0.0],
        [14, 0.0],
        [15, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE5'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [16, 0.0],
        [17, 0.0],
        [18, 0.0],
        [19, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'SURFACE6'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [20, 0.0],
        [21, 0.0],
        [22, 0.0],
        [23, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE7'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [24, -1000.0],
        [25, -1000.0],
        [26, -1000.0],
        [27, -1000.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.2],
        ['YOUNGS_MODULUS'],
        [1, 30000],
    ],
    BIOT_CONSTANT=1.0,
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION_FLOW',
    LINEAR_SOLVER=[2, 1, 1e-10, 10000, 1.0, 100, 4],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION_FLOW',
    TIME_UNIT='SECOND',
    TIME_STEPS=[45, 0.25],
    TIME_END=10.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
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
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [4],
        [10],
    ],
)
model.write_input()
model.run_model()
