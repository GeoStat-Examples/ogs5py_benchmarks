# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='h2_line_root',
    task_id='h2_line',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 2.006494565],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 2.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Xylene',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 2e-05],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Cons_Tracer',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 2e-05],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Oxygen',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-05],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Fe2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Sulfate',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1e-05],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='S',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
)
model.gli.read_file('h2_line.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 2.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Xylene',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Cons_Tracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Oxygen',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-05],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Metab_O',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Biomass_Aerobic',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-06],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Goethite',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.2],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='bioFe3',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.02],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Metab_Fe3',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Fe2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Biomass_Ironreducer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-06],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Sulfate',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-05],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='S',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Meta_ProductS',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Biomass_Sulfatereducer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-06],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=1,
    RELATIVE_ERROR=1e-06,
    MIN_TIMESTEP=1e-06,
    INITIAL_TIMESTEP=0.0001,
    BACTERIACAPACITY=100.0,
)
model.krc.add_block(
    main_key='REACTION',
    NAME='DoubleMonod',
    TYPE='monod',
    BACTERIANAME='Biomass_Aerobic',
    EQUATION=[1, 'Xylene', '+', 10.5, 'O2', '=', 8, 'CO2', '+', 5, 'H2O'],
    RATECONSTANT=[1.1574e-07, 1.0],
    GROWTH=1,
    MONODTERMS=[
        ['Xylene', 1.5e-05, 1.0],
        ['Oxygen', 2e-06, 1.0],
    ],
    INHIBITIONTERMS=[],
    PRODUCTIONSTOCH=[
        ['Xylene', -6.27],
        ['Oxygen', -65.83],
        ['Metab_O', 50.16],
        ['CO2', 50.16],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='DoubleMonodDecay',
    TYPE='monod',
    BACTERIANAME='Biomass_Aerobic',
    EQUATION=['Biomass_Aerobic', '=', 'Biomass_Aerobic'],
    RATECONSTANT=[-1.1574e-08, 1.0],
    GROWTH=1,
    MONODTERMS=[],
    INHIBITIONTERMS=[],
    PRODUCTIONTERMS=[],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='Fe-bio-dissolution',
    TYPE='exchange',
    SORPTION_TYPE='linear',
    EQUATION=['Goethite', '=', '-', 'bioFe3'],
    EXCHANGE_PARAMETERS=[1.15741e-10, 0.0],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='DoubleMonod',
    TYPE='monod',
    BACTERIANAME='Biomass_Ironreducer',
    EQUATION=[1, 'C8H10', '+', 42, 'FeOOH', '+', 84, 'H', '=', 8, 'CO2', '+', 42, 'Fe', '+', 68, 'H2O'],
    RATECONSTANT=[1.1574e-07, 1.0],
    GROWTH=1,
    MONODTERMS=[
        ['Xylene', 1e-06, 1.0],
        ['bioFe3', 1e-06, 1.0],
    ],
    INHIBITIONTERMS=[
        ['Oxygen', 5e-08, 1.0],
        ['Sulfate', 5e-07, 1.0],
    ],
    PRODUCTIONSTOCH=[
        ['Xylene', -20.8],
        ['bioFe3', -873.6],
        ['Metab_Fe3', 166.4],
        ['Fe2', 166.4],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='DoubleMonodDecay',
    TYPE='monod',
    BACTERIANAME='Biomass_Ironreducer',
    EQUATION=['Biomass_Ironreducer', '=', 'Biomass_Ironreducer'],
    RATECONSTANT=[-1.1574e-08, 1.0],
    GROWTH=1,
    MONODTERMS=[],
    INHIBITIONTERMS=[],
    PRODUCTIONTERMS=[],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='DoubleMonod',
    TYPE='monod',
    BACTERIANAME='Biomass_Sulfatereducer',
    EQUATION=[1, 'C8H10', '+', 5.25, 'SO4', '+', 5.25, 'H', '=', 8, 'CO2', '+', 5.25, 'HS', '+', 5, 'H2O'],
    RATECONSTANT=[1.1574e-07, 1.0],
    GROWTH=1,
    MONODTERMS=[
        ['Xylene', 5e-06, 1.0],
        ['Sulfate', 2e-08, 1.0],
    ],
    INHIBITIONTERMS=['Oxygen', 1e-07, 1.0],
    PRODUCTIONSTOCH=[
        ['Xylene', -31.2],
        ['Sulfate', -165.45],
        ['S', 249.6],
        ['Meta_ProductS', 249.6],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='DoubleMonodDecay',
    TYPE='monod',
    BACTERIANAME='Biomass_Sulfatereducer',
    EQUATION=['Biomass_Sulfatereducer', '=', 'Biomass_Sulfatereducer'],
    RATECONSTANT=[-1.1574e-08, 1.0],
    GROWTH=1,
    MONODTERMS=[],
    INHIBITIONTERMS=[],
    PRODUCTIONTERMS=[],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Cons_Tracer',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Xylene',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Oxygen',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Metab_O',
    MOBILE=0,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO2',
    MOBILE=0,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Biomass_Aerobic',
    MOBILE=0,
    DIFFUSION=[1, 0.0],
    TRANSPORT_PHASE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Goethite',
    MOBILE=0,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='bioFe3',
    MOBILE=0,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Fe2',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Metab_Fe3',
    MOBILE=0,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Biomass_Ironreducer',
    MOBILE=0,
    DIFFUSION=[1, 0.0],
    TRANSPORT_PHASE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Sulfate',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='S',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=0,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Meta_ProductS',
    MOBILE=0,
    DIFFUSION=[1, 1e-09],
    TRANSPORT_PHASE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Biomass_Sulfatereducer',
    MOBILE=0,
    DIFFUSION=[1, 0.0],
    TRANSPORT_PHASE=2,
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
    NAME='Layer1',
    GEO_TYPE=['LAYER', 1],
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.24],
    VOL_BIO=[1, 0.01],
    VOL_MAT=[1, 0.75],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.00215],
    MASS_DISPERSION=[1, 0.25, 0.05],
    DENSITY=[1, 2000.0],
)
model.msh.read_file('h2_line.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 2000, 0.5, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='NO_PCS',
    NOD_VALUES=[
        ['HEAD'],
        ['Cons_Tracer'],
        ['Xylene'],
        ['Oxygen'],
        ['Metab_O'],
        ['CO2'],
        ['Biomass_Aerobic'],
        ['Goethite'],
        ['bioFe3'],
        ['Metab_Fe3'],
        ['Fe2'],
        ['Biomass_Ironreducer'],
        ['Sulfate'],
        ['S'],
        ['Meta_ProductS'],
        ['Biomass_Sulfatereducer'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 20],
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
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', -0.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[200, 432000.0],
    TIME_END=1.44e+65,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[200, 432000.0],
    TIME_END=1.44e+65,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
