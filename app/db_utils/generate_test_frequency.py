import re
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, select

from core.models.db_base import engine
from core.models.db_code_value_set import CodeSet
from core.models.db_code_value import CodeValue
from core.dbutils.db_get_or_create import db_get_or_create
from core.dbutils.db_utils import convert_to_key
from core.dbutils.db_uar_get_funcs import uar_get_code_by, uar_get_code_display
from core.models.db_frequency import FrequencySchedule, ScheduledTimeOfDay, ScheduledDayOfWeek


def generate_test_freq():
    """ Generate a test frequency in the FrequencySchedule table """
    with Session(engine) as session:
        # q12h frequency code value
        cv_freq = uar_get_code_by('DISPLAY', 4003, 'q12h')  
        cv_activity_pharmacy = uar_get_code_by('DISPLAY', 106, 'Pharmacy')  
                
        print(cv_freq, cv_activity_pharmacy)

        ##################################################
        # Create a 'q12h' frequency 
        db_get_or_create(
                session,
                FrequencySchedule,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q12h'),
                activity_type_cd        = uar_get_code_by('DISPLAY', 106, 'Pharmacy'),    # CS 106 Activity Type
                default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                frequency_type          = 1,       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                freq_qualifier          = 14,      # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                min_interval_nbr        = 2,       # The suggested minimum elapsed time between administrations.
                min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),   # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                # parent_entity_id        = Column(BigInteger, nullable=True )    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                prn_default_ind         = False,                              # PRN order indicator
            )

        db_get_or_create(
                session,
                FrequencySchedule,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q12h'),
                activity_type_cd        = 0,    #  0: general, CS 106 Activity Type
                default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                frequency_type          = 1,                       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                min_interval_nbr        = 2,                       # The suggested minimum elapsed time between administrations.
                min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),     # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                # parent_entity_id        = Column(BigInteger, nullable=True )    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                prn_default_ind         = False,                              # PRN order indicator
            )

        ##################################################
        # Create a 'q8h' frequency - Pharmacy 
        db_get_or_create(
                session,
                FrequencySchedule,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q8h'),
                activity_type_cd        = uar_get_code_by('DISPLAY', 106, 'Pharmacy'),    # CS 106 Activity Type
                default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                frequency_type          = 1,                       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                min_interval_nbr        = 2,                       # The suggested minimum elapsed time between administrations.
                min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),     # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                prn_default_ind         = False,                              # PRN order indicator
            )
        db_get_or_create(
                session,
                ScheduledTimeOfDay,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q8h'),
                activity_type_cd        = uar_get_code_by('DISPLAY', 106, 'Pharmacy'),    # CS 106 Activity Type
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                parent_entity_id        = 0,    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                time_of_day             = 480   # 08:00    8 x 60mins = 480 mins 
            )
        db_get_or_create(
                session,
                ScheduledTimeOfDay,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q8h'),
                activity_type_cd        = uar_get_code_by('DISPLAY', 106, 'Pharmacy'),    # CS 106 Activity Type
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                parent_entity_id        = 0,    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                time_of_day             = 960   # 16:00    8 x 60mins = 480 mins 
            )
        db_get_or_create(
                session,
                ScheduledTimeOfDay,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q8h'),
                activity_type_cd        = uar_get_code_by('DISPLAY', 106, 'Pharmacy'),    # CS 106 Activity Type
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                parent_entity_id        = 0,    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                time_of_day             = 0     # 00:00    8 x 60mins = 480 mins 
            )


        ##################################################
        # Create a 'q8h' frequency - General 
        db_get_or_create(
                session,
                FrequencySchedule,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q8h'),
                activity_type_cd        = 0,    #  0: general, CS 106 Activity Type
                default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                frequency_type          = 1,                       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                min_interval_nbr        = 2,                       # The suggested minimum elapsed time between administrations.
                min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),     # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                # parent_entity_id        = Column(BigInteger, nullable=True )    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                prn_default_ind         = False,                              # PRN order indicator
            )


        ##################################################
        # Create a 'q12h Interval' frequency 
        db_get_or_create(
                session,
                FrequencySchedule,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q12h interval'),
                activity_type_cd        = uar_get_code_by('DISPLAY', 106, 'Pharmacy'),    # CS 106 Activity Type
                default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                frequency_type          = 3,       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                freq_qualifier          = 14,      # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                interval                = 12,        # Defines the interval of the frequency scheduled defined as interval_units.  Only applicable to frequency_type of 3.
                interval_units          = 2,        # 1-minute, 2-hour, 3-day
                min_interval_nbr        = 2,        # The suggested minimum elapsed time between administrations.
                min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),     # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                # parent_entity_id        = Column(BigInteger, nullable=True )    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                prn_default_ind         = False,                              # PRN order indicator
            )

        ##################################################
        # Create a 'q2day' interval frequency 
        db_get_or_create(
                session,
                FrequencySchedule,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q2day'),
                activity_type_cd        = 0,    #  0: general, CS 106 Activity Type
                default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                frequency_type          = 3,                       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                interval                = 2,        # Defines the interval of the frequency scheduled defined as interval_units.  Only applicable to frequency_type of 3.
                interval_units          = 3,        # 1-minute, 2-hour, 3-day
                min_interval_nbr        = 2,                       # The suggested minimum elapsed time between administrations.
                min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),     # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                # parent_entity_id        = Column(BigInteger, nullable=True )    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                prn_default_ind         = False,                              # PRN order indicator
            )
        db_get_or_create(
                session,
                ScheduledTimeOfDay,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'q2day'),
                activity_type_cd        = 0,    #  0: general, CS 106 Activity Type
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                parent_entity_id        = 0,    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                time_of_day             = 480   # 08:00    8 x 60mins = 480 mins 
            )

        ##################################################
        # Create a 'BID' frequency 
        db_get_or_create(
                session,
                FrequencySchedule,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'BID'),
                activity_type_cd        = uar_get_code_by('DISPLAY', 106, 'Pharmacy'),    # CS 106 Activity Type
                default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                frequency_type          = 1,                       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                min_interval_nbr        = 2,                       # The suggested minimum elapsed time between administrations.
                min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),     # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                # parent_entity_id        = Column(BigInteger, nullable=True )    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                prn_default_ind         = False,                              # PRN order indicator
            )

        db_get_or_create(
                session,
                FrequencySchedule,
                frequency_cd            = uar_get_code_by('DISPLAY', 4003, 'BID'),
                activity_type_cd        = 0,    #  0: general, CS 106 Activity Type
                default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                frequency_type          = 1,                       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                freq_qualifier          = 14,        # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                min_interval_nbr        = 2,                       # The suggested minimum elapsed time between administrations.
                min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),     # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                # parent_entity_id        = Column(BigInteger, nullable=True )    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                prn_default_ind         = False,                              # PRN order indicator
            )

