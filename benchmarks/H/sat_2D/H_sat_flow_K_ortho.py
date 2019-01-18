# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='H_sat_flow_K_ortho_root',
    task_id='H_sat_flow_K_ortho',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_0'],
    DIS_TYPE=['CONSTANT', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'PLY_1'],
    DIS_TYPE=['CONSTANT', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_4'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_5'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_0'],
    DIS_TYPE=['CONSTANT', 1000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_1'],
    DIS_TYPE=['CONSTANT', 1000],
)
model.gli.read_file('H_sat_flow_K_ortho.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Tracer',
    MOBILE=1,
    TRANSPORT_PHASE=0,
    DIFFUSION=[1, 6e-10],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='LAYER0',
    GEO_TYPE=['LAYER', 0],
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ANISOTROPIC', 1e-15, 0.0, 0.0, 1e-14],
    MASS_DISPERSION=[1, 10, 10],
    DENSITY=[1, 2000.0],
)
model.msh.read_file('H_sat_flow_K_ortho.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1605.064889],
        ['CONDUCTIVITY:'],
        [1, 0.00118799939],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='PRESSURE1',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 10, 0.0],
    ELE_GAUSS_POINTS=3,
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
        ['PRESSURE1'],
        ['Tracer'],
    ],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_2'],
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'PLY_3'],
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='TECPLOT',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.rfd.read_file('H_sat_flow_K_ortho.rfd')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[300, 100000.0],
    TIME_END=30000000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[300, 100000.0],
    TIME_END=30000000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
