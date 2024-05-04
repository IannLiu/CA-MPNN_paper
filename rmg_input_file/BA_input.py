# Data sources
database(
    thermoLibraries=['primaryThermoLibrary', 'DFT_QCI_thermo', 'CBS_QB3_1dHR', 'thermo_DFT_CCSDTF12_BAC','CHO','FFCM1(-)'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

# List of species
species(
    label='BA',
    reactive=True,
    structure=SMILES("CCCCOC(C)=O"),
)

species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]"),
)

# Reaction systems
simpleReactor(
    temperature=(1200,'K'),
    pressure=(10,'bar'),
    initialMoleFractions={
        "BA": 0.1,
        "Ar":0.9
    },
    terminationConversion={
        'BA': 0.99,
    },
    terminationTime=(10,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceMoveToCore=0.05,
    toleranceInterruptSimulation=0.05,
    toleranceKeepInEdge=0.001,
    maximumEdgeSpecies=100000,
    minCoreSizeForPrune=50,
    minSpeciesExistIterationsForPrune=2,
    filterReactions=True,
    maxNumObjsPerIter=5,
    
)

options(
    units='si',
    generateOutputHTML=False,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)


generatedSpeciesConstraints(
    allowed=['input species', 'seed mechanisms', 'reaction libraries'],
    maximumCarbonAtoms=15,
    maximumOxygenAtoms=8,
    maximumRadicalElectrons=2,
    maximumSingletCarbenes=1,
    maximumCarbeneRadicals=0,
    allowSingletO2=True
)
