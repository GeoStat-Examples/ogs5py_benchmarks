# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='pds_root',
    task_id='pds',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.gli.read_file('pds.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='A',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='B',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=2,
    RELATIVE_ERROR=1e-06,
    MIN_TIMESTEP=1e-11,
    INITIAL_TIMESTEP=10,
    DEBUG_OUTPUT=[],
    ACTIVITY_MODEL=0,
    LAGNEAU_BENCHMARK=[],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='Bprecip',
    CHEMAPPNAME='B',
    MINERALNAME='B',
    TYPE='Mineralkinetics',
    EQUATION=[1, 'A', '=', 'B'],
    EQUILIBRIUM_CONSTANT=['UNIFORM', -4],
    RATE_EXPONENTS=[1, 1],
    REACTIVE_SURFACE_AREA=[0, 10000.0],
    BASETERM=[-7.698970004, 10000],
    PRODUCTIONSTOCH=['A', -1],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='A',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='B',
    MOBILE=0,
    DIFFUSION=0,
    TRANSPORT_PHASE=0,
    MOLAR_WEIGHT=0.4,
    MINERAL_DENSITY=1000,
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[13, 0.05],
    VOL_BIO=[1, 0.0],
    VOL_MAT=[1, 0.95],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.0001157],
    MASS_DISPERSION=[1, 0.005, 0.1],
    DENSITY=[1, 1500.0],
)
model.msh.read_file('pds.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1500.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 0.5, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['A'],
        ['B'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_LINE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 200],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['A'],
        ['B'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 10],
)
model.out.add_block(
    main_key='OUTPUT',
    ELE_VALUES=[
        ['POROSITY'],
        ['PERMEABILITY'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [100],
        [500],
        [1000],
        [2000],
        [3000],
        [4000],
        [5000],
        [7000],
        [10000],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.rei.add_block(
    main_key='REACTION_INTERFACE',
    MOL_PER='VOLUME',
    WATER_CONCENTRATION='CONSTANT',
    PRESSURE=['CONSTANT', 1.0],
    TEMPERATURE=['CONSTANT', 298.15],
)
model.rfd.read_file('pds.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[1000, 10],
    TIME_END=10000000000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[1000, 10],
    TIME_END='1e10.0',
    TIME_START=0.0,
)
model.write_input()
model.run_model()
