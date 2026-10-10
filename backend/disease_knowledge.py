"""
AgriIntel - Structured Crop Disease Knowledge Base
Verified agricultural intelligence and botanical guidance for all 54 model classes.
"""

# Map of raw model class names to verified agricultural information.
DISEASE_KNOWLEDGE = {
    # -------------------------------------------------------------
    # APPLE (4 Classes)
    # -------------------------------------------------------------
    "Apple___Apple_scab": {
        "crop": "Apple",
        "crop_display": "Apple",
        "condition": "Apple Scab",
        "pathogen": "Venturia inaequalis (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Apple scab is a serious fungal disease that affects foliage, blossoms, and developing fruit. It produces olive-green to black velvety spots that can cause premature defoliation and corky, cracked fruit blemishes.",
        "symptoms": [
            "Olive-green to dull brown velvety spots on upper leaf surfaces.",
            "Deformed, puckered leaves that turn yellow and drop prematurely.",
            "Corky, scabby, dark brown spots on fruit skin, often causing fruit cracking.",
            "Infected blossoms can blight and drop without setting fruit."
        ],
        "recommended_next_steps": [
            "Inspect both upper and lower leaf surfaces and developing apples for scabby lesions.",
            "Prune infected twigs and collect fallen leaves to reduce overwintering fungal spores.",
            "Avoid overhead irrigation to minimize the duration of leaf wetness.",
            "Consult your local horticulture department or KVK for region-specific spray schedules."
        ],
        "preventive_practices": [
            "Plant scab-resistant apple cultivars (e.g., Liberty, Prima, Enterprise) when establishing orchards.",
            "Prune trees annually in winter to promote open canopy structure and rapid leaf drying.",
            "Apply flaked urea or compost fallen leaves in autumn to accelerate leaf decomposition.",
            "Apply protective fungicide sprays (such as captan or mancozeb) prior to anticipated spring rain events."
        ]
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "crop_display": "Apple",
        "condition": "Black Rot",
        "pathogen": "Botryosphaeria obtusa (Fungus)",
        "is_healthy": False,
        "severity": "High",
        "description": "Black rot (also known as frogeye leaf spot) attacks apple leaves, fruit, and woody bark. It creates characteristic circular lesions with dark borders and causes firm, concentric dark rot on ripening fruit.",
        "symptoms": [
            "Small purple specks on leaves expanding into circular 'frogeye' spots with tan centers and dark purple margins.",
            "Firm brown rot on apples starting near the calyx, turning black with concentric rings of pycnidia.",
            "Sunken, reddish-brown bark cankers on branches and scaffold limbs.",
            "Mummified fruit shriveling and remaining attached to twigs over winter."
        ],
        "recommended_next_steps": [
            "Prune out dead wood, cankered branches, and all mummified apples hanging from trees.",
            "Burn or deeply bury pruned wood to eliminate the primary spore inoculum.",
            "Maintain sanitation beneath the tree canopy by destroying fallen infected fruit.",
            "Consult a horticulture specialist before applying post-bloom protective treatments."
        ],
        "preventive_practices": [
            "Avoid mechanical damage to bark and trunks during harvesting and mowing.",
            "Paint tree trunks with white latex paint to minimize winter sunscald cracking.",
            "Follow a balanced fertilization schedule to avoid tender excessive vegetative growth.",
            "Apply approved protective fungicides from silver tip stage through petal fall."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "crop_display": "Apple",
        "condition": "Cedar Apple Rust",
        "pathogen": "Gymnosporangium juniperi-virginianae (Fungus)",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Cedar apple rust is a heteroecious fungal disease that requires both apple trees and eastern red cedar/juniper species to complete its complex two-year life cycle. It causes bright orange foliar spotting.",
        "symptoms": [
            "Bright yellow-orange circular lesions on upper leaf surfaces appearing in late spring.",
            "Raised dark orange spots with minute black pycnia dots in the center.",
            "Tube-like aecial structures protruding from the undersides of leaves in mid-summer.",
            "Premature defoliation in severe cases, reducing tree vigor and fruit size."
        ],
        "recommended_next_steps": [
            "Inspect surrounding landscape within a 1–2 km radius for cedar or juniper trees bearing gall-like growths.",
            "Remove cedar galls from ornamental junipers before gelatinous orange tendrils appear in spring.",
            "Do not spray insecticides; rust is caused by a fungus.",
            "Consult a local extension agent for timing of protective rust fungicides."
        ],
        "preventive_practices": [
            "Plant rust-resistant apple varieties such as Redfree, Freedom, or Liberty.",
            "Maintain a buffer distance between commercial apple orchards and wild juniper stands.",
            "Apply protective fungicides (such as myclobutanil or mancozeb) starting at pink bud through petal fall.",
            "Monitor weather forecasts during spring budbreak for prolonged moist periods."
        ]
    },
    "Apple___healthy": {
        "crop": "Apple",
        "crop_display": "Apple",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The apple foliage displays uniform color and structure without visible signs of fungal spotting, rust pustules, or bacterial blight from the trained classes.",
        "symptoms": [
            "Vibrant green, well-developed leaves with intact margins.",
            "Absence of chlorotic spotting, brown necrotic margins, or velvety patches.",
            "Normal shoot extension and healthy leaf turgor."
        ],
        "recommended_next_steps": [
            "Continue regular weekly orchard scouting, checking both sides of foliage.",
            "Maintain balanced irrigation and monitor soil moisture levels.",
            "Keep orchard records of phenological stages (bud break, bloom, petal fall)."
        ],
        "preventive_practices": [
            "Perform balanced dormant winter pruning to encourage sunlight penetration.",
            "Maintain soil organic matter and apply balanced NPK based on leaf tissue testing.",
            "Promote beneficial predatory mites and pollinators in the orchard ecosystem."
        ]
    },

    # -------------------------------------------------------------
    # BLUEBERRY (1 Class)
    # -------------------------------------------------------------
    "Blueberry___healthy": {
        "crop": "Blueberry",
        "crop_display": "Blueberry",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The blueberry leaf exhibits characteristic healthy morphology and coloration, with no evidence of foliar blights, rust, or anthracnose from the trained classes.",
        "symptoms": [
            "Smooth, lustrous green leaves with intact venation.",
            "Absence of interveinal chlorosis, leaf scorch, or necrotic spots.",
            "Healthy cane and bud development."
        ],
        "recommended_next_steps": [
            "Maintain soil pH in the optimal acidic range (4.5 to 5.2).",
            "Monitor drip irrigation lines to ensure consistent root zone moisture without waterlogging.",
            "Scout regularly for blueberry maggot or fruit rot symptoms as berries develop."
        ],
        "preventive_practices": [
            "Apply organic pine bark or sawdust mulch (5-8 cm depth) to conserve moisture and maintain acidity.",
            "Use drip irrigation rather than overhead sprinklers to keep leaves dry.",
            "Prune older canes (over 6 years old) during winter dormancy to stimulate vigorous young growth."
        ]
    },

    # -------------------------------------------------------------
    # CHERRY (2 Classes)
    # -------------------------------------------------------------
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry (including sour)",
        "crop_display": "Cherry",
        "condition": "Powdery Mildew",
        "pathogen": "Podosphaera clandestina (Fungus)",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Powdery mildew in cherry is a fungal disorder characterized by patches of white powdery mycelial growth on young foliage and fruit stems, leading to curled leaves and stunted terminal shoots.",
        "symptoms": [
            "Circular patches of white, powdery fungal growth on the undersides of young leaves.",
            "Leaves becoming upwardly curled, puckered, or distorted.",
            "Infected shoots exhibiting stunted terminal growth with a bleached appearance.",
            "Immature cherries developing webby fungal blemishes and fail to ripen properly."
        ],
        "recommended_next_steps": [
            "Prune infected sucker shoots and dense interior foliage to enhance air circulation.",
            "Avoid high rates of late-season nitrogen fertilizer that stimulate succulent vulnerable foliage.",
            "Inspect underside of young leaves at the canopy top where mildew typically initiates.",
            "Consult local agricultural advisories for approved horticultural oils or sulfur sprays."
        ],
        "preventive_practices": [
            "Ensure wide tree spacing and open-center canopy architecture during training.",
            "Apply preventive sulfur or potassium bicarbonate sprays during warm, humid spring weather.",
            "Avoid overhead sprinkler irrigation that raises canopy humidity levels.",
            "Remove and compost fallen leaf debris in late autumn."
        ]
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry (including sour)",
        "crop_display": "Cherry",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The cherry foliage is healthy with uniform green color, firm leaf texture, and no detectable mildew mycelium or shot-hole lesions.",
        "symptoms": [
            "Uniformly green, fully expanded leaves with smooth margins.",
            "No white powdery coatings, chlorotic spotting, or perforated leaf tissue.",
            "Strong terminal shoots with healthy active buds."
        ],
        "recommended_next_steps": [
            "Continue regular weekly orchard monitoring throughout the growing season.",
            "Maintain mulching around the drip line to conserve soil moisture.",
            "Scout for cherry fruit flies and aphids during petal fall."
        ],
        "preventive_practices": [
            "Carry out routine post-harvest pruning to open the canopy to sunlight.",
            "Apply balanced fertilizer according to soil test recommendations.",
            "Manage orchard floor vegetation to prevent weeds harboring fungal vectors."
        ]
    },

    # -------------------------------------------------------------
    # CORN / MAIZE (4 Classes)
    # -------------------------------------------------------------
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (maize)",
        "crop_display": "Corn (Maize)",
        "condition": "Gray Leaf Spot",
        "pathogen": "Cercospora zeae-maydis (Fungus)",
        "is_healthy": False,
        "severity": "High",
        "description": "Gray leaf spot is a major foliar disease of maize favored by prolonged warm, humid weather. The fungus forms distinct rectangular lesions bounded strictly by parallel leaf veins, reducing photosynthetic area.",
        "symptoms": [
            "Small tan spots with yellow halos expanding into long, narrow, rectangular lesions.",
            "Lesions strictly delimited by leaf veins, measuring 2 to 7 cm long.",
            "Mature lesions turning distinctly gray under humid conditions due to fungal sporulation.",
            "Severe blight leading to premature dry-down, blighted canopy, and stalk lodging."
        ],
        "recommended_next_steps": [
            "Assess disease severity on the ear leaf and leaves above the ear during tasseling and silking.",
            "Check stalk integrity before harvest; harvest affected fields early to minimize lodging losses.",
            "Avoid working in wet fields to prevent spore dispersal.",
            "Consult local agricultural extension for economic threshold guidelines regarding fungicide applications."
        ],
        "preventive_practices": [
            "Plant maize hybrids with high genetic tolerance or resistance to gray leaf spot.",
            "Practice crop rotation with non-host crops (soybean, wheat, or pulses) for at least one full year.",
            "Manage previous crop residue through tillage or accelerated decomposition where appropriate.",
            "Ensure balanced fertilization, particularly avoiding potassium deficiency which worsens leaf blights."
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (maize)",
        "crop_display": "Corn (Maize)",
        "condition": "Common Rust",
        "pathogen": "Puccinia sorghi (Fungus)",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Common rust of maize produces cinnamon-brown to dark brown powdery pustules on both leaf surfaces. It thrives in cool to moderate temperatures with high humidity and morning dews.",
        "symptoms": [
            "Small, oval to elongate powdery pustules scattered over both upper and lower leaf surfaces.",
            "Pustules erupting through the leaf epidermis to release powdery, cinnamon-brown urediniospores.",
            "Surrounding leaf tissue may turn chlorotic or necrotic when pustule density is high.",
            "Pustules turning dark brownish-black late in the season as winter teliospores form."
        ],
        "recommended_next_steps": [
            "Scout lower and middle canopy leaves leading up to the tasseling stage.",
            "Differentiate from southern rust (common rust pustules occur equally on both sides; southern rust mainly on upper surface).",
            "Monitor weather; rust development slows significantly when temperatures exceed 30°C.",
            "Consult local agricultural authorities if rust pustules appear on leaves above the ear leaf before blister stage."
        ],
        "preventive_practices": [
            "Select maize hybrids carrying specific resistance genes (e.g., Rp genes) or general tolerance.",
            "Plant early in the season to allow crops to mature before regional airborne rust spore clouds arrive.",
            "Maintain optimal crop nutrition with balanced nitrogen and phosphorus.",
            "Destroy volunteer maize plants in surrounding ditches and borders."
        ]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (maize)",
        "crop_display": "Corn (Maize)",
        "condition": "Northern Leaf Blight",
        "pathogen": "Exserohilum turcicum (Fungus)",
        "is_healthy": False,
        "severity": "High",
        "description": "Northern corn leaf blight (NCLB) is a devastating foliar disease that produces large, elliptical, cigar-shaped lesions. It can cause severe grain yield loss if the upper canopy is blighted prior to grain filling.",
        "symptoms": [
            "Large, elongated, elliptical or 'cigar-shaped' grayish-green to tan lesions (2.5 to 15 cm long).",
            "Lesions develop first on lower leaves and rapidly progress upward toward the ear leaves.",
            "Dark olive-green to black fungal sporulation visible within lesions during damp humid mornings.",
            "Individual lesions coalescing into large blighted areas, causing entire leaves to wither."
        ],
        "recommended_next_steps": [
            "Scout weekly from vegetative stage V8 through soft dough stage, focusing on the ear leaf zone.",
            "Assess percentage of green leaf area retained above the primary ear.",
            "Test stalk strength as maturity nears, as blighted plants are susceptible to secondary stalk rots.",
            "Consult extension guidelines on economic thresholds before considering fungicide intervention."
        ],
        "preventive_practices": [
            "Plant certified NCLB-resistant maize hybrids possessing multigenic and race-specific Ht genes.",
            "Rotate fields with non-grass crops such as soybeans, canola, or sunflowers for 1 to 2 seasons.",
            "Till or chop crop residue post-harvest to speed fungal breakdown in the soil.",
            "Maintain balanced soil fertility according to soil analysis."
        ]
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (maize)",
        "crop_display": "Corn (Maize)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The corn foliage shows strong vigor, uniform dark green leaf blades, and no cigar-shaped blights, vein-bound spots, or rust pustules.",
        "symptoms": [
            "Uniform dark green, broad leaf blades with prominent midrib.",
            "Smooth leaf surface without lesions, pustules, or striping.",
            "Strong stalk development and normal tassel emergence."
        ],
        "recommended_next_steps": [
            "Continue regular field walking and scouting across representative field zones.",
            "Monitor soil nitrogen and moisture requirements during critical silking and grain fill windows.",
            "Inspect fields for fall armyworm or stem borer activity."
        ],
        "preventive_practices": [
            "Apply split nitrogen doses to match crop uptake curves.",
            "Implement integrated weed management to minimize weed competition for water and nutrients.",
            "Ensure uniform seedbed preparation and optimal plant population density."
        ]
    },

    # -------------------------------------------------------------
    # GRAPE (4 Classes)
    # -------------------------------------------------------------
    "Grape___Black_rot": {
        "crop": "Grape",
        "crop_display": "Grape",
        "condition": "Black Rot",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "is_healthy": False,
        "severity": "High",
        "description": "Black rot is one of the most destructive fungal diseases of cultivated grapes. It attacks leaves, shoots, and fruit clusters, turning developing berries into shriveled, hard, black mummies.",
        "symptoms": [
            "Small circular reddish-brown spots on leaves, surrounded by a distinct dark band.",
            "Tiny black pimple-like pycnidia forming in a ring just inside the margin of leaf lesions.",
            "Infected berries turning dull brown, rotting completely within 48 hours.",
            "Berries shriveling into hard, wrinkled black mummies that remain attached to clusters."
        ],
        "recommended_next_steps": [
            "Inspect clusters and shoot tips immediately; remove and destroy visibly rotting bunches.",
            "Prune out mummified berries and infected canes during dormancy, never leaving them on trellises.",
            "Avoid overhead irrigation to minimize canopy moisture.",
            "Consult local viticulture advisories for protective spray timings before bloom."
        ],
        "preventive_practices": [
            "Practice open canopy training (e.g., vertical shoot positioning) to facilitate rapid drying.",
            "Remove wild grapevines within 100 meters of the vineyard perimeter.",
            "Apply protective fungicide sprays starting from 2–3 inch shoot growth through post-bloom.",
            "Cultivate beneath grape rows to bury overwintered mummies before spring bud break."
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "crop_display": "Grape",
        "condition": "Esca (Black Measles)",
        "pathogen": "Fungal wood decay complex (Phaeoacremonium & Phaeomoniella)",
        "is_healthy": False,
        "severity": "High",
        "description": "Esca is a complex grapevine trunk disease affecting mature vines. It causes striking 'tiger-stripe' foliar chlorosis, internal wood rot, and dark speckled spots ('measles') on ripening berries.",
        "symptoms": [
            "'Tiger-stripe' appearance on leaves: interveinal yellow or red chlorosis leading to necrotic stripes with green veins.",
            "Small, dark, circular speckles or purple spots on berry skin ('black measles').",
            "Berries splitting, shriveling, or developing an unpalatable taste.",
            "Internal cross-section of cordons/trunks showing dark necrotic vascular spotting and spongy white rot."
        ],
        "recommended_next_steps": [
            "Tag and record symptomatic vines during late summer for selective winter management.",
            "Prune symptomatic vines separately and last, sanitizing pruning shears between cuts.",
            "Avoid making large pruning wounds in wet weather when airborne spores are abundant.",
            "Consult a viticulture expert regarding trunk renewal or vine surgery techniques."
        ],
        "preventive_practices": [
            "Coat major winter pruning wounds immediately with approved wound sealant or bio-protectant (Trichoderma).",
            "Delay pruning until late winter when wound healing proceeds more rapidly.",
            "Minimize vine water and heat stress through regulated deficit irrigation and balanced crop load.",
            "Purchase certified clean, hot-water treated planting stock when establishing new vineyard blocks."
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "crop_display": "Grape",
        "condition": "Isariopsis Leaf Blight",
        "pathogen": "Pseudocercospora cladosporioides / Phaeoisariopsis (Fungus)",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Isariopsis leaf spot produces irregular brown necrotic blights on grape foliage, often leading to premature leaf drop and reduced sugar accumulation in developing berries.",
        "symptoms": [
            "Irregular, angular reddish-brown to dark brown lesions on older leaves.",
            "Lesions expanding and coalescing into large blighted patches, often bounded by larger veins.",
            "Foliage curling, drying, and dropping prematurely in late season.",
            "Weakened cane maturation and poor berry sugar levels due to lost photosynthetic area."
        ],
        "recommended_next_steps": [
            "Collect and destroy fallen leaf debris beneath the canopy to minimize overwintering spores.",
            "Prune dense canopy shoots to improve sunlight penetration and air movement.",
            "Check both sides of foliage for fungal tufts during humid periods.",
            "Seek local agricultural extension recommendations for post-harvest protective sprays."
        ],
        "preventive_practices": [
            "Maintain trellis wires and perform timely shoot tucking and summer leaf thinning around fruit zones.",
            "Apply approved copper or mancozeb based protective sprays in early spring if historical pressure exists.",
            "Ensure proper vine nutrition, avoiding excess late nitrogen.",
            "Avoid low-lying, poorly drained sites when establishing vines."
        ]
    },
    "Grape___healthy": {
        "crop": "Grape",
        "crop_display": "Grape",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "Grape foliage displays vibrant green color, strong canopy vigor, intact margins, and no visible signs of black rot, measles striping, or downy/powdery mildew.",
        "symptoms": [
            "Lush, uniformly green lobed leaves with clean margins.",
            "Absence of interveinal chlorosis, tiger-striping, or concentric spots.",
            "Healthy tendril development and clean cluster stems."
        ],
        "recommended_next_steps": [
            "Continue regular canopy management including shoot positioning and selective leaf pulling.",
            "Maintain scheduled monitoring for powdery mildew and berry moth activity.",
            "Monitor vine water status to optimize cluster ripening."
        ],
        "preventive_practices": [
            "Maintain open canopy architecture for light interception and rapid air drying.",
            "Follow balanced petiole-tested fertilizer applications.",
            "Keep vineyard floor vegetation mowed to discourage humidity buildup."
        ]
    },

    # -------------------------------------------------------------
    # ORANGE / CITRUS (1 Class)
    # -------------------------------------------------------------
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange",
        "crop_display": "Orange / Citrus",
        "condition": "Huanglongbing (Citrus Greening)",
        "pathogen": "Candidatus Liberibacter asiaticus (Bacteria vectored by Asian citrus psyllid)",
        "is_healthy": False,
        "severity": "Critical",
        "description": "Huanglongbing (HLB or Citrus Greening) is arguably the most devastating bacterial disease of citrus worldwide. It causes asymmetric blotchy mottle, stunted root systems, twig dieback, and small, misshapen, bitter fruit.",
        "symptoms": [
            "Asymmetrical blotchy mottle: yellow discoloration on one side of the leaf midrib does not match the other side.",
            "Yellow shoots appearing distinctly within an otherwise green tree canopy ('yellow dragon').",
            "Vein corking, vein enlargement, and leaves taking on an upright, leathery posture.",
            "Fruit remain small, lopsided, poorly colored (greening persists at base), with aborted dark seeds and bitter juice."
        ],
        "recommended_next_steps": [
            "CRITICAL: Report suspect trees immediately to your regional horticulture officer or plant quarantine authority.",
            "Collect leaf tissue for official laboratory PCR testing to verify diagnosis before tree removal.",
            "Inspect flush shoots for Asian citrus psyllid nymphs (producing white waxy secretions) or adults feeding at a 45-degree angle.",
            "Mark confirmed positive trees for prompt eradication to prevent inoculum spread to neighboring groves."
        ],
        "preventive_practices": [
            "Plant only certified disease-free citrus nursery saplings from certified insect-screened nurseries.",
            "Implement area-wide coordinated psyllid vector management using biological controls (Tamarixia radiata) and approved sprays.",
            "Remove and destroy wild citrus relatives (such as Murraya paniculata / orange jasmine) acting as psyllid reservoirs.",
            "Apply foliar micronutrient and root-health programs to maintain tree stamina while young."
        ]
    },

    # -------------------------------------------------------------
    # PADDY / RICE (10 Classes)
    # -------------------------------------------------------------
    "Paddy___bacterial_leaf_blight": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Bacterial Leaf Blight",
        "pathogen": "Xanthomonas oryzae pv. oryzae (Bacteria)",
        "is_healthy": False,
        "severity": "High",
        "description": "Bacterial leaf blight (BLB) is one of the most destructive rice diseases, particularly in irrigated and rainfed lowland ecosystems. It produces water-soaked to yellowish-white wavy lesions along leaf margins.",
        "symptoms": [
            "Water-soaked stripes starting near leaf tips and progressing down the margins.",
            "Lesions enlarge, turning straw-yellow to grayish-white with characteristic wavy, undulating margins.",
            "Milky bacterial ooze beads drying into amber crusted droplets on affected leaves in early morning.",
            "'Kresek' (seedling wilt phase): leaves roll, wither, and entire young seedlings collapse."
        ],
        "recommended_next_steps": [
            "Drain excess stagnant standing water from fields temporarily for 2–3 days if feasible.",
            "Immediately suspend top-dressing of urea / nitrogenous fertilizers; avoid excess nitrogen.",
            "Avoid clipping seedling leaf tips at transplanting, which creates entry wounds for bacteria.",
            "Consult local KVK or agricultural officer for recommended bactericidal seed and foliar guidelines."
        ],
        "preventive_practices": [
            "Grow BLB-resistant or tolerant rice cultivars (e.g., Swarna Sub-1, IR64 variants, Ajaya, PR 126).",
            "Maintain balanced fertilization with appropriate potassium (potash) to strengthen plant cell walls.",
            "Ensure field sanitation: eradicate wild grass weeds (such as Leersia hexandra) along bunds.",
            "Practice hot water seed treatment (52–54°C for 10 minutes) or approved chemical seed dressing before sowing."
        ]
    },
    "Paddy___bacterial_leaf_streak": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Bacterial Leaf Streak",
        "pathogen": "Xanthomonas oryzae pv. oryzicola (Bacteria)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Bacterial leaf streak (BLS) attacks rice leaf blades, producing narrow, translucent, water-soaked linear streaks confined between veins. In high humidity, yellow bacterial droplets bead along the streaks.",
        "symptoms": [
            "Fine, narrow, water-soaked interveinal streaks running parallel to leaf veins.",
            "Streaks turn yellowish-brown to grayish-brown with tiny amber-colored bacterial exudate beads.",
            "Lesions coalesce, causing large portions of the leaf blade to turn brown and die back from the tip.",
            "Leaves appear scorched and grayish from a distance in heavily infected fields."
        ],
        "recommended_next_steps": [
            "Avoid high nitrogen top-dressing while the streak symptoms are actively spreading.",
            "Regulate water levels to prevent field-to-field flood overflow that carries bacterial inoculum.",
            "Check for wounding from strong winds or insects that facilitate bacterial entry.",
            "Contact your local agricultural extension service for field confirmation."
        ],
        "preventive_practices": [
            "Use certified disease-free seed from reliable agricultural universities or state seed corporations.",
            "Plant resistant varieties adapted to your agro-climatic region.",
            "Apply balanced NPK with split nitrogen applications rather than single heavy doses.",
            "Plow under rice stubble thoroughly post-harvest to accelerate breakdown of infected straw."
        ]
    },
    "Paddy___bacterial_panicle_blight": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Bacterial Panicle Blight",
        "pathogen": "Burkholderia glumae / gladioli (Bacteria)",
        "is_healthy": False,
        "severity": "High",
        "description": "Bacterial panicle blight is an emerging disease of rice favored by unusually high night temperatures and high humidity during the heading stage. It causes floret sterility and upright, blighted panicles.",
        "symptoms": [
            "Affected panicles remain upright because grains fail to fill and remain empty.",
            "Floret husks turn straw-colored to light brown, starting from the base of the grain.",
            "A distinct dark reddish-brown ring or band often separates the diseased husk area from green portions.",
            "Panicle branches and rachis remain green while grains turn prematurely brown."
        ],
        "recommended_next_steps": [
            "Examine upright panicles during the milk and soft-dough stages to distinguish from stem borer damage.",
            "Record affected field areas and monitor weather (disease surges during nighttime temperatures above 25°C).",
            "Do not spray standard fungal blast chemicals; this condition is bacterial.",
            "Consult a plant pathologist or university rice specialist for region-specific guidelines."
        ],
        "preventive_practices": [
            "Adjust sowing dates so that flowering and heading avoid the hottest, most humid weeks of the season.",
            "Plant cultivars with documented partial resistance to bacterial panicle blight.",
            "Use certified clean seed and avoid recycling seeds from fields showing panicle blight.",
            "Avoid excessive nitrogen fertilization that increases canopy humidity and susceptibility."
        ]
    },
    "Paddy___blast": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Rice Blast",
        "pathogen": "Magnaporthe oryzae / Pyricularia oryzae (Fungus)",
        "is_healthy": False,
        "severity": "High to Critical",
        "description": "Rice blast is historically the most widespread and damaging fungal disease of rice. It can attack all aboveground plant parts: leaf blast, collar rot, neck blast, and panicle node blast.",
        "symptoms": [
            "Spindle-shaped or elliptical 'eye-like' spots with pointed ends, gray/white centers, and brown margins.",
            "Spots enlarge, coalesce, and cause complete burning or withering of the foliage ('leaf blast').",
            "Blackish-brown discoloration at the neck node of the panicle ('neck blast'), causing it to snap over.",
            "Severe yield loss due to chaffy, unfilled, or completely broken panicles."
        ],
        "recommended_next_steps": [
            "Maintain standing water depth (5–7 cm) in the paddy field; water stress exacerbates blast.",
            "Halt further urea application immediately; excess nitrogen fuels rapid blast proliferation.",
            "Inspect leaf collars and emerging panicle necks for dark brown rot.",
            "Consult local agricultural officer or KVK for recommended protective sprays (e.g., tricyclazole, isoprothiolane)."
        ],
        "preventive_practices": [
            "Grow blast-resistant cultivars recommended for your state (e.g., MTU 1010, RNR 15048, BPT 5204 resistant lines).",
            "Treat seed before sowing with Trichoderma viride or carbendazim.",
            "Avoid excessive or late-season nitrogen applications; apply silicon fertilizers where soil is depleted.",
            "Maintain proper plant spacing (20 × 15 cm) to facilitate air circulation and lower canopy moisture."
        ]
    },
    "Paddy___brown_spot": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Brown Spot",
        "pathogen": "Bipolaris oryzae / Cochliobolus miyabeanus (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Brown spot of rice is a chronic fungal disease often associated with poor soil fertility, nutrient imbalance, and water stress. It causes small oval spots on leaf blades, leaf sheaths, and glumes.",
        "symptoms": [
            "Small, oval to circular dark brown spots distributed evenly across the leaf blade.",
            "Mature spots show gray or light brown centers surrounded by a distinct yellow or reddish halo.",
            "Dark brown to black discoloration on grains ('pecky rice'), lowering seed germination and milling quality.",
            "Seedling blighting in nursery beds sown with infected seeds."
        ],
        "recommended_next_steps": [
            "Conduct a soil test to evaluate potassium, manganese, zinc, and organic matter deficiencies.",
            "Avoid letting fields dry out completely; provide uniform intermittent irrigation.",
            "Apply balanced top-dressing of potash (muriate of potash) along with nitrogen.",
            "Contact your local agricultural extension service for advice on seed treatment and soil amendments."
        ],
        "preventive_practices": [
            "Treat seeds with hot water (52°C for 10 min) or approved fungicidal seed dressers before nursery sowing.",
            "Incorporate green manure or compost to improve soil organic content and nutrient retention.",
            "Apply balanced NPK fertilizers supplemented with zinc sulphate (25 kg/ha in zinc-deficient soils).",
            "Maintain clean bunds free from weed hosts such as wild grasses."
        ]
    },
    "Paddy___dead_heart": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Dead Heart (Stem Borer Damage)",
        "pathogen": "Scirpophaga incertulas (Yellow Stem Borer insect larvae)",
        "is_healthy": False,
        "severity": "High",
        "description": "Dead heart is a symptom caused by rice stem borer larvae (chiefly Yellow Stem Borer). The caterpillar bores into the central tiller, severing the vascular bundle and causing the central shoot to dry out and die.",
        "symptoms": [
            "The central unfurled leaf shoot turns straw-colored, withers, and dries up while outer leaves remain green.",
            "The dried central tiller pulls out easily by hand, revealing a chewed, rotting base with insect frass.",
            "Minute entrance bore-holes visible near the water line or lower node of the tiller.",
            "In the reproductive stage, the same borer causes 'white earheads' (panicles with empty, bleached grains)."
        ],
        "recommended_next_steps": [
            "Pull suspect central shoots: if they detach effortlessly with a chewed base, stem borer is confirmed.",
            "Install pheromone traps (5 traps per acre) to monitor adult stem borer moth populations.",
            "Look for buff-colored hairy egg masses on leaf tips in the nursery or main field.",
            "Consult local agricultural extension for economic threshold levels (5% dead hearts or 1 moth/trap/day)."
        ],
        "preventive_practices": [
            "Clip the top 2 inches of seedling leaf tips before transplanting to eliminate stem borer egg masses.",
            "Conserve beneficial predators: spiders, dragonflies, and egg parasitoids (Trichogramma japonicum).",
            "Release egg parasitoid Trichogramma japonicum @ 50,000/ha weekly when moth activity is detected.",
            "Harvest rice close to the ground and plow the stubble promptly to destroy overwintering larvae."
        ]
    },
    "Paddy___downy_mildew": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Downy Mildew (Crazy Top)",
        "pathogen": "Sclerophthora macrospora (Oomycete)",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Downy mildew of rice (often referred to as 'crazy top') is an oomycete infection occurring predominantly in waterlogged, flooded low-lying fields. It causes chlorotic mottling and bizarre leaf-like floral structures.",
        "symptoms": [
            "Pale yellow, chlorotic mottling and white speckling along leaf veins.",
            "Leaves becoming thick, twisted, curled, and leathery.",
            "Severe stunting and excessive tillering of infected young plants.",
            "'Crazy top' symptom: normal panicles are replaced by twisted, leafy structures that produce no grain."
        ],
        "recommended_next_steps": [
            "Improve field surface drainage to eliminate prolonged standing water puddles in nursery beds.",
            "Rogue out and destroy severely deformed, stunted 'crazy top' hills.",
            "Do not use seeds from fields that experienced downy mildew outbreaks.",
            "Consult local extension officers if flooding occurs repeatedly in the region."
        ],
        "preventive_practices": [
            "Avoid creating seedbeds in low-lying depressions susceptible to flash flooding.",
            "Ensure leveled fields with functional drainage channels to prevent prolonged submergence.",
            "Use certified seed free from oospores.",
            "Practice crop rotation in fields with chronic downy mildew history."
        ]
    },
    "Paddy___hispa": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Rice Hispa Damage",
        "pathogen": "Dicladispa armigera (Chrysomelid beetle pest)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Rice hispa is an insect pest where both spiny adult beetles and leaf-mining grubs feed voraciously on rice leaves. They scrape off green tissue, leaving characteristic parallel white streaks.",
        "symptoms": [
            "Adults scrape leaf epidermis, producing distinctive parallel white streaks along the leaf blade.",
            "Larvae mine between leaf surfaces, creating irregular blister-like white translucent patches.",
            "Heavily damaged leaves wither, dry up, and give the entire field a scorched, bleached appearance.",
            "Small, black, spiny beetles (4–5 mm) visible crawling on the leaves."
        ],
        "recommended_next_steps": [
            "Use a sweep net across the field canopy to capture and gauge hispa adult density.",
            "Clip and destroy damaged leaf tips containing hispa eggs and grubs.",
            "Avoid high nitrogen applications that promote succulent leaf tissue attractive to beetles.",
            "Consult local agricultural advisories for economic threshold values (2 adults/hill or 1 leaf/hill damaged)."
        ],
        "preventive_practices": [
            "Clip seedling tips before transplanting to destroy hispa eggs.",
            "Encourage natural biocontrol agents like eulophid parasitoid wasps and spiders.",
            "Keep field bunds clean of wild alternative grass hosts (e.g., Echinochloa colonum).",
            "Practice deep summer plowing to expose pupae to predatory birds and heat."
        ]
    },
    "Paddy___normal": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Normal Healthy Rice",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The rice plant appears healthy and vigorous. Leaf blades show uniform chlorophyll distribution with no evidence of blast eye-spots, bacterial blights, hispa scraping, or dead-heart symptoms.",
        "symptoms": [
            "Lush, upright, vibrant green leaf blades with uniform color.",
            "Absence of spindle-shaped lesions, water-soaked margins, or brown speckles.",
            "Healthy tillering and normal development corresponding to crop stage."
        ],
        "recommended_next_steps": [
            "Continue regular field walking and monitoring of bunds and water channels.",
            "Maintain alternate wetting and drying (AWD) water management to conserve water and strengthen roots.",
            "Apply scheduled split nitrogen doses with appropriate neem-coated urea."
        ],
        "preventive_practices": [
            "Follow integrated pest and disease management (IPM) guidelines.",
            "Maintain soil health by incorporating crop residue and applying balanced NPK + zinc.",
            "Keep bunds weed-free to eliminate reservoir hosts for insect vectors."
        ]
    },
    "Paddy___tungro": {
        "crop": "Paddy",
        "crop_display": "Paddy (Rice)",
        "condition": "Rice Tungro Disease",
        "pathogen": "RTBV & RTSV (Viruses vectored by Green Leafhopper, Nephotettix virescens)",
        "is_healthy": False,
        "severity": "Critical",
        "description": "Rice tungro is a composite viral disease transmitted non-persistently by green leafhoppers. It causes severe stunting, yellow-to-orange leaf discoloration, reduced tillering, and delayed maturity.",
        "symptoms": [
            "Severe stunting of the rice plant with significantly reduced tiller count.",
            "Distinct yellow to orange-yellow discoloration of leaves starting from the tips and spreading downward.",
            "Younger leaves may show mottled stripes or interveinal chlorosis.",
            "Panicles remain small, poorly exerted, and contain mostly sterile or dark-stained grains."
        ],
        "recommended_next_steps": [
            "Inspect fields for green leafhopper (GLH) adults and nymphs on the lower plant canopy.",
            "Rogue out and bury severely stunted, orange-yellow hills to eliminate viral reservoirs.",
            "Set up light traps at night to monitor green leafhopper population surges.",
            "Report suspected outbreaks promptly to the nearest agricultural officer or KVK."
        ],
        "preventive_practices": [
            "Plant tungro-resistant or tolerant varieties (e.g., Vikramarya, IR36, CR 1009, Lalat).",
            "Synchronize planting schedules with neighboring farmers to avoid continuous green host bridges.",
            "Apply neem-based formulations or recommended vector-control sprays when GLH exceeds threshold (1 hopper/tiller).",
            "Plow stubble immediately after harvest to destroy surviving viral host plants."
        ]
    },

    # -------------------------------------------------------------
    # PEACH (2 Classes)
    # -------------------------------------------------------------
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "crop_display": "Peach",
        "condition": "Bacterial Spot",
        "pathogen": "Xanthomonas arboricola pv. pruni (Bacteria)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Bacterial spot attacks leaves, twigs, and fruit of peach trees. It is characterized by small angular water-soaked leaf spots that drop out, creating a 'shot-hole' appearance.",
        "symptoms": [
            "Small, angular, water-soaked purple to dark brown spots on the underside of leaves.",
            "Infected tissue dries, drops out, leaving a ragged 'shot-hole' perforation.",
            "Severe yellowing of affected leaves, leading to heavy early summer defoliation.",
            "Sunken, pitted brown cankers on fruit with gum oozing from cracks."
        ],
        "recommended_next_steps": [
            "Avoid overhead sprinkler irrigation that splashes bacteria between branches.",
            "Prune out dead, cankered twigs during dry winter periods.",
            "Collect and dispose of fallen infected leaves and mummified fruit.",
            "Consult local extension services for dormant and bloom copper spray programs."
        ],
        "preventive_practices": [
            "Select bacterial spot-tolerant peach cultivars suited to your climate.",
            "Avoid planting orchards in highly exposed, windblown, or sandy sites without windbreaks.",
            "Maintain moderate, balanced nitrogen fertility to avoid excessive soft growth.",
            "Apply dormant copper sprays in autumn and early spring before bud swell."
        ]
    },
    "Peach___healthy": {
        "crop": "Peach",
        "crop_display": "Peach",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The peach foliage shows healthy, lanceolate leaves with smooth margins and no shot-hole perforations, leaf curl, or bacterial spots.",
        "symptoms": [
            "Uniform green lanceolate leaves with glossy upper surface.",
            "No angular necrotic perforations or yellowing.",
            "Normal shoot vigor and healthy fruit set."
        ],
        "recommended_next_steps": [
            "Maintain routine weekly orchard scouting.",
            "Monitor for oriental fruit moth and peach tree borer activity.",
            "Maintain regular drip irrigation scheduling."
        ],
        "preventive_practices": [
            "Perform open-center pruning to facilitate light and air flow.",
            "Apply dormant horticultural oils to suppress overwintering scales and mites.",
            "Follow soil-test recommendations for balanced fertilizer application."
        ]
    },

    # -------------------------------------------------------------
    # PEPPER / BELL PEPPER (2 Classes)
    # -------------------------------------------------------------
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Pepper, bell",
        "crop_display": "Bell Pepper",
        "condition": "Bacterial Spot",
        "pathogen": "Xanthomonas euvesicatoria / perforans (Bacteria)",
        "is_healthy": False,
        "severity": "High",
        "description": "Bacterial spot is a devastating foliar and fruit disease of bell peppers favored by warm, rainy conditions. It causes small water-soaked spots, severe defoliation, and rough scabby fruit lesions.",
        "symptoms": [
            "Small, water-soaked, circular to irregular lesions on lower leaf surfaces.",
            "Lesions enlarge to 3–5 mm with dark brown margins and sunken tan centers.",
            "Extensive leaf yellowing followed by severe defoliation, exposing fruit to sunscald.",
            "Raised, rough, warty, scabby spots on fruit surface."
        ],
        "recommended_next_steps": [
            "Avoid handling plants or cultivating fields while foliage is wet with dew or rain.",
            "Rogue out and destroy severely diseased plants in nurseries or small plots.",
            "Use drip irrigation rather than overhead sprinklers to prevent water splashing.",
            "Consult agricultural authorities for registered copper-mancozeb tank mixes."
        ],
        "preventive_practices": [
            "Use certified pathogen-free seeds treated with hot water (50°C for 25 minutes) or bleach.",
            "Plant bacterial spot-resistant bell pepper hybrids (races 1–5 or 1–10 resistant).",
            "Practice at least a 2-year crop rotation out of solanaceous crops (tomato, potato, eggplant).",
            "Sanitize equipment, trays, and stakes with 10% household bleach between seasons."
        ]
    },
    "Pepper,_bell___healthy": {
        "crop": "Pepper, bell",
        "crop_display": "Bell Pepper",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The bell pepper foliage exhibits dark green color, smooth leaf texture, and no signs of bacterial spot, viral mottling, or anthracnose.",
        "symptoms": [
            "Dark green, smooth, broad leaves with intact margins.",
            "Absence of water-soaked specks, necrotic holes, or mosaic mottling.",
            "Normal canopy density and healthy flower blossom development."
        ],
        "recommended_next_steps": [
            "Maintain consistent drip irrigation to prevent blossom end rot.",
            "Scout regularly for thrips, aphids, and whiteflies.",
            "Provide support or staking for heavy-yielding plants."
        ],
        "preventive_practices": [
            "Apply mulch around plant bases to conserve moisture and suppress weeds.",
            "Maintain balanced fertilization with adequate calcium and potassium.",
            "Ensure proper crop spacing for good ventilation between rows."
        ]
    },

    # -------------------------------------------------------------
    # POTATO (3 Classes)
    # -------------------------------------------------------------
    "Potato___Early_blight": {
        "crop": "Potato",
        "crop_display": "Potato",
        "condition": "Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Early blight is a common fungal disease of potatoes that primarily targets older, lower leaves as plants mature or experience stress. It forms characteristic dark concentric target-board lesions.",
        "symptoms": [
            "Dark brown to black circular lesions on older lower leaves.",
            "Lesions display distinct concentric rings ('target-board' or bullseye pattern).",
            "Leaf tissue surrounding lesions turns chlorotic and yellow.",
            "Severe infection leads to defoliation, reducing tuber size and dry matter accumulation."
        ],
        "recommended_next_steps": [
            "Remove and destroy severely affected lower leaves where feasible.",
            "Avoid overhead irrigation, particularly late in the day, to shorten leaf wetness periods.",
            "Ensure adequate nitrogen and potassium fertility; stressed plants are far more susceptible.",
            "Consult local agricultural extension for economic thresholds and recommended fungicide options."
        ],
        "preventive_practices": [
            "Rotate potato fields with non-solanaceous crops (corn, wheat, pulses) for 2 to 3 years.",
            "Use certified, disease-free seed tubers from trusted agricultural agencies.",
            "Maintain wide plant spacing and wide ridges to facilitate air flow.",
            "Apply protective fungicides (such as chlorothalonil or mancozeb) starting around canopy closure."
        ]
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "crop_display": "Potato",
        "condition": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "is_healthy": False,
        "severity": "Critical",
        "description": "Late blight is the devastating water-mold disease that triggered the Irish Potato Famine. Under cool, humid, foggy, or rainy conditions, it can obliterate an entire potato canopy within a week and cause tuber rot.",
        "symptoms": [
            "Water-soaked, irregular pale-green lesions that rapidly turn dark brown to purplish-black.",
            "Delicate white cottony mold visible on the underside of leaves at lesion margins during humid mornings.",
            "Lesions expand rapidly across entire leaf blades and petiole stems, causing rapid foliar collapse.",
            "Tubers develop a granular reddish-brown dry rot extending into the flesh beneath the skin."
        ],
        "recommended_next_steps": [
            "URGENT: Inspect the entire field immediately and check local agricultural university late blight forecast warnings.",
            "Isolate and destroy localized 'hot spots' of infected plants (bag and remove; do not compost in open piles).",
            "Kill haulms (vines) at least two weeks before harvest to prevent tuber infection during digging.",
            "Consult local agricultural officer or KVK for immediate regional emergency blight advisory."
        ],
        "preventive_practices": [
            "Plant certified disease-free, late blight-resistant seed tubers (e.g., Kufri Girdhari, Kufri Himalini).",
            "Eliminate cull potato piles and volunteer potatoes near fields before planting season.",
            "Apply prophylactic protective contact fungicides (e.g., mancozeb, cymoxanil) before anticipated rain/fog periods.",
            "Ensure proper hilling (earthing up) with loose soil to create a physical barrier preventing spores from washing down to tubers."
        ]
    },
    "Potato___healthy": {
        "crop": "Potato",
        "crop_display": "Potato",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "Potato foliage shows robust vegetative development, deep green color, and complete absence of water-soaked blight lesions or target-board spots.",
        "symptoms": [
            "Uniform dark green, pinnate leaves with healthy leaf margins.",
            "Absence of necrotic lesions, cottony sporulation, or leaf curling.",
            "Sturdy stems and vigorous vegetative growth."
        ],
        "recommended_next_steps": [
            "Perform regular weekly field walks, checking lower leaves inside the dense canopy.",
            "Maintain proper earthing-up around potato ridges.",
            "Monitor soil moisture to ensure adequate tuber bulking without waterlogging."
        ],
        "preventive_practices": [
            "Follow recommended preventative spray schedules if local weather conditions favor blight.",
            "Apply balanced fertilizer with adequate potash to improve tuber quality and disease resistance.",
            "Monitor for potato aphids and leafhoppers which vector potato viruses."
        ]
    },

    # -------------------------------------------------------------
    # RASPBERRY (1 Class)
    # -------------------------------------------------------------
    "Raspberry___healthy": {
        "crop": "Raspberry",
        "crop_display": "Raspberry",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The raspberry foliage displays characteristic healthy compound leaf structure, bright green coloration, and no signs of spur blight, cane botrytis, or rust.",
        "symptoms": [
            "Healthy compound leaves with serrated margins and uniform green color.",
            "No purple/brown lesions along canes or leaf midribs.",
            "Vigorous primocane extension and healthy floricane fruit buds."
        ],
        "recommended_next_steps": [
            "Maintain trellis wires and secure canes for optimal air circulation.",
            "Maintain organic mulch to conserve root moisture.",
            "Prune out spent floricanes immediately after harvesting berries."
        ],
        "preventive_practices": [
            "Ensure rows are well spaced and weeded to prevent humidity buildup.",
            "Use drip irrigation directly along row bases rather than overhead watering.",
            "Apply balanced compost or fertilizer in early spring as new primocanes emerge."
        ]
    },

    # -------------------------------------------------------------
    # SOYBEAN (1 Class)
    # -------------------------------------------------------------
    "Soybean___healthy": {
        "crop": "Soybean",
        "crop_display": "Soybean",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The soybean trifoliate leaves show healthy dark green color, normal leaf expansion, and absence of Asian soybean rust, frogeye leaf spot, or bacterial pustules.",
        "symptoms": [
            "Uniform green trifoliate leaves with clean, intact margins.",
            "No rust pustules on undersides of leaves, mosaic mottling, or necrotic frogeye spots.",
            "Healthy root nodulation and normal pod formation."
        ],
        "recommended_next_steps": [
            "Continue regular scouting through reproductive stages (flowering R1 through seed fill R6).",
            "Monitor for pod borer, stem fly, or defoliating caterpillar infestations.",
            "Check soil moisture levels during the critical pod filling window."
        ],
        "preventive_practices": [
            "Inoculate seeds with Bradyrhizobium japonicum before planting for optimal biological nitrogen fixation.",
            "Follow crop rotation with non-legumes (such as maize or wheat) to disrupt disease cycles.",
            "Maintain balanced phosphorus and potassium fertilization according to soil tests."
        ]
    },

    # -------------------------------------------------------------
    # SQUASH (1 Class)
    # -------------------------------------------------------------
    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "crop_display": "Squash / Cucurbit",
        "condition": "Powdery Mildew",
        "pathogen": "Podosphaera xanthii / Erysiphe cichoracearum (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Powdery mildew is the most prevalent disease of squash, pumpkins, and other cucurbits. It appears as powdery white fungal growth over leaf surfaces, causing premature senescing and reduced fruit sweetness.",
        "symptoms": [
            "Talcum powder-like white circular colonies on both upper and lower leaf surfaces.",
            "Spots expand and coalesce, eventually covering entire leaf blades and petioles in white talc.",
            "Infected leaves turn yellow, brown, and dry to a crisp papery consistency.",
            "Fruit suffer sunscald and lack sweetness due to premature loss of functional leaves."
        ],
        "recommended_next_steps": [
            "Prune off heavily colonized older leaves at the base of the plant to improve airflow.",
            "Avoid overhead sprinkler irrigation; keep water off the foliage.",
            "Inspect underside of older leaves where mildew usually initiates before moving upward.",
            "Consult local agricultural extension for approved bio-fungicides (e.g., potassium bicarbonate, neem oil) or synthetic options."
        ],
        "preventive_practices": [
            "Plant powdery mildew-resistant squash cultivars where available.",
            "Ensure generous row spacing (1.5 to 2 m) and weed-free beds for sunlight penetration.",
            "Apply preventative sulfur or potassium bicarbonate sprays early when conditions favor mildew.",
            "Dispose of infected crop residue promptly at the conclusion of harvest."
        ]
    },

    # -------------------------------------------------------------
    # STRAWBERRY (2 Classes)
    # -------------------------------------------------------------
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "crop_display": "Strawberry",
        "condition": "Leaf Scorch",
        "pathogen": "Diplocarpon earlianum (Fungus)",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Leaf scorch attacks strawberry foliage, petioles, and calyxes. It causes numerous small, irregular purple spots that coalesce, giving leaves a scorched, burnt appearance.",
        "symptoms": [
            "Numerous small, irregular, purple to dark reddish spots on the upper leaf surface.",
            "Spots enlarge and coalesce without distinct white centers (distinguishing from common leaf spot).",
            "Leaf tissue between spots turns purplish-brown, curls upward at edges, and looks burnt or scorched.",
            "Infected flower calyxes dry out ('dead calyx'), reducing fruit market value."
        ],
        "recommended_next_steps": [
            "Rake and remove scorched foliage after harvest during bed renovation.",
            "Avoid overhead irrigation; water early in the day so foliage dries rapidly.",
            "Ensure plants are not overcrowded in matted rows.",
            "Consult a local horticulture specialist for approved fungicide options."
        ],
        "preventive_practices": [
            "Plant certified disease-free strawberry runners of scorch-resistant cultivars.",
            "Renovate June-bearing strawberry beds immediately after harvest by mowing old foliage.",
            "Ensure raised beds with excellent drainage and adequate plant spacing (30–35 cm).",
            "Maintain straw mulch to reduce soil splash onto lower leaves."
        ]
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "crop_display": "Strawberry",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "Strawberry plant shows healthy trifoliate leaves, vigorous crown development, intact serrated margins, and no visible signs of scorch, leaf spot, or powdery mildew.",
        "symptoms": [
            "Lush, dark green trifoliate leaves with clean serrations.",
            "Absence of purple speckling, scorched margins, or powdery white coatings.",
            "Healthy runner and crown development."
        ],
        "recommended_next_steps": [
            "Maintain clean straw mulching around the plants to keep developing berries off bare soil.",
            "Check regularly for two-spotted spider mites and gray mold (Botrytis).",
            "Provide consistent moisture through drip irrigation."
        ],
        "preventive_practices": [
            "Renovate strawberry beds annually to maintain plant vigor.",
            "Apply balanced fertilizer according to soil test recommendations.",
            "Ensure full sun exposure and well-drained planting beds."
        ]
    },

    # -------------------------------------------------------------
    # TOMATO (10 Classes)
    # -------------------------------------------------------------
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Bacterial Spot",
        "pathogen": "Xanthomonas perforans / euvesicatoria (Bacteria)",
        "is_healthy": False,
        "severity": "High",
        "description": "Bacterial spot is a damaging disease of tomatoes prevalent in warm, humid, and rainy climates. It creates small dark greasy spots on leaves and stems, leading to severe leaf drop and blistered fruit.",
        "symptoms": [
            "Small, dark brown to black circular lesions (1–3 mm) with a water-soaked or greasy appearance.",
            "Lesions develop a thin yellow halo and frequently cause leaf margins to brown and curl.",
            "Extensive leaf yellowing and defoliation, exposing fruit to sunscald.",
            "Fruit develop small, raised, blister-like black spots that become rough and scabby."
        ],
        "recommended_next_steps": [
            "Avoid handling, pruning, or picking from plants when foliage is wet.",
            "Disinfect pruning shears and staking tools regularly using 10% bleach or rubbing alcohol.",
            "Shift to drip irrigation; eliminate overhead sprinkler watering.",
            "Consult local agricultural extension for recommended bactericidal treatments (e.g., copper + mancozeb tank mixes)."
        ],
        "preventive_practices": [
            "Purchase certified pathogen-free seeds or perform hot-water seed treatment (50°C for 25 min).",
            "Rotate tomato plots with non-solanaceous crops for a minimum of 2 years.",
            "Stake and prune plants to improve airflow and facilitate rapid leaf drying.",
            "Apply preventative copper-based bactericides during rainy or high-humidity periods."
        ]
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Early blight is one of the most common tomato diseases, attacking older lower leaves first. It is characterized by dark brown spots with concentric ring 'target board' patterns and yellowing tissue.",
        "symptoms": [
            "Dark brown to black spots with distinct concentric rings ('target-board' pattern) on older leaves.",
            "Yellow halo surrounding individual lesions; leaves gradually turn yellow and drop.",
            "Dark, sunken, elongated cankers on stems of seedlings and mature plants.",
            "Dark, leathery, sunken spots near the stem end of developing tomatoes."
        ],
        "recommended_next_steps": [
            "Prune off affected lower leaves up to 30 cm above the ground to eliminate soil-splash contact.",
            "Mulch heavily around the base of plants using clean straw or plastic mulch.",
            "Stake and cage vines to elevate foliage away from damp ground.",
            "Consult local agricultural officer or KVK for recommended preventative fungicides (e.g., mancozeb, copper hydroxide)."
        ],
        "preventive_practices": [
            "Practice a 3-year crop rotation without tomatoes, potatoes, or eggplants.",
            "Plant early blight-tolerant tomato varieties (e.g., Mountain Supreme, Defiant).",
            "Water at the base with drip irrigation or soaker hoses, never overhead.",
            "Clear and burn or deeply bury all solanaceous crop residues after harvest."
        ]
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "is_healthy": False,
        "severity": "Critical",
        "description": "Late blight is a fast-moving, highly destructive pathogen of tomatoes and potatoes that flourishes in cool, wet, or foggy weather. It causes rapid vine collapse and greasy brown fruit rot.",
        "symptoms": [
            "Large, irregular, water-soaked greenish-black lesions on leaves that rapidly enlarge.",
            "White, fuzzy, cottony fungal growth on the underside of infected leaves in moist conditions.",
            "Dark brown to black greasy-looking cankers on stems and petioles.",
            "Firm, greasy, golden-brown to dark brown rot on green or ripening tomatoes."
        ],
        "recommended_next_steps": [
            "URGENT: Inspect all plants immediately; late blight can spread across an entire garden in days.",
            "Immediately bag and remove heavily infected plants; do not leave on compost piles.",
            "Avoid overhead watering and minimize all plant handling during damp conditions.",
            "Contact your local agricultural extension service immediately for regional alert information and chemical recommendations."
        ],
        "preventive_practices": [
            "Plant late blight-resistant tomato varieties (e.g., Mountain Magic, Iron Lady, Legend).",
            "Eliminate volunteer potato and tomato plants in early spring.",
            "Ensure wide spacing (60–90 cm between plants) for maximum airflow.",
            "Apply preventative fungicides (such as mancozeb or chlorothalonil) before cool rainy spells."
        ]
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Leaf Mold",
        "pathogen": "Passalora fulva / Fulvia fulva (Fungus)",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Tomato leaf mold primarily affects tomatoes grown in greenhouses, high tunnels, or areas with high relative humidity (>85%). It produces pale yellow spots on upper leaf surfaces and velvety olive-green mold underneath.",
        "symptoms": [
            "Pale green to yellow spots with indistinct margins on the upper leaf surface.",
            "Olive-green, velvety to brown fungal mold growth directly beneath spots on the leaf underside.",
            "Older leaves become infected first, progressing upward through the plant canopy.",
            "Leaves curl, wither, and drop prematurely, reducing fruit yield."
        ],
        "recommended_next_steps": [
            "Significantly increase ventilation in polyhouses/greenhouses to lower relative humidity below 85%.",
            "Prune lower suckers and dense leaves to improve air circulation within the canopy.",
            "Avoid wetting foliage during irrigation; water exclusively through drip lines.",
            "Consult agricultural extension for registered bio-fungicides or copper sprays."
        ],
        "preventive_practices": [
            "Select leaf mold-resistant tomato varieties (hybrids carrying Cf resistance genes).",
            "Install exhaust fans or open sidewalls in protected cultivation structures.",
            "Sanitize greenhouse structures and interior stakes thoroughly between growing seasons.",
            "Keep plant spacing generous (minimum 50–60 cm between plants)."
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Septoria Leaf Spot",
        "pathogen": "Septoria lycopersici (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Septoria leaf spot is a widespread foliar disease that produces numerous small circular spots with dark borders and light gray centers studded with tiny black pycnidia specks.",
        "symptoms": [
            "Numerous small (2–4 mm), circular spots with dark brown margins and pale gray/tan centers.",
            "Tiny black specks (pycnidia) visible inside the centers of older spots with a hand lens.",
            "Yellowing of leaf tissue surrounding dense spot clusters.",
            "Progressive defoliation from bottom upward, exposing fruit to sunscald (fruit itself is rarely infected)."
        ],
        "recommended_next_steps": [
            "Remove and discard severely spotted lower leaves early in the season.",
            "Apply straw, leaf, or plastic mulch around the plant base to block fungal spores splashing from soil.",
            "Stake and prune tomatoes to maintain an open canopy structure.",
            "Consult local agricultural extension for recommended protective sprays."
        ],
        "preventive_practices": [
            "Practice a 2 to 3-year crop rotation away from solanaceous plants.",
            "Eradicate weed hosts like horsenettle and nightshade around garden perimeters.",
            "Irrigate at soil level with drip lines rather than overhead watering.",
            "Remove and destroy all tomato crop debris at the end of the growing season."
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Two-Spotted Spider Mite Damage",
        "pathogen": "Tetranychus urticae (Arachnid pest)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Two-spotted spider mites are microscopic arachnids that feed on the undersides of tomato leaves by piercing plant cells. They thrive in hot, dry, and dusty conditions, causing stippling and fine webbing.",
        "symptoms": [
            "Fine yellow or white stippling (tiny dots) on the upper surface of leaves.",
            "Leaves take on a bronzed, dusty, or bleached appearance as feeding intensifies.",
            "Fine, silky webbing covering the undersides of leaves and leaf axils.",
            "Leaves turn brown, dry out, curl, and drop, leading to stunted plant growth."
        ],
        "recommended_next_steps": [
            "Inspect the underside of leaves with a 10x hand lens to confirm active mites and eggs.",
            "Spray the undersides of foliage with a strong jet of water to dislodge mites and reduce dust.",
            "Avoid broad-spectrum pyrethroid insecticides that kill beneficial predatory mites.",
            "Apply horticultural insecticidal soap, neem oil, or an approved miticide if threshold is exceeded."
        ],
        "preventive_practices": [
            "Encourage and release predatory mites (e.g., Phytoseiulus persimilis or Neoseiulus californicus).",
            "Keep soil adequately watered; water-stressed plants are preferred mite hosts.",
            "Control dust along roadways and pathways adjacent to tomato plots.",
            "Remove heavily infested individual plants to prevent migration to neighboring rows."
        ]
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Target Spot",
        "pathogen": "Corynespora cassiicola (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Target spot is a fungal disease favored by warm, humid conditions. It produces circular brown lesions with faint concentric rings on leaves, stems, and fruit, and can cause significant foliage loss.",
        "symptoms": [
            "Small, pinpoint brown spots that expand into circular lesions with light brown centers.",
            "Lesions show subtle concentric rings and often develop yellow halos.",
            "Elongated brown cankers on stems and petioles.",
            "Fruit develop sunken, circular lesions with light brown centers and darker margins."
        ],
        "recommended_next_steps": [
            "Prune lower suckers and leaves to increase airflow within the plant canopy.",
            "Remove and destroy infected plant parts showing target spot lesions.",
            "Switch to drip irrigation to keep leaf blades dry.",
            "Consult local agricultural extension for recommended target spot fungicides."
        ],
        "preventive_practices": [
            "Maintain wide plant spacing (at least 60 cm between plants in rows).",
            "Rotate crops for at least 2 years out of solanaceous and cucurbit hosts.",
            "Stake and tie plants to keep fruit and foliage off the soil.",
            "Destroy crop residues promptly after final harvest."
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "pathogen": "Tomato Yellow Leaf Curl Virus (Vectored by Whitefly, Bemisia tabaci)",
        "is_healthy": False,
        "severity": "Critical",
        "description": "Tomato Yellow Leaf Curl Virus (TYLCV) is a devastating viral disease transmitted by silverleaf whiteflies. It causes severe plant stunting, erect bushy growth, upward leaf curling, and catastrophic flower drop.",
        "symptoms": [
            "Severe upward cupping and curling of leaflet margins.",
            "Pronounced yellowing (chlorosis) along leaf margins and interveinal areas.",
            "Leaflets become small, crinkled, and leathery.",
            "Severe plant stunting with a bushy appearance; flowers drop before fruit set, causing near-total yield loss."
        ],
        "recommended_next_steps": [
            "Inspect the underside of leaves for tiny whiteflies; disturb foliage gently to check for flying adults.",
            "Rogue out and destroy infected plants immediately (seal in bags before disposal to trap whiteflies).",
            "Install yellow sticky traps (10–15 traps per acre) to monitor and suppress whitefly numbers.",
            "Consult local agricultural advisories for registered whitefly management options (e.g., neem oil, insecticidal soaps)."
        ],
        "preventive_practices": [
            "Plant TYLCV-resistant tomato hybrids (e.g., US 440, Sakata varieties with Ty resistance genes).",
            "Use 40–50 mesh insect-proof netting in nurseries to prevent whitefly infestation of young seedlings.",
            "Apply reflective silver plastic mulches that repel whiteflies during early crop stages.",
            "Maintain field boundaries free from alternative weed hosts (e.g., Datura, Solanum nigrum)."
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Tomato Mosaic Virus (ToMV)",
        "pathogen": "Tomato Mosaic Tobamovirus (Mechanically transmitted virus)",
        "is_healthy": False,
        "severity": "High",
        "description": "Tomato mosaic virus is an extremely stable, easily transmitted viral pathogen. It spreads mechanically via hands, pruning tools, and grafting, causing leaf mosaic patterns, distortion, and internal fruit browning.",
        "symptoms": [
            "Mottling of leaves with alternating light green and dark green mosaic patches.",
            "Leaf distortion: narrowing of leaves into 'shoestring' or 'fern-leaf' shapes.",
            "Young leaves showing blistering, puckering, and stunted growth.",
            "Internal brown necrosis (brown streaks) inside the flesh of green or ripening tomatoes."
        ],
        "recommended_next_steps": [
            "CRITICAL: Wash hands thoroughly with soap and water before and after touching tomato plants.",
            "Disinfect pruning shears between plants using skimmed milk (20%) or trisodium phosphate (TSP).",
            "Immediately remove and dispose of infected plants (do not compost in garden).",
            "Do not smoke or use tobacco products near tomatoes, as tobacco products can harbor mosaic tobamoviruses."
        ],
        "preventive_practices": [
            "Plant ToMV-resistant tomato cultivars (check seed packets for 'ToMV' or 'Tm-2a' resistance).",
            "Use certified virus-free seed from reputable sources.",
            "Disinfect stakes, trellises, and pots with a 10% bleach solution between seasons.",
            "Handle plants with clean gloves and avoid unnecessary mechanical contact."
        ]
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "crop_display": "Tomato",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The tomato foliage displays strong vigor, deep green color, healthy leaf texture, and complete absence of fungal blights, viral mottling, or bacterial spot lesions.",
        "symptoms": [
            "Deep green, well-expanded compound leaves with clean serrated margins.",
            "Absence of target-board spots, yellow margins, water-soaked specks, or leaf curl.",
            "Healthy stem extension and active blossom clusters."
        ],
        "recommended_next_steps": [
            "Continue regular weekly scouting, examining lower leaves and stems for early disease signs.",
            "Maintain consistent drip irrigation to keep soil moisture uniform.",
            "Prune side suckers to maintain single or double leaders for optimal fruit production."
        ],
        "preventive_practices": [
            "Stake and cage vines to keep foliage off bare ground.",
            "Apply organic mulch around the root zone to conserve moisture and block soil splash.",
            "Follow balanced fertilization with adequate calcium and potassium."
        ]
    },

    # -------------------------------------------------------------
    # WHEAT (6 Classes)
    # -------------------------------------------------------------
    "Wheat___healthy": {
        "crop": "Wheat",
        "crop_display": "Wheat",
        "condition": "Healthy Wheat",
        "pathogen": "None detected",
        "is_healthy": True,
        "severity": "None",
        "description": "The wheat crop demonstrates healthy vegetative or reproductive growth, clean green flag leaves, and complete absence of rust pustules, powdery mildew, or septoria blotches.",
        "symptoms": [
            "Clean, uniformly green flag leaves and leaf sheaths.",
            "No orange/yellow rust pustules, powdery white patches, or brown blotches.",
            "Strong tillering and normal spike / head emergence."
        ],
        "recommended_next_steps": [
            "Perform weekly field walks through representative field transects.",
            "Monitor during critical boot, heading, and grain-filling stages for any rust incursions.",
            "Ensure timely irrigation during crown root initiation (CRI), booting, and milk stages."
        ],
        "preventive_practices": [
            "Sow certified rust-resistant wheat varieties recommended for your agro-ecological zone.",
            "Ensure timely sowing (typically first fortnight of November in Indo-Gangetic Plains).",
            "Apply balanced NPK fertilization with recommended zinc sulphate."
        ]
    },
    "Wheat___leaf_rust": {
        "crop": "Wheat",
        "crop_display": "Wheat",
        "condition": "Leaf Rust (Brown Rust)",
        "pathogen": "Puccinia triticina (Fungus)",
        "is_healthy": False,
        "severity": "High",
        "description": "Leaf rust (also called brown rust) is the most common wheat rust worldwide. It produces small, round to oval orange-brown powdery pustules scattered randomly across the upper leaf surface.",
        "symptoms": [
            "Small, circular to oval bright orange-brown powdery pustules (uredinia) on upper leaf surfaces.",
            "Pustules scattered randomly rather than arranged in distinct stripes.",
            "Spore powder rubs off readily on fingers or a white cloth.",
            "Heavily infected leaves turn chlorotic, senesce prematurely, and cause shriveled grain."
        ],
        "recommended_next_steps": [
            "Check the flag leaf and penultimate leaf to evaluate infection severity.",
            "Determine the wheat growth stage; infections before flowering cause the highest yield losses.",
            "Consult the nearest ICAR wheat research station or state agricultural university advisory.",
            "Apply recommended triazole fungicides (e.g., propiconazole 25 EC @ 0.1%) if threshold is crossed."
        ],
        "preventive_practices": [
            "Plant recommended leaf rust-resistant wheat varieties (e.g., HD 2967, DBW 187, PBW 550, WH 1105).",
            "Avoid late sowing, which exposes crops to warmer spring temperatures favoring rust multiplication.",
            "Apply balanced nitrogen; avoid excessive urea top-dressing that softens leaf tissues.",
            "Participate in regional surveillance networks reporting rust appearances."
        ]
    },
    "Wheat___powdery_mildew": {
        "crop": "Wheat",
        "crop_display": "Wheat",
        "condition": "Powdery Mildew",
        "pathogen": "Blumeria graminis f. sp. tritici (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Powdery mildew of wheat attacks leaves, stems, and heads, producing white, cottony fungal colonies that turn dull gray. It is favored by cool, cloudy, humid conditions and dense crop canopies.",
        "symptoms": [
            "White, fluffy, cottony or powdery patches on upper leaf surfaces, leaf sheaths, and glumes.",
            "Powdery patches enlarge, coalesce, and turn dull grayish-brown.",
            "Small black specks (cleistothecia fruiting bodies) appear embedded in the mature gray patches.",
            "Lower leaves turn yellow and die early; severe infection reduces spikelet count and grain filling."
        ],
        "recommended_next_steps": [
            "Scout lower leaves in dense, heavily fertilized portions of the field.",
            "Avoid over-irrigating during cloudy, humid weather spells.",
            "Assess whether mildew has reached the upper two canopy leaves (flag leaf and F-1).",
            "Consult local extension officer for recommended fungicide interventions if disease spreads upward."
        ],
        "preventive_practices": [
            "Grow resistant wheat cultivars recommended for your state.",
            "Avoid excessive seeding rates that create an overly dense, humid microclimate.",
            "Balance nitrogen fertilizer with adequate potassium and phosphorus.",
            "Practice crop rotation with non-cereal crops."
        ]
    },
    "Wheat___septoria": {
        "crop": "Wheat",
        "crop_display": "Wheat",
        "condition": "Septoria Tritici Blotch",
        "pathogen": "Zymoseptoria tritici / Septoria tritici (Fungus)",
        "is_healthy": False,
        "severity": "Moderate to High",
        "description": "Septoria leaf blotch produces rectangular to irregular brown lesions bounded by leaf veins. Inside mature lesions, conspicuous tiny black specks (pycnidia) form, serving as key diagnostic markers.",
        "symptoms": [
            "Initial light green to yellow oval spots that elongate into irregular brown lesions.",
            "Lesions restricted longitudinally by parallel leaf veins.",
            "Prominent tiny black specks (pycnidia) clearly visible inside mature tan lesions.",
            "Blighted areas coalesce, causing rapid drying of leaves during rainy weather."
        ],
        "recommended_next_steps": [
            "Monitor lower leaves after periods of continuous rain or heavy morning dews.",
            "Use a hand lens to confirm the presence of black pycnidia dots inside lesions.",
            "Evaluate if lesions are climbing upward from the lower canopy to the flag leaf.",
            "Consult regional wheat advisories for fungicide recommendations if weather remains wet."
        ],
        "preventive_practices": [
            "Plant certified wheat varieties with documented tolerance to Septoria blotch.",
            "Incorporate or manage previous wheat stubble to accelerate residue decomposition.",
            "Practice crop rotation with broadleaf crops (chickpea, mustard, lentils).",
            "Maintain optimal row spacing to facilitate canopy drying."
        ]
    },
    "Wheat___stem_rust": {
        "crop": "Wheat",
        "crop_display": "Wheat",
        "condition": "Stem Rust (Black Rust)",
        "pathogen": "Puccinia graminis f. sp. tritici (Fungus)",
        "is_healthy": False,
        "severity": "Critical",
        "description": "Stem rust (black rust) is the most destructive wheat rust. It attacks stems, leaf sheaths, and spikes, producing large reddish-brown to black elongated pustules that rupture the epidermis and cause lodging and crop failure.",
        "symptoms": [
            "Large, elongated, reddish-brown pustules predominantly on stems, leaf sheaths, and glumes.",
            "Pustules violently rupture the plant epidermis, leaving ragged edges of torn plant tissue.",
            "Pustules turn dark black late in the season as black teliospores develop.",
            "Stems become severely weakened and brittle, leading to extensive lodging and complete crop loss."
        ],
        "recommended_next_steps": [
            "CRITICAL: Report any suspected stem rust occurrence immediately to the nearest wheat research institute or agricultural department.",
            "Check lower stems, sheaths, and awns closely for torn epidermal pustules.",
            "Do not delay; stem rust can develop explosively under warm (20–30°C) conditions.",
            "Follow emergency state agricultural advisories on fungicide applications (e.g., propiconazole or tebuconazole)."
        ],
        "preventive_practices": [
            "Sow stem-rust resistant cultivars approved by national wheat improvement programs (e.g., Sr-gene carrying varieties).",
            "Eradicate alternate hosts (barberry, Berberis vulgaris) near wheat fields if present.",
            "Participate in global and national rust surveillance programs.",
            "Avoid late sowing to ensure wheat matures before high-temperature rust season."
        ]
    },
    "Wheat___yellow_rust": {
        "crop": "Wheat",
        "crop_display": "Wheat",
        "condition": "Yellow Rust (Stripe Rust)",
        "pathogen": "Puccinia striiformis f. sp. tritici (Fungus)",
        "is_healthy": False,
        "severity": "Critical",
        "description": "Yellow rust (stripe rust) is a major threat in cooler wheat-growing regions (such as northern India, hills, and foothill plains). It forms distinctive bright yellow powdery pustules arranged in narrow parallel stripes.",
        "symptoms": [
            "Bright yellow to orange-yellow powdery pustules arranged in narrow, parallel stripes along leaf veins.",
            "Stripes resemble yellow sewing machine stitches running the length of the leaf blade.",
            "Yellow powdery urediniospores readily rub off on fingers or white paper.",
            "Severe infection causes complete chlorosis of flag leaves and severely shriveled grains."
        ],
        "recommended_next_steps": [
            "Inspect fields early in the season (January–February), especially in cooler northern tracts and foothill regions.",
            "Look for localized yellow patches or 'foci' in fields and treat them immediately before spores spread.",
            "Report stripe rust detections to local Krishi Vigyan Kendra or regional wheat research directorate.",
            "Spray recommended fungicides (e.g., propiconazole 25 EC @ 0.1% or tebuconazole) upon first detection."
        ],
        "preventive_practices": [
            "Sow stripe rust-resistant cultivars recommended by ICAR-IIWBR (e.g., DBW 187, DBW 222, HD 3226, PBW 725).",
            "Avoid sowing susceptible older varieties in yellow-rust prone districts.",
            "Sow timely (first half of November) so plants develop adult plant resistance before peak spore arrival.",
            "Engage in community-level monitoring with neighboring farmers to treat early infection hot spots."
        ]
    },

    # =============================================================
    # COTTON (Expanded Knowledge Base - 5 Profiles)
    # =============================================================
    "Cotton___Bacterial_Blight": {
        "crop": "Cotton",
        "crop_display": "Cotton",
        "condition": "Bacterial Blight (Black Arm)",
        "pathogen": "Xanthomonas citri pv. malvacearum (Bacteria)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Bacterial blight is a major bacterial disease of cotton causing seedling blight, angular leaf spots delimited by veins, black arm lesions on branches, and boll rot.",
        "symptoms": [
            "Angular water-soaked spots on leaves delimited by small veins, later turning dark reddish-brown to black.",
            "Dark elongated lesions on petioles and vegetative branches ('black arm' phase), causing branch breakage.",
            "Water-soaked oily round spots on developing bolls, resulting in boll rotting and stained lint.",
            "Seedling death when circular lesions form on cotyledons ('cotyledonary phase')."
        ],
        "recommended_next_steps": [
            "Inspect underside of leaves in morning dew for water-soaked angular patches.",
            "Avoid inter-cultivation when cotton plants are wet with rain or irrigation.",
            "Rogue out severely infected seedlings in early crop stages.",
            "Consult local KVK or agricultural officer for recommended bactericide (copper oxychloride + streptocycline) sprays."
        ],
        "preventive_practices": [
            "Delint seed acid treatment (commercial sulphuric acid 100 ml/kg seed) to destroy seed-borne bacteria.",
            "Sow certified resistant cotton hybrids recommended for your regional agro-climatic zone.",
            "Maintain balanced fertilization; avoid excess nitrogen that promotes lush soft tissue.",
            "Collect and burn cotton stubble immediately after harvest to break inoculum continuity."
        ]
    },
    "Cotton___Leaf_Curl_Virus": {
        "crop": "Cotton",
        "crop_display": "Cotton",
        "condition": "Cotton Leaf Curl Virus (CLCuV)",
        "pathogen": "Cotton Leaf Curl Begomovirus (Vectored by Whitefly, Bemisia tabaci)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Cotton Leaf Curl Virus (CLCuD) is a devastating viral disease in northern and central cotton zones. It causes upward or downward leaf curling, vein thickening, leaf enations (cup-like growths), and severe stunting.",
        "symptoms": [
            "Upward or downward cupping and curling of young leaf margins.",
            "Thickening and darkening of veins on the underside of leaves.",
            "Enations: small, leaf-like outgrowths developing on the underside of primary leaf veins.",
            "Severe plant stunting, shortened internodes, and drastic reduction in boll formation."
        ],
        "recommended_next_steps": [
            "Scout weekly for whitefly nymphs and adults on the underside of upper canopy leaves.",
            "Install yellow sticky traps (10–15 per acre) along field borders to monitor vector influx.",
            "Rogue out and destroy CLCuV-infected plants during early vegetative stage (before 60 days).",
            "Consult state agricultural university weekly pest advisories for whitefly economic thresholds."
        ],
        "preventive_practices": [
            "Grow CLCuD-resistant Bt cotton hybrids approved by regional agricultural authorities.",
            "Avoid planting cotton near alternate weed hosts (such as Abutilon indicum, Sida cordifolia).",
            "Spray neem-based formulations (azadirachtin 1500 ppm @ 1 L/ha) upon early whitefly detection.",
            "Promote natural predators like green lacewings (Chrysoperla carnea) and predatory mites."
        ]
    },
    "Cotton___Fusarium_Wilt": {
        "crop": "Cotton",
        "crop_display": "Cotton",
        "condition": "Fusarium Wilt",
        "pathogen": "Fusarium oxysporum f. sp. vasinfectum (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Fusarium wilt is a soil-borne vascular fungal disease favored by acidic or sandy soils and root-knot nematode wounding. It causes yellowing, drooping, vascular browning, and plant death.",
        "symptoms": [
            "Yellowing (chlorosis) starting along leaf margins and spreading inward between veins.",
            "Wilting of foliage progressing from lower branches upward, leading to leaf drop.",
            "Dark brown to black discoloration in the xylem vascular ring visible when stems are sliced longitudinally.",
            "Young plants wilt rapidly while older plants suffer stunted growth and premature death."
        ],
        "recommended_next_steps": [
            "Cut lower stem open lengthwise: presence of a brown or black vascular cylinder confirms vascular wilt.",
            "Check root zone for root-knot nematode galls which facilitate fungal entry.",
            "Avoid moving soil or farm implements from wilt-infested patches to clean fields.",
            "Consult regional extension specialists for soil bio-inoculant recommendations."
        ],
        "preventive_practices": [
            "Plant wilt-resistant cotton cultivars adapted to local soil types.",
            "Seed treatment with Trichoderma viride or Pseudomonas fluorescens @ 10 g/kg seed.",
            "Rotate cotton with non-host crops (such as sorghum, pearl millet, or wheat) for 3–4 seasons.",
            "Apply farmyard manure enriched with Trichoderma to enhance antagonistic soil microflora."
        ]
    },
    "Cotton___Alternaria_Leaf_Spot": {
        "crop": "Cotton",
        "crop_display": "Cotton",
        "condition": "Alternaria Leaf Spot",
        "pathogen": "Alternaria macrospora / alternata (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Alternaria leaf spot is a widespread fungal foliar disease in cotton, particularly severe when plants experience potassium deficiency, drought stress, or during prolonged cloudy humid spells.",
        "symptoms": [
            "Small circular to irregular brown spots (1–10 mm) with distinct concentric rings.",
            "Lesions develop a purple or reddish-brown border, with brittle centers that may drop out.",
            "Extensive leaf spotting leads to premature defoliation and boll shedding.",
            "Stems and bracts may also develop sunken elongated necrotic cankers."
        ],
        "recommended_next_steps": [
            "Scout canopy during peak boll-setting stage when nutrient demand is highest.",
            "Test soil or petiole potassium levels; potassium-stressed cotton is highly vulnerable.",
            "Apply foliar potassium nitrate (KNO3 @ 1%) to strengthen leaf physiological defense.",
            "Consult local agricultural officer for protective fungicide sprays if spots spread to upper leaves."
        ],
        "preventive_practices": [
            "Maintain balanced soil fertility with split potassium applications.",
            "Avoid waterlogging and improve drainage in cotton fields.",
            "Destroy crop debris post-harvest to minimize overwintering fungal spores.",
            "Apply prophylactic protective contact fungicides (mancozeb or copper oxychloride) during early monsoon showers."
        ]
    },
    "Cotton___healthy": {
        "crop": "Cotton",
        "crop_display": "Cotton",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The cotton plant displays healthy, broad palmate leaves with dark green coloration, sturdy branching, and no visible signs of leaf curl, bacterial blight, or fungal spotting.",
        "symptoms": [
            "Uniform dark green palmate leaves with smooth clean margins.",
            "Absence of vein thickening, enations, angular water-soaked lesions, or chlorotic mottling.",
            "Healthy square and sympodial branch development."
        ],
        "recommended_next_steps": [
            "Continue regular weekly field scouting across random crop rows.",
            "Monitor ETL (economic threshold level) for sucking pests (jassids, thrips, whiteflies).",
            "Maintain timely weeding and intercultural operations."
        ],
        "preventive_practices": [
            "Follow integrated pest management (IPM) with border crops (maize, marigold).",
            "Apply balanced fertilizer according to soil test recommendations.",
            "Ensure regulated irrigation during critical flowering and boll development phases."
        ]
    },

    # =============================================================
    # CHILLI / PEPPER (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Chilli___Leaf_Curl_Virus": {
        "crop": "Chilli",
        "crop_display": "Chilli",
        "condition": "Chilli Leaf Curl Virus (ChiLCV)",
        "pathogen": "Chilli Leaf Curl Virus (Vectored by Whitefly, Bemisia tabaci)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Chilli leaf curl virus is one of the most destructive diseases in chilli cultivation. Transmitted by whiteflies, it causes upward curling of leaves, crinkling, vein clearing, severe stunting, and bushy bushy growth.",
        "symptoms": [
            "Upward curling and cupping of leaf margins with puckered leaf surfaces.",
            "Vein clearing and chlorosis along secondary leaf veins.",
            "Severe reduction in leaf size ('little leaf' appearance) and shortened internodes.",
            "Flower bud drop and small, deformed, seedless pods, causing total yield failure."
        ],
        "recommended_next_steps": [
            "Inspect nursery beds and main field for whitefly vectors under leaves.",
            "Eradicate and bury infected virus-carrying plants promptly during early crop establishment.",
            "Place yellow sticky traps (15–20 per acre) across the field at canopy level.",
            "Consult local extension officer for recommended vector management (neem oil or diafenthiuron)."
        ],
        "preventive_practices": [
            "Raise seedlings in insect-proof nylon net nurseries (40–50 mesh).",
            "Grow border barrier crops of maize, sorghum, or pearl millet (3–4 rows) to filter insect vectors.",
            "Plant tolerant or resistant chilli hybrids recommended for your district.",
            "Spray neem oil (10,000 ppm @ 2 ml/L) at 10-day intervals from transplanting."
        ]
    },
    "Chilli___Anthracnose": {
        "crop": "Chilli",
        "crop_display": "Chilli",
        "condition": "Anthracnose / Dieback",
        "pathogen": "Colletotrichum capsici / gloeosporioides (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Anthracnose (also known as ripe fruit rot and dieback) causes brown circular sunken lesions with concentric rings of black acervuli on mature fruits, and dieback of young twigs from the tip downward.",
        "symptoms": [
            "Circular or elongated sunken lesions on green and ripe fruits.",
            "Concentric rings of minute black dots (acervuli) inside fruit lesions.",
            "Dieback: twigs wither and dry up from tips downward, turning straw-colored with gumming.",
            "Small circular spots with grayish-white centers on leaves during humid weather."
        ],
        "recommended_next_steps": [
            "Pick and safely destroy infected fruit immediately; do not leave rotting fruit in the field.",
            "Prune back blighted twig tips 2 inches into healthy green wood using sanitized clippers.",
            "Avoid overhead irrigation to keep maturing chilli fruits dry.",
            "Consult agricultural authorities for recommended protective fungicide sprays (azoxystrobin or mancozeb)."
        ],
        "preventive_practices": [
            "Treat seed before sowing with Trichoderma viride (10 g/kg) or thiram (3 g/kg).",
            "Plant resistant chilli cultivars recommended by ICAR-IIHR.",
            "Ensure proper crop spacing and weed eradication to lower canopy humidity.",
            "Collect and burn crop residues immediately after harvest."
        ]
    },
    "Chilli___Bacterial_Spot": {
        "crop": "Chilli",
        "crop_display": "Chilli",
        "condition": "Bacterial Spot",
        "pathogen": "Xanthomonas euvesicatoria (Bacteria)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Bacterial spot of chilli produces small water-soaked dark spots on foliage and stems, causing heavy leaf drop and blistered rough spots on pods.",
        "symptoms": [
            "Small circular to angular water-soaked dark brown spots on lower leaf surfaces.",
            "Leaf tissue turns chlorotic around spots, resulting in severe early defoliation.",
            "Rough, raised, scabby dark brown spots on developing chilli pods.",
            "Elongated dark cankers along stems and fruiting branches."
        ],
        "recommended_next_steps": [
            "Halt all overhead sprinkler irrigation; switch to drip lines.",
            "Do not work in chilli fields when foliage is wet from morning dew.",
            "Sanitize harvesting crates and shears with disinfectant.",
            "Seek local extension guidance for copper-based bactericide applications."
        ],
        "preventive_practices": [
            "Use certified pathogen-free seeds treated with hot water (50°C for 25 min).",
            "Rotate crops for at least 2 years out of solanaceous vegetables (tomato, brinjal, potato).",
            "Apply balanced fertilizer with adequate potassium to harden plant cell walls.",
            "Eradicate solanaceous weeds around field borders."
        ]
    },
    "Chilli___healthy": {
        "crop": "Chilli",
        "crop_display": "Chilli",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The chilli plant exhibits dark green, lustrous lanceolate leaves with smooth margins and no signs of leaf curl cupping, anthracnose lesions, or bacterial speckling.",
        "symptoms": [
            "Smooth, vibrant green, fully expanded leaves.",
            "Absence of upward curling, mottled venation, or necrotic fruit spots.",
            "Healthy blossom set and vigorous branching."
        ],
        "recommended_next_steps": [
            "Continue regular weekly scouting for thrips and mites on leaf undersides.",
            "Maintain uniform drip fertigation schedule.",
            "Mulch rows with silver/black reflective film to deter sucking pests."
        ],
        "preventive_practices": [
            "Install yellow and blue sticky traps for early pest surveillance.",
            "Ensure balanced fertilization with calcium to prevent fruit blossom end rot.",
            "Follow integrated pest management (IPM) practices."
        ]
    },

    # =============================================================
    # GROUNDNUT / PEANUT (Expanded Knowledge Base - 3 Profiles)
    # =============================================================
    "Groundnut___Early_Late_Leaf_Spot": {
        "crop": "Groundnut",
        "crop_display": "Groundnut (Peanut)",
        "condition": "Tikka Leaf Spot (Early & Late)",
        "pathogen": "Cercospora arachidicola (Early) & Phaeoisariopsis personata (Late) (Fungi)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Tikka disease is the most economically damaging foliar disease of groundnut. Early leaf spot produces reddish-brown spots with yellow halos, while late leaf spot produces darker circular spots with carbon-black sporulation underneath.",
        "symptoms": [
            "Early leaf spot: circular reddish-brown spots with conspicuous bright yellow halos on upper leaf surfaces.",
            "Late leaf spot: smaller, darker carbon-black circular spots mostly on lower leaf surface without prominent yellow halos.",
            "Spots coalesce, leading to extensive premature defoliation and weakened peg attachment.",
            "Severely reduced pod yield and oil content; pods detach in soil during harvest."
        ],
        "recommended_next_steps": [
            "Scout canopy beginning 35–40 days after sowing, checking lower foliage first.",
            "Avoid excessive moisture stress followed by sudden heavy irrigation.",
            "Collect and burn severely infected crop debris after harvest.",
            "Consult local agricultural research station for recommended protective sprays (hexaconazole or tebuconazole)."
        ],
        "preventive_practices": [
            "Seed treatment with Trichoderma viride (4 g/kg) or carbendazim (2 g/kg seed).",
            "Grow Tikka-tolerant cultivars recommended by ICRISAT and ICAR (e.g., Kadiri 6, ICGV lines).",
            "Practice crop rotation with cereals (pearl millet, sorghum, maize).",
            "Apply gypsum (400 kg/ha) at peak flowering to strengthen pod shells and plant vigor."
        ]
    },
    "Groundnut___Rust": {
        "crop": "Groundnut",
        "crop_display": "Groundnut (Peanut)",
        "condition": "Groundnut Rust",
        "pathogen": "Puccinia arachidis (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Groundnut rust produces small, orange-brown powdery pustules on the lower surface of leaves. Often appearing alongside Tikka disease, it causes leaves to dry up and curl like paper without dropping immediately.",
        "symptoms": [
            "Minute round reddish-brown to orange powdery pustules primarily on lower leaf surfaces.",
            "Pustules rupture the epidermis, releasing powdery cinnamon-brown urediniospores.",
            "Infected leaves curl upward, dry out, and turn brown, remaining attached to the stem ('curled parchment' look).",
            "Severely blighted plants mature prematurely, producing small shriveled pods."
        ],
        "recommended_next_steps": [
            "Inspect leaf undersides regularly during warm, humid weather.",
            "Differentiate from Tikka: rust pustules are raised and powdery; Tikka spots are flat necrotic lesions.",
            "Apply recommended combined fungicide spray (e.g. tebuconazole + trifloxystrobin) if rust threshold is reached.",
            "Report severe early-season rust outbreaks to local agricultural extension."
        ],
        "preventive_practices": [
            "Plant rust-resistant or moderately resistant groundnut cultivars.",
            "Early sowing to escape peak airborne spore showers.",
            "Intercrop with cereal crops (sorghum, pearl millet 4:1 ratio) to reduce disease spread.",
            "Eradicate volunteer groundnut plants during off-season."
        ]
    },
    "Groundnut___healthy": {
        "crop": "Groundnut",
        "crop_display": "Groundnut (Peanut)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The groundnut canopy displays healthy, vibrant tetrafoliate leaves, robust stems, clean leaf surfaces, and absence of Tikka spots, rust pustules, or bud necrosis.",
        "symptoms": [
            "Lush green tetrafoliate compound leaves with clean margins.",
            "Absence of yellow-ringed circular spots, orange pustules, or leaf curling.",
            "Strong peg initiation and normal nodulation."
        ],
        "recommended_next_steps": [
            "Maintain soil moisture during critical flowering, pegging, and pod-formation stages.",
            "Apply recommended gypsum dose (400–500 kg/ha) at 45 days after sowing.",
            "Scout regularly for tobacco caterpillar and leaf miner."
        ],
        "preventive_practices": [
            "Inoculate seeds with Rhizobium culture before sowing.",
            "Maintain weed-free conditions during early vegetative phase.",
            "Follow integrated nutrient and pest management recommendations."
        ]
    },

    # =============================================================
    # MANGO (Expanded Knowledge Base - 5 Profiles)
    # =============================================================
    "Mango___Anthracnose": {
        "crop": "Mango",
        "crop_display": "Mango",
        "condition": "Anthracnose",
        "pathogen": "Colletotrichum gloeosporioides (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Anthracnose is the most widespread fungal disease of mango. It causes dark brown circular foliar lesions, blossom blight, twig dieback, and 'tear-stain' black rot on developing and ripening mango fruits.",
        "symptoms": [
            "Small dark brown to black circular lesions on young leaves, expanding and causing leaf distortion.",
            "Blossom blight: flower panicles turn black, dry up, and drop, resulting in total fruit set failure.",
            "Twig cankers: young terminal shoots wither and turn black.",
            "Fruit lesions: dark, sunken circular spots or vertical 'tear-stain' black streaks, causing rot."
        ],
        "recommended_next_steps": [
            "Prune dead twigs and blighted panicles after harvest; burn pruned wood.",
            "Avoid overhead irrigation during flowering and fruit setting.",
            "Collect and destroy fallen infected leaves and mummified mangoes.",
            "Consult local horticulture extension officer for pre-bloom and post-bloom protective spray timings."
        ],
        "preventive_practices": [
            "Prune tree canopy annually after harvest to improve sunlight penetration and air movement.",
            "Apply prophylactic copper oxychloride (3 g/L) before flowering and after harvest.",
            "Dip harvested fruits in hot water (52°C for 5 minutes) to prevent post-harvest anthracnose decay.",
            "Maintain orchard sanitation and weed suppression."
        ]
    },
    "Mango___Powdery_Mildew": {
        "crop": "Mango",
        "crop_display": "Mango",
        "condition": "Powdery Mildew",
        "pathogen": "Oidium mangiferae (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Powdery mildew attacks mango blossoms, flower stalks, young leaves, and marble-sized fruitlets. Characterized by white powdery fungal mycelium, it causes massive floral shedding and yield loss.",
        "symptoms": [
            "White talcum powder-like fungal growth on panicle branches, flowers, and fruitlets.",
            "Infected flowers fail to open and drop prematurely, leaving bare panicle rachises.",
            "Young foliage develops powdery white patches, curls upward, and turns purplish-brown.",
            "Infected fruitlets turn brown, develop corky skin cracking, and drop at marble size."
        ],
        "recommended_next_steps": [
            "Scout flowering panicles at bud-burst and panicle emergence stages.",
            "Dust with fine wettable sulfur or apply approved triazole (hexaconazole) at early panicle emergence.",
            "Monitor weather: cool nights with morning dew and warm dry days trigger severe mildew waves.",
            "Follow university spray schedules timed strictly before 50% blossom opening to protect pollinator bees."
        ],
        "preventive_practices": [
            "Prune inner dense crisscrossing branches during post-harvest canopy management.",
            "Plant powdery mildew-tolerant cultivars (such as Neelum) where adapted.",
            "Apply preventive wettable sulfur (2 g/L) at panicle emergence.",
            "Manage orchard weeds that elevate microclimatic humidity."
        ]
    },
    "Mango___Bacterial_Canker": {
        "crop": "Mango",
        "crop_display": "Mango",
        "condition": "Bacterial Canker",
        "pathogen": "Xanthomonas campestris pv. mangiferaeindicae (Bacteria)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Bacterial canker causes water-soaked angular black lesions on mango leaves, raised star-shaped cankers on fruit with gummy exudate, and branch cankers that cause twig dieback.",
        "symptoms": [
            "Angular water-soaked spots on leaves surrounded by clear yellow halos, turning dark black.",
            "Raised, rough, star-shaped cracks (cankers) on fruit with sticky bacterial gum oozing out.",
            "Black longitudinal cankers on petioles and young green shoots.",
            "Severe leaf drop and premature dropping of infected fruitlets."
        ],
        "recommended_next_steps": [
            "Prune cankered twigs and burn infected plant debris.",
            "Avoid mechanical wounding of branches during harvest or pruning.",
            "Establish windbreaks around orchards to reduce wind-driven branch rubbing and bacterial spread.",
            "Seek advice from regional horticulture officer on copper bactericide spray schedules."
        ],
        "preventive_practices": [
            "Use certified disease-free grafted saplings from accredited nurseries.",
            "Spray copper oxychloride (3 g/L) + streptocycline (100 ppm) during active vegetative flush.",
            "Avoid planting highly susceptible cultivars in high-rainfall, wind-prone zones.",
            "Sanitize pruning tools between cuts with 10% household bleach."
        ]
    },
    "Mango___Die_Back": {
        "crop": "Mango",
        "crop_display": "Mango",
        "condition": "Die Back",
        "pathogen": "Lasiodiplodia theobromae (Botryodiplodia) (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Die back is a vascular fungal disease that causes terminal shoots to dry up and die from the tip downward. Leaves turn brown, shrivel, and remain attached to the dead branch.",
        "symptoms": [
            "Discoloration and darkening of terminal green twigs, spreading downward into older wood.",
            "Leaves turn dull brown, roll upward, and dry out, remaining attached to dead branches.",
            "Brownish discoloration visible in the xylem vascular tissues when twigs are cut open.",
            "Bark splitting and dark gum exudation from cankered branches."
        ],
        "recommended_next_steps": [
            "Prune infected branches at least 3–4 inches below the discolored wood into healthy green tissue.",
            "Immediately paint cut surfaces with copper oxychloride paste or Bordeaux paste.",
            "Collect and burn all pruned dead branches.",
            "Control stem borer beetles whose tunnels create entry wounds for the fungus."
        ],
        "preventive_practices": [
            "Maintain balanced tree nutrition and ensure adequate irrigation to prevent heat/drought stress.",
            "Avoid making large ragged pruning wounds; use sharp bypass pruners.",
            "Spray copper oxychloride (3 g/L) post-harvest after completion of pruning.",
            "Paint main trunks with Bordeaux paste before monsoon onset."
        ]
    },
    "Mango___healthy": {
        "crop": "Mango",
        "crop_display": "Mango",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The mango foliage exhibits healthy, leathery, dark green lanceolate leaves with intact margins, glossy surface, and no evidence of anthracnose, mildew, or canker lesions.",
        "symptoms": [
            "Lustrous, deep green, lanceolate leaves with clean margins.",
            "Absence of angular black spots, powdery coatings, or terminal shoot dieback.",
            "Healthy vegetative flushes and sturdy branch architecture."
        ],
        "recommended_next_steps": [
            "Continue regular monthly orchard inspection.",
            "Monitor for mango hopper and gall midge activity during vegetative flushes.",
            "Apply post-harvest fertilizer dose (FYM + NPK) according to tree age."
        ],
        "preventive_practices": [
            "Conduct center-opening pruning in winter to allow sunlight into the tree core.",
            "Maintain clean orchard basin and mulch with organic biomass.",
            "Follow integrated pest and disease management guidelines."
        ]
    },

    # =============================================================
    # BANANA (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Banana___Black_Sigatoka": {
        "crop": "Banana",
        "crop_display": "Banana",
        "condition": "Black Sigatoka (Black Leaf Streak)",
        "pathogen": "Pseudocercospora fijiensis / Mycosphaerella fijiensis (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Black Sigatoka is the most devastating foliar disease of banana globally. It produces narrow reddish-brown to black streaks parallel to leaf veins that expand into large necrotic blights, causing premature leaf death and small, poorly filled fruit bunches.",
        "symptoms": [
            "Minute rusty brown to reddish-brown streaks (1–5 mm) on the underside of leaves parallel to veins.",
            "Streaks enlarge and coalesce into dark brown or black elliptical spots with sunken gray centers.",
            "Extensive foliar necrosis causing large leaf sections to collapse and dry up rapidly.",
            "Premature ripening and under-filled fruit bunches due to severe loss of functional leaves."
        ],
        "recommended_next_steps": [
            "'De-leafing': cut off and destroy heavily necrotic leaf sections to lower airborne spore load.",
            "Ensure functional field drainage to lower standing water and humidity within the plantation.",
            "Improve plant spacing (1.8 × 1.8 m or wider) to encourage rapid leaf drying.",
            "Consult regional horticultural advisories for registered systemic and protectant fungicide rotation."
        ],
        "preventive_practices": [
            "Plant Sigatoka-resistant or tolerant banana cultivars where commercially viable.",
            "Maintain optimal potassium nutrition to enhance leaf physiological resistance.",
            "Use drip irrigation rather than overhead sprinklers.",
            "Practice sanitary de-leafing regularly at 2-week intervals."
        ]
    },
    "Banana___Panama_Disease": {
        "crop": "Banana",
        "crop_display": "Banana",
        "condition": "Panama Disease (Fusarium Wilt)",
        "pathogen": "Fusarium oxysporum f. sp. cubense (FOC / TR4) (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Panama disease is a catastrophic soil-borne vascular wilt disease of banana. The fungus enters through roots, clogs water-conducting vessels, and causes lower leaf yellowing, petiole buckling, pseudostem splitting, and plant death.",
        "symptoms": [
            "Prominent yellowing of the oldest lower leaves, progressing from margins toward the midrib.",
            "Buckling (skirting) of petioles at the pseudostem junction; dead leaves hang down like an apron.",
            "Longitudinal splitting of the base of the pseudostem.",
            "Cross-section of pseudostem or corm reveals distinctive reddish-brown to dark purple vascular strands."
        ],
        "recommended_next_steps": [
            "CRITICAL: Report suspected Panama wilt to regional agricultural officer or ICAR-NRCB immediately.",
            "Do NOT move suckers, soil, water, or farming tools from affected plantations to uninfected fields.",
            "Isolate affected mats: dig a trench around infected plants and treat with urea + lime.",
            "Eradicate confirmed infected mats by burning or applying bio-containment protocols."
        ],
        "preventive_practices": [
            "Plant only certified, tissue-cultured, disease-free banana plantlets.",
            "Adopt strict biosecurity: clean and disinfect footwear, tractor tires, and tools with quaternary ammonium compounds.",
            "Rotate severely infested fields with paddy (flooding for 3 months suppresses fungal chlamydospores).",
            "Incorporate beneficial biocontrol agents (Trichoderma viride + Pseudomonas fluorescens) in planting pits."
        ]
    },
    "Banana___Cordana_Leaf_Spot": {
        "crop": "Banana",
        "crop_display": "Banana",
        "condition": "Cordana Leaf Spot",
        "pathogen": "Cordana musae (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Cordana leaf spot produces large, oval to diamond-shaped pale brown lesions with prominent concentric rings and bright yellow halos, commonly developing from leaf margins toward the midrib.",
        "symptoms": [
            "Large oval or diamond-shaped pale brown to tan lesions with distinct concentric zonations.",
            "Bright yellow halo surrounding each individual lesion.",
            "Lesions commonly initiate along leaf margins and expand inward along leaf veins.",
            "Grayish fungal sporulation visible on the underside of spots during humid conditions."
        ],
        "recommended_next_steps": [
            "Prune off heavily spotted leaf tips during routine plantation sanitation.",
            "Avoid excessive shade and overcrowding in the banana grove.",
            "Ensure proper drainage to reduce microclimatic humidity.",
            "Consult local extension officer for protective fungicide recommendations if spreading rapidly."
        ],
        "preventive_practices": [
            "Maintain recommended planting density to allow free airflow.",
            "Apply balanced fertilizer with adequate potash.",
            "Clear weeds and maintain clean inter-row spaces.",
            "Follow standard de-leafing practices."
        ]
    },
    "Banana___healthy": {
        "crop": "Banana",
        "crop_display": "Banana",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The banana plant displays broad, vibrant green, healthy leaves with smooth lamina, robust pseudostem, clean petioles, and absence of Sigatoka streaks or vascular yellowing.",
        "symptoms": [
            "Huge, lush green leaves with clean undamaged lamina.",
            "Absence of black streaks, yellow margins, petiole buckling, or pseudostem splitting.",
            "Vigorous cigar leaf emergence and strong bunch emergence."
        ],
        "recommended_next_steps": [
            "Maintain scheduled drip fertigation according to crop stage.",
            "Practice desuckering to leave only one daughter sucker per mat.",
            "Provide bunch propping using bamboo or polyproylene poles."
        ],
        "preventive_practices": [
            "Apply organic manure and biofertilizers at planting.",
            "Maintain clean irrigation channels.",
            "Follow integrated crop management recommendations."
        ]
    },

    # =============================================================
    # PIGEON PEA / ARHAR (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Pigeon_pea___Fusarium_Wilt": {
        "crop": "Pigeon pea",
        "crop_display": "Pigeon Pea (Arhar / Red Gram)",
        "condition": "Fusarium Wilt",
        "pathogen": "Fusarium udum (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Fusarium wilt is the most destructive disease of pigeon pea (arhar). It causes sudden wilting, dark purple vascular band on the stem, and browning of xylem vessels, leading to total plant death.",
        "symptoms": [
            "Sudden drooping and drying of leaves on one or more branches while remaining green.",
            "A distinct dark purple to black band runs vertically up the stem from ground level.",
            "Peeling the bark reveals dark brown to black vascular discoloration in the wood.",
            "Entire plant withers and dies within days, especially around flowering and pod-fill stages."
        ],
        "recommended_next_steps": [
            "Peel bark of lower stem to verify dark purple vertical band and xylem browning.",
            "Uproot and burn wilted plants to eliminate fungal chlamydospores from the field.",
            "Do not allow irrigation water to flow from wilt-affected patches to healthy rows.",
            "Consult local KVK or agricultural university for wilt-resistant seeds."
        ],
        "preventive_practices": [
            "Grow Fusarium wilt-resistant pigeon pea varieties (e.g., Asha / ICPL 87119, Maruthi / ICP 8863, BSMR 736).",
            "Seed treatment with Trichoderma viride @ 10 g/kg seed before sowing.",
            "Practice 3 to 4-year crop rotation with non-host crops (sorghum, maize, or cotton).",
            "Intercrop pigeon pea with sorghum (sorghum root exudates suppress Fusarium udum populations)."
        ]
    },
    "Pigeon_pea___Sterility_Mosaic": {
        "crop": "Pigeon pea",
        "crop_display": "Pigeon Pea (Arhar / Red Gram)",
        "condition": "Sterility Mosaic Disease (SMD)",
        "pathogen": "Pigeonpea Sterility Mosaic Emaravirus (Vectored by Eriophyid mite, Aceria cajani)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Sterility mosaic disease (known as 'green plague' of arhar) is transmitted by microscopic eriophyid mites. Infected plants become bushy, produce small mottled leaves, and completely fail to produce flowers and pods.",
        "symptoms": [
            "Mottling and light green to yellowish mosaic patches on leaves.",
            "Severe reduction in leaf size, excessive vegetative branching, and a stunted bushy appearance.",
            "Sterility: plants completely fail to flower or set pods ('sterility mosaic').",
            "Infected plants stand out conspicuously in the field as dense, bushy, dark green patches."
        ],
        "recommended_next_steps": [
            "Rogue out and destroy infected SMD plants as early as possible (within 45 days of sowing).",
            "Inspect underside of leaves using a 20x hand lens for tiny eriophyid mites.",
            "Spray recommended acaricide (e.g., wettable sulfur @ 3 g/L or propargite) to control mite vectors.",
            "Consult local extension officer if mosaic patches appear across the field."
        ],
        "preventive_practices": [
            "Sow SMD-resistant pigeon pea cultivars (e.g., ICP 8863, ICPL 87119 / Asha, BSMR 853).",
            "Avoid summer pigeon pea cultivation that bridges mite populations between seasons.",
            "Eradicate wild perennial pigeon pea and weed hosts around field bunds.",
            "Maintain optimal plant spacing to allow good air circulation."
        ]
    },
    "Pigeon_pea___Phytophthora_Blight": {
        "crop": "Pigeon pea",
        "crop_display": "Pigeon Pea (Arhar / Red Gram)",
        "condition": "Phytophthora Blight",
        "pathogen": "Phytophthora cajani (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Phytophthora blight is a fast-spreading water-mold disease favored by heavy rains, cloud cover, and waterlogged soil conditions. It causes water-soaked foliar lesions, stem girdling, and rapid shoot death.",
        "symptoms": [
            "Circular to irregular water-soaked lesions on leaves, turning dark brown.",
            "Dark brown to black necrotic cankers girdling the main stem and branches.",
            "Stems break easily at the point of the canker during wind or rain.",
            "Rapid withering and collapse of entire plants within a few days under warm, waterlogged conditions."
        ],
        "recommended_next_steps": [
            "Ensure immediate field surface drainage to remove standing rainwater.",
            "Avoid low-lying, poorly drained fields for pigeon pea cultivation.",
            "Rogue out and burn dead plants showing stem cankers.",
            "Consult agricultural officer for recommended oomycete fungicide sprays (metalaxyl-M or cymoxanil)."
        ],
        "preventive_practices": [
            "Plant pigeon pea on raised beds or broad bed and furrow (BBF) systems to facilitate rapid drainage.",
            "Seed treatment with metalaxyl-M (Apron XL @ 3 g/kg seed) before sowing.",
            "Plant Phytophthora blight-tolerant cultivars (e.g., ICPL 151, ICPL 87).",
            "Rotate with crops like pearl millet or sorghum."
        ]
    },
    "Pigeon_pea___healthy": {
        "crop": "Pigeon pea",
        "crop_display": "Pigeon Pea (Arhar / Red Gram)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The pigeon pea plant displays healthy trifoliate leaves, sturdy stem branching, clean petioles, active nodulation, and normal floral and pod formation.",
        "symptoms": [
            "Vibrant green trifoliate leaves with clean, intact margins.",
            "Absence of purple stem bands, mosaic mottling, sterility, or cankers.",
            "Normal flowering and healthy pod filling."
        ],
        "recommended_next_steps": [
            "Monitor canopy during flowering and pod development for pod borer (Helicoverpa armigera) activity.",
            "Install pheromone traps (5 traps per acre) for pod borer surveillance.",
            "Provide protective irrigation during critical flowering and pod development if dry spell occurs."
        ],
        "preventive_practices": [
            "Inoculate seeds with Rhizobium culture and PSB (phosphorus solubilizing bacteria).",
            "Apply balanced fertilizer with sulfur (gypsum @ 200 kg/ha).",
            "Implement integrated pest management practices."
        ]
    },

    # =============================================================
    # TURMERIC (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Turmeric___Leaf_Blotch": {
        "crop": "Turmeric",
        "crop_display": "Turmeric (Haldi)",
        "condition": "Leaf Blotch",
        "pathogen": "Taphrina maculans (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate to High",
        "description": "Leaf blotch is a common fungal foliar disease in turmeric grown in humid regions. It produces small, yellow-brown to dirty-yellow spots on upper leaf surfaces that merge into large irregular necrotic blotches.",
        "symptoms": [
            "Small, oval or rectangular, yellowish spots on both leaf surfaces.",
            "Lesions turn reddish-brown to dirty dark brown with age, coalescing into extensive blotches.",
            "Upper leaves dry up and present a scorched appearance, drastically reducing rhizome bulking.",
            "In severe attacks, entire leaf lamina withers prematurely."
        ],
        "recommended_next_steps": [
            "Inspect fields during monsoon months when relative humidity exceeds 85%.",
            "Collect and destroy heavily spotted leaves to check secondary spore spread.",
            "Apply foliar sprays of mancozeb (0.25%) or copper oxychloride (0.25%) at initial symptom onset.",
            "Ensure proper drainage to prevent stagnant water around turmeric beds."
        ],
        "preventive_practices": [
            "Select disease-free seed rhizomes from certified seed nurseries.",
            "Treat seed rhizomes before planting with mancozeb (0.3%) solution for 30 minutes.",
            "Adopt wider spacing to improve aeration within the crop canopy.",
            "Apply balanced potassium and neem cake to boost foliar resistance."
        ]
    },
    "Turmeric___Rhizome_Rot": {
        "crop": "Turmeric",
        "crop_display": "Turmeric (Haldi)",
        "condition": "Rhizome Rot (Soft Rot)",
        "pathogen": "Pythium aphanidermatum / Pythium graminicola (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Rhizome rot is the most destructive disease of turmeric. The pathogen attacks the pseudostem collar and underground rhizomes, causing wet rotting, unpleasant foul odor, and rapid wilting of entire clumps.",
        "symptoms": [
            "Progressive yellowing of lower leaves moving upward along pseudostem margins.",
            "Water-soaked brown discoloration at the collar region near the soil line.",
            "Pseudostem pulls out easily from the underground rhizome when gently tugged.",
            "Underground rhizomes soften, decay, and emit an offensive foul smell."
        ],
        "recommended_next_steps": [
            "Immediately drench infected clumps and surrounding buffer rows with metalaxyl-mancozeb (0.2%) or Bordeaux mixture (1%).",
            "Dig out and safely burn rotten clumps along with surrounding infested soil.",
            "Create immediate drainage furrows to evacuate standing rainwater.",
            "Consult local spice research station or KVK for bio-control drenching protocols."
        ],
        "preventive_practices": [
            "Plant turmeric strictly on raised beds (15–20 cm high) with deep inter-bed drainage channels.",
            "Treat seed rhizomes with Trichoderma harzianum bio-agent (10 g/kg seed) or metalaxyl (2 g/L).",
            "Avoid planting turmeric in heavy, poorly drained clay soils with water stagnation history.",
            "Incorporate neem cake (2 tonnes/ha) into soil during final land preparation."
        ]
    },
    "Turmeric___Dry_Leaf": {
        "crop": "Turmeric",
        "crop_display": "Turmeric (Haldi)",
        "condition": "Dry Leaf / Leaf Spot",
        "pathogen": "Colletotrichum curcumae (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Colletotrichum leaf spot causes brown spots with grey centers on turmeric leaves, leading to leaf scorching and premature drying during the post-monsoon rhizome development phase.",
        "symptoms": [
            "Elliptical to circular brown spots with distinct grey or ash-colored centers.",
            "Spots surrounded by a prominent bright yellow chlorotic halo.",
            "Central dead tissue becomes brittle and can drop out, leaving shot-holes.",
            "Extensive drying and marginal curling of affected leaves."
        ],
        "recommended_next_steps": [
            "Remove and compost or bury dried, severely spotted lower leaves.",
            "Spray carbendazim (0.1%) or propiconazole (0.1%) when first spots appear on middle leaves.",
            "Maintain soil moisture without creating waterlogged conditions."
        ],
        "preventive_practices": [
            "Follow crop rotation with non-host crops like maize, pulses, or finger millet.",
            "Solarize nursery beds before planting to eliminate resting fungal sclerotia.",
            "Apply foliar micronutrient sprays (zinc and boron) to maintain leaf cuticle toughness."
        ]
    },
    "Turmeric___Healthy": {
        "crop": "Turmeric",
        "crop_display": "Turmeric (Haldi)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The turmeric crop displays healthy, broad, upright lanceolate leaves with deep lush green coloration, sturdy pseudostems, and vigorous tillering.",
        "symptoms": [
            "Broad, elongated green leaves with clean margins and no spotting or yellowing.",
            "Firm, upright pseudostems securely anchored in the soil.",
            "Absence of water-soaking at the collar region or scorching on leaf tips."
        ],
        "recommended_next_steps": [
            "Maintain regular weekly field inspection during rainy and post-monsoon phases.",
            "Ensure weed-free raised beds and periodic earthing-up around pseudostems.",
            "Apply top-dressed nitrogen and potassium as per local fertilizer schedule."
        ],
        "preventive_practices": [
            "Maintain proper bed drainage throughout the monsoon season.",
            "Apply organic mulch (green leaves or paddy straw @ 10–12 tonnes/ha) for moisture conservation.",
            "Rotate crops annually to maintain soil microbial health."
        ]
    },

    # =============================================================
    # PALM / OIL PALM / ARECANUT (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Palm___Fungal_Disease": {
        "crop": "Palm",
        "crop_display": "Palm (Oil Palm / Arecanut)",
        "condition": "Fungal Basal Stem Rot / Bud Rot",
        "pathogen": "Ganoderma boninense / Phytophthora palmivora",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Fungal pathogens such as Ganoderma and Phytophthora attack oil palm and areca palm stems and growing spears. Basal stem rot destroys vascular tissues, causing spear rot, skirt collapse of lower fronds, and tree death.",
        "symptoms": [
            "Multiple unopened spear leaves remaining in the central crown.",
            "Lower fronds wilting, snapping, and hanging down like a skirt around the trunk.",
            "Bracket fungi (conks) emerging on the lower trunk base near ground level.",
            "Internal brown dry rot and decay of bole and vascular trunk tissue."
        ],
        "recommended_next_steps": [
            "Excavate trenching (1 m deep, 0.5 m wide) around infected palms to isolate root networks.",
            "Trunk-inject hexaconazole or drench collar with thiram/copper fungicides in early stages.",
            "Safely fell and incinerate heavily infected, non-viable palms to stop spore release.",
            "Consult specialized palm plantation extension officer for bio-agent treatment."
        ],
        "preventive_practices": [
            "Incorporate Trichoderma harzianum or T. asperellum into soil around planting holes.",
            "Avoid damaging palm trunks and root flares during weeding and mechanized harvesting.",
            "Maintain adequate spacing and remove competing vegetation."
        ]
    },
    "Palm___Magnesium_Deficiency": {
        "crop": "Palm",
        "crop_display": "Palm (Oil Palm / Arecanut)",
        "condition": "Magnesium Deficiency (Orange Frond)",
        "pathogen": "Physiological Abiotic Disorder (Nutrient Deficiency)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Magnesium deficiency is a widespread nutritional disorder in acid sandy soils or peat soils. It causes vivid orange-yellow chlorosis of leaflets on older, lower fronds exposed to strong sunlight.",
        "symptoms": [
            "Bright orange to golden-yellow discoloration of leaflets on older lower fronds.",
            "Shaded leaflets remain green while sun-exposed leaflets exhibit intense discoloration.",
            "Necrosis and desiccated brown tips developing along leaf edges as deficiency advances.",
            "Stunted bunch development and reduced oil content in harvest."
        ],
        "recommended_next_steps": [
            "Conduct foliar tissue analysis (Frond 17 sampling) to confirm Mg concentration.",
            "Apply kieserite (magnesium sulfate @ 1.5–2.5 kg/palm) or dolomitic limestone based on soil pH.",
            "Avoid excessive potassium fertilizer application, which inhibits magnesium uptake."
        ],
        "preventive_practices": [
            "Apply balanced K:Mg ratio fertilizers as recommended by palm agronomy institutes.",
            "Broadcast dolomite or kieserite in the weeded palm circle.",
            "Maintain soil organic matter through frond stacking along inter-row avenues."
        ]
    },
    "Palm___Scale_Insect": {
        "crop": "Palm",
        "crop_display": "Palm (Oil Palm / Arecanut)",
        "condition": "Scale Insect Infestation",
        "pathogen": "Ischnaspis filiformis / Aonidiella orientalis (Insect Pest)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Armored scale insects colonize the underside of palm leaflets and frond petiole bases, sucking plant sap and secreting honeydew that leads to sooty mould and chlorotic spotting.",
        "symptoms": [
            "Small, waxy, brownish or white scale-like encrustations on the undersides of leaflets.",
            "Chlorotic yellow pinhead spots where scale insects have punctured leaf cells.",
            "Premature drying, browning, and dying back of heavily infested fronds.",
            "Secondary black sooty mould coating frond surfaces."
        ],
        "recommended_next_steps": [
            "Prune and safely dispose of heavily encrusted lower fronds.",
            "Release natural predators such as predatory ladybird beetles (Chilocorus spp.).",
            "Spray horticultural neem oil (2%) or systemic insecticide (imidacloprid or acetamiprid) with a wetting agent."
        ],
        "preventive_practices": [
            "Maintain sanitary canopy aeration by regular frond pruning.",
            "Conserve beneficial parasitoid wasps and ladybird predators.",
            "Avoid indiscriminate use of broad-spectrum pyrethroids that destroy natural enemies."
        ]
    },
    "Palm___Dryness": {
        "crop": "Palm",
        "crop_display": "Palm (Oil Palm / Arecanut)",
        "condition": "Drought Stress / Desiccation",
        "pathogen": "Abiotic Environmental Stress (Water Deficit)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate to High",
        "description": "Prolonged water deficit and high vapor pressure deficit (VPD) cause palm stomatal closure, spear leaf bunching, and premature desiccation of lower fronds.",
        "symptoms": [
            "Accumulation of multiple unopened spear leaves in the crown.",
            "Premature browning, drying, and snapping of lower fronds at the petiole base.",
            "Inflorescence abortion and reduction in fresh fruit bunch (FFB) weight.",
            "Reduced leaf emission rate and stunted trunk expansion."
        ],
        "recommended_next_steps": [
            "Provide supplemental drip or furrow irrigation (at least 150–200 L/palm/day during drought).",
            "Stack pruned fronds heavily in the palm basin to conserve soil moisture.",
            "Avoid deep root pruning or cultivation near palm bases during hot dry weather."
        ],
        "preventive_practices": [
            "Establish leguminous cover crops (Mucuna bracteata) in young palm plantations.",
            "Construct water harvesting contour bunds and silt pits on undulating terrain.",
            "Apply empty fruit bunches (EFB) mulch around palm basins."
        ]
    },

    # =============================================================
    # SUGARCANE (Expanded Knowledge Base - 5 Profiles)
    # =============================================================
    "Sugarcane___Red_Rot": {
        "crop": "Sugarcane",
        "crop_display": "Sugarcane (Ganna)",
        "condition": "Red Rot",
        "pathogen": "Colletotrichum falcatum (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Known as the 'cancer of sugarcane', red rot is the most destructive disease affecting sugarcane across the globe. It destroys stalk interior tissues, causing severe sucrose conversion to glucose and total mill rejection.",
        "symptoms": [
            "Third and fourth leaves from top show yellowing, withering, and drying along margins.",
            "Splitting open the infected stalk reveals blood-red discoloration with diagnostic white horizontal cross-bands.",
            "Alcoholic or acidic fermenting odor emanating from split canes.",
            "Stalks become hollow, shriveled, and produce tiny black fruiting bodies on rind nodes."
        ],
        "recommended_next_steps": [
            "Immediately eradicate and safely burn all wilted clumps; do not use them for seed or fodder.",
            "Stop irrigation through infected rows to prevent water-borne spore dispersal.",
            "Harvest surviving canes early to minimize sucrose inversion losses.",
            "Consult sugarcane breeding institute or factory extension officer for resistant variety setts."
        ],
        "preventive_practices": [
            "Plant certified red rot resistant cultivars (e.g., Co 0238 replacements, Co 86032, Co 0118).",
            "Treat seed setts with carbendazim (0.1%) or moist hot air treatment (MHAT at 54°C for 2.5 hours).",
            "Practice minimum 2–3 year crop rotation with paddy or green manure crops in infected fields.",
            "Ensure field sanitation and destroy all post-harvest trash and stubble."
        ]
    },
    "Sugarcane___Smut": {
        "crop": "Sugarcane",
        "crop_display": "Sugarcane (Ganna)",
        "condition": "Culmicolous Smut",
        "pathogen": "Sporisorium scitamineum (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Sugarcane smut is characterized by the production of a long, black, curved, whip-like structure from the terminal shoot of infected stalks. Affected clumps become grassy and produce thin, useless canes.",
        "symptoms": [
            "Production of an unmistakable pencil-thick, whip-like structure up to 1 meter long from the stalk apex.",
            "Whip is initially covered by a thin silvery membrane that ruptures to release billions of black powdery spores.",
            "Stunted clumps with excessive thin tillers ('grassy shoot-like' appearance).",
            "Slender, erect leaves with narrow lamina."
        ],
        "recommended_next_steps": [
            "Carefully cover the smut whip with a damp cloth or plastic bag, cut it at the base, and burn it to prevent spore scattering.",
            "Rogue out and destroy the entire infected clump including underground stool roots.",
            "Never take ratoon crops from smut-infested fields."
        ],
        "preventive_practices": [
            "Use disease-free seed setts from certified nursery plots.",
            "Dip seed setts in triadimefon (0.1%) or propiconazole (0.1%) before planting.",
            "Grow smut-tolerant sugarcane varieties recommended for your agro-climatic zone.",
            "Avoid moisture stress during early tillering stage."
        ]
    },
    "Sugarcane___Rust": {
        "crop": "Sugarcane",
        "crop_display": "Sugarcane (Ganna)",
        "condition": "Brown Rust",
        "pathogen": "Puccinia melanocephala (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate to High",
        "description": "Sugarcane rust attacks leaf lamina during cool, humid weather, creating elongated brown pustules that rupture the epidermis and drastically reduce green photosynthesizing leaf area.",
        "symptoms": [
            "Small, elongated yellowish specks on both leaf surfaces, expanding into reddish-brown lesions.",
            "Lesions form raised pustules (uredinia) that rupture, exposing rusty brown powdery spores.",
            "Severely affected leaves dry up prematurely from tips backward.",
            "Canopy takes on a burnt, rusty brown hue across the field."
        ],
        "recommended_next_steps": [
            "Apply foliar sprays of mancozeb (0.3%) or propiconazole (0.1%) at early pustule onset.",
            "Ensure good field ventilation by detripping (removing dry lower senescent leaves).",
            "Avoid excessive late nitrogen fertilization which promotes lush, susceptible foliage."
        ],
        "preventive_practices": [
            "Plant rust-resistant sugarcane cultivars.",
            "Maintain optimal row spacing (120–150 cm) for adequate air circulation.",
            "Balance NPK fertilization with adequate potassium and silica."
        ]
    },
    "Sugarcane___Yellow_Leaf_Disease": {
        "crop": "Sugarcane",
        "crop_display": "Sugarcane (Ganna)",
        "condition": "Yellow Leaf Disease (YLD)",
        "pathogen": "Sugarcane yellow leaf virus (SCYLV) / Phytoplasma",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate to High",
        "description": "Yellow leaf disease is an emerging viral disorder transmitted by the sugarcane aphid (Melanaphis sacchari). It causes intense midrib yellowing on mature leaves and decreases cane weight and sugar yield by up to 30%.",
        "symptoms": [
            "Intense yellowing of the central leaf midrib on leaves 3 to 6 from the spindle.",
            "Yellowing gradually spreads into the adjacent leaf blade lamina.",
            "Under side of the midrib develops a pinkish or purplish reddish hue in winter months.",
            "Shortening of terminal internodes, bunching of crown leaves, and premature drying."
        ],
        "recommended_next_steps": [
            "Scout for sugarcane aphid colonies under leaf surfaces and spray imidacloprid (0.05%) or thiamethoxam.",
            "Rogue out severely stunted clumps during early crop growth.",
            "Ensure adequate irrigation during peak vegetative growth."
        ],
        "preventive_practices": [
            "Use virus-indexed tissue-cultured plantlets or heat-treated setts.",
            "Control aphid vectors in nursery fields.",
            "Avoid taking successive ratoon crops from YLD-affected fields."
        ]
    },
    "Sugarcane___Healthy": {
        "crop": "Sugarcane",
        "crop_display": "Sugarcane (Ganna)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The sugarcane clump displays vigorous, thick stalks with healthy green leaf canopy, clean leaf midribs, uniform internode spacing, and sturdy tillering.",
        "symptoms": [
            "Broad, rich green leaves with intact, clean midribs and no chlorosis or rust pustules.",
            "Firm, solid stalks with healthy rind coloration and intact wax coating.",
            "Uniform tiller population with vigorous vegetative growth."
        ],
        "recommended_next_steps": [
            "Perform timely earthing-up at 90 and 120 days to support stalks against lodging.",
            "Trash mulching between rows to conserve soil moisture and suppress weeds.",
            "Apply scheduled fertilizer splits according to crop age."
        ],
        "preventive_practices": [
            "Follow drip irrigation and fertigation for optimal nutrient utilization.",
            "Adopt wide-row planting (4–5 feet) for maximum sunlight interception.",
            "Regular scouting for early shoot borer and internode borer."
        ]
    },

    # =============================================================
    # COFFEE (Expanded Knowledge Base - 3 Profiles)
    # =============================================================
    "Coffee___Leaf_Rust": {
        "crop": "Coffee",
        "crop_display": "Coffee (Kafi)",
        "condition": "Coffee Leaf Rust (Roya)",
        "pathogen": "Hemileia vastatrix (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Coffee leaf rust is the most historically devastating disease of Arabica coffee worldwide. It produces powdery orange-yellow spore patches on the undersides of leaves, causing massive premature defoliation and branch dieback.",
        "symptoms": [
            "Yellowish oily spots on the upper leaf surface expanding over time.",
            "Corresponding lower surface produces bright powdery orange-yellow fungal spore clusters (urediniospores).",
            "Infected spots turn brown and necrotic from the center outward.",
            "Massive leaf drop leading to bare twigs, berry shriveling, and tree exhaustion."
        ],
        "recommended_next_steps": [
            "Apply protective Bordeaux mixture (0.5%) or copper oxychloride (0.3%) prior to southwest monsoon showers.",
            "Apply systemic fungicide (hexaconazole 0.1% or cyproconazole) if rust incidence exceeds 5–10% of leaves.",
            "Regulate shade tree canopy to provide 40–50% filtered sunlight and improve air movement."
        ],
        "preventive_practices": [
            "Plant rust-resistant Arabica cultivars (e.g., Catimor, Sln 795, Chandragiri, Ruiru 11).",
            "Maintain optimal shade management with two-tier shade trees (Erythrina, Grevillea).",
            "Apply balanced fertilizer with adequate potassium to strengthen leaf cuticle."
        ]
    },
    "Coffee___Cercospora_Leaf_Spot": {
        "crop": "Coffee",
        "crop_display": "Coffee (Kafi)",
        "condition": "Brown Eye Spot (Berry Blotch)",
        "pathogen": "Cercospora coffeicola (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Brown eye spot attacks coffee foliage and developing berries, particularly in unshaded nurseries or stressed plantations with poor nutrition.",
        "symptoms": [
            "Circular brown lesions on leaves with characteristic ash-grey centers and reddish-brown margins ('bird's eye' pattern).",
            "Prominent yellow halo surrounding each spot on upper leaf surfaces.",
            "Sunken, dark brown lesions on developing coffee cherries, causing premature drop.",
            "Seedlings in nurseries show heavy leaf drop and stunted growth."
        ],
        "recommended_next_steps": [
            "Provide 50% overhead shade in nurseries and young field clearings.",
            "Spray copper oxychloride (0.3%) or carbendazim (0.1%) upon symptom appearance.",
            "Apply foliar urea (1%) to boost nitrogen nutrition in seedlings."
        ],
        "preventive_practices": [
            "Avoid growing coffee seedlings in full, unshaded sunlight.",
            "Maintain soil organic matter and balanced fertilization.",
            "Ensure regular irrigation without waterlogging root zones."
        ]
    },
    "Coffee___Healthy": {
        "crop": "Coffee",
        "crop_display": "Coffee (Kafi)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The coffee bush displays deep glossy green, elliptical leaves with wavy margins, vigorous primary and secondary branching, and healthy berry cluster development.",
        "symptoms": [
            "Lustrous dark green leaves with clean, undamaged surfaces.",
            "Absence of orange powdery rust spots or necrotic eye lesions.",
            "Sturdy lateral branches with healthy node spacing and abundant blossom/berry sets."
        ],
        "recommended_next_steps": [
            "Monitor shade tree density ahead of monsoon seasons.",
            "Conduct seasonal soil testing and apply balanced NPK-Mg fertilizer splits.",
            "Prune suckers and dead tertiary twigs post-harvest."
        ],
        "preventive_practices": [
            "Maintain integrated pest management for coffee berry borer (Hypothenemus hampei).",
            "Mulch tree basins with dry leaves to conserve soil moisture.",
            "Regular weed slashing along terrace rows."
        ]
    },

    # =============================================================
    # TEA (Expanded Knowledge Base - 3 Profiles)
    # =============================================================
    "Tea___Blister_Blight": {
        "crop": "Tea",
        "crop_display": "Tea (Chai)",
        "condition": "Blister Blight",
        "pathogen": "Exobasidium vexans (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Blister blight is the most damaging foliar disease of tea bushes in high-altitude tea-growing tracts. It directly attacks tender harvestable shoots (two leaves and a bud), causing translucent blisters, blackened shoots, and severe crop loss.",
        "symptoms": [
            "Small, pale yellowish, translucent spots on young tender leaves.",
            "Spot depresses on the upper surface, creating a corresponding convex, chalky-white blister on the lower surface.",
            "Blister ruptures, releasing white basidiospores, and turns brown and necrotic.",
            "Tender succulent stems develop cankers, snap off, and die back."
        ],
        "recommended_next_steps": [
            "Apply protective weekly sprays of copper oxychloride (0.2%) mixed with propiconazole or hexaconazole (0.05%) during monsoon months.",
            "Practice short plucking rounds (every 5–7 days) to harvest tender shoots before blisters mature.",
            "Thin out dense shade tree branches to allow early morning sunlight penetration."
        ],
        "preventive_practices": [
            "Select blister-resistant tea clones for replanting in disease-prone high elevations.",
            "Maintain optimal shade density (filtered light, 40–50%).",
            "Prune tea bushes during dry weather to facilitate rapid recovery."
        ]
    },
    "Tea___Red_Rust": {
        "crop": "Tea",
        "crop_display": "Tea (Chai)",
        "condition": "Red Rust (Algal Leaf Spot)",
        "pathogen": "Cephaleuros parasiticus (Parasitic Green Alga)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Red rust is unique as it is caused by a parasitic green alga rather than a fungus. It attacks tea leaves and woody stems of unthrifty, weakened bushes, producing velvety orange-red patches.",
        "symptoms": [
            "Circular, raised, velvety reddish-orange patches on older mature leaves and branches.",
            "Algal fruiting filaments give the spots their characteristic bristly red appearance.",
            "Bark of affected branches cracks, peels, and shows internal dieback.",
            "Severe debilitation of tea bushes with poor flush production."
        ],
        "recommended_next_steps": [
            "Prune out severely affected, dead, and hidebound twigs during routine bush sanitation.",
            "Apply copper oxychloride (0.25%) sprays during the algal spore release season (April–June).",
            "Improve bush vitality by correcting soil acidity and applying balanced potash (K2O)."
        ],
        "preventive_practices": [
            "Improve drainage in low-lying, waterlogged tea sections.",
            "Correct soil nutrient deficiencies, especially potassium and zinc.",
            "Avoid harsh pruning that weakens bush framework."
        ]
    },
    "Tea___Healthy": {
        "crop": "Tea",
        "crop_display": "Tea (Chai)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The tea bush presents a dense, uniform, vibrant green plucking table with succulent two-leaves-and-a-bud flushes, clean mature maintenance foliage, and sturdy frame branching.",
        "symptoms": [
            "Lush light-green tender terminal shoots with velvety unopened buds.",
            "Clean dark green maintenance leaves without blisters, spots, or algal patches.",
            "Healthy bush canopy with continuous vegetative flush."
        ],
        "recommended_next_steps": [
            "Maintain disciplined plucking intervals (7–10 days) to sustain bush productivity.",
            "Apply balanced N:K fertilizer splits based on crop harvest targets.",
            "Scout for tea mosquito bug (Helopeltis theivora) and red spider mite."
        ],
        "preventive_practices": [
            "Maintain soil organic mulch with tea prunings.",
            "Regulate shade tree lopping twice a year.",
            "Maintain soil pH between 4.5 and 5.5."
        ]
    },

    # =============================================================
    # ONION (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Onion___Purple_Blotch": {
        "crop": "Onion",
        "crop_display": "Onion (Pyaz)",
        "condition": "Purple Blotch",
        "pathogen": "Alternaria porri (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Purple blotch is one of the most widespread fungal diseases of onion. It causes sunken, elliptical lesions with dark purple centers on leaves and seed stalks, leading to leaf lodging and up to 50% yield reduction.",
        "symptoms": [
            "Small water-soaked lesions developing on leaves, rapidly turning brown to deep purple with reddish borders.",
            "Concentric dark rings visible within the purple blotches.",
            "Lesions girdle the cylindrical tubular leaf, causing the upper portion to bend, collapse, and dry.",
            "Seed stalks girdle and break, causing total loss of the onion seed crop."
        ],
        "recommended_next_steps": [
            "Apply foliar sprays of mancozeb (0.25%) or propiconazole (0.1%) with an agricultural sticker/spreader (due to waxy onion foliage).",
            "Avoid overhead sprinkler irrigation that keeps onion leaves wet for prolonged hours.",
            "Harvest bulbs only when neck tissues are completely dry."
        ],
        "preventive_practices": [
            "Treat seed with thiram or captan (3 g/kg seed) before sowing.",
            "Dip onion seedlings in carbendazim solution (0.1%) before transplanting.",
            "Practice 3-year crop rotation with non-allium crops.",
            "Ensure wide row spacing and raised bed planting."
        ]
    },
    "Onion___Downy_Mildew": {
        "crop": "Onion",
        "crop_display": "Onion (Pyaz)",
        "condition": "Downy Mildew",
        "pathogen": "Peronospora destructor (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Downy mildew thrives during cool, damp, foggy mornings, producing violet-grey fuzzy sporulation on onion foliage that leads to leaf collapse and dwarfed, soft, rot-prone bulbs.",
        "symptoms": [
            "Pale green to yellowish oval patches on older tubular leaves.",
            "Lesions become covered with a diagnostic fine, purplish-grey, velvet-like downy growth.",
            "Infected leaf tips wither, turn white, and collapse downwards.",
            "Bulbs remain small, soft, and produce spongy necks that rot rapidly during storage."
        ],
        "recommended_next_steps": [
            "Spray metalaxyl-mancozeb (0.2%) or dimethomorph (0.1%) with an adherent spreader at first symptom notice.",
            "Destroy diseased crop residues and cull piles near onion fields.",
            "Ensure field drains are clear to prevent humidity buildup."
        ],
        "preventive_practices": [
            "Plant onion sets and seedlings on well-drained raised beds oriented with prevailing wind.",
            "Do not plant onions in shaded or low-lying water-retaining plots.",
            "Rotate crops with cereals, pulses, or brassicas."
        ]
    },
    "Onion___Stemphylium_Leaf_Blight": {
        "crop": "Onion",
        "crop_display": "Onion (Pyaz)",
        "condition": "Stemphylium Leaf Blight",
        "pathogen": "Stemphylium vesicarium (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate to High",
        "description": "Stemphylium leaf blight attacks onion leaves and seed scapes, often invading through thrips feeding punctures or sunscald injury, causing severe blighting from leaf tips downwards.",
        "symptoms": [
            "Small yellow to pale orange flecks developing into elongated spindle-shaped lesions.",
            "Lesions expand, turn dark brown to black from dense conidial masses.",
            "Severe blighting begins from the leaf tip and progresses downwards, drying the entire foliage.",
            "Seed stalks break prematurely before seed umbels mature."
        ],
        "recommended_next_steps": [
            "Control onion thrips (Thrips tabaci) promptly using spinosad or fipronil to prevent entry wounds.",
            "Spray azoxystrobin (0.1%) or tebuconazole (0.1%) with a quality non-ionic sticker.",
            "Maintain optimal soil moisture to avoid leaf tip burn."
        ],
        "preventive_practices": [
            "Use certified clean seed and dip seedlings in bio-agent Trichoderma before planting.",
            "Adopt drip irrigation rather than overhead sprinklers.",
            "Follow integrated pest and disease management."
        ]
    },
    "Onion___Healthy": {
        "crop": "Onion",
        "crop_display": "Onion (Pyaz)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The onion plant displays erect, tubular, waxy blue-green leaves with clean tips, sturdy necks, and healthy bulb swelling underground.",
        "symptoms": [
            "Firm, erect tubular leaves with characteristic waxy bloom and vibrant blue-green color.",
            "Absence of purple lesions, fuzzy downy mildew, or tip dieback.",
            "Healthy bulb formation with tight neck tissue."
        ],
        "recommended_next_steps": [
            "Stop irrigation 10–15 days prior to harvest to promote proper bulb curing.",
            "Monitor weekly for thrips under the leaf axils.",
            "Weed carefully to avoid mechanical injury to shallow bulb roots."
        ],
        "preventive_practices": [
            "Follow balanced fertilization (high potassium and sulfur for pungency and storage quality).",
            "Harvest at 50% top neck fall for best storage longevity.",
            "Cur bulbs in well-ventilated dry sheds."
        ]
    },

    # =============================================================
    # COCONUT (Expanded Knowledge Base - 3 Profiles)
    # =============================================================
    "Coconut___Bud_Rot": {
        "crop": "Coconut",
        "crop_display": "Coconut (Nariyal)",
        "condition": "Bud Rot",
        "pathogen": "Phytophthora palmivora (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Bud rot is a lethal disease of coconut palms, especially during the heavy southwest monsoon. The pathogen attacks the central crown and heart leaf bud, resulting in soft rot of the growing spear and rapid palm mortality.",
        "symptoms": [
            "Yellowing, wilting, and collapse of the innermost central spear leaf.",
            "Spear leaf base turns soft, rots, and pulls out effortlessly with a foul putrid stench.",
            "Outer fronds turn yellow and droop progressively, leaving an empty crown top ('cabbage rot').",
            "Complete death of the palm if apical bud tissues decay."
        ],
        "recommended_next_steps": [
            "In early stages: climb the palm, cut away all rotten tissues, and clean the central crown.",
            "Apply Bordeaux paste or copper oxychloride paste to the cleaned crown and protect with a plastic cap during rain.",
            "Drench surrounding crowns prophylactically with Bordeaux mixture (1%) or metalaxyl (0.2%).",
            "Cut down and incinerate dead palms to prevent beetle-borne spore transfer."
        ],
        "preventive_practices": [
            "Place fungicide sachets (mancozeb / copper) in leaf axils before monsoon onset.",
            "Control rhinoceros beetle (Oryctes rhinoceros) which creates entry wounds in crown tissues.",
            "Maintain clean canopy hygiene in coastal and high-rainfall belts."
        ]
    },
    "Coconut___Root_Wilt": {
        "crop": "Coconut",
        "crop_display": "Coconut (Nariyal)",
        "condition": "Root Wilt Disease",
        "pathogen": "Phytoplasma (Transmitted by Lace Bug and Plant Hopper)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Coconut root wilt is a non-lethal but severely debilitating phytoplasmal disease common in south India. It causes characteristic flaccidity and ribbing of leaflets, general yellowing, and drastic yield drop.",
        "symptoms": [
            "Diagnostic ribbing and flaccidity of leaflets; leaflets bend inward like a canoe.",
            "General chlorotic yellowing and marginal necrosis of fronds.",
            "Premature opening of spathes, female flower shedding, and tiny deformed nuts with thin kernel.",
            "Extensive rotting of feeder root tips underground."
        ],
        "recommended_next_steps": [
            "Apply high doses of magnesium sulfate (500 g/palm/year) to counteract chlorosis.",
            "Spray neem oil garlic emulsion (2%) to control vector lace bugs (Stephanitis typica).",
            "Apply balanced fertilizer with green manure (Pueraria or cowpea) in palm basins.",
            "Rogue out severely diseased, uneconomic palms yielding fewer than 10 nuts/year."
        ],
        "preventive_practices": [
            "Plant root-wilt tolerant coconut hybrids (e.g., Kalparaksha, Kalpasree, Chandra Kalpa).",
            "Maintain intensive intercropping and organic recycling in coconut gardens.",
            "Provide regular summer irrigation."
        ]
    },
    "Coconut___Healthy": {
        "crop": "Coconut",
        "crop_display": "Coconut (Nariyal)",
        "condition": "Healthy Palm",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The coconut palm displays a magnificent hemispherical crown of 30–35 vibrant green pinnate fronds, an erect central spear, sturdy trunk, and robust nut clusters at each leaf axil.",
        "symptoms": [
            "Radiant dark green fronds radiating evenly from a full, dense crown.",
            "Firm, upright growing central spear leaf with no browning.",
            "Consistent bunch setting with well-filled nuts at regular developmental stages."
        ],
        "recommended_next_steps": [
            "Apply scheduled organic manure (compost/vermicompost @ 50 kg) and chemical fertilizers per palm basin.",
            "Apply magnesium sulfate (500 g) and common salt (1–2 kg) for coastal/inland health.",
            "Provide basin irrigation (200–250 L/palm every 4–5 days during dry summer)."
        ],
        "preventive_practices": [
            "Install pheromone traps for red palm weevil and rhinoceros beetle surveillance.",
            "Maintain mulch around root zones within a 2-meter radius of the bole.",
            "Periodically clear dry spathes and fronds."
        ]
    },

    # =============================================================
    # MUSTARD / RAPESEED (Expanded Knowledge Base - 3 Profiles)
    # =============================================================
    "Mustard___White_Rust": {
        "crop": "Mustard",
        "crop_display": "Mustard (Sarson)",
        "condition": "White Rust (Staghead)",
        "pathogen": "Albugo candida (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "White rust is a major disease of mustard and crucifers. It produces chalky white blisters on leaf undersides and causes systemic floral malformations known as 'staghead', resulting in severe seed yield loss.",
        "symptoms": [
            "Raised, shiny white or creamy porcelain-like pustules (blisters) on leaf undersides.",
            "Corresponding upper leaf surface displays yellow chlorotic patches.",
            "Systemic floral infection transforms inflorescences into swollen, twisted, sterile 'staghead' structures.",
            "Siliquae (pods) fail to develop or become severely deformed with shriveled seeds."
        ],
        "recommended_next_steps": [
            "Spray metalaxyl-mancozeb (0.2%) or mancozeb (0.25%) at initial pustule appearance (45–50 days after sowing).",
            "Collect and destroy malformed 'stagheads' to prevent resting oospore contamination in soil.",
            "Avoid dense plant stands that retain morning dew."
        ],
        "preventive_practices": [
            "Plant white-rust resistant or tolerant mustard cultivars (e.g., NRCDR-2, RH-0749, Pusa Mustard 25).",
            "Treat seed with metalaxyl (6 g/kg seed) before sowing.",
            "Practice early sowing (first fortnight of October in north India) to escape peak disease pressure.",
            "Rotate crops with non-cruciferous hosts."
        ]
    },
    "Mustard___Alternaria_Blight": {
        "crop": "Mustard",
        "crop_display": "Mustard (Sarson)",
        "condition": "Alternaria Blight (Black Spot)",
        "pathogen": "Alternaria brassicae / Alternaria brassicicola (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Alternaria blight attacks leaves, stems, and seed pods of mustard during cool humid weather. It causes concentric dark target-like spots and pod shatter, reducing seed oil content and yield by 30–60%.",
        "symptoms": [
            "Circular brown necrotic spots with distinct concentric rings ('target board' pattern) on leaves.",
            "Lesions coalesce, causing leaf yellowing and rapid premature defoliation.",
            "Elongated black lesions on stems and developing siliquae (pods).",
            "Infected pods produce shriveled, discolored seeds and shatter prematurely."
        ],
        "recommended_next_steps": [
            "Apply prophylactic spray of mancozeb (0.25%) or iprodione (0.2%) at 45 and 60 days after sowing.",
            "Ensure timely harvesting to avoid losses from pod shattering.",
            "Avoid over-irrigation during flowering and pod development stages."
        ],
        "preventive_practices": [
            "Use certified, healthy, disease-free seed.",
            "Perform hot water seed treatment (50°C for 20 minutes) or seed dressing with thiram (3 g/kg).",
            "Destroy crop stubble immediately after threshing.",
            "Maintain balanced fertilization with sulfur."
        ]
    },
    "Mustard___Healthy": {
        "crop": "Mustard",
        "crop_display": "Mustard (Sarson)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The mustard crop displays vigorous vegetative growth with broad dark green lower leaves, sturdy erect branching stems, vibrant bright yellow blossoms, and healthy pod setting.",
        "symptoms": [
            "Broad, lush green leaves free of white blisters or concentric brown target spots.",
            "Erect, sturdy stems with abundant floral racemes.",
            "Normal pod (siliqua) development with plump seeds."
        ],
        "recommended_next_steps": [
            "Monitor for mustard aphid (Lipaphis erysimi) during flowering stage.",
            "Provide light irrigation at flowering and siliqua formation stages.",
            "Maintain timely weeding during early canopy establishment."
        ],
        "preventive_practices": [
            "Ensure balanced fertilization with sulfur (gypsum @ 250 kg/ha for higher oil content).",
            "Adopt recommended spacing (30 cm x 10 cm) for optimal canopy aeration.",
            "Follow integrated pest management."
        ]
    },

    # =============================================================
    # GINGER (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Ginger___Rhizome_Rot": {
        "crop": "Ginger",
        "crop_display": "Ginger (Adrak)",
        "condition": "Rhizome Rot (Soft Rot)",
        "pathogen": "Pythium aphanidermatum / Pythium myriotylum (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Rhizome rot (soft rot) is the most destructive disease of ginger. The pathogen infects collar tissues near the soil level, causing water-soaking, collar collapse, foul-smelling rhizome maceration, and total plot devastation during heavy monsoon rains.",
        "symptoms": [
            "Yellowing begins on the margins of lower leaves and advances progressively upwards along the pseudostem.",
            "Collar region at ground level turns soft, water-soaked, and easily breaks off when pulled.",
            "Underground rhizomes rot into a soft, putrid pulp with a distinctive offensive odor.",
            "Whole clumps wither, dry up, and collapse in patches across the field."
        ],
        "recommended_next_steps": [
            "Immediately drench infected clumps and surrounding buffer beds with metalaxyl-mancozeb (0.2%) or Bordeaux mixture (1%).",
            "Dig out and safely burn rotting clumps along with infested rhizosphere soil.",
            "Excavate drainage furrows between beds to immediately eliminate standing water.",
            "Consult local spice research institute (IISR) or KVK for bio-agent treatment."
        ],
        "preventive_practices": [
            "Plant exclusively on raised beds (15–20 cm high, 1 m wide) with excellent drainage channels.",
            "Treat seed rhizomes before planting with mancozeb (0.3%) for 30 minutes, or Trichoderma harzianum bio-agent (10 g/kg).",
            "Apply neem cake (2 tonnes/ha) at planting to suppress soil-borne oomycetes and nematodes.",
            "Avoid planting ginger in fields with a history of water stagnation or soft rot."
        ]
    },
    "Ginger___Bacterial_Wilt": {
        "crop": "Ginger",
        "crop_display": "Ginger (Adrak)",
        "condition": "Bacterial Wilt",
        "pathogen": "Ralstonia solanacearum (Bacterium)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Bacterial wilt is a rapid, devastating vascular disease of ginger. Unlike fungal soft rot, the leaves retain green coloration initially while curling inward and rapidly wilting, with characteristic white bacterial ooze emerging from cut stem bases.",
        "symptoms": [
            "Rapid downward bronze-green wilting and inward rolling of leaves, starting from the lower foliage.",
            "Basal portion of pseudostem develops dark water-soaked discoloration without foul odor initially.",
            "Stem cutting test: dipping a cut pseudostem base in clear water yields milky white bacterial streaming threads.",
            "Vascular bundles in rhizomes show dark brown discoloration."
        ],
        "recommended_next_steps": [
            "Immediately rogue out wilted plants and quarantine the spot by drenching with bleaching powder (copper sulfate / formaline).",
            "Do not irrigate through affected beds to prevent bacteria from washing into healthy rows.",
            "Do not use rhizomes from affected fields for seed multiplication."
        ],
        "preventive_practices": [
            "Use certified, disease-free seed rhizomes from bacterial wilt-free zones.",
            "Solarize nursery beds with clear polythene sheets for 30 days during summer.",
            "Apply agricultural lime to raise soil pH above 6.5 in acidic tracts.",
            "Practice 3 to 4 year crop rotation with non-solanaceous and non-zingiberaceous crops."
        ]
    },
    "Ginger___Phyllosticta_Leaf_Spot": {
        "crop": "Ginger",
        "crop_display": "Ginger (Adrak)",
        "condition": "Leaf Spot (Phyllosticta)",
        "pathogen": "Phyllosticta zingiberi (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Phyllosticta leaf spot is a widespread foliar fungal disease that causes oval yellow spots with white centers on ginger leaves during humid monsoon months, reducing photosynthetic capacity and rhizome yield.",
        "symptoms": [
            "Small oval to elongated yellowish spots appearing on young leaves.",
            "Spots enlarge with papery white or light grey centers and dark reddish-brown margins.",
            "Centers of older lesions may tear or drop out, creating shot-hole symptoms.",
            "Severe infections cause leaves to dry up prematurely and shred."
        ],
        "recommended_next_steps": [
            "Spray mancozeb (0.25%) or carbendazim (0.1%) at first symptom onset during monsoon showers.",
            "Remove and destroy severely spotted lower leaves to reduce secondary conidial spread.",
            "Maintain soil moisture without creating waterlogged canopy humidity."
        ],
        "preventive_practices": [
            "Provide light overhead shade or intercrop with maize/pigeon pea.",
            "Apply mulch with green leaves (10–12 tonnes/ha) at planting and repeated after weeding.",
            "Treat seed rhizomes before sowing with protective contact fungicides."
        ]
    },
    "Ginger___Healthy": {
        "crop": "Ginger",
        "crop_display": "Ginger (Adrak)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The ginger crop exhibits vigorous upright pseudostems with lush, lanceolate green leaves, firm collar tissues securely anchored in the soil, and healthy tillering.",
        "symptoms": [
            "Lustrous emerald green lanceolate leaves with smooth, intact margins and no rolling.",
            "Firm, upright pseudostems with no basal water-soaking or collar softening.",
            "Vigorous clump tillering with multiple healthy shoots emerging from rhizomes."
        ],
        "recommended_next_steps": [
            "Perform timely earthing-up at 45 and 90 days after planting to cover developing rhizomes.",
            "Replenish green leaf mulch after weeding to conserve moisture and suppress soil erosion.",
            "Apply scheduled fertilizer splits according to soil test recommendations."
        ],
        "preventive_practices": [
            "Maintain continuous bed drainage throughout the heavy monsoon season.",
            "Adopt crop rotation with leguminous green manure crops.",
            "Monitor weekly for shoot borer (Conogethes punctiferalis) activity."
        ]
    },

    # =============================================================
    # CARDAMOM (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Cardamom___Capsule_Rot": {
        "crop": "Cardamom",
        "crop_display": "Cardamom (Elaichi)",
        "condition": "Capsule Rot (Azhukal Disease)",
        "pathogen": "Phytophthora meadii / Phytophthora nicotianae (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Azhukal (capsule and shoot rot) is the most destructive disease of small cardamom in the Western Ghats during the southwest monsoon. It attacks leaves, tender shoots, panicles, and capsules, causing water-soaking, capsule shedding, and clump decay.",
        "symptoms": [
            "Water-soaked lesions on young leaves expanding into brown patches with rotting and shredding.",
            "Immature capsules develop dull water-soaked discoloration, rot, and shed excessively ('Azhukal' rotting).",
            "Infected panicles decay, turn black, and fail to mature capsules.",
            "Pseudostems develop brown lesions near the base, wither, and break off easily."
        ],
        "recommended_next_steps": [
            "Spray Bordeaux mixture (1%) with a quality sticker to both foliage and panicles before monsoon onset.",
            "Drench the plant base with copper oxychloride (0.2%) or metalaxyl-mancozeb (0.2%).",
            "Clear trash around clump collars to prevent moisture retention and splash dispersal.",
            "Collect and burn rotten capsules and fallen debris."
        ],
        "preventive_practices": [
            "Incorporate Trichoderma harzianum mass-multiplied in neem cake-FYM mixture into clump basins.",
            "Regulate overhead shade to prevent dripping from shade trees during continuous rains.",
            "Construct deep contour trenches along slopes to eliminate standing water."
        ]
    },
    "Cardamom___Katte_Mosaic": {
        "crop": "Cardamom",
        "crop_display": "Cardamom (Elaichi)",
        "condition": "Katte Disease (Cardamom Mosaic Virus)",
        "pathogen": "Cardamom mosaic virus (CdMV, Potyvirus, Vectored by Banana Aphid, Pentalonia nigronervosa)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Katte (mosaic) disease is a chronic, systemic viral disorder that causes total yield collapse. Transmitted by banana aphids, it produces discontinuous chlorotic stripes parallel to veins, causing stunting and clump degeneration.",
        "symptoms": [
            "Characteristic discontinuous pale green to yellowish-green stripes running parallel to secondary leaf veins.",
            "New emerging leaves show intense mosaic mottling, reduction in leaf size, and crinkling.",
            "Clumps become progressively dwarfed with slender, shortened pseudostems.",
            "Panicles become stunted, produce few flowers, and yield tiny, empty capsules."
        ],
        "recommended_next_steps": [
            "Immediately rogue out and completely destroy infected clumps; do not leave roots in the soil.",
            "Spray dimethoate (0.05%) or imidacloprid to control aphid vector colonies on nearby banana/cardamom plants.",
            "Never use suckers or planting material from Katte-affected plantations."
        ],
        "preventive_practices": [
            "Plant only virus-tested, certified clonal seedlings or micropropagated plantlets.",
            "Maintain regular plantation surveillance and rogue out virus reservoirs immediately.",
            "Eradicate wild alternate host Zingiberaceae plants in the plantation periphery."
        ]
    },
    "Cardamom___Clump_Rot": {
        "crop": "Cardamom",
        "crop_display": "Cardamom (Elaichi)",
        "condition": "Clump Rot (Rhizome Rot)",
        "pathogen": "Rhizoctonia solani / Pythium vexans (Fungus/Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Clump rot affects the underground rhizomes and pseudostem bases of cardamom clumps during warm, waterlogged conditions, causing yellowing, rotting of rhizome nodes, and clump collapse.",
        "symptoms": [
            "Progressive yellowing and drying of foliage starting from the oldest pseudostems.",
            "Pseudostems become brittle and break off at the ground level with slight pressure.",
            "Underground rhizomes soften, turn dark brown to black, and feeder roots decay.",
            "Decayed rhizomes show internal vascular browning and hollow centers."
        ],
        "recommended_next_steps": [
            "Drench affected clump basins and immediate buffer radius with carbendazim (0.1%) or fosetyl-Al (0.2%).",
            "Remove and burn dead pseudostems and rotten rhizome pieces.",
            "Improve drainage around the plant clump base."
        ],
        "preventive_practices": [
            "Apply Trichoderma bio-agent enriched compost in clump basins twice annually (pre- and post-monsoon).",
            "Avoid planting cardamom in heavy soils with poor internal drainage.",
            "Maintain balanced fertilization with adequate potassium and organic compost."
        ]
    },
    "Cardamom___Healthy": {
        "crop": "Cardamom",
        "crop_display": "Cardamom (Elaichi)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The cardamom clump displays a luxuriant canopy of broad, dark green lanceolate leaves with wavy margins, sturdy upright pseudostems, vigorous tillers, and healthy prostrate panicles set with plump green capsules.",
        "symptoms": [
            "Vibrant, uniform dark green leaves with clean lamina and no mosaic mottling or water-soaked lesions.",
            "Sturdy, erect pseudostems firmly rooted with no basal collar browning.",
            "Prolific panicle emergence from the clump base with continuous floral and capsule development."
        ],
        "recommended_next_steps": [
            "Maintain 50% filtered canopy shade through systematic shade tree lopping.",
            "Provide regular micro-sprinkler or drip irrigation during dry summer months.",
            "Trashing: remove old dried pseudostems and hanging leaves once a year before monsoon."
        ],
        "preventive_practices": [
            "Mulch plant basins with dried forest leaves to preserve moisture and suppress weeds.",
            "Maintain soil organic matter and apply rock phosphate and potash.",
            "Install yellow sticky traps for thrips surveillance."
        ]
    },

    # =============================================================
    # BLACK PEPPER (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Black_Pepper___Quick_Wilt": {
        "crop": "Black Pepper",
        "crop_display": "Black Pepper (Kali Mirch)",
        "condition": "Quick Wilt (Foot Rot)",
        "pathogen": "Phytophthora capsici (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Quick wilt (foot rot) is the most destructive disease of black pepper worldwide. During heavy monsoon showers, the pathogen infects the collar region, feeder roots, and aerial leaves, causing rapid wilting, massive leaf drop, and sudden vine death within days.",
        "symptoms": [
            "Collar infection: dark brown water-soaked lesions develop at the collar region (ground level), girdling the stem.",
            "Foliage: rapid yellowing, wilting, and catastrophic defoliation within 7–14 days while vines remain attached to standards.",
            "Leaf infection: dark circular lesions with fimbriate (feather-like) margins on leaves exposed to rain splash.",
            "Spikes: berry rot and complete spike shedding.",
            "Feeder roots: blackening and complete decay of feeder root systems."
        ],
        "recommended_next_steps": [
            "Apply prophylactic spray of Bordeaux mixture (1%) to the vine canopy before southwest monsoon rains.",
            "Drench the vine basin (5–10 liters per vine) with copper oxychloride (0.2%) or potassium phosphonate (0.3%).",
            "Prune low-hanging runner shoots within 30 cm of ground level to eliminate rain-splash infection pathways.",
            "Immediately rogue out and safely burn dead vines and solarize the planting pit."
        ],
        "preventive_practices": [
            "Apply Trichoderma harzianum (50 g mass-multiplied in FYM) in each vine basin twice a year.",
            "Ensure proper drainage channels between vine rows on hillside terraces.",
            "Plant Phytophthora-tolerant black pepper varieties (e.g., IISR Shakthi, IISR Thevam).",
            "Never use cuttings from vines with a history of foot rot."
        ]
    },
    "Black_Pepper___Slow_Decline": {
        "crop": "Black Pepper",
        "crop_display": "Black Pepper (Kali Mirch)",
        "condition": "Slow Decline (Slow Wilt)",
        "pathogen": "Radopholus similis / Meloidogyne incognita (Nematodes) + Fusarium solani",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Slow decline is a debilitating root disease complex caused by burrowing/root-knot nematodes interacting with soil fungi. Vines show gradual foliar yellowing, internode shortening, stunted growth, and progressive dieback over multiple seasons.",
        "symptoms": [
            "Gradual, progressive chlorotic yellowing of foliage across the entire vine canopy.",
            "Internode shortening and reduction in leaf size giving a bushy, stunted appearance.",
            "Progressive dieback of terminal branches from top to bottom.",
            "Roots show extensive necrosis, cortical sloughing, and root galls (from Meloidogyne).",
            "Gradual reduction in spike length and berry setting over 2–3 seasons."
        ],
        "recommended_next_steps": [
            "Apply neem cake (1–2 kg per vine basin) to suppress nematode populations.",
            "Apply bio-nematicide Paecilomyces lilacinus or Pochonia chlamydosporia in the root zone.",
            "Prune severely dieback-affected branches and apply paste of copper oxychloride.",
            "Provide protective irrigation during hot summer months to reduce drought-nematode stress."
        ],
        "preventive_practices": [
            "Use nematode-free rooted cuttings raised in solarized nursery potting mixture.",
            "Incorporate green manure (Pueraria or sunn hemp) into vine basins.",
            "Maintain balanced fertilization with adequate potassium and micronutrients."
        ]
    },
    "Black_Pepper___Anthracnose": {
        "crop": "Black Pepper",
        "crop_display": "Black Pepper (Kali Mirch)",
        "condition": "Anthracnose (Pollu Disease)",
        "pathogen": "Colletotrichum gloeosporioides (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate to High",
        "description": "Anthracnose affects leaves, stems, and fruiting spikes of black pepper. On spikes, it causes partial or total drying and shedding of developing berries (known as fungal 'Pollu'), causing direct crop yield losses.",
        "symptoms": [
            "Leaves: circular to irregular dark brown spots with concentric rings and chlorotic halos.",
            "Spikes: brown necrotic lesions on the spike axis, causing premature drying and shedding of berries.",
            "Berries: shriveled, hollow, blackened, and empty berries on affected spikes.",
            "Tender branches: tip dieback with brownish necrosis advancing downwards."
        ],
        "recommended_next_steps": [
            "Apply foliar spray of carbendazim-mancozeb (0.1%) or Bordeaux mixture (1%) when spike emergence begins.",
            "Control pepper pollu beetle (Longitarsus nigripennis) whose feeding punctures facilitate fungal entry.",
            "Prune shaded, dense canopy to increase aeration and sunlight penetration."
        ],
        "preventive_practices": [
            "Regulate shade tree lopping twice a year (June and October).",
            "Maintain vine hygiene and remove dried, infected spikes from the previous harvest.",
            "Apply balanced fertilizer splits to strengthen berry set."
        ]
    },
    "Black_Pepper___Healthy": {
        "crop": "Black Pepper",
        "crop_display": "Black Pepper (Kali Mirch)",
        "condition": "Healthy Vine",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The black pepper vine displays vigorous climbing growth on support standards (live trees or poles), featuring thick, lustrous dark green ovate leaves, sturdy orthotropic climbing stems, and dense pendulous fruiting spikes loaded with uniform berries.",
        "symptoms": [
            "Lustrous, thick, dark green leaves with clean, intact margins and no yellowing.",
            "Firm climbing stem securely attached to support standards with healthy adventitious roots.",
            "Long, fully set pendulous fruiting spikes with compact, well-developed green berries."
        ],
        "recommended_next_steps": [
            "Tie young climbing vines to support standards at regular intervals of 30 cm.",
            "Prune excess branches on support trees to allow 40–50% filtered sunlight.",
            "Apply scheduled organic manure (10 kg FYM) and NPK fertilizer splits per vine."
        ],
        "preventive_practices": [
            "Mulch vine basins with dry leaves before summer to conserve moisture.",
            "Construct inward-sloping terraces to minimize soil erosion on hill slopes.",
            "Scout regularly for pollu beetle and scale insect infestations."
        ]
    },

    # =============================================================
    # TOBACCO (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Tobacco___Mosaic_Virus": {
        "crop": "Tobacco",
        "crop_display": "Tobacco (Tambaku)",
        "condition": "Tobacco Mosaic Virus (TMV)",
        "pathogen": "Tobacco Mosaic Virus (TMV, Tobamovirus - Mechanically Transmitted)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Tobacco mosaic virus is an extremely stable, mechanically transmitted virus that causes light/dark green mosaic mottling, leaf blistering, and malformation on tobacco leaves, degrading cured leaf quality and market grade.",
        "symptoms": [
            "Characteristic light green and dark green mosaic patterns on leaves, especially on younger growth.",
            "Raised dark green blisters and puckering of the leaf blade lamina.",
            "Narrowing, distortion, and 'shoestring' malformation of younger leaves.",
            "Stunted plant growth and uneven leaf ripening with necrotic flecking ('mosaic burn')."
        ],
        "recommended_next_steps": [
            "Immediately rogue out infected seedlings and plants; burn or deeply bury them away from fields.",
            "Workers must wash hands and tools thoroughly with soap and water or trisodium phosphate (20%) before handling healthy plants.",
            "Strictly forbid tobacco smoking or chewing by workers inside tobacco nurseries and fields."
        ],
        "preventive_practices": [
            "Plant TMV-resistant tobacco varieties (e.g., Virginia Gold resistant lines).",
            "Sterilize nursery soil with steam or solarization before sowing.",
            "Practice 2 to 3 year crop rotation with non-solanaceous crops."
        ]
    },
    "Tobacco___Black_Shank": {
        "crop": "Tobacco",
        "crop_display": "Tobacco (Tambaku)",
        "condition": "Black Shank",
        "pathogen": "Phytophthora nicotianae (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Black shank is a lethal soil-borne disease of tobacco. It produces black, sunken lesions at the base of the stalk, destroys root systems, and causes sudden wilting and drying of the entire plant during warm, humid weather.",
        "symptoms": [
            "Rapid wilting of leaves during the heat of the day, turning brown and drying without falling.",
            "Blackening and rotting of the lower stalk near the soil line, extending several inches upward ('black shank').",
            "Splitting the lower stalk lengthwise reveals blackened, disc-like plates in the dried pith tissue.",
            "Root system turns completely black, rots, and disintegrates."
        ],
        "recommended_next_steps": [
            "Apply metalaxyl-mancozeb (0.2%) soil drench around plant bases upon first appearance.",
            "Rogue out and destroy infected stalks to prevent resting oospore buildup in soil.",
            "Improve drainage to avoid standing water in furrows."
        ],
        "preventive_practices": [
            "Plant black-shank resistant cultivars.",
            "Rotate crops for at least 3 years with grass, maize, or pasture crops.",
            "Avoid transplanting into fields with high soil moisture and disease history."
        ]
    },
    "Tobacco___Frog_Eye_Leaf_Spot": {
        "crop": "Tobacco",
        "crop_display": "Tobacco (Tambaku)",
        "condition": "Frog Eye Leaf Spot",
        "pathogen": "Cercospora nicotianae (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate",
        "description": "Frog eye leaf spot causes circular spots with white parchment-like centers and dark borders on mature tobacco leaves, severely diminishing the commercial grade and usability of wrapper and flue-cured leaves.",
        "symptoms": [
            "Circular spots with ash-grey or white parchment-like centers surrounded by narrow dark brown to red borders ('frogeye' appearance).",
            "Tiny black dots (fruiting conidiophores) visible in lesion centers under magnification.",
            "Spots coalesce, creating large irregular dead patches on cured tobacco leaves.",
            "Severe infections in curing barns cause 'barn spot' blemishes."
        ],
        "recommended_next_steps": [
            "Apply protective foliar sprays of mancozeb (0.2%) or thiophanate-methyl (0.1%) when spots first appear on lower leaves.",
            "Prime lower mature leaves promptly to prevent secondary fungal spread.",
            "Maintain proper air ventilation and humidity control during barn curing."
        ],
        "preventive_practices": [
            "Avoid excessive nitrogen fertilization that delays leaf maturity.",
            "Destroy seedbed plant residues and wild solanaceous weeds.",
            "Maintain optimal field spacing for rapid leaf drying."
        ]
    },
    "Tobacco___Healthy": {
        "crop": "Tobacco",
        "crop_display": "Tobacco (Tambaku)",
        "condition": "Healthy Foliage",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The tobacco plant displays large, broad, erect to spreading dark green leaves with clean lamina, sticky glandular pubescence, sturdy thick stems, and uniform growth.",
        "symptoms": [
            "Large, broad, uniform leaves with smooth margins and no mosaic mottling or necrotic spots.",
            "Sturdy, upright stalk with healthy green bark and clean collar region.",
            "Normal leaf thickness, elasticity, and uniform physiological maturation."
        ],
        "recommended_next_steps": [
            "Perform timely topping (removal of terminal flower head) to stimulate expansion of upper leaves.",
            "Apply suckericides or desucker manually to prevent axillary shoot growth.",
            "Scout for tobacco caterpillar (Spodoptera litura) and aphids."
        ],
        "preventive_practices": [
            "Follow balanced NPK fertilization (adequate potassium for good leaf burn and texture).",
            "Maintain weed-free beds during vegetative establishment.",
            "Harvest leaves at optimum technical maturity (priming 3–4 leaves per picking)."
        ]
    },

    # =============================================================
    # RUBBER (Expanded Knowledge Base - 4 Profiles)
    # =============================================================
    "Rubber___Abnormal_Leaf_Fall": {
        "crop": "Rubber",
        "crop_display": "Rubber (Hevea)",
        "condition": "Abnormal Leaf Fall",
        "pathogen": "Phytophthora botryosa / Phytophthora meadii (Oomycete)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Abnormal leaf fall is the most damaging disease of rubber plantations in south India. During the continuous southwest monsoon, it attacks green pods, petiole bases, and leaves, causing heavy unseasonal defoliation and up to 30–50% latex crop loss.",
        "symptoms": [
            "Dark water-soaked lesions develop on green petioles with a characteristic droplet of coagulated latex in the lesion center.",
            "Heavy defoliation: green leaves shed rapidly, blanketing the plantation floor during July–August.",
            "Green developing rubber pods rot, turn black, and remain hanging on the tree ('pod rot').",
            "Terminal twigs rot and die back, causing canopy thinning."
        ],
        "recommended_next_steps": [
            "Prophylactic aerial or high-pressure spray of copper oxychloride in oil (oil-based copper @ 8 kg in 40 L spray oil/ha) prior to southwest monsoon rains.",
            "Spray Bordeaux mixture (1%) to young replanted clearings before monsoon onset.",
            "Collect and burn rotten pods from ground level to reduce overwintering spore reservoirs."
        ],
        "preventive_practices": [
            "Plant tolerant rubber clones (e.g., RRII 105 has high productivity with managed spraying; RRII 414, RRII 430).",
            "Maintain clean canopy hygiene in valleys and foggy plantation pockets.",
            "Ensure regular annual pre-monsoon prophylactic fungicide scheduling."
        ]
    },
    "Rubber___Powdery_Mildew": {
        "crop": "Rubber",
        "crop_display": "Rubber (Hevea)",
        "condition": "Powdery Mildew (Oidium)",
        "pathogen": "Oidium heveae (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Moderate to High",
        "description": "Powdery mildew attacks tender emerging leaves during the refoliation period (January–March), producing white powdery fungal patches that cause crinkling, leaf curling, and premature leaf fall.",
        "symptoms": [
            "White, talcum-like powdery fungal patches on both surfaces of tender young refoliating leaves.",
            "Affected leaves curl, crinkle, become distorted, and turn ash-grey.",
            "Tender leaves wither and fall off, leaving bare petioles attached to twigs ('spider leg' appearance).",
            "Repeated refoliation exhausts the tree, leading to severe latex yield reduction."
        ],
        "recommended_next_steps": [
            "Dust wettable sulfur (325 mesh @ 10–12 kg/ha) using power dusters early in the morning when dew is present.",
            "Apply systemic fungicide (hexaconazole 0.1% or triadimefon 0.1%) during tender refoliation stage.",
            "Repeat dusting at 7–10 day intervals during peak refoliation."
        ],
        "preventive_practices": [
            "Induce uniform, early winter refoliation through balanced fertilization.",
            "Plant rubber clones that show rapid refoliation to escape peak fungal spore season.",
            "Ensure adequate soil nutrition with potassium and magnesium."
        ]
    },
    "Rubber___Corynespora_Leaf_Fall": {
        "crop": "Rubber",
        "crop_display": "Rubber (Hevea)",
        "condition": "Corynespora Leaf Fall (CLF)",
        "pathogen": "Corynespora cassiicola (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Corynespora leaf fall is an aggressive emerging fungal disease of rubber. It produces characteristic 'railway track' vein lesions, causing severe defoliation of both young and mature leaves and causing tree dieback in susceptible clones.",
        "symptoms": [
            "Dark brown to black necrotic lesions along secondary leaf veins with characteristic 'herringbone' or 'railway track' appearance.",
            "Circular spots with papery grey centers and yellow halos on the leaf blade lamina.",
            "Repeated defoliation of both young flushes and mature maintenance foliage throughout the year.",
            "Extensive terminal shoot dieback and latex tapping cessation."
        ],
        "recommended_next_steps": [
            "Spray mancozeb (0.25%) or propiconazole (0.1%) upon symptom appearance on young flush leaves.",
            "Avoid planting highly susceptible clones (e.g., RRIM 600, RRIC 100) in high disease-pressure tracts.",
            "Prune dead terminal twigs and spray copper fungicides."
        ],
        "preventive_practices": [
            "Plant CLF-resistant or tolerant clones recommended by the Rubber Research Institute.",
            "Maintain optimal fertilizer management to support canopy recovery.",
            "Establish multi-clonal planting designs to prevent epidemic disease spread."
        ]
    },
    "Rubber___Healthy": {
        "crop": "Rubber",
        "crop_display": "Rubber (Hevea)",
        "condition": "Healthy Canopy",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The rubber tree exhibits a dense, domed canopy of glossy trifoliate leaves, a straight sturdy trunk with smooth healthy tapping bark, clean branch framework, and regular latex yield.",
        "symptoms": [
            "Lustrous dark green trifoliate leaves with clean, intact margins and no powdery mildew or abnormal spotting.",
            "Healthy, thick tapping panel bark with smooth renewal and no black stripe or canker.",
            "Dense canopy providing complete shading of inter-row avenues."
        ],
        "recommended_next_steps": [
            "Maintain disciplined tapping practices (half-spiral d/2 or d/3 system) to preserve bark longevity.",
            "Apply bark protectant paste (fungicide-wax formulation) on tapping panels during rainy months.",
            "Apply scheduled NPK-Mg fertilizer blends as per soil and leaf test results."
        ],
        "preventive_practices": [
            "Maintain leguminous cover crops (Mucuna bracteata) in young clearings.",
            "Avoid excessive downward tapping into the collar zone.",
            "Rain-guard tapping panels with polythene aprons before monsoon to enable uninterrupted tapping."
        ]
    },

    # =============================================================
    # CASHEW (Expanded Knowledge Base - 3 Profiles)
    # =============================================================
    "Cashew___Tea_Mosquito_Bug_Blight": {
        "crop": "Cashew",
        "crop_display": "Cashew (Kaju)",
        "condition": "Tea Mosquito Bug Blight / Dieback",
        "pathogen": "Helopeltis antonii (Mirid Bug) + Colletotrichum gloeosporioides",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "Critical",
        "description": "Tea mosquito bug is the primary pest-disease complex in cashew cultivation. The bug injects toxic saliva into succulent shoots, panicles, and developing nuts, creating water-soaked necrotic lesions that are colonized by Gloeosporium fungi, causing total blossom blight and dieback.",
        "symptoms": [
            "Water-soaked elongated brownish lesions on succulent terminal shoots, petioles, and panicle branches.",
            "Resin exudation from feeding punctures, hardening into dark gummy crusts.",
            "Blossom blight: entire floral panicles turn black, dry up, and present a scorched, burnt appearance.",
            "Dieback: shoots dry up from the tip downwards, resulting in complete crop failure."
        ],
        "recommended_next_steps": [
            "Adopt 3-spray schedule: 1st spray at flushing (lambda-cyhalothrin 0.003%), 2nd spray at flowering (acetamiprid or carbaryl), 3rd spray at fruit set.",
            "Prune dead, blighted twigs 5 cm below the dead wood and apply Bordeaux paste.",
            "Scout canopy early in the morning when adult mirid bugs are active on tender flushes."
        ],
        "preventive_practices": [
            "Prune criss-cross branches in August to allow maximum canopy sunlight penetration.",
            "Conserve natural predators such as weaver ants (Oecophylla smaragdina).",
            "Plant cashew varieties with synchronized, short flowering duration (e.g., Bhaskara, Ullal-3)."
        ]
    },
    "Cashew___Anthracnose": {
        "crop": "Cashew",
        "crop_display": "Cashew (Kaju)",
        "condition": "Anthracnose",
        "pathogen": "Colletotrichum gloeosporioides (Fungus)",
        "is_healthy": False,
        "model_trained_v4": False,
        "severity": "High",
        "description": "Anthracnose attacks tender cashew leaves, flowers, and developing cashew apples and nuts during humid rainy periods, causing necrotic spotting, floral blight, and fruit mummification.",
        "symptoms": [
            "Reddish-brown water-soaked spots on tender leaves expanding into large irregular necrotic blights.",
            "Leaves curl, become crinkled, and drop prematurely.",
            "Floral panicles develop black necrotic lesions and wither.",
            "Developing cashew nuts and apples show sunken black lesions, fail to develop, and mummify on the tree."
        ],
        "recommended_next_steps": [
            "Spray Bordeaux mixture (1%) or copper oxychloride (0.25%) at the time of new vegetative flush and panicle emergence.",
            "Prune out dead shoots and mummified nuts and burn them.",
            "Ensure canopy aeration by selective center pruning."
        ],
        "preventive_practices": [
            "Plant anthracnose-tolerant cashew hybrids.",
            "Maintain weed-free tree basins and provide balanced NPK-fertilization.",
            "Combine disease management with tea mosquito bug surveillance."
        ]
    },
    "Cashew___Healthy": {
        "crop": "Cashew",
        "crop_display": "Cashew (Kaju)",
        "condition": "Healthy Canopy",
        "pathogen": "None detected",
        "is_healthy": True,
        "model_trained_v4": False,
        "severity": "None",
        "description": "The cashew tree displays an umbrella-shaped dense canopy with leathery, glossy green obovate leaves, vigorous new vegetative flushes, prolific inflorescences, and healthy nut/apple set.",
        "symptoms": [
            "Leathery dark green obovate leaves with clean, undamaged surfaces and no gummy exudation.",
            "Vigorous pinkish-green terminal flushes with no necrotic lesions or scorching.",
            "Healthy flowering panicles loaded with developing cashew nuts and plump apples."
        ],
        "recommended_next_steps": [
            "Apply scheduled manure (FYM @ 20 kg) and chemical fertilizers in circular trenches around the canopy drip line.",
            "Prune dry branches and root-suckers annually in August–September.",
            "Provide protective summer irrigation during nut development to prevent fruit drop."
        ],
        "preventive_practices": [
            "Mulch tree basins with cashew prunings and dry biomass.",
            "Terrace sloping cashew orchards to conserve rainwater.",
            "Inspect trunk bases regularly for cashew stem and root borer (Plocaederus ferrugineus)."
        ]
    }
}