def generate_test_freq_all():
    """ Generate all frequencies in the FrequencySchedule table """
    with Session(engine) as session:
        # Query frequency code value
        stmt = select(
                CodeValue.code_value
            ).where(
                and_(
                    CodeValue.code_set==4003,
                    CodeValue.active_ind==True 
                )
            )

        freqs = session.execute(stmt).all()

        cv_activity_pharmacy = uar_get_code_by('DISPLAY', 106, 'Pharmacy')  
        for f in freqs:
            db_get_or_create(
                    session,
                    FrequencySchedule,
                    frequency_cd            = f[0],
                    activity_type_cd        = cv_activity_pharmacy,    # CS 106 Activity Type
                    default_par_val         = 2,       # A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN.  Order catalog-level par values will override this
                    frequency_type          = 1,       # 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time
                    freq_qualifier          = 14,      # Defines the domain of ordering attributes which point to the appropriate schedule for a specific order.  Frequency_qualifier = 16 represents custom frequencies
                    min_interval_nbr        = 2,       # The suggested minimum elapsed time between administrations.
                    min_interval_unit_cd    = uar_get_code_by('DISPLAY', 54, 'hour'),   # CS 54. The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.)
                    # parent_entity           = Column(String(32), nullable=True)     # "Applies to:". These act as pointers to the flexing agent.  Frequencies are flexed by the following:  Physician, Location, Location Group, Orderable, Therapeutic Class.  In the case of an Ad-hoc frequency, this will be ORDERS
                    # parent_entity_id        = Column(BigInteger, nullable=True )    # Parent entity id for merge.   Root entity will vary depending on type of frequencies.    Qualifiers 10 & 8 will refer to the code_value table  qualifier 4 to the order_catalog  Qualifier 6 to the alt_sel_cat table  Qualifier 12 to prsnl table  Qualifier 16 to the orders table
                    prn_default_ind         = False,                              # PRN order indicator
                )


if __name__ == '__main__':
    # generate_test_freq_all()
    generate_test_freq()