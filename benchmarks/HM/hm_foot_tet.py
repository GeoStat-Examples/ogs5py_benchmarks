# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS, ASC

model = OGS(
    task_root='hm_foot_tet_root',
    task_id='hm_foot_tet',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'TOP'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'X0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'X1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'Y0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'Y1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('hm_foot_tet.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC:', 1e-10],
)
model.msh.read_file('hm_foot_tet.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    ELASTICITY=[
        ['POISSION:', 0.43],
        ['YOUNGS_MODULUS'],
        [1, 30000.0],
    ],
    PLASTICITY=[
        ['DRUCKER-PRAGER'],
        [1e+16],
        [-1000000.0],
        [19.0],
        [2.0],
        [0.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 3000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
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
        ['STRAIN_ZZ'],
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
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
        ['STRAIN_ZZ'],
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_AXIS'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1.0],
        [5.0],
        [10.0],
        [20.0],
        [50.0],
        [100.0],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE=[
        ['LIQUID_FLOW'],
        ['DEFORMATION'],
    ],
    MEMORY_TYPE=0,
    ST_RHS=2,
)
model.rfd.add_block(
    PROJECT=['BENCHMARK:', 'ELASTIC', 'DEFORMATION', 'ITER.', 'COUPLED', 'WITH', 'SAT.', 'FLUID', 'FLOW,', '3D'],
)
model.rfd.add_block(
    RENUMBER=0,
)
model.rfd.add_block(
    REFERENCE_CONDITIONS=[9.81, 0.0, '0.0.000000'],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 1.0],
        [1296000.0, 1.0],
        [2592000.0, 1.0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'FOOT'],
    DIS_TYPE=['CONSTANT_NEUMANN', -1000.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION_FLOW',
    TIME_STEPS=[1, 1.0],
    TIME_END=20.0,
    TIME_START=0.0,
    TIME_CONTROL=[],
)
asc_file = ASC(
    file_name='hm_foot_tet_DEFORMATION_FLOW_ST_RHS',
    file_ext='.asc',
)
asc_file.read_file('hm_foot_tet_DEFORMATION_FLOW_ST_RHS.asc')
model.add_asc(asc_file)
model.write_input()
model.run_model()