# 16 Crops currently supported by the v4.2 YOLO Computer Vision Model
VISION_MODEL_SUPPORTED_CROPS = [
    "Apple",
    "Blueberry",
    "Cherry (including sour)",
    "Corn (maize)",
    "Grape",
    "Orange",
    "Paddy",
    "Peach",
    "Pepper, bell",
    "Potato",
    "Raspberry",
    "Soybean",
    "Squash",
    "Strawberry",
    "Tomato",
    "Wheat"
]

# 20 Additional Crops available in the Knowledge Base & Live Search (v5 Training Candidates)
EXPANDED_KNOWLEDGE_CROPS = [
    "Banana",
    "Black Pepper",
    "Cardamom",
    "Cashew",
    "Chilli",
    "Coconut",
    "Coffee",
    "Cotton",
    "Ginger",
    "Groundnut",
    "Mango",
    "Mustard",
    "Onion",
    "Palm",
    "Pigeon pea",
    "Rubber",
    "Sugarcane",
    "Tea",
    "Tobacco",
    "Turmeric"
]

# Complete set of crops available in the Knowledge Base (36 Total Crops)
SUPPORTED_CROPS = VISION_MODEL_SUPPORTED_CROPS
ALL_KNOWLEDGE_CROPS = sorted(list(set(VISION_MODEL_SUPPORTED_CROPS + EXPANDED_KNOWLEDGE_CROPS)))

