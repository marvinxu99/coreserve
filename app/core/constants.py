# Global constants
from enum import Enum, unique, auto, IntFlag, Flag


END_EFFECTIVE_DATE_ISO = '2100-12-31 00:00:00'


@unique
class FrequencyType(Enum):
    """Frequency Type
        # 1 = time of day, 
        # 2 = day of week, 
        # 3 = interval, 
        # 4 = onetime only, 
        # 5 = no specific time (Unscheduled)
    """
    TIME_OF_DAY   = 1
    DAY_OF_WEEK   = 2
    INTERVAL      = 3
    ONE_TIME_ONLY = 4
    UNSCHEDULED   = 5


@unique
class CodeSet(Enum):
    """Code Sets"""
    FREQUENCY            = 4003


@unique
class ResultType(Enum):
    """Resut Type """
    Alpha               = 1
    AlphaAndFreeText    = 2
    Date                = 3
    DateAndTime         = 4
    Calculation         = 5
    FreeText            = 6
    Interpretation      = 7
    Multi               = 8
    MultiAndFreeText    = 9
    Numeric             = 10
    Provider            = 11
    ReadOnly            = 12
    Text                = 13
    Time                = 14




    