# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='Wool_lines_coup_root',
    task_id='Wool_lines_coup',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT3'],
    DIS_TYPE=['CONSTANT', -2250.39756],
)
model.gli.read_file('Wool_lines_coup.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', -2250.39756],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-06],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 756.0],
    VISCOSITY=[1, 0.00147],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    SURFACE_FRICTION=[1333333, 1.0, 2.0],
    RILL=[0.001, 0.0005],
    WIDTH=1.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.42],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5.616e-12],
    PERMEABILITY_SATURATION=[4, 0.053, 1.0, 0.75],
    CAPILLARY_PRESSURE=[4, 6.0],
)
model.msh.read_file('Wool_lines_coup.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.1, 20, 0.0],
    ELE_GAUSS_POINTS=3,
    COUPLING_CONTROL=['LMAX', 1e-12],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='OVERLAND_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['NEWTON', 1e-05, 1e-08, 100, 0.0],
    ELE_GAUSS_POINTS=3,
    COUPLING_CONTROL=['LMAX', 1e-12],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES='SATURATION1',
    GEO_TYPE=['POLYLINE', 'SATURATION'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [180],
        [360],
        [540],
        [720],
        [900],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES='WDEPTH',
    GEO_TYPE=['POLYLINE', 'UP'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [180],
        [360],
        [540],
        [720],
        [900],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES='FLUX',
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES='HEAD',
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='OVERLAND_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.read_file('Wool_lines_coup.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=[
        ['CRITICALDEPTH', 1],
        [0.001],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'UP'],
    DIS_TYPE=['CONSTANT_NEUMANN', 1],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'UP'],
    DIS_TYPE=[
        ['CONSTANT_NEUMANN', 1],
        ['PCS', 'RICHARDS_FLOW'],
        ['PRESSURE1'],
        [0.0283333333, 0.001],
    ],
    NODE_AVERAGING=[],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'UP'],
    DIS_TYPE=[
        ['CONSTANT', 1],
        ['PCS', 'OVERLAND_FLOW'],
        ['HEAD'],
        [0.0283333333, 0.001],
    ],
    NODE_AVERAGING=[],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_STEPS=[900, 1],
    TIME_END=900,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='OVERLAND_FLOW',
    TIME_STEPS=[900, 1],
    TIME_END=900,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