# Unsupported crops examples for transparent rejection messages
UNSUPPORTED_CROPS_EXAMPLES = [
    "Jute",
    "Flax",
    "Betel vine",
    "Vanilla",
    "Clove",
    "Nutmeg",
    "Arecanut"
]

def is_vision_model_supported(crop_name: str) -> bool:
    """Check if a crop has an active trained vision model in v4.2."""
    if not crop_name:
        return False
    norm = crop_name.lower().replace("_", " ").strip()
    return any(norm in c.lower() for c in VISION_MODEL_SUPPORTED_CROPS)

def normalize_key(name: str) -> str:
    """Normalize label strings for robust lookup."""
    return (
        str(name or "")
        .replace("___", " ")
        .replace("_", " ")
        .replace("-", " ")
        .lower()
        .strip()
    )

NORMALIZED_KNOWLEDGE = {
    normalize_key(k): v for k, v in DISEASE_KNOWLEDGE.items()
}

def get_disease_info(class_name: str) -> dict:
    """
    Retrieve verified agricultural knowledge for a crop disease class.
    Returns structured data or None if outside supported knowledge base.
    """
    if not class_name:
        return None
    # Exact match first
    if class_name in DISEASE_KNOWLEDGE:
        return DISEASE_KNOWLEDGE[class_name]
    # Normalized lookup
    norm = normalize_key(class_name)
    if norm in NORMALIZED_KNOWLEDGE:
        return NORMALIZED_KNOWLEDGE[norm]
    return None

