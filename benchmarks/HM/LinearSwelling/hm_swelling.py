# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='hm_swelling_root',
    task_id='hm_swelling',
    output_dir='out',
)
model.msh.read_file('hm_swelling.msh')
model.gli.read_file('hm_swelling.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
    DEACTIVATED_SUBDOMAIN=[
        [1],
        [2],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.rfd.read_file('hm_swelling.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 10000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 25.0],
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
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'TOP'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [3],
        [2, -70000000.0],
        [0, -70000000.0],
        [1, 100000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [3],
        [0, 25.0],
        [1, 25.0],
        [2, 25.0],
    ],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.41],
    DIFFUSION=2273,
    TORTUOSITY=[1, 0.8],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2e-21],
    PERMEABILITY_SATURATION=[
        [0, 3],
        [0, 3],
    ],
    CAPILLARY_PRESSURE=[0, 2],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.01],
    DIFFUSION=2273,
    TORTUOSITY=[1, 0.8],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-17],
    HEAT_DISPERSION=[1, 1.0, 1.0],
    PERMEABILITY_SATURATION=[
        [4, 0.0, 1.0, 0.6],
        [4, 0.0, 1.0, 0.6],
    ],
    CAPILLARY_PRESSURE=[4, 0.006673469387755102],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
    TORTUOSITY=[1, 0.8],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-21],
    HEAT_DISPERSION=[1, 0.01, 0.01],
    PERMEABILITY_SATURATION=[
        [3, 0.0, 0.0, 0.0],
        [3, 0.0, 0.0, 0.0],
    ],
    CAPILLARY_PRESSURE=[1, 0.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, -1600.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [3],
        ['CONDUCTIVITY:'],
        [3],
    ],
    ELASTICITY=[
        ['POISSION', 0.35],
        ['YOUNGS_MODULUS:'],
        [1, 317000000.0],
    ],
    SWELLING_PRESSURE_TYPE=[2, 14286000.0],
    BIOT_CONSTANT=0.0,
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, -2700.0],
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
    BIOT_CONSTANT=0.0,
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, -2700.0],
    THERMAL=[
        ['EXPANSION', 0.0],
        ['CAPACITY:'],
        [1, 732.5],
        ['CONDUCTIVITY:'],
        [1, 50.2],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 200000000000.0],
    ],
    BIOT_CONSTANT=0.0,
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
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 2, 1e-10, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 25, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 0, 1e-10, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 25, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 0, 1e-10, 2000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_STEPS=[
        [4, 0.001],
        [1, 0.006],
        [9, 0.01],
        [9, 0.1],
        [9, 1],
        [30, 1],
        [2, 2],
        [1, 10],
        [1, 16],
        [1, 30],
        [1, 40],
        [10, 86],
        [90, 100],
        [100, 900],
        [90, 10000],
    ],
    TIME_END=10000.0,
    TIME_START=0.0,
    TIME_UNIT='YEAR',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[
        [4, 0.001],
        [1, 0.006],
        [9, 0.01],
        [9, 0.1],
        [9, 1],
        [30, 1],
        [2, 2],
        [1, 10],
        [1, 16],
        [1, 30],
        [1, 40],
        [10, 86],
        [90, 100],
        [100, 900],
        [90, 10000],
        [100, 900],
        [90, 10000],
    ],
    TIME_END=10000.0,
    TIME_START=0.0,
    TIME_UNIT='YEAR',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
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
        [0],
        [0.02],
        [0.1],
        [0.2],
        [0.3],
        [0.4],
        [0.5],
        [0.6],
        [0.7],
        [0.8],
        [0.9],
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [8],
        [9],
        [10],
        [11],
        [12],
        [13],
        [14],
        [15],
        [16],
        [20],
        [50],
        [80],
        [100],
        [1000],
        [10000],
        [100000],
        [1000000],
    ],
    AMPLIFIER=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
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
    GEO_TYPE=['POLYLINE', 'H_PROFILE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [0.9],
        [1],
        [10],
        [100],
        [1000],
        [10000],
        [100000],
        [1000000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
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
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
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
    GEO_TYPE=['POINT', 'POINT8'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
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
    GEO_TYPE=['POINT', 'POINT9'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 2],
)
model.write_input()
model.run_model()
