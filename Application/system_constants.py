# System constants used across BBE

# General
NUM_OF_SIMS = 1
NUM_OF_COMPETITORS = 4
NUM_OF_EXCHANGES = 1
PRE_RACE_BETTING_PERIOD_LENGTH = 12
IN_PLAY_CUT_OFF_PERIOD = 2
SESSION_SPEED_MULTIPLIER = 1

# Data Store Attributes
RACE_DATA_FILENAME = 'data/race_event_core.csv'

# Message Protocol Numbers
EXCHANGE_UPDATE_MSG_NUM = 1
RACE_UPDATE_MSG_NUM = 2

# Exchange Attributes
MIN_ODDS = 1.1
MAX_ODDS = 20.00

# Print-Outs
TBBE_VERBOSE = False
SIM_VERBOSE = False
EXCHANGE_VERBOSE = False

# Event Attributes
# average horse races are between 5 and 12 (1005 - 2414) furlongs or could go min - max (400 - 4000)
RACE_LENGTH = 2000
MIN_RACE_LENGTH = 400
MAX_RACE_LENGTH = 4000

MIN_RACE_UNDULATION = 0
MAX_RACE_UNDULATION = 100

MIN_RACE_TEMPERATURE = 0
MAX_RACE_TEMPERATUE = 50

# Betting Agent Attributes
NUM_EX_ANTE_SIMS = 25
NUM_IN_PLAY_SIMS = 25



#OD models

MODEL_NAME = 'RA'
OPINION_COMPETITOR = 1 # Bettors will be expressing opinions about this competitor. Opinions are in the range of [0,1].

MAX_OP = 1
MIN_OP = 0

# intensity of interactions
mu = 0.2 # used for all models eg. 0.2
delta = 0.25# used for Bounded Confidence Model eg. 0.1
lmda = 1 # used for Relative Disagreement Model eg. 0.1

#Bounded confidence

u_min = 0.2
u_max = 2
u_steps = 19

#range of global proportion of extremists (pe)
pe_min = 0.025
pe_max = 0.1
pe_steps = 12

u_e = 0.1 # extremism uncertainty
extreme_distance = 0 # how close one has to be to be an "extremist"
# Min_mod_op = MIN_OP + extreme_distance
# Max_mod_op = MAX_OP - extreme_distance
plus_neg = [1, 1] # [1, 1] for both pos and neg extremes respectively

# whether or not to start with extremes
extreme_start = 0


