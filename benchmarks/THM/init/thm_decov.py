# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='thm_decov_root',
    task_id='thm_decov',
    output_dir='out',
)
model.msh.read_file('thm_decov.msh')
model.gli.read_file('thm_decov.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NUM_TYPE='EXCAVATION',
    RELOAD=[1, 1],
)
model.rfd.read_file('thm_decov.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
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
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_XX',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [3],
        [0, '-32.1e6+0.55e5*y'],
        [1, '-32.1e6+0.55e5*y'],
        [2, '-32.1e6+0.55e5*y'],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_YY',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [3],
        [0, '-13243500+26487*y'],
        [1, '-13243500+26487*y'],
        [2, '-13243500+26487*y'],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='STRESS_ZZ',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [3],
        [0, '-10.6e6+0.2e5*y'],
        [1, '-10.6e6+0.2e5*y'],
        [2, '-10.6e6+0.2e5*y'],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT_NEUMANN', -12766950.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='EXCAVATION',
    GEO_TYPE=[
        ['NULL', 'NULL'],
        ['EXCAVATION_DOMAIN', 0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='EXCAVATION',
    GEO_TYPE=[
        ['POLYLINE', 'ARC2'],
        ['EXCAVATION_DOMAIN', 2],
    ],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 900],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 900],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 900],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
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
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 0, 1e-10, 2000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
    GRAVITY_PROFILE=1,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[1, 0.001],
    TIME_END=1000000.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE='DOMAIN:',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
