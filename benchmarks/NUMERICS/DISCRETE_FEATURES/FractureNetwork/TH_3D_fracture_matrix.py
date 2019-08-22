# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='TH_3D_fracture_matrix_root',
    task_id='TH_3D_fracture_matrix',
    output_dir='out',
)
model.msh.read_file('TH_3D_fracture_matrix.msh')
model.gli.read_file('TH_3D_fracture_matrix.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 10000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 70],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 150],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE=0,
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.01,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE='Extr_Kluft',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.01,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE=2,
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.01,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE=3,
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.01,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE=4,
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.01,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE='Trans_Kluft',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.01,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE='Inj_Kluft',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.01,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-12],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE='matrix',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-20],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2600.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 1000.0],
        ['CONDUCTIVITY'],
        [1, 3],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DAT_TYPE='LIQUID',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4680.0],
    SPECIFIC_HEAT_CONDUCTIVITY=[1, 0.6],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CONCENTRATION1',
    MOBILE=1,
    DIFFUSION=[1, 1e-08],
    ISOTHERM=[1, 0.0004],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 2, 1e-09, 2000, 1.0, 1, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-10, 1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 0.5, 1, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-10, 1, 0.0],
    ELE_SUPG=[1, 0, 0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_END=1e+99,
    TIME_START=0,
    TIME_STEPS=[10, 2592000],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_END=1e+99,
    TIME_START=0,
    TIME_STEPS=[10, 2592000],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='NO_PCS',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['TEMPERATURE1'],
    ],
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
    ],
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
