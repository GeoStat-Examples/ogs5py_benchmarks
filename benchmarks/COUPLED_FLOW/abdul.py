# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS, GLIext

model = OGS(
    task_root='abdul_root',
    task_id='abdul',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT8'],
    DIS_TYPE=['CONSTANT', 3.0586544],
)
model.gli.read_file('abdul.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0001],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['GRADIENT', 0, 0, 9810],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEO_TYPE=['SURFACE:', 'SURFACE0'],
    SURFACE_FRICTION=[6.67, 0.5, 0.667],
    RILL=[0.001, 0.0001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.33],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2.95e-13],
    PERMEABILITY_SATURATION=[4, 0, 1.0, 0.336],
    CAPILLARY_PRESSURE=[4, 1.43],
)
model.msh.read_file('abdul.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='OVERLAND_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['NEWTON', 0.001, 0, 20, 0.0],
    ELE_GAUSS_POINTS=2,
    COUPLING_CONTROL=['LMAX', 1e-12],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 1.0, 20, 0.0],
    COUPLING_CONTROL=['LMAX', 1e-12],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 1, 1e-12, 1000, 1.0, 1, 2],
    COUPLING_CONTROL=['LMAX', 1e-12],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES=[
        ['HEAD'],
        ['WDEPTH'],
        ['COUPLING'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES=[
        ['WDEPTH'],
        ['HEAD'],
        ['FLUX'],
    ],
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES=[
        ['WDEPTH'],
        ['HEAD'],
        ['FLUX'],
    ],
    GEO_TYPE=['POINT', 'POINT5'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POLYLINE', 'OUTPUT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='GROUNDWATER_FLOW',
    NOD_VALUES=[
        ['HEAD'],
        ['PRESSURE'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='OVERLAND_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.add_block(
    PROJECT=['Triangle', 'elements', 'for', 'flow'],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 1e-06],
        [50000.0, 1e-06],
        [51000.0, 0.0],
        [100000.0, 0.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0, 6e-06],
        [899, 6e-06],
        [900, 0.0],
        [2000, 0.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.263158, 94762.59157],
        [0.267515, 91685.9559],
        [0.271874, 88744.95928],
        [0.276233, 85940.07159],
        [0.280595, 83261.14768],
        [0.28496, 80700.7136],
        [0.289328, 78251.84117],
        [0.293701, 75907.05201],
        [0.298078, 73661.0092],
        [0.302461, 71507.25135],
        [0.306851, 69440.31488],
        [0.311247, 67456.02925],
        [0.315651, 65549.18104],
        [0.320064, 63715.38317],
        [0.324486, 61950.95509],
        [0.328918, 60252.06796],
        [0.333361, 58615.1618],
        [0.337815, 57037.27056],
        [0.342281, 55515.26757],
        [0.34676, 54046.23781],
        [0.351252, 52627.77081],
        [0.355759, 51256.99285],
        [0.36028, 49932.10492],
        [0.364817, 48650.54561],
        [0.36937, 47410.47418],
        [0.373941, 46209.62864],
        [0.378529, 45046.65518],
        [0.383135, 43919.76368],
        [0.387761, 42827.04154],
        [0.392406, 41767.38204],
        [0.397104, 40732.12909],
        [0.401858, 39720.16941],
        [0.406638, 38737.14486],
        [0.411449, 37781.03921],
        [0.416295, 36850.19883],
        [0.42118, 35943.10391],
        [0.423638, 35498.08728],
        [0.426107, 35058.53414],
        [0.428587, 34624.37211],
        [0.431079, 34195.3589],
        [0.433584, 33771.26437],
        [0.436102, 33352.03506],
        [0.438633, 32937.61774],
        [0.441178, 32527.79967],
        [0.443737, 32122.53595],
        [0.446312, 31721.47272],
        [0.448901, 31324.88412],
        [0.451506, 30932.4261],
        [0.454128, 30543.92126],
        [0.456766, 30159.49049],
        [0.459421, 29778.96016],
        [0.462094, 29402.16562],
        [0.464785, 29029.08831],
        [0.467495, 28659.57361],
        [0.470223, 28293.74107],
        [0.472971, 27931.30808],
        [0.47574, 27572.13726],
        [0.478528, 27216.47816],
        [0.481338, 26863.94025],
        [0.484169, 26514.64633],
        [0.487022, 26168.46907],
        [0.489897, 25825.40633],
        [0.492795, 25485.33834],
        [0.495717, 25148.1518],
        [0.498662, 24813.96475],
        [0.501631, 24482.66488],
        [0.504625, 24154.14602],
        [0.507645, 23828.30782],
        [0.51069, 23505.26598],
        [0.513761, 23184.9206],
        [0.516858, 22867.27898],
        [0.519983, 22552.14688],
        [0.523135, 22239.63692],
        [0.526316, 21929.56335],
        [0.529729, 21602.66333],
        [0.533178, 21278.24899],
        [0.536668, 20955.89337],
        [0.540203, 20635.28979],
        [0.543786, 20316.24252],
        [0.547424, 19998.22487],
        [0.551118, 19681.26069],
        [0.554875, 19364.87447],
        [0.558697, 19049.03868],
        [0.56259, 18733.411],
        [0.566557, 18417.91614],
        [0.570603, 18102.33587],
        [0.574732, 17786.55074],
        [0.578947, 17470.53192],
        [0.583206, 17157.53416],
        [0.587558, 16844.07072],
        [0.592008, 16530.00691],
        [0.596559, 16215.36452],
        [0.601214, 15900.17278],
        [0.605979, 15584.27103],
        [0.610857, 15267.71425],
        [0.615852, 14950.50006],
        [0.620968, 14632.6364],
        [0.626209, 14314.14069],
        [0.631579, 13995.0391],
        [0.637949, 13625.66043],
        [0.644473, 13257.23744],
        [0.65113, 12891.18689],
        [0.657895, 12528.99386],
        [0.663722, 12224.61594],
        [0.66961, 11923.9151],
        [0.675554, 11627.09393],
        [0.681553, 11334.1369],
        [0.687604, 11045.11659],
        [0.693705, 10760.0451],
        [0.699853, 10478.97041],
        [0.706045, 10201.92788],
        [0.71228, 9928.854474],
        [0.718554, 9659.810718],
        [0.724866, 9394.718478],
        [0.731212, 9133.618943],
        [0.73759, 8876.461012],
        [0.743998, 8623.188332],
        [0.750433, 8373.778018],
        [0.756893, 8128.162014],
        [0.763374, 7886.342009],
        [0.769876, 7648.165191],
        [0.776395, 7413.623049],
        [0.782928, 7182.663486],
        [0.789474, 6955.159914],
        [0.798107, 6660.805846],
        [0.806849, 6368.932743],
        [0.815789, 6076.460542],
        [0.824396, 5800.212352],
        [0.83319, 5522.944326],
        [0.842105, 5246.567946],
        [0.850821, 4980.512299],
        [0.859591, 4716.511165],
        [0.868421, 4453.994132],
        [0.877148, 4197.302197],
        [0.885924, 3941.421366],
        [0.894737, 3686.164196],
        [0.903489, 3433.730071],
        [0.912262, 3181.024074],
        [0.921053, 2927.283496],
        [0.930467, 2653.810363],
        [0.939798, 2379.407612],
        [0.948947, 2105.103423],
        [0.960526, 1745.971671],
        [0.973684, 1309.857679],
        [0.980978, 1045.469781],
        [0.986842, 812.064433],
        [0.99, 673.9199562],
        [0.992883, 535.6239947],
        [0.995438, 397.315566],
        [0.997773, 246.0336965],
        [1, 0.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.263158, 2.07503e-05],
        [0.298078, 4.66308e-05],
        [0.401858, 0.00032926],
        [0.448901, 0.000685049],
        [0.501631, 0.001439977],
        [0.551118, 0.002726198],
        [0.601214, 0.004971344],
        [0.65113, 0.008733459],
        [0.699853, 0.014760626],
        [0.706045, 0.015757066],
        [0.750433, 0.025008577],
        [0.798107, 0.040802981],
        [0.806849, 0.044637085],
        [0.824396, 0.053492718],
        [0.842105, 0.064318363],
        [0.850821, 0.07048909],
        [0.868421, 0.085030454],
        [0.877148, 0.093469847],
        [0.894737, 0.113614792],
        [0.903489, 0.125556289],
        [0.912262, 0.139120665],
        [0.921053, 0.154636926],
        [0.930467, 0.173877476],
        [0.939798, 0.196331427],
        [0.948947, 0.222616279],
        [0.960526, 0.264385035],
        [0.973684, 0.330504916],
        [0.980978, 0.382377217],
        [0.986842, 0.439029657],
        [0.99, 0.479216859],
        [0.992883, 0.526322329],
        [0.995438, 0.58312444],
        [0.997773, 0.663125026],
        [1, 1],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 0.5],
        [10000.0, 0.6],
        [20000.0, 0.7],
        [30000.0, 0.8],
        [40000.0, 0.9],
        [50000.0, 1.0],
        [60000.0, 0.9],
        [70000.0, 0.8],
        [80000.0, 0.7],
        [90000.0, 0.6],
        [100000.0, 0.5],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'TOPO'],
    DIS_TYPE=['CONSTANT_NEUMANN', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'CRITICALDEPTH'],
    DIS_TYPE=[
        ['CRITICALDEPTH', 1],
        [0.0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['COLUMN', 'TOP'],
    DIS_TYPE=[
        ['CONSTANT', 1],
        ['PCS', 'OVERLAND_FLOW'],
        ['HEAD'],
        [0.0275, 0.001],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_END=20,
    TIME_START=0.0,
    TIME_STEPS=[1, 0.7],
)
gli_ext_file = GLIext(
    file_name='SFC_BC_RIGHT_L1',
    file_ext='.tin',
)
gli_ext_file.read_file('SFC_BC_RIGHT_L1.tin')
model.add_gli_ext(gli_ext_file)
gli_ext_file = GLIext(
    file_name='SFC_BC_LEFT_L1',
    file_ext='.tin',
)
gli_ext_file.read_file('SFC_BC_LEFT_L1.tin')
model.add_gli_ext(gli_ext_file)
model.write_input()
model.run_model()
