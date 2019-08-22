# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='creep_after_excavation_root',
    task_id='creep_after_excavation',
    output_dir='out',
)
model.msh.read_file('creep_after_excavation.msh')
model.gli.read_file('creep_after_excavation.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TIM_TYPE='STEADY',
    TEMPERATURE_UNIT='KELVIN',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.rfd.read_file('creep_after_excavation.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'left'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'right'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'bottom'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'top'],
    DIS_TYPE=['CONSTANT', 310.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'bottom'],
    DIS_TYPE=['CONSTANT', 320.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'circle'],
    DIS_TYPE=['CONSTANT', 300.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 300.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'top'],
    DIS_TYPE=['CONSTANT_NEUMANN', -10000000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
    THERMAL=[
        ['EXPANSION', 4e-05],
        ['CAPACITY:'],
        [1, 0.0],
        ['CONDUCTIVITY:'],
        [1, 5],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS'],
        [1, 7000000000.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2170.0],
    THERMAL=[
        ['EXPANSION', 4e-05],
        ['CAPACITY:'],
        [1, 0.0],
        ['CONDUCTIVITY:'],
        [1, 5],
    ],
    ELASTICITY=[
        ['POISSION', 0.27],
        ['YOUNGS_MODULUS'],
        [1, 7650000000.0],
    ],
    CREEP=[0.18, 4.9, 1000000.0, 54000.0, 293.0, 1e-08, 400],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    NON_LINEAR_SOLVER=['NEWTON', 1e-08, 1e-12, 50, 0.0],
    LINEAR_SOLVER=[2, 0, 1e-12, 2000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 0, 1e-10, 200, 1.0, 100, 4],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[
        [1, 0.001],
        [1, 0.09],
        [1, 0.1],
        [1, 0.8],
        [50, 1.0],
    ],
    TIME_END=50,
    TIME_START=0.0,
    TIME_UNIT='DAY',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[
        [1, 0.001],
        [1, 0.09],
        [1, 0.1],
        [1, 0.8],
        [50, 1.0],
    ],
    TIME_END=50,
    TIME_START=0.0,
    TIME_UNIT='DAY',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['TEMPERATURE1'],
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_YY'],
        ['STRAIN_XY'],
        ['STRAIN_ZZ'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=[
        [1.0],
        [5.0],
        [8.0],
        [10.0],
        [20.0],
        [30.0],
        [40.0],
        [50.0],
    ],
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
    GEO_TYPE=['POINT', 'point_top'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
