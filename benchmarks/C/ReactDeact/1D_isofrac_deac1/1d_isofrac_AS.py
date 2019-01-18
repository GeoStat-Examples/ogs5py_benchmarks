# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='1d_isofrac_AS_root',
    task_id='1d_isofrac_AS',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 100.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT:', 97.81],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='PCE-l',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.98921763658],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='PCE-h',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.010782363425],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE-l',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE-h',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.98921763658],
)
model.gli.read_file('1d_isofrac_AS.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Micros',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='PCE-l',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='PCE-h',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE-l',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE-h',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=1,
    RELATIVE_ERROR=1e-10,
    MIN_TIMESTEP=1e-08,
    INITIAL_TIMESTEP=0.0001,
    NO_REACTIONS=['POINT', 'POINT0'],
    REACTION_DEACTIVATION=[1, 1e-22, 1, 'RELATIVE', 1e-05],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='PCE-deg-l',
    TYPE='monod',
    BACTERIANAME='Micros',
    EQUATION=[1, 'PCE-l', '=', 1, 'TCE-l'],
    RATECONSTANT=[6365.741, 1.0],
    GROWTH=0,
    MONODTERMS=['PCE-l', 100000000000.0, 1.0],
    INHIBITIONTERMS=[],
    PRODUCTIONTERMS=[],
    PRODUCTIONSTOCH=[
        ['PCE-l', -1],
        ['TCE-l', 1],
    ],
    ISOTOPE_FRACTIONATION=['PCE-l', 'PCE-h', 0.0],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='PCE-deg-h',
    TYPE='monod',
    BACTERIANAME='Micros',
    EQUATION=[1, 'PCE-h', '=', 1, 'TCE-h'],
    RATECONSTANT=[6365.741, 1.0],
    GROWTH=0,
    MONODTERMS=['PCE-h', 100000000000.0, 1.0],
    INHIBITIONTERMS=[],
    PRODUCTIONTERMS=[],
    PRODUCTIONSTOCH=[
        ['PCE-h', -1],
        ['TCE-h', 1],
    ],
    ISOTOPE_FRACTIONATION=['PCE-l', 'PCE-h', -5.2],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='PCE-l',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='PCE-h',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TCE-l',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TCE-h',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Micros',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Tracer',
    MOBILE=1,
    DIFFUSION=[1, 3.0093e-10],
    DECAY=[1, 6.365741e-08, 1.0],
    TRANSPORT_PHASE=0,
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
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.25],
    VOL_MAT=[1, 0.74],
    VOL_BIO=[1, 0.01],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.000115741],
    MASS_DISPERSION=[1, 1.0, 1e-10],
    DENSITY=[1, 2650.0],
)
model.msh.read_file('1d_isofrac_AS.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2.65],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='FLUID_MOMENTUM',
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
        ['PCE-l'],
        ['PCE-h'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_LINE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=630720000,
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
model.rfd.read_file('1d_isofrac_AS.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT:', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[200, 3153600],
    TIME_END=6307200000,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[200, 3153600],
    TIME_END=6307200000,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
