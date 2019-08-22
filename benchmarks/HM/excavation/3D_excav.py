# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='3D_excav_root',
    task_id='3D_excav',
    output_dir='out',
)
model.msh.read_file('3D_excav.msh')
model.gli.read_file('3D_excav.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    BOUNDARY_CONDITION_OUTPUT=[],
    TIME_CONTROLLED_EXCAVATION=[1, 1, 0, 1],
    NEGLECT_H_INI_EFFECT=2,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    BOUNDARY_CONDITION_OUTPUT=[],
    TIME_CONTROLLED_EXCAVATION=[1, 1, 0, 1],
    NEGLECT_H_INI_EFFECT=2,
)
model.rfd.read_file('3D_excav.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'RIGHT'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'FROUNT'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'BACK'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 0],
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
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'RIGHT'],
    DIS_TYPE=['CONSTANT', 1000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 1000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'BACK'],
    DIS_TYPE=['CONSTANT', 1000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    DIS_TYPE=['CONSTANT', 1000000.0],
    EXCAVATION=[1, 1],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_XX',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [2],
        [0, -12000000.0],
        [1, -12000000.0],
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
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1000000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.156],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-19],
    STORAGE=[1, 7.14418e-10],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.156],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-19],
    STORAGE=[1, 7.14418e-10],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500.0],
    ELASTICITY=[
        ['POISSION', 0.2],
        ['YOUNGS_MODULUS'],
        [1, 8000000000.0],
    ],
    BIOT_CONSTANT=0.6,
    GRAVITY_CONSTANT=0,
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500.0],
    ELASTICITY=[
        ['POISSION', 0.2],
        ['YOUNGS_MODULUS'],
        [1, 8000000000.0],
    ],
    BIOT_CONSTANT=0.6,
    GRAVITY_CONSTANT=0,
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
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 1, 1e-16, 10000, 1.0, 100, 4],
    COUPLING_CONTROL=['LMAX', 1e-06],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 5, 1e-12, 10000, 1.0, 100, 4],
    COUPLING_CONTROL=['LMAX', 1e-06],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLWO',
    TIME_STEPS=[5, 3600],
    TIME_END=18000,
    TIME_START=0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[5, 3600],
    TIME_END=18000,
    TIME_START=0,
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
        ['STRESS_XZ'],
        ['STRESS_YY'],
        ['STRESS_YZ'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_XZ'],
        ['STRAIN_YY'],
        ['STRAIN_YZ'],
        ['STRAIN_ZZ'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
