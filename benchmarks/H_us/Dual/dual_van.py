# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='dual_van_root',
    task_id='dual_van',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', -98100],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', -98100],
)
model.gli.read_file('dual_van.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', -98100],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', -98100],
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
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.5],
    TORTUOSITY=[1, 0.8],
    STORAGE=[1, 1.019367991845056e-09],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.2418828104353078e-14],
    HEAT_DISPERSION=[1, 1.0, 1.0],
    PERMEABILITY_SATURATION=[4, 0.21052, 1.0, 0.3333333333333333],
    CAPILLARY_PRESSURE=[4, 0.5],
    TRANSFER_COEFFICIENT=120.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.5],
    TORTUOSITY=[1, 0.8],
    STORAGE=[1, 1.019367991845056e-09],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2.359648129270963e-11],
    HEAT_DISPERSION=[1, 1.0, 1.0],
    PERMEABILITY_SATURATION=[4, 0.0, 1.0, 0.5],
    CAPILLARY_PRESSURE=[4, 10],
    TRANSFER_COEFFICIENT=120.0,
)
model.msh.read_file('dual_van.msh')
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
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 200, 0.0],
    ELE_GAUSS_POINTS=3,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['SATURATION2'],
    ],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=[
        [1e-07],
        [0.009],
        [0.01],
        [0.019],
        [0.02],
        [0.029],
        [0.03],
        [0.04],
        [0.05],
        [0.06],
        [0.07],
        [0.08],
        [0.09],
        [0.1],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
    MEDIUM_TYPE=['CONTINUUM', 0.95],
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.add_block(
    PROJECT=['NETZ', 'AUS', '1D-ELEMENTEN'],
)
model.rfd.add_block(
    CURVE=[
        [0.26315789, 4.4323e-05],
        [0.39473684, 0.00026547],
        [0.52631579, 0.00159003],
        [0.57894737, 0.00325358],
        [0.63157895, 0.00665757],
        [0.65789474, 0.00952343],
        [0.78947368, 0.05704014],
        [0.81578947, 0.08159396],
        [0.84210526, 0.11671736],
        [0.86842105, 0.16696017],
        [0.89473684, 0.23883078],
        [0.92105263, 0.34163922],
        [0.94894737, 0.49931406],
        [0.96052632, 0.58449912],
        [0.97368421, 0.69907308],
        [0.98684211, 0.8361059],
        [1.0, 1.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.26315789, 44627.5611],
        [0.39473684, 26399.6732],
        [0.52631579, 15616.8683],
        [0.57894737, 12658.7874],
        [0.63157895, 10261.0136],
        [0.65789474, 9238.24221],
        [0.78947368, 5464.93174],
        [0.81578947, 4920.21206],
        [0.84210526, 4429.78757],
        [0.86842105, 3988.24638],
        [0.89473684, 3590.71602],
        [0.92105263, 3232.80969],
        [0.94894737, 2892.29884],
        [0.96052632, 2462.21599],
        [0.97368421, 2050.45507],
        [0.98684211, 1707.55369],
        [1.0, 1421.99634],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 1.0],
        [300.0, 1.0],
        [301.0, 1.0],
        [10080.0, 1.0],
        [10081.0, 0.0],
        [100000000000.0, 0.0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.5],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_UNIT='DAY',
    TIME_END=0.1,
    TIME_START=0.0,
    TIME_STEPS=[
        [5000, 1e-07],
        [9500, 1e-06],
        [9000, 1e-05],
    ],
)
model.write_input()
model.run_model()
