# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='hm_foot_tri_root',
    task_id='hm_foot_tri',
    output_dir='out',
)
model.msh.read_file('hm_foot_tri.msh')
model.gli.read_file('hm_foot_tri.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE=[
        ['LIQUID_FLOW'],
        ['DEFORMATION'],
    ],
)
model.rfd.read_file('hm_foot_tri.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'P_TOP'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'UX_LEFT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'UX_RIGHT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'UX_BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'UY_BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION_FLOW',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'TRACTION_Y'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 2],
        [0, -1000.0],
        [1, -1000.0],
    ],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    ELASTICITY=[
        ['POISSION', 0.2],
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
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-09, 10000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION_FLOW',
    TIME_STEPS=[20, 1.0],
    TIME_END=20.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
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
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
    ],
    GEO_TYPE=['POLYLINE', 'ex2_Out_axis'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1.0],
        [5.0],
        [10.0],
        [20.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='DEFORMATION_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
    ],
    GEO_TYPE=['POLYLINE', 'ex2_out_Bedge'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1.0],
        [5.0],
        [10.0],
        [20.0],
    ],
)
model.write_input()
model.run_model()
