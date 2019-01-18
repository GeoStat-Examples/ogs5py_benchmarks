# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='thm_cube_root',
    task_id='thm_cube',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'RIGHT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'FRONT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'BACK'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 7],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 8],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 9],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 10],
)
model.ddc.read_file('thm_cube.ddc')
model.gli.read_file('thm_cube.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [3],
        [0, -1000000.0],
        [1, -1000000.0],
        [2, -1000000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=[
        ['SUB_DOMAIN'],
        [3],
        [0, 20.0],
        [1, 20.0],
        [2, 20.0],
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
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.01],
    DIFFUSION=273,
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
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.01],
    DIFFUSION=273,
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
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.01],
    DIFFUSION=273,
    TORTUOSITY=[1, 0.8],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-17],
    HEAT_DISPERSION=[1, 1.0, 1.0],
    PERMEABILITY_SATURATION=[
        [4, 0.0, 1.0, 0.6],
        [4, 0.0, 1.0, 0.6],
    ],
    CAPILLARY_PRESSURE=[4, 0.006673469387755102],
)
model.msh.read_file('thm_cube.msh')
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
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 2, 1e-10, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 25, 0.0],
    COUPLING_ITERATIONS=[6, 0.001],
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
    LINEAR_SOLVER=[2, 0, 1e-10, 3000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['VELOCITY_X'],
        ['VELOCITY_Y'],
        ['VELOCITY_Z'],
        ['TEMPERATURE1'],
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
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [0.02],
        [1],
        [10],
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
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['VELOCITY_X'],
        ['VELOCITY_Y'],
        ['VELOCITY_Z'],
        ['TEMPERATURE1'],
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
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POLYLINE', 'H_PROFILE_0'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
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
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['VELOCITY_X'],
        ['VELOCITY_Y'],
        ['VELOCITY_Z'],
        ['TEMPERATURE1'],
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
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POLYLINE', 'V_PROFILE_0'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
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
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['VELOCITY_X'],
        ['VELOCITY_Y'],
        ['VELOCITY_Z'],
        ['TEMPERATURE1'],
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
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT0'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['VELOCITY_X'],
        ['VELOCITY_Y'],
        ['VELOCITY_Z'],
        ['TEMPERATURE1'],
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
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT3'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE_CAP'],
        ['SATURATION1'],
        ['VELOCITY_X'],
        ['VELOCITY_Y'],
        ['VELOCITY_Z'],
        ['TEMPERATURE1'],
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
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT6'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.rfd.read_file('thm_cube.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT_NEUMANN', -12766950.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_STEPS=[4, 0.001],
    TIME_END=1000000.0,
    TIME_START=0.0,
    TIME_UNIT='YEAR',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[4, 0.001],
    TIME_END=1000000.0,
    TIME_START=0.0,
    TIME_UNIT='YEAR',
)
model.write_input()
model.run_model()
