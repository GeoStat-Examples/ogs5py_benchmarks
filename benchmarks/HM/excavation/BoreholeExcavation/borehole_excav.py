# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='borehole_excav_root',
    task_id='borehole_excav',
    output_dir='out',
)
model.msh.read_file('borehole_excav.msh')
model.gli.read_file('borehole_excav.gli')
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
model.rfd.read_file('borehole_excav.rfd')
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
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    NON_GRAVITY=[],
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
model.write_input()
model.run_model()
