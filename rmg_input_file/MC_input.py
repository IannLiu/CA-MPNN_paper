# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'], 
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

# List of species
species(
    label='methane',
    reactive=True,
    structure=SMILES("C"),
)

species(
    label='O2',
    reactive=True,
    structure=SMILES("[O][O]"),
)


species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]"),
)

# Reaction systems
simpleReactor(
    temperature=(1500,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "methane": 1,
        "O2": 3,
    },
    terminationConversion={
        'methane': 0.99,
    },
    terminationTime=(1,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.01,
    maximumEdgeSpecies=100000,
    minCoreSizeForPrune=50,
    minSpeciesExistIterationsForPrune=2,
)

options(
    units='si',
    generateOutputHTML=False,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)

generatedSpeciesConstraints(
    maximumCarbonAtoms=15,
    maximumOxygenAtoms=8,
    maximumRadicalElectrons=2,
    maximumSingletCarbenes=1,
    maximumCarbeneRadicals=0,
    allowSingletO2=True
)
