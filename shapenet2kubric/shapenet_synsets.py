#!/usr/bin/env python3
# Copyright 2021 The Kubric Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Copyright 2021 The Kubric Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

CATEGORY_NAMES = {
    "04250224": "sniper rifle",
    "04529681": "vertical file",
    "03045228": "clipper",
    "04097373": "roadster",
    "03761084": "microwave",
    "03086457": "concert grand",
    "03710193": "mailbox",
    "03100346": "convertible",
    "02801938": "basket",
    "02843684": "birdhouse",
    "03983396": "pop bottle",
    "03165096": "daybed",
    "03909406": "pendulum clock",
    "04530566": "vessel",
    "03789171": "motion-picture camera",
    "03335030": "fighter",
    "03773504": "missile",
    "03891251": "park bench",
    "02831724": "berth",
    "03002210": "chair of state",
    "02694662": "alarm clock",
    "04152593": "screen",
    "03237340": "dresser",
    "04610013": "yacht",
    "04608329": "writing desk",
    "03046257": "clock",
    "04363082": "surface ship",
    "03261776": "earphone",
    "02814860": "beacon",
    "03759954": "microphone",
    "04164868": "secretary",
    "03642806": "laptop",
    "04522168": "vase",
    "03196062": "digital camera",
    "04515003": "upright",
    "03063599": "coffee mug",
    "04349401": "subwoofer",
    "02823428": "beer bottle",
    "03676759": "liquid crystal display",
    "03630262": "lab bench",
    "02808440": "bathtub",
    "04468005": "train",
    "03881534": "panda car",
    "02992529": "cellular telephone",
    "04501947": "turret",
    "20000039": "short table",
    "20000038": "round table",
    "03938244": "pillow",
    "03673027": "liner",
    "20000030": "leather couch",
    "20000037": "rectangular table",
    "20000036": "cabinet table",
    "02946270": "camp chair",
    "02884994": "box camera",
    "02773838": "bag",
    "03180732": "destroyer escort",
    "02676566": "acoustic guitar",
    "04222210": "single bed",
    "03466162": "guided missile",
    "03464628": "guard boat",
    "04554684": "washer",
    "03896103": "passenger ship",
    "03029197": "church tower",
    "03785016": "moped",
    "03643737": "laser printer",
    "03231368": "drafting table",
    "03015149": "chesterfield",
    "04398951": "tea table",
    "02842573": "biplane",
    "02818832": "bed",
    "03254374": "dugout canoe",
    "03809312": "narrowbody aircraft",
    "04349306": "subway train",
    "02691156": "airplane",
    "04583620": "widebody aircraft",
    "03594945": "jeep",
    "03207941": "dishwasher",
    "03063968": "coffee table",
    "02964075": "card table",
    "03604311": "jumbojet",
    "03196598": "digital display",
    "03948459": "pistol",
    "04487081": "trolleybus",
    "02920259": "bunk bed",
    "03360622": "flat bench",
    "04552696": "warship",
    "03811295": "nautilus",
    "03482405": "hamper",
    "04576002": "wheelchair",
    "04590933": "Windsor chair",
    "04569063": "webcam",
    "03718212": "man-of-war",
    "03850492": "operating table",
    "02690373": "airliner",
    "03786621": "Morris chair",
    "04380533": "table lamp",
    "02823510": "beer can",
    "03376595": "folding chair",
    "03513137": "helmet",
    "04224543": "sister ship",
    "02920083": "bunk",
    "03078802": "commuter",
    "04590021": "window seat",
    "02755529": "attack submarine",
    "04301000": "stand",
    "04401088": "telephone",
    "04255768": "soda fountain",
    "04128837": "sailing vessel",
    "03168217": "deck chair",
    "03262932": "easy chair",
    "02769075": "background",
    "03260849": "Eames chair",
    "02924116": "bus",
    "04361260": "supporting tower",
    "03114504": "cot",
    "04312432": "steeple",
    "20000013": "two-door cabinet",
    "20000012": "tall cabinet",
    "04004475": "printer",
    "03467517": "guitar",
    "04256520": "sofa",
    "03018349": "china cabinet",
    "03649674": "lawn chair",
    "04567746": "weather ship",
    "03180504": "destroyer",
    "04591631": "wine bar",
    "02789487": "bar",
    "03141065": "cruiser",
    "03957315": "planter",
    "04285965": "sport utility",
    "03238586": "dressing table",
    "04265428": "space helmet",
    "02929923": "buzz bomb",
    "04322801": "stock car",
    "04459122": "touring car",
    "04556948": "watchtower",
    "03211117": "display",
    "03095699": "container ship",
    "02793199": "bark",
    "02954340": "cap",
    "02874214": "booth",
    "03100240": "convertible",
    "04559451": "water faucet",
    "02867715": "bomber",
    "20000008": "bed cabinet",
    "20000009": "box cabinet",
    "20000006": "king size beds",
    "20000007": "misc beds",
    "20000004": "headboard beds",
    "20000005": "headless beds",
    "20000002": "transport airplane",
    "20000000": "straight wing",
    "20000001": "swept wing",
    "02932891": "cabin cruiser",
    "02964196": "card table",
    "03141327": "cruise ship",
    "03179701": "desk",
    "03085013": "computer keyboard",
    "04460130": "tower",
    "03543394": "hot rod",
    "02826886": "bell tower",
    "03920867": "pew",
    "03693474": "love seat",
    "04330267": "stove",
    "04037443": "racer",
    "02871439": "bookshelf",
    "03845190": "oil tanker",
    "03085219": "computer monitor",
    "04086273": "revolver",
    "03321419": "fanjet",
    "04158807": "sea boat",
    "04593077": "wing chair",
    "04348184": "submersible",
    "04194289": "ship",
    "03246933": "drop-leaf table",
    "04225987": "skateboard",
    "04061681": "reception desk",
    "03367059": "floor lamp",
    "03359566": "flask",
    "04599124": "woofer",
    "02792552": "barge",
    "03329663": "ferry",
    "04115456": "rowing boat",
    "03603722": "jug",
    "03090000": "conference table",
    "03119396": "coupe",
    "04436012": "tilt-top table",
    "04090263": "rifle",
    "04166281": "sedan",
    "03158885": "dagger",
    "03900194": "patrol boat",
    "03092883": "console table",
    "03394480": "freight train",
    "20000040": "side table",
    "20000041": "workshop table",
    "03595860": "jet",
    "02965300": "cargo ship",
    "03174079": "delta wing",
    "02781338": "ballistic missile",
    "04206790": "shot tower",
    "04502670": "tweeter",
    "03498781": "hatchback",
    "03769722": "minibike",
    "03347617": "fire tower",
    "04379243": "table",
    "04309348": "steamer",
    "03519387": "high-rise",
    "04429376": "throne",
    "03939178": "pilot boat",
    "03962852": "platform bed",
    "04024983": "punt",
    "02834778": "bicycle",
    "03358726": "flash camera",
    "04244997": "small boat",
    "03140900": "cruiser",
    "02699629": "altar",
    "02811618": "battle cruiser",
    "03545470": "houseboat",
    "03049924": "cloth cap",
    "03896233": "passenger train",
    "03775636": "mixing faucet",
    "03859170": "outboard motorboat",
    "04409011": "tender",
    "04381587": "table-tennis table",
    "04012084": "propeller plane",
    "04146614": "school bus",
    "04095210": "river boat",
    "04177820": "settle",
    "02958343": "car",
    "04099969": "rocking chair",
    "03928116": "piano",
    "02738535": "armchair",
    "03002711": "chaise longue",
    "03351262": "fishing boat",
    "02799323": "baseball cap",
    "03610682": "kepi",
    "03609235": "kayak",
    "04409128": "tender",
    "04263257": "soup bowl",
    "03797390": "mug",
    "02981792": "catamaran",
    "04582349": "wicker basket",
    "03379051": "football helmet",
    "04062428": "recliner",
    "04074963": "remote control",
    "03199901": "dinghy",
    "03373611": "flying boat",
    "04591713": "wine bottle",
    "03790512": "motorcycle",
    "03636649": "lamp",
    "02814533": "beach wagon",
    "02824058": "beer mug",
    "03179910": "desk phone",
    "03280644": "electrostatic printer",
    "02880940": "bowl",
    "03982430": "pool table",
    "04331277": "straight chair",
    "03452741": "grand piano",
    "02942699": "camera",
    "03001627": "chair",
    "20000011": "garage cabinet",
    "20000010": "desk cabinet",
    "04028581": "pylon",
    "04603729": "worktable",
    "20000015": "ball chair",
    "04548280": "wall clock",
    "20000016": "barcelona chair",
    "20000019": "butterfly chair",
    "20000018": "bean chair",
    "03452594": "grandfather clock",
    "03115762": "couch",
    "03981566": "pontoon",
    "03620967": "kitchen table",
    "02952374": "canteen",
    "03977592": "police boat",
    "02693413": "air-to-air missile",
    "02933112": "cabinet",
    "03085602": "computer screen",
    "02956393": "capital ship",
    "04347754": "submarine",
    "03782190": "monitor",
    "02747177": "ashcan",
    "04255586": "soda can",
    "03388549": "four-poster",
    "03870105": "pace car",
    "03624134": "knife",
    "04466871": "trail bike",
    "03164605": "davenport",
    "03488438": "handset",
    "04160586": "seaplane",
    "03541269": "hospital ship",
    "04363210": "surface-to-air missile",
    "02687172": "aircraft carrier",
    "04177755": "settee",
    "03670208": "limousine",
    "03770679": "minivan",
    "03923379": "phial",
    "03904060": "pedestal table",
    "03492922": "hard hat",
    "02858304": "boat",
    "02828884": "bench",
    "04387095": "tam",
    "02894337": "breakfast table",
    "03632729": "ladder-back",
    "03991062": "pot",
    "03050864": "clothes hamper",
    "02947660": "canal boat",
    "02946921": "can",
    "03540914": "hospital bed",
    "03116530": "counter",
    "02930766": "cab",
    "20000028": "double couch",
    "20000029": "L-shaped couch",
    "02701002": "ambulance",
    "04220250": "silo",
    "20000020": "cantilever chair",
    "20000021": "NO. 14 chair",
    "20000022": "rex chair",
    "20000023": "tulip chair",
    "20000024": "wassily chair",
    "20000025": "X chair",
    "20000026": "zigzag chair",
    "20000027": "club chair",
    "03691459": "loudspeaker",
    "04285008": "sports car",
    "03986949": "portmantea",
    "03653583": "lectern",
    "03211616": "display panel",
    "02812949": "bayonet",
    "04128499": "sailboat",
    "03325088": "faucet",
    "02957862": "captain's chair",
    "03742115": "medicine chest",
    "04344873": "studio couch",
    "03593526": "jar",
    "04600486": "workbench",
    "03790230": "motorboat",
    "02961451": "carbine",
    "03047052": "clock tower",
    "04273569": "speedboat",
    "03947888": "pirate",
    "02876657": "bottle",
    "03482252": "hammock",
    "04099429": "rocket",
    "03465151": "guard ship",
    "03361380": "flat panel display",
    "02971579": "car train",
    "03337140": "file",
    "04044498": "radiotelephone",
    "02951358": "canoe",
    "03011741": "checkout",
    "04146862": "school ship",
    "04373704": "swivel chair"}