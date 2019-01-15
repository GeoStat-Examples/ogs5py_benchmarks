# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS, GEMinit, ASC

model = OGS(
    task_root='ab1d_root',
    task_id='ab1d',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 10.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 10.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Ael',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Bel',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 2],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-H',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.000199450916354453],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Inrt',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-O',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0100997255469342],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Zz',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Ael',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 3],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Bel',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 1.0],
    TIM_TYPE=['CURVE', 4],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-H',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.000199449988669848],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Inrt',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-O',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.0100997250739968],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Zz',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gem.add_block(
    main_key='GEM_PROPERTIES',
    GEM_THREADS=1,
    GEM_INIT_FILE='TestSolub-dat.lst',
    FLAG_CALCULATE_BOUNDARY_NODE=1,
    FLAG_POROSITY_CHANGE=1,
    MIN_POROSITY=1e-15,
    MAX_POROSITY=1.0,
    FLAG_COUPLING_HYDROLOGY=0,
    TEMPERATURE_GEM=298.15,
    TRANSPORT_B=1,
    KINETIC_GEM=[
        ['AB-solid', 1, 1, 0.0, 0.0, 0.0, 0.0, -7.69897, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 'H+', 0.0, 0.0, 0.0],
        [4, 10000.0],
    ],
)
model.gli.read_file('ab1d.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 10.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Zz',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='1-Ael',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='2-Bel',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='3-H',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='4-Inrt',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='5-O',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='6-Zz',
    MOBILE=1,
    DIFFUSION=[9, 1e-10, 1.0],
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
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.157e-06],
    MASS_DISPERSION=[1, 0.0067, 0.00067],
    DENSITY=[1, 1800.0],
)
model.msh.read_file('ab1d.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
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
        ['1-Ael'],
        ['2-Bel'],
        ['3-H'],
        ['4-Inrt'],
        ['5-O'],
        ['6-Zz'],
    ],
    ELE_VALUES=[
        ['POROSITY'],
        ['VELOCITY_X'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='VTK',
    TIM_TYPE=['STEPS', 10],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
    RELOAD=[2, 1],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 1.186390678805],
        [100.0, 1.188239098615],
        [200.0, 1.190103572204],
        [300.0, 1.1919841708],
        [400.0, 1.193880963792],
        [500.0, 1.195794018649],
        [600.0, 1.197723400848],
        [700.0, 1.199669173786],
        [800.0, 1.201631398706],
        [900.0, 1.203610134608],
        [1000.0, 1.205605438167],
        [1100.0, 1.207617363646],
        [1200.0, 1.209645962809],
        [1300.0, 1.211691284832],
        [1400.0, 1.213753376212],
        [1500.0, 1.215832280674],
        [1600.0, 1.21792803908],
        [1700.0, 1.22004068933],
        [1800.0, 1.222170266273],
        [1900.0, 1.224316801602],
        [2000.0, 1.226480323761],
        [2100.0, 1.228660857841],
        [2200.0, 1.230858425484],
        [2300.0, 1.233073044776],
        [2400.0, 1.235304730148],
        [2500.0, 1.237553492267],
        [2600.0, 1.239819337936],
        [2700.0, 1.242102269988],
        [2800.0, 1.244402287175],
        [2900.0, 1.246719384064],
        [3000.0, 1.24905355093],
        [3100.0, 1.251404773645],
        [3200.0, 1.25377303357],
        [3300.0, 1.256158307447],
        [3400.0, 1.25856056729],
        [3500.0, 1.260979780271],
        [3600.0, 1.263415908618],
        [3700.0, 1.2658689095],
        [3800.0, 1.268338734917],
        [3900.0, 1.270825331598],
        [4000.0, 1.273328640886],
        [4100.0, 1.275848598632],
        [4200.0, 1.278385135092],
        [4300.0, 1.280938174816],
        [4400.0, 1.283507636546],
        [4500.0, 1.286093433112],
        [4600.0, 1.28869547133],
        [4700.0, 1.291313651902],
        [4800.0, 1.293947869317],
        [4900.0, 1.296598011752],
        [5000.0, 1.299263960982],
        [5100.0, 1.301945592285],
        [5200.0, 1.304642774351],
        [5300.0, 1.307355369198],
        [5400.0, 1.310083232088],
        [5500.0, 1.312826211443],
        [5600.0, 1.315584148768],
        [5700.0, 1.318356878583],
        [5800.0, 1.321144228344],
        [5900.0, 1.323946018382],
        [6000.0, 1.326762061843],
        [6100.0, 1.329592164625],
        [6200.0, 1.332436125329],
        [6300.0, 1.33529373521],
        [6400.0, 1.338164778135],
        [6500.0, 1.341049030545],
        [6600.0, 1.343946261422],
        [6700.0, 1.346856232268],
        [6800.0, 1.349778697077],
        [6900.0, 1.352713402329],
        [7000.0, 1.355660086976],
        [7100.0, 1.358618482449],
        [7200.0, 1.361588312657],
        [7300.0, 1.364569294005],
        [7400.0, 1.367561135411],
        [7500.0, 1.370563538339],
        [7600.0, 1.373576196831],
        [7700.0, 1.376598797549],
        [7800.0, 1.379631019834],
        [7900.0, 1.382672535755],
        [8000.0, 1.385723010189],
        [8100.0, 1.388782100885],
        [8200.0, 1.39184945856],
        [8300.0, 1.394924726986],
        [8400.0, 1.398007543094],
        [8500.0, 1.401097537086],
        [8600.0, 1.404194332554],
        [8700.0, 1.407297546611],
        [8800.0, 1.410406790027],
        [8900.0, 1.413521667376],
        [9000.0, 1.416641777196],
        [9100.0, 1.419766712149],
        [9200.0, 1.422896059199],
        [9300.0, 1.426029399793],
        [9400.0, 1.429166310054],
        [9500.0, 1.432306360981],
        [9600.0, 1.43544911866],
        [9700.0, 1.438594144479],
        [9800.0, 1.441740995358],
        [9900.0, 1.444889223981],
        [10000.0, 1.448038379038],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 0.8136093211948],
        [100.0, 0.8117609013848],
        [200.0, 0.8098964277958],
        [300.0, 0.8080158291996],
        [400.0, 0.8061190362081],
        [500.0, 0.8042059813506],
        [600.0, 0.802276599152],
        [700.0, 0.8003308262136],
        [800.0, 0.7983686012937],
        [900.0, 0.796389865392],
        [1000.0, 0.7943945618334],
        [1100.0, 0.7923826363544],
        [1200.0, 0.790354037191],
        [1300.0, 0.7883087151676],
        [1400.0, 0.7862466237876],
        [1500.0, 0.7841677193256],
        [1600.0, 0.7820719609203],
        [1700.0, 0.7799593106697],
        [1800.0, 0.7778297337271],
        [1900.0, 0.7756831983981],
        [2000.0, 0.7735196762395],
        [2100.0, 0.7713391421589],
        [2200.0, 0.7691415745159],
        [2300.0, 0.7669269552237],
        [2400.0, 0.7646952698525],
        [2500.0, 0.7624465077334],
        [2600.0, 0.7601806620636],
        [2700.0, 0.7578977300117],
        [2800.0, 0.7555977128249],
        [2900.0, 0.7532806159355],
        [3000.0, 0.7509464490697],
        [3100.0, 0.7485952263551],
        [3200.0, 0.7462269664301],
        [3300.0, 0.7438416925528],
        [3400.0, 0.7414394327105],
        [3500.0, 0.7390202197288],
        [3600.0, 0.7365840913817],
        [3700.0, 0.7341310905004],
        [3800.0, 0.7316612650827],
        [3900.0, 0.7291746684017],
        [4000.0, 0.7266713591141],
        [4100.0, 0.7241514013676],
        [4200.0, 0.7216148649077],
        [4300.0, 0.7190618251839],
        [4400.0, 0.716492363454],
        [4500.0, 0.713906566888],
        [4600.0, 0.7113045286698],
        [4700.0, 0.7086863480977],
        [4800.0, 0.7060521306833],
        [4900.0, 0.7034019882481],
        [5000.0, 0.700736039018],
        [5100.0, 0.6980544077154],
        [5200.0, 0.6953572256492],
        [5300.0, 0.6926446308015],
        [5400.0, 0.6899167679117],
        [5500.0, 0.6871737885574],
        [5600.0, 0.6844158512316],
        [5700.0, 0.6816431214172],
        [5800.0, 0.6788557716565],
        [5900.0, 0.6760539816177],
        [6000.0, 0.6732379381569],
        [6100.0, 0.6704078353751],
        [6200.0, 0.6675638746713],
        [6300.0, 0.6647062647903],
        [6400.0, 0.6618352218653],
        [6500.0, 0.6589509694555],
        [6600.0, 0.6560537385776],
        [6700.0, 0.653143767732],
        [6800.0, 0.6502213029228],
        [6900.0, 0.6472865976714],
        [7000.0, 0.6443399130236],
        [7100.0, 0.6413815175507],
        [7200.0, 0.6384116873427],
        [7300.0, 0.6354307059952],
        [7400.0, 0.6324388645887],
        [7500.0, 0.6294364616606],
        [7600.0, 0.6264238031693],
        [7700.0, 0.6234012024507],
        [7800.0, 0.6203689801664],
        [7900.0, 0.6173274642446],
        [8000.0, 0.6142769898115],
        [8100.0, 0.6112178991149],
        [8200.0, 0.6081505414397],
        [8300.0, 0.6050752730138],
        [8400.0, 0.6019924569058],
        [8500.0, 0.598902462914],
        [8600.0, 0.5958056674458],
        [8700.0, 0.592702453389],
        [8800.0, 0.5895932099735],
        [8900.0, 0.586478332624],
        [9000.0, 0.583358222804],
        [9100.0, 0.5802332878508],
        [9200.0, 0.5771039408008],
        [9300.0, 0.5739706002068],
        [9400.0, 0.5708336899459],
        [9500.0, 0.5676936390187],
        [9600.0, 0.56455088134],
        [9700.0, 0.5614058555207],
        [9800.0, 0.5582590046418],
        [9900.0, 0.5551107760193],
        [10000.0, 0.5519616209621],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 1.02478458751],
        [100.0, 1.025045161539],
        [200.0, 1.025308469437],
        [300.0, 1.025574539704],
        [400.0, 1.025843401133],
        [500.0, 1.026115082812],
        [600.0, 1.026389614125],
        [700.0, 1.026667024756],
        [800.0, 1.02694734469],
        [900.0, 1.027230604221],
        [1000.0, 1.027516833948],
        [1100.0, 1.027806064784],
        [1200.0, 1.028098327955],
        [1300.0, 1.028393655003],
        [1400.0, 1.028692077793],
        [1500.0, 1.028993628511],
        [1600.0, 1.02929833967],
        [1700.0, 1.029606244113],
        [1800.0, 1.029917375013],
        [1900.0, 1.030231765881],
        [2000.0, 1.030549450566],
        [2100.0, 1.030870463257],
        [2200.0, 1.031194838489],
        [2300.0, 1.031522611146],
        [2400.0, 1.031853816459],
        [2500.0, 1.032188490019],
        [2600.0, 1.032526667769],
        [2700.0, 1.032868386016],
        [2800.0, 1.03321368143],
        [2900.0, 1.033562591048],
        [3000.0, 1.033915152278],
        [3100.0, 1.034271402901],
        [3200.0, 1.034631381075],
        [3300.0, 1.034995125338],
        [3400.0, 1.035362674614],
        [3500.0, 1.035734068211],
        [3600.0, 1.036109345828],
        [3700.0, 1.03648854756],
        [3800.0, 1.036871713896],
        [3900.0, 1.037258885728],
        [4000.0, 1.03765010435],
        [4100.0, 1.038045411465],
        [4200.0, 1.038444849186],
        [4300.0, 1.038848460039],
        [4400.0, 1.03925628697],
        [4500.0, 1.039668373345],
        [4600.0, 1.040084762953],
        [4700.0, 1.040505500013],
        [4800.0, 1.040930629176],
        [4900.0, 1.041360195526],
        [5000.0, 1.041794244587],
        [5100.0, 1.042232822323],
        [5200.0, 1.042675975145],
        [5300.0, 1.043123749913],
        [5400.0, 1.043576193938],
        [5500.0, 1.044033354988],
        [5600.0, 1.044495281291],
        [5700.0, 1.044962021535],
        [5800.0, 1.045433624877],
        [5900.0, 1.045910140942],
        [6000.0, 1.046391619829],
        [6100.0, 1.046878112114],
        [6200.0, 1.047369668851],
        [6300.0, 1.047866341579],
        [6400.0, 1.048368182324],
        [6500.0, 1.048875243602],
        [6600.0, 1.049387578421],
        [6700.0, 1.049905240288],
        [6800.0, 1.05042828321],
        [6900.0, 1.050956761695],
        [7000.0, 1.051490730761],
        [7100.0, 1.052030245934],
        [7200.0, 1.052575363254],
        [7300.0, 1.053126139277],
        [7400.0, 1.053682631079],
        [7500.0, 1.054244896258],
        [7600.0, 1.054812992938],
        [7700.0, 1.055386979773],
        [7800.0, 1.055966915947],
        [7900.0, 1.056552861178],
        [8000.0, 1.057144875724],
        [8100.0, 1.057743020382],
        [8200.0, 1.058347356492],
        [8300.0, 1.05895794594],
        [8400.0, 1.05957485116],
        [8500.0, 1.060198135138],
        [8600.0, 1.060827861413],
        [8700.0, 1.06146409408],
        [8800.0, 1.062106897793],
        [8900.0, 1.062756337764],
        [9000.0, 1.063412479773],
        [9100.0, 1.064075390159],
        [9200.0, 1.064745135832],
        [9300.0, 1.065421784269],
        [9400.0, 1.066105403518],
        [9500.0, 1.066796062201],
        [9600.0, 1.06749382951],
        [9700.0, 1.068198775217],
        [9800.0, 1.068910969667],
        [9900.0, 1.069630483786],
        [10000.0, 1.070357389076],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 0.9752154124897],
        [100.0, 0.9749548384605],
        [200.0, 0.9746915305633],
        [300.0, 0.9744254602964],
        [400.0, 0.974156598867],
        [500.0, 0.9738849171878],
        [600.0, 0.973610385875],
        [700.0, 0.9733329752445],
        [800.0, 0.9730526553098],
        [900.0, 0.972769395779],
        [1000.0, 0.9724831660515],
        [1100.0, 0.9721939352156],
        [1200.0, 0.9719016720451],
        [1300.0, 0.9716063449968],
        [1400.0, 0.971307922207],
        [1500.0, 0.9710063714891],
        [1600.0, 0.97070166033],
        [1700.0, 0.9703937558875],
        [1800.0, 0.970082624987],
        [1900.0, 0.9697682341187],
        [2000.0, 0.969450549434],
        [2100.0, 0.9691295367428],
        [2200.0, 0.9688051615105],
        [2300.0, 0.9684773888544],
        [2400.0, 0.9681461835406],
        [2500.0, 0.9678115099813],
        [2600.0, 0.9674733322311],
        [2700.0, 0.9671316139839],
        [2800.0, 0.9667863185698],
        [2900.0, 0.9664374089516],
        [3000.0, 0.9660848477217],
        [3100.0, 0.965728597099],
        [3200.0, 0.9653686189252],
        [3300.0, 0.9650048746616],
        [3400.0, 0.9646373253861],
        [3500.0, 0.9642659317894],
        [3600.0, 0.9638906541719],
        [3700.0, 0.9635114524402],
        [3800.0, 0.9631282861039],
        [3900.0, 0.962741114272],
        [4000.0, 0.9623498956497],
        [4100.0, 0.9619545885347],
        [4200.0, 0.9615551508141],
        [4300.0, 0.9611515399608],
        [4400.0, 0.9607437130298],
        [4500.0, 0.9603316266554],
        [4600.0, 0.9599152370471],
        [4700.0, 0.9594944999865],
        [4800.0, 0.9590693708237],
        [4900.0, 0.9586398044737],
        [5000.0, 0.9582057554134],
        [5100.0, 0.9577671776774],
        [5200.0, 0.9573240248552],
        [5300.0, 0.9568762500874],
        [5400.0, 0.956423806062],
        [5500.0, 0.9559666450116],
        [5600.0, 0.9555047187091],
        [5700.0, 0.9550379784649],
        [5800.0, 0.9545663751231],
        [5900.0, 0.9540898590579],
        [6000.0, 0.9536083801708],
        [6100.0, 0.9531218878864],
        [6200.0, 0.9526303311493],
        [6300.0, 0.952133658421],
        [6400.0, 0.9516318176759],
        [6500.0, 0.9511247563982],
        [6600.0, 0.9506124215789],
        [6700.0, 0.9500947597117],
        [6800.0, 0.9495717167903],
        [6900.0, 0.9490432383051],
        [7000.0, 0.9485092692392],
        [7100.0, 0.9479697540663],
        [7200.0, 0.9474246367464],
        [7300.0, 0.9468738607234],
        [7400.0, 0.9463173689215],
        [7500.0, 0.9457551037423],
        [7600.0, 0.9451870070617],
        [7700.0, 0.9446130202269],
        [7800.0, 0.9440330840534],
        [7900.0, 0.9434471388218],
        [8000.0, 0.9428551242756],
        [8100.0, 0.9422569796177],
        [8200.0, 0.9416526435078],
        [8300.0, 0.94104205406],
        [8400.0, 0.9404251488399],
        [8500.0, 0.9398018648619],
        [8600.0, 0.9391721385869],
        [8700.0, 0.9385359059199],
        [8800.0, 0.9378931022074],
        [8900.0, 0.9372436622356],
        [9000.0, 0.9365875202274],
        [9100.0, 0.9359246098412],
        [9200.0, 0.9352548641683],
        [9300.0, 0.9345782157312],
        [9400.0, 0.9338945964817],
        [9500.0, 0.9332039377994],
        [9600.0, 0.9325061704898],
        [9700.0, 0.931801224783],
        [9800.0, 0.9310890303327],
        [9900.0, 0.9303695162142],
        [10000.0, 0.9296426109238],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[100000, 100.0],
    TIME_END=10000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100000, 100.0],
    TIME_END=10000.0,
    TIME_START=0.0,
)
gem_init_file = GEMinit(
    file_name='TestSolub-dat',
    file_ext='.lst',
)
gem_init_file.read_file('TestSolub-dat.lst')
model.add_gem_init(gem_init_file)
asc_file = ASC(
    file_name='ab1d_MASS_TRANSPORT_6-Zz_primary_value',
    file_ext='.asc',
)
asc_file.read_file('ab1d_MASS_TRANSPORT_6-Zz_primary_value.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_MASS_TRANSPORT_5-O_primary_value',
    file_ext='.asc',
)
asc_file.read_file('ab1d_MASS_TRANSPORT_5-O_primary_value.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_m_xDC_gem',
    file_ext='.asc',
)
asc_file.read_file('ab1d_m_xDC_gem.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_m_porosity_gem',
    file_ext='.asc',
)
asc_file.read_file('ab1d_m_porosity_gem.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_MASS_TRANSPORT_3-H_primary_value',
    file_ext='.asc',
)
asc_file.read_file('ab1d_MASS_TRANSPORT_3-H_primary_value.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_m_bIC_gem',
    file_ext='.asc',
)
asc_file.read_file('ab1d_m_bIC_gem.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_m_fluid_volume_gem',
    file_ext='.asc',
)
asc_file.read_file('ab1d_m_fluid_volume_gem.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_MASS_TRANSPORT_1-Ael_primary_value',
    file_ext='.asc',
)
asc_file.read_file('ab1d_MASS_TRANSPORT_1-Ael_primary_value.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_MASS_TRANSPORT_4-Inrt_primary_value',
    file_ext='.asc',
)
asc_file.read_file('ab1d_MASS_TRANSPORT_4-Inrt_primary_value.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_GROUNDWATER_FLOW_HEAD_primary_value',
    file_ext='.asc',
)
asc_file.read_file('ab1d_GROUNDWATER_FLOW_HEAD_primary_value.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_MASS_TRANSPORT_2-Bel_primary_value',
    file_ext='.asc',
)
asc_file.read_file('ab1d_MASS_TRANSPORT_2-Bel_primary_value.asc')
model.add_asc(asc_file)
asc_file = ASC(
    file_name='ab1d_time_gem',
    file_ext='.asc',
)
asc_file.read_file('ab1d_time_gem.asc')
model.add_asc(asc_file)
model.write_input()
model.run_model()
