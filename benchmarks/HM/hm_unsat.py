# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='hm_unsat_root',
    task_id='hm_unsat',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
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
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('hm_unsat.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
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
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.2975],
    PERMEABILITY_TENSOR=['ISOTROPIC', 4.5e-13],
    PERMEABILITY_SATURATION=[
        [0, 2],
        [0, 2],
    ],
    CAPILLARY_PRESSURE=[0, 1],
)
model.msh.read_file('hm_unsat.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, -2000.0],
    ELASTICITY=[
        ['POISSION', 0.4],
        ['YOUNGS_MODULUS'],
        [1, 1300000.0],
    ],
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
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE='DOMAIN',
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POLYLINE', 'RIGHT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [5.0],
        [10.0],
        [20.0],
        [30.0],
        [60.0],
        [120.0],
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
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT0'],
    DAT_TYPE='TECPLOT',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.rfd.add_block(
    PROJECT=['BENCHMARK:', 'Staggered', 'scheme', 'for', 'unsaturated', 'consolidation.', 'WW'],
)
model.rfd.add_block(
    CURVE=[
        [0.9, 9938.064],
        [0.91, 9516.018],
        [0.92, 9065.393],
        [0.93, 8589.271],
        [0.94, 8052.432],
        [0.95, 7469.886],
        [0.96, 6813.948],
        [0.97, 6052.562],
        [0.98, 5121.663],
        [0.9825, 4847.584],
        [0.985, 4549.372],
        [0.9875, 4220.252],
        [0.99, 3849.668],
        [0.9925, 3419.508],
        [0.995, 2893.579],
        [0.9975, 2174.942],
        [1.0, 0.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.575, 0.0],
        [0.6, 0.12693],
        [0.625, 0.18214],
        [0.65, 0.2373],
        [0.675, 0.29242],
        [0.7, 0.34748],
        [0.725, 0.40248],
        [0.75, 0.45743],
        [0.775, 0.51231],
        [0.8, 0.56711],
        [0.825, 0.62184],
        [0.85, 0.67646],
        [0.875, 0.73098],
        [0.9, 0.78536],
        [0.925, 0.83958],
        [0.95, 0.89358],
        [0.975, 0.94723],
        [1.0, 1.0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_STEPS=[120, 1.0],
    TIME_END=120.0,
    TIME_START=0.0,
    TIME_UNIT='MINUTE',
)
model.write_input()
model.run_model()
