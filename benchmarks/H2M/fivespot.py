# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='fivespot_root',
    task_id='fivespot',
    output_dir='out',
)
model.msh.read_file('fivespot.msh')
model.gli.read_file('fivespot.gli')
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
model.rfd.read_file('fivespot.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'inject'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'inject'],
    DIS_TYPE=['CONSTANT', 1500000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'pump'],
    DIS_TYPE=['CONSTANT', 1000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'pump'],
    DIS_TYPE=['CONSTANT', 105018.5554],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'Front'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'back'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'Left'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'Right'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'top'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'bottom'],
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 105018.5554],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 105018.5554],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='RESERVOIR',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.206],
    PERMEABILITY_TENSOR=['ORTHOTROPIC', 1e-13, 1e-13, 1e-13],
    PERMEABILITY_SATURATION=[
        [0, 1],
        [0, 2],
    ],
    CAPILLARY_PRESSURE=[0, 3],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
    BIOT_CONSTANT=1.0,
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    FLUID_NAME='WATER',
    DENSITY=[1, 1000],
    VISCOSITY=[1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    FLUID_NAME='CARBON_DIOXIDE',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.004],
    GRAVITY=0.0,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 0, 1e-10, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 15, 1.0],
    ELE_GAUSS_POINTS=2,
    COUPLING_CONTROL=['LMAX', 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 0, 1e-12, 2000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=2,
    COUPLING_CONTROL=['LMAX', 0.001],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_END=20,
    TIME_START=0.0,
    TIME_UNIT='DAY',
    TIME_STEPS=[
        [1, 0.01],
        [1, 0.04],
        [1, 0.05],
        [2, 0.25],
        [1, 0.4],
        [5, 1.0],
        [8, 2.0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_END=20,
    TIME_START=0.0,
    TIME_UNIT='DAY',
    TIME_STEPS=[
        [1, 0.01],
        [1, 0.04],
        [1, 0.05],
        [2, 0.25],
        [1, 0.4],
        [5, 1.0],
        [8, 2.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
    ],
    GEO_TYPE=['POLYLINE', 'prof_y'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1.0],
        [2.0],
        [5.0],
        [10.0],
        [16],
        [20],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=[
        [1.0],
        [5.0],
        [10.0],
        [16],
        [20],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
    ],
    GEO_TYPE=['POINT', 'PUMP_t'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
    ],
    GEO_TYPE=['POINT', 'PUMP_b'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
    ],
    GEO_TYPE=['POINT', 'inject_t'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
        ['VELOCITY_Z2'],
    ],
    GEO_TYPE=['POINT', 'inject_b'],
    DAT_TYPE='TECPLOT',
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
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE=['POLYLINE', 'prof_y'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1.0],
        [2.0],
        [5.0],
        [10.0],
        [16],
        [20],
    ],
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
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=[
        [1.0],
        [5.0],
        [10.0],
        [16],
        [20],
    ],
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
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE=['POINT', 'PUMP_t'],
    DAT_TYPE='TECPLOT',
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
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE=['POINT', 'PUMP_b'],
    DAT_TYPE='TECPLOT',
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
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE=['POINT', 'inject_t'],
    DAT_TYPE='TECPLOT',
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
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE=['POINT', 'inject_b'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
