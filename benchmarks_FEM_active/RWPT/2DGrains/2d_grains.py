# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='2d_grains_root',
    task_id='2d_grains',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_LEFT'],
    DIS_TYPE=['CONSTANT', 0.1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_RIGHT'],
    DIS_TYPE=['CONSTANT', 0],
)
model.gli.read_file('2d_grains.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='vapor',
    MOBILE=1,
    DIFFUSION=[1, 1e-15],
    DECAY=[1, 0.0, 1.0],
    ISOTHERM=[5, 0.01, 0.1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4000],
    HEAT_CONDUCTIVITY=[1, 1e-08],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-06],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-08],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-08],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-08],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-08],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-08],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-08],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.msh.read_file('2d_grains.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 2, 1e-16, 5000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='FLUID_MOMENTUM',
    ELE_GAUSS_POINTS=2,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='GROUNDWATER_FLOW',
    NOD_VALUES=[
        ['HEAD'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    RWPT_VALUES='PARTICLES',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIM_TYPE='STEADY',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='FLUID_MOMENTUM',
    NUM_TYPE='STEADY',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RANDOM_WALK',
)
model.pct.read_file('2d_grains.pct')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[60, 600000.0],
    TIME_END=1e+99,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='FLUID_MOMENTUM',
    TIME_STEPS=[60, 600000.0],
    TIME_END=1e+99,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RANDOM_WALK',
    TIME_STEPS=[60, 600000.0],
    TIME_END=1e+99,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
