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
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='C(4)',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-07],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ca',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-07],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Mg',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Cl',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 2.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pH',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 7.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pe',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 4.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Calcite',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 4.70588e-10],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Dolomite(dis)',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 4.70588e-10],
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
    PRIMARY_VARIABLE='C(4)',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.123],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ca',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.123],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Mg',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-09],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Cl',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-09],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H+',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.23027e-07],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pH',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 9.91],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='pe',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 4.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO3-2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0001],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='HCO3-',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='a_HCO3-',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Calcite',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.057412],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Dolomite(dis)',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=2,
    RELATIVE_ERROR=1e-06,
    MIN_TIMESTEP=1e-11,
    INITIAL_TIMESTEP=0.1,
    DEBUG_OUTPUT=[],
    NO_REACTIONS=[],
    ACTIVITY_MODEL=2,
)
model.krc.add_block(
    main_key='REACTION',
    NAME='Dolomite(dis)',
    CHEMAPPNAME='Dolomite(dis)',
    MINERALNAME='Dolomite(dis)',
    TYPE='Mineralkinetics',
    EQUATION=['Dolomite(dis)', '=', 'Ca', '+', 'Mg', '+', 2, 'CO3-2'],
    EQUILIBRIUM_CONSTANT=['UNIFORM', -17.09],
    RATE_EXPONENTS=[1.0, 1.0],
    REACTIVE_SURFACE_AREA=[0, 6000.0],
    PRECIPITATION_FACTOR=1,
    BASETERM=[-7.53, 52200],
    MECHANISMTERM=[
        [-3.19, 36100],
        ['H+', 0.5],
    ],
    PRODUCTIONSTOCH=[
        ['Ca', -1.0],
        ['Mg', -1.0],
        ['CO3-2', -2.0],
        ['C(4)', -2.0],
    ],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='C(4)',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
    VALENCE=-2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Ca',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
    VALENCE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Mg',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
    VALENCE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Cl',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
    VALENCE=-1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='pH',
    MOBILE=0,
    DIFFUSION=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='pe',
    MOBILE=0,
    DIFFUSION=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='H+',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
    VALENCE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO3-2',
    MOBILE=0,
    DIFFUSION=[1, 0.0],
    VALENCE=-2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='HCO3-',
    MOBILE=0,
    DIFFUSION=[1, 0.0],
    VALENCE=-1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='a_HCO3-',
    MOBILE=0,
    DIFFUSION=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Calcite',
    MOBILE=0,
    DIFFUSION=0,
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Dolomite(dis)',
    MOBILE=0,
    DIFFUSION=0,
    TRANSPORT_PHASE=1,
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
    POROSITY=[1, 0.32],
    VOL_MAT=[1, 0.68],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.157e-12],
    MASS_DISPERSION=[1, 0.0067, 0.1],
    DENSITY=[1, 1800.0],
)
model.msh.read_file('pds.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
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
        ['C(4)'],
        ['Ca'],
        ['Mg'],
        ['Cl'],
        ['pH'],
        ['pe'],
        ['Calcite'],
        ['Dolomite(dis)'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['C(4)'],
        ['Ca'],
        ['Mg'],
        ['Cl'],
        ['pH'],
        ['pe'],
        ['CO3-2'],
        ['HCO3-'],
        ['a_HCO3-'],
        ['Calcite'],
        ['Dolomite(dis)'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_LINE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.0],
        [100.0],
        [1000.0],
        [10000.0],
        [21000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['C(4)'],
        ['Ca'],
        ['Mg'],
        ['Cl'],
        ['pH'],
        ['pe'],
        ['CO3-2'],
        ['HCO3-'],
        ['a_HCO3-'],
        ['Calcite'],
        ['Dolomite(dis)'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.0],
        [100.0],
        [1000.0],
        [10000.0],
        [21000.0],
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
model.pqc.read_file('pds.pqc')
model.rei.add_block(
    main_key='REACTION_INTERFACE',
    MOL_PER='VOLUME',
    WATER_CONCENTRATION='CONSTANT',
    PRESSURE=['CONSTANT', 1.0],
    TEMPERATURE=['CONSTANT', 298.15],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', -2.9976852e-06],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[210, 100.0],
    TIME_END=21000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[210, 100.0],
    TIME_END=21000.0,
    TIME_START=0.0,
)
model.pqcdat.read_file('model.dat')
model.write_input()
model.run_model()
