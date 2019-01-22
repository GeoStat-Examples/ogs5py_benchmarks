# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='1d_TCE_Ion_root',
    task_id='1d_TCE_Ion',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 257.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE-mat',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='trans-DCE-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='trans-DCE-mat',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='cis-DCE-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 240.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='cis-DCE-mat',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-DCE-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.048],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-DCE-mat',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Acet-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Acet-mat',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ClAcet-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ClAcet-mat',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='VC-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.168],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='VC-mat',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ethylen-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ethylen-mat',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='C4-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ethan-mob',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='mobile',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 257.0],
)
model.gli.read_file('1d_TCE_Ion.gli')
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
    PRIMARY_VARIABLE='TCE-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TCE-mat',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='trans-DCE-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='trans-DCE-mat',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='cis-DCE-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='cis-DCE-mat',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-DCE-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-DCE-mat',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Acet-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Acet-mat',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ClAcet-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ClAcet-mat',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='VC-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='VC-mat',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ethylen-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ethylen-mat',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='C4-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ethan-mob',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=[
        ['CONSTANT', 1e-10],
        [0, 0, 1e-10],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='mobile',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='TCE-mat-deg',
    TYPE='monod',
    BACTERIANAME='TCE-mat',
    RATECONSTANT=[-7.52315e-08, 1.0],
    GROWTH=1,
    PRODUCTIONSTOCH=[
        ['trans-DCE-mat', -0.000754],
        ['cis-DCE-mat', -0.017505],
        ['11-DCE-mat', -0.00432],
        ['ClAcet-mat', -0.977421],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='trans-DCE-mat',
    TYPE='monod',
    BACTERIANAME='trans-DCE-mat',
    RATECONSTANT=[-9.86204e-07, 1.0],
    GROWTH=1,
    PRODUCTIONSTOCH=[
        ['Acet-mat', -0.988107],
        ['VC-mat', -0.011893],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='cis-DCE-mat-deg',
    TYPE='monod',
    BACTERIANAME='cis-DCE-mat',
    RATECONSTANT=[-5.11464e-07, 1.0],
    GROWTH=1,
    PRODUCTIONSTOCH=[
        ['Acet-mat', -0.939655],
        ['VC-mat', -0.060345],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='11-DCE-mat-deg',
    TYPE='monod',
    BACTERIANAME='11-DCE-mat',
    RATECONSTANT=[-8.20106e-07, 1.0],
    GROWTH=1,
    PRODUCTIONSTOCH=['Ethylen-mat', -1.0],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='Acet-mat-deg',
    TYPE='monod',
    BACTERIANAME='Acet-mat',
    RATECONSTANT=[-2.55765e-06, 1.0],
    GROWTH=1,
    PRODUCTIONSTOCH=[
        ['Ethylen-mat', -0.992113],
        ['C4-mob', -0.007887],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='ClAcet-mat-deg',
    TYPE='monod',
    BACTERIANAME='ClAcet-mat',
    RATECONSTANT=[-1.42416e-06, 1.0],
    GROWTH=1,
    PRODUCTIONSTOCH=['Acet-mat', -1.0],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='VC-mat-deg',
    TYPE='monod',
    BACTERIANAME='VC-mat',
    RATECONSTANT=[-6.06481e-06, 1.0],
    GROWTH=1,
    PRODUCTIONSTOCH=['Ethylen-mat', -1.0],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='Ethylen-mat-deg',
    TYPE='monod',
    BACTERIANAME='Ethylen-mat',
    RATECONSTANT=[-1.99074e-06, 1.0],
    GROWTH=1,
    PRODUCTIONSTOCH=['Ethan-mob', -1.0],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='langmuir1',
    TYPE='exchange',
    SORPTION_TYPE='langmuir',
    EQUATION=['TCE-mat', '=', 'TCE-mob'],
    EXCHANGE_PARAMETERS=[5.78704e-08, 2.39583e-05, 1],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='langmuir2',
    TYPE='exchange',
    SORPTION_TYPE='langmuir',
    EQUATION=['trans-DCE-mat', '=', 'trans-DCE-mob'],
    EXCHANGE_PARAMETERS=[1.02431e-08, 1.73611e-05, 1],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='langmuir3',
    TYPE='exchange',
    SORPTION_TYPE='langmuir',
    EQUATION=['cis-DCE-mat', '=', 'cis-DCE-mob'],
    EXCHANGE_PARAMETERS=[1.73611e-07, 0.000162037, 1],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='langmuir4',
    TYPE='exchange',
    SORPTION_TYPE='langmuir',
    EQUATION=['11-DCE-mat', '=', '11-DCE-mob'],
    EXCHANGE_PARAMETERS=[1.02431e-08, 1.73611e-05, 1],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='langmuir5',
    TYPE='exchange',
    SORPTION_TYPE='langmuir',
    EQUATION=['Acet-mat', '=', 'Acet-mob'],
    EXCHANGE_PARAMETERS=[5.78704e-08, 1.38889e-05, 1],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='langmuir6',
    TYPE='exchange',
    SORPTION_TYPE='langmuir',
    EQUATION=['ClAcet-mat', '=', 'ClAcet-mob'],
    EXCHANGE_PARAMETERS=[5.78704e-08, 6.01852e-06, 1],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='langmuir7',
    TYPE='exchange',
    SORPTION_TYPE='langmuir',
    EQUATION=['VC-mat', '=', 'VC-mob'],
    EXCHANGE_PARAMETERS=[3.47222e-08, 1.73611e-05, 1],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='langmuir8',
    TYPE='exchange',
    SORPTION_TYPE='langmuir',
    EQUATION=['Ethylen-mat', '=', 'Ethylen-mob'],
    EXCHANGE_PARAMETERS=[3.47222e-08, 1.73611e-05, 1],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=1,
    RELATIVE_ERROR=1e-08,
    MIN_TIMESTEP=0.1,
    INITIAL_TIMESTEP=10.0,
    SURFACES=[1, 2000.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TCE-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TCE-mat',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='trans-DCE-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='trans-DCE-mat',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='cis-DCE-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='cis-DCE-mat',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='11-DCE-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='11-DCE-mat',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Acet-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Acet-mat',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='ClAcet-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='ClAcet-mat',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='VC-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='VC-mat',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Ethylen-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Ethylen-mat',
    MOBILE=0,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='C4-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Ethan-mob',
    MOBILE=1,
    DIFFUSION=[1, 0],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='mobile',
    MOBILE=1,
    DIFFUSION=[1, 0],
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
    PERMEABILITY_TENSOR=['ISOTROPIC', 5.787037e-07],
    MASS_DISPERSION=[1, 0.01, 1e-10],
    DENSITY=[1, 2650.0],
)
model.msh.read_file('1d_TCE_Ion.msh')
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
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['TCE-mob'],
        ['TCE-mat'],
        ['trans-DCE-mob'],
        ['trans-DCE-mat'],
        ['cis-DCE-mob'],
        ['cis-DCE-mat'],
        ['11-DCE-mob'],
        ['11-DCE-mat'],
        ['Acet-mob'],
        ['Acet-mat'],
        ['ClAcet-mob'],
        ['ClAcet-mat'],
        ['VC-mob'],
        ['VC-mat'],
        ['Ethylen-mob'],
        ['Ethylen-mat'],
        ['C4-mob'],
        ['Ethan-mob'],
        ['mobile'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_LINE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 50],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['TCE-mob'],
        ['TCE-mat'],
        ['trans-DCE-mob'],
        ['trans-DCE-mat'],
        ['cis-DCE-mob'],
        ['cis-DCE-mat'],
        ['11-DCE-mob'],
        ['11-DCE-mat'],
        ['Acet-mob'],
        ['Acet-mat'],
        ['ClAcet-mob'],
        ['ClAcet-mat'],
        ['VC-mob'],
        ['VC-mat'],
        ['Ethylen-mob'],
        ['Ethylen-mat'],
        ['C4-mob'],
        ['Ethan-mob'],
        ['mobile'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 50],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['TCE-mob'],
        ['TCE-mat'],
        ['trans-DCE-mob'],
        ['trans-DCE-mat'],
        ['cis-DCE-mob'],
        ['cis-DCE-mat'],
        ['11-DCE-mob'],
        ['11-DCE-mat'],
        ['Acet-mob'],
        ['Acet-mat'],
        ['ClAcet-mob'],
        ['ClAcet-mat'],
        ['VC-mob'],
        ['VC-mat'],
        ['Ethylen-mob'],
        ['Ethylen-mat'],
        ['C4-mob'],
        ['Ethan-mob'],
        ['mobile'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 10],
)
model.out.add_block(
    main_key='OUTPUT',
    ELE_VALUES='VELOCITY1_X',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 10],
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
model.rfd.read_file('1d_TCE_Ion.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT:', 'POINT1'],
    DIS_TYPE=['CONSTANT', -5.78704e-08],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[100, 43200.0],
    TIME_END=43200000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100, 43200.0],
    TIME_END=43200000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
