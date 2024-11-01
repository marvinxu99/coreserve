import re
from sqlalchemy.orm import Session

from core.models.db_base import engine
from core.models.db_code_value_set import CodeSet
from core.models.db_code_value import CodeValue
from core.dbutils.db_get_or_create import db_get_or_create
from core.dbutils.db_utils import convert_to_key


def SU_codevalues_cs54():
    """ Codeset 54: Units of Measure """

    # format: (display, description)
    code_values = (
        ('ohm', 'ohm'),
        ('ampere', 'ampere'),
        ('mC', 'millicoulomb'),
        ('g/mol', 'gram(s) per mole EXT'),
        ('mg/L FEU', 'milligram per litre fibrinogen equivalent unit EXT'),
        ('mmol/mol', 'millimole per mole EXT'),
        ('mmol/vol', 'millimoles per volume EXT'),
        ('pmol/(8 x10*8 RBC)', 'picomole per 8 times 10 to the power of 8 red blood cell EXT'),
        ('ug/s', 'microgram per second (Lab) EXT'),
        ('umol/mol', 'micromole per mole (Lab) EXT'),
        ('AI', 'Avidity Index for Ab measurements (Lab) EXT'),
        ('cmH2O/min', 'centimetre of water per minute'),
        ('mmol/s', 'millimole/seconds'),
        ('rpm', 'Revolutions/minute'),
        ('uW/cm2/nm', 'Micro-watts/centimeter squared/nanometer'),
        ('tab/cap', 'tablet/capsule'),
        ('dollars/day', 'Dollars/day'),
        ('dollars/h', 'Dollars/hour'),
        ('dollars/min', 'Dollars/minute'),
        ('dollars/month', 'Dollars/month'),
        ('dollars/sec', 'Dollars/second'),
        ('dollars/unit', 'Dollars/unit'),
        ('dollars/week', 'Dollars/week'),
        ('dollars/year', 'Dollars/year'),
        ('% NaCl', 'percent sodium chloride'),
        ('1/2 day', '1/2 Day'),
        ('absorbency', 'absorbency'),
        ('ACE Units', 'Angiotensin converting enzyme units'),
        ('ampoule', 'ampoule'),
        ('Angstrom', 'Angstrom'),
        ('APL unit/mL', 'Arbitrary units of IgA isotype for phospholipid antigens/mil'),
        ('application', 'application'),
        ('APS unit/mL', 'Arbitrary units of IgA isotype for phosphatidylserine antibo'),
        ('AUC (CARBOplatin)', 'area under the curve (CARBOplatin)'),
        ('AU/mL', 'Arbitrary units/milliliter'),
        ('bag', 'bag'),
        ('bands', 'Bands'),
        ('bar', 'bar'),
        ('bases', 'Bases'),
        ('bead', 'Bead'),
        ('blister', 'Blister'),
        ('block', 'block'),
        ('bolus', 'bolus'),
        ('bottle', 'bottle'),
        ('box', 'box'),
        ('bpm', 'beat/minute'),
        ('br/min', 'breath/minute'),
        ('Bethesda unit', 'Bethesda unit'),
        ('cal/oz', 'cal/oz'),
        ('can', 'can'),
        ('canister', 'canister'),
        ('cap', 'capsule'),
        ('cartridge', 'cartridge'),
        ('carton', 'carton'),
        ('case', 'case'),
        ('cassette', 'cassette'),
        ('casts', 'Casts'),
        ('cells', 'Cells'),
        ('cells/mcL', 'Cells/microliter'),
        ('cg', 'centigram'),
        ('cL', 'Centiliter'),
        ('cM', 'Centimorgan'),
        ('CFU/mL', 'colony forming unit/millilitre'),
        ('cGy', 'Centigray'),
        ('cm', 'centimetre'),
        ('cm2', 'Square centimeter'),
        ('cm3', 'Cubic centimeter'),
        ('cmH2O', 'centimetre of water'),
        ('cm H2O/L/sec', 'centimetre of water/litre/second'),
        ('cm/sec', 'Centimeter/second'),
        ('cm/sec/sec', 'Centimeter/second/second'),
        ('container', 'container'),
        ('cP units', 'Centipoise units'),
        ('copies/mL', 'copies/millilitre'),
        ('cylinder', 'cylinder'),
        ('Da', 'Dalton'),
        ('day', 'day'),
        ('dB', 'decibel'),
        ('DegC', 'degree Celsius'),
        ('DegF', 'degree Fahrenheit'),
        ('degree', 'degree'),
        ('Delta G', 'Delta G (DG), the Gibbs free energy of transfer'),
        ('delta OD', 'Delta optical density'),
        ('dgm', 'Decigram'),
        ('disc', 'disc'),
        ('dL', 'decilitre'),
        ('dL/day', 'Deciliter/day'),
        ('dL/h', 'Deciliter/hour'),
        ('dL/min', 'Deciliter/minute'),
        ('dm', 'Decimeter'),
        ('dm2', 'Square decimeter'),
        ('dollars', 'Dollars'),
        ('doses or times', 'doses or times'),
        ('dpm', 'Disintegrations/minute'),
        ('drop', 'drop'),
        ('drops/kg', 'Drops/kilogram'),
        ('dyne-sec/cm5', 'dyne-second/centimetre5'),
        ('dyne-sec/cm5/m2', 'dyne-second/centimetre5/metre squared'),
        ('each', 'each'),
        ('EI unit', 'Enzyme Immunoassay unit'),
        ('EU', 'enzyme-linked immunosorbent assay unit'),
        ('ET unit/mL', 'Endotoxin units/milliliter'),
        ('Ehrlich unit/24 h', 'Ehrlich unit/24 hour'),
        ('euros', 'Euros'),
        ('film', 'Film'),
        ('fL', 'femtolitre'),
        ('fl oz', 'Fluid ounce'),
        ('French', 'French'),
        ('ft', 'foot'),
        ('ft2', 'Square foot'),
        ('g/EA', 'Gram/each'),
        ('g/kg', 'gram/kilogram'),
        ('g/kg/day', 'Gram/kilogram/day'),
        ('g/kg/h', 'Grams/kilogram/hour'),
        ('g/kg/min', 'Gram/kilogram/minute'),
        ('g/m2', 'gram/metre squared'),
        ('gallon', 'gallon'),
        ('gauge', 'gauge'),
        ('g', 'gram'),
        ('g/24h', 'Grams/24 hours'),
        ('g/5h', 'Grams/5 hours'),
        ('g/day', 'gram/day'),
        ('g/dL', 'Grams/deciliter'),
        ('g/h', 'gram/hour'),
        ('g/L', 'gram/litre'),
        ('g/min', 'Grams/minute'),
        ('g/mL', 'gram/millilitre'),
        ('g/210 L', 'Grams/210 liters'),
        ('g/g Cr', 'Grams/gram of creatinine'),
        ('g-m', 'Gram-meter'),
        ('g-m/beat', 'Gram-meter/beat'),
        ('g-m/beat/m2', 'Gram-meter/beat/square meter'),
        ('g-m/m2', 'Gram-meter/square meter'),
        ('g-m/m2/beat', 'Gram-meter/square meter/beat'),
        ('g/spec', 'Grams/specimen'),
        ('GPL units', 'Arbitrary units of IgG isotype for phospholipid antigens'),
        ('GPL-U/mL', 'IgG anti-cardiolipin unit/millilitre'),
        ('gum', 'gum'),
        ('Hz', 'hertz'),
        ('hour', 'hour'),
        ('per HPF', 'per high power field'),
        ('implant', 'implant'),
        ('in2', 'Square inch'),
        ('in', 'Inch'),
        ('inh', 'Inhalation'),
        ('inhaler', 'inhaler'),
        ('inhaler_refill', 'Inhaler Refill'),
        ('insert', 'Insert'),
        ('IU', 'international unit'),
        ('IntlUnit/dL', 'International Unit/Decilitre'),
        ('IntlUnit/EA', 'International Unit/Each'),
        ('IntlUnit/g', 'International Unit/Gram'),
        ('IntlUnit/h', 'International Unit/Hour'),
        ('IU/L', 'international unit/litre'),
        ('IU/mL', 'international unit/millilitre'),
        ('IntlUnit/day', 'International Unit/Day'),
        ('IU/g Hb', 'international unit/gram hemoglobin'),
        ('IntlUnit/kg', 'International Unit/Kilogram'),
        ('IntlUnit/kg/day', 'International Unit/Kilogram/Day'),
        ('IntlUnit/kg/h', 'International Unit/Kilogram/Hour'),
        ('IntlUnit/kg/min', 'International Unit/Kilogram/Minute'),
        ('IntlUnit/m2', 'International Unit/Square Meter'),
        ('IntlUnit/m2/day', 'International Unit/Square Meter/Day'),
        ('IntlUnit/min', 'International Unit/Minute'),
        ('IV_bag', 'intravenous_bag'),
        ('kcal', 'kilocalorie'),
        ('kcal/day', 'kilocalorie/day'),
        ('kcal/dL', 'kilocalorie/decilitre'),
        ('kcal/g', 'kilocalorie/gram'),
        ('kcal/h', 'kilocalorie/hour'),
        ('kcal/kg', 'kilocalorie/kilogram'),
        ('kcal/kg/day', 'kilocalorie/kilogram/day'),
        ('kcal/kg/h', 'kilocalorie/kilogram/hour'),
        ('kcal/kg/min', 'kilocalorie/kilogram/minute'),
        ('kcal/L', 'kilocalorie/litre'),
        ('kcal/min', 'kilocalorie/minute'),
        ('kcal/mL', 'kilocalorie/millilitre'),
        ('kcal/oz', 'kilocalorie/ounce'),
        ('kcal/tbsp', 'kilocalorie/tablespoon'),
        ('kcal/total kcal', 'kilocalorie/total kilocalorie'),
        ('kcal/tsp', 'kilocalorie/teaspoon'),
        ('Kelvin', 'Kelvin'),
        ('kg', 'kilogram'),
        ('kg/day', 'kilogram/day'),
        ('kg/h', 'kilogram/hour'),
        ('kg/m3', 'kilogram/cubic metre'),
        ('kg/min', 'kilogram/minute'),
        ('kg/s', 'kilogram/second'),
        ('kg-m', 'Kilogram-meter'),
        ('kg-m/m2', 'Kilogram-meter/square meter'),
        ('kg/m2', 'kilogram/metre squared'),
        ('kb', 'Kilobase'),
        ('kb pairs', 'Kilobase pairs'),
        ('kd', 'Kilodalton'),
        ('kit', 'kit'),
        ('K.I.U.', 'Kallikrein inhibitory units'),
        ('K.I.U./mL', 'Kallikrein inhibitory units/milliliter'),
        ('kJoule', 'Kilojoules'),
        ('kPa', 'Kilopascal'),
        ('kU/L', 'kilounit/litre'),
        ('L', 'litre'),
        ('L/24 h', 'litre/24 hour'),
        ('L/day', 'litre/day'),
        ('L/h', 'litre/hour'),
        ('L/min', 'litre/minute'),
        ('L/min/m2', 'litre/minute/metre squared'),
        ('L/sec', 'Liters/second'),
        ('lb', 'pound'),
        ('L/kg', 'Liters/kilogram'),
        ('log 10', 'Log base 10'),
        ('log copies/mL', 'Log copies/milliliter'),
        ('log10 IU/mL', 'log base 10 international unit/millilitre'),
        ('lozenge', 'lozenge'),
        ('per LPF', 'per low power field'),
        ('m', 'metre'),
        ('m2', 'metre squared'),
        ('m2/hr', 'square meter per hour'),
        ('m2/min', 'square meters per minute'),
        ('m2/day', 'metre squared/day'),
        ('m3', 'Cubic meter'),
        ('m3/sec', 'Cubic meter/second'),
        ('mA', 'milliampere'),
        ('MBq', 'megabecquerel'),
        ('mcEq/L', 'Microequivalents/liter'),
        ('mcg', 'microgram'),
        ('mcg/24h', 'Micrograms/24 hours'),
        ('mcg/day', 'microgram/day'),
        ('mcg/dL', 'Micrograms/deciliter'),
        ('mcg/EA', 'Micrograms/each'),
        ('mcg/g', 'Micrograms/gram'),
        ('mcg/kg', 'microgram/kilogram'),
        ('mcg/kg/day', 'Micrograms/kilogram/day'),
        ('mcg/kg/min', 'microgram/kilogram/minute'),
        ('ug/L', 'microgram/litre'),
        ('mcg/m2', 'microgram/metre squared'),
        ('mcg/m2/h', 'microgram/metre squared/hour'),
        ('mcg/mg', 'Micrograms/milligram'),
        ('mcg/min', 'microgram/minute'),
        ('mcg/mL FEU', 'microgram/millilitre fibrinogen equivalent unit'),
        ('mcg Eq/mL', 'Microgram equivalents/milliliter'),
        ('mcg/g Cr', 'Micrograms/gram creatinine'),
        ('mcg/g dry wt', 'Micrograms/gram dry weight'),
        ('mcg/g Hb', 'Micrograms/gram hemoglobin'),
        ('mcg/kg/h', 'microgram/kilogram/hour'),
        ('mcg/m2/day', 'microgram/meter squared/day'),
        ('mcg/mg Cr', 'Micrograms/milligram creatinine'),
        ('mcg N/dL', 'Micrograms nitrogen/deciliter'),
        ('mcg/spec', 'Micrograms/specimen'),
        ('mcg T4/dL', 'Micrograms T4 (thyroxine)/deciliter'),
        ('mcIU/mL', 'Micro International Units/Milliliter'),
        ('uL', 'microlitre'),
        ('mcmol', 'micromole'),
        ('umol/day', 'micromole/day'),
        ('mcmol/dL', 'Micromoles/Deciliter'),
        ('mcmol/g', 'Micromoles/gram'),
        ('mcmol/mL', 'Micromoles/Milliliter'),
        ('mcmol/mol', 'Micromoles/Mole'),
        ('umol/g creatinine', 'micromole/gram creatinine'),
        ('mcmol/g/yr', 'Micromoles/gram/year'),
        ('microhm', 'microhm'),
        ('Microunit', 'Microunit'),
        ('Microunit/mL', 'Microunits/Milliliter'),
        ('mcV', 'microvolt'),
        ('Megabase', 'Megabase'),
        ('mEq', 'milliequivalent'),
        ('mEq/day', 'Milliequivalents/day'),
        ('mEq/dL', 'Milliequivalents/deciliter'),
        ('mEq/EA', 'Milliequivalent/each'),
        ('mEq/h', 'milliequivalent/hour'),
        ('mEq/kg/day', 'Milliequivalents/kilogram/day'),
        ('mEq/kg/h', 'milliequivalent/kilogram/hour'),
        ('mEq/kg/min', 'Milliequivalents/kilogram/minute'),
        ('mEq/L', 'Milliequivalents/liter'),
        ('mEq/min', 'milliequivalent/minute'),
        ('mEq/mL', 'milliequivalent/millilitre'),
        ('mEq/24 h', 'Milliequivalents/24 hours'),
        ('mEq/kg', 'milliequivalent/kilogram'),
        ('mEq/m2', 'milliequivalent/metre squared'),
        ('meter/sec', 'Meters/second'),
        ('mg', 'milligram'),
        ('mg/24h', 'Milligrams/24 hours'),
        ('mg/mL', 'milligram/millilitre'),
        ('mg/day', 'milligram/day'),
        ('mg/dL', 'Milligrams/deciliter'),
        ('mg/EA', 'Milligram/each'),
        ('mg/g', 'milligram/gram'),
        ('mg/h', 'milligram/hour'),
        ('mg/kg', 'milligram/kilogram'),
        ('mg/kg/min', 'milligram/kilogram/minute'),
        ('mg/L', 'milligram/litre'),
        ('mg/m2', 'milligram/metre squared'),
        ('mg/min', 'milligram/minute'),
        ('mg/mmol', 'Milligrams/millimole'),
        ('mg/2 h', 'Milligrams/2 hours'),
        ('mg/dL RBC', 'Milligrams/deciliter RBC'),
        ('mg/g Cr', 'Milligrams/gram creatinine'),
        ('mg Hb/gm', 'Milligrams hemoglobin/gram'),
        ('mg/kg/day', 'Milligrams/kilogram/day'),
        ('mg/kg/h', 'milligram/kilogram/hour'),
        ('mg-m/beat', 'Milligram-meter/beat'),
        ('mg/m2/day', 'milligram/metre squared/day'),
        ('mg/m2/h', 'Milligram/meter2/hour'),
        ('mg/mmol creatinine', 'milligram/millimole creatinine'),
        ('mg PE', 'Milligram Phenytoin Equivalents'),
        ('mg PE/kg/dose', 'Milligram Phenytoin Equivalents/kilogram/dose'),
        ('mg/spec', 'Milligrams/specimen'),
        ('miles', 'Miles'),
        ('million IU', 'million international unit'),
        ('millionunits/h', 'Million units/hour'),
        ('minute', 'minute'),
        ('mIU', 'Milli International Units'),
        ('mIU/h', 'Milli International Units/hour'),
        ('mIU/L', 'Milli International Units/liter'),
        ('mIU/mL', 'milli-international unit/millilitre'),
        ('mL', 'mL'),
        ('mL/beat', 'Milliliters/beat'),
        ('mL/cm H2O', 'millilitre/cm H2O'),
        ('mL/day', 'Milliliters/day'),
        ('mL/EA', 'Milliliter/each'),
        ('mL/h', 'millilitre/hour'),
        ('mL/kg', 'millilitre/kilogram'),
        ('mL/kg/day', 'millilitre/kilogram/day'),
        ('mL/kg/h', 'millilitre/kilogram/hour'),
        ('mL/L', 'millilitre/litre'),
        ('mL/m2/beat', 'Milliliters/square meter/beat'),
        ('mL/m2/min', 'Milliliter/square meter/minute'),
        ('mL/min', 'millilitre/minute'),
        ('mL/mL', 'Milliliters/milliliter of administered volume'),
        ('mL O2/dL blood', 'Milliliter of oxygen/deciliter of blood'),
        ('mL/kg/min', 'Milliliter/kilogram/minute'),
        ('mL/m2', 'millilitre/metre squared'),
        ('mL/m2/day', 'Milliliter/square meter/day'),
        ('mL/m2/h', 'Milliliter/square meter/hour'),
        ('mL/min/1.73 m2', 'millilitre/minute/1.73 metre squared'),
        ('mL/min/SA', 'Milliliters/minute/surface area'),
        ('mL/s', 'millilitre/second'),
        ('mm', 'millimetre'),
        ('mm/h', 'Millimeter/hour'),
        ('mm 1st HR', 'Millimeters 1st hour'),
        ('mm2', 'Square millimeter'),
        ('mm3', 'Cubic millimeter'),
        ('mm H2O', 'millimetre H2O'),
        ('mmHg', 'millimetre mercury'),
        ('mmol', 'millimole'),
        ('mmol/day', 'millimole/day'),
        ('mmol/dL', 'Millimoles/deciliter'),
        ('mmol/EA', 'Millimoles/each'),
        ('mmol/h', 'millimole/hour'),
        ('mmol/kg', 'millimole/kilogram'),
        ('mmol/kg/day', 'Millimoles/kilogram/day'),
        ('mmol/kg/h', 'Millimoles/kilogram/hour'),
        ('mmol/kg/min', 'Millimoles/kilogram/minute'),
        ('mmol/L', 'millimole/litre'),
        ('mmol/m2', 'millimole/metre squared'),
        ('mmol/min', 'Millimoles/minute'),
        ('mmol/mL', 'millimole/millilitre'),
        ('mmol/mmol', 'Millimoles/millimole'),
        ('mmol/spec', 'Millimoles/specimen'),
        ('mol', 'mole'),
        ('MoM', 'multiple of the median'),
        ('month', 'month'),
        ('mOsm', 'Milliosmoles'),
        ('mOsm/dL', 'Milliosmoles/deciliter'),
        ('mOsm/kg', 'milliosmole/kilogram'),
        ('mOsm/L', 'Milliosmoles/liter'),
        ('mOsm/mL', 'Milliosmoles/milliliter'),
        ('mOsm/kg H2O', 'Milliosmoles/kilogram H2O'),
        ('million PFU', 'million plaque forming unit'),
        ('MPL', 'Arbitrary units of IgM isotype for phospholipid antigens'),
        ('MPL-U/mL', 'IgM anti-cardiolipin unit/millilitre'),
        ('MPS unit/mL', 'Arbitrary units of IgM isotype for phosphatidylserine antige'),
        ('ms', 'millisecond'),
        ('million_unit', 'million unit'),
        ('millionunits/day', 'Million units/day'),
        ('millionunits/kg/dose', 'Million units/kilogram/dose'),
        ('milliunit/m2', 'million unit/metre squared/dose'),
        ('milliunit/g Hb', 'milliunit/gram hemoglobin'),
        ('milliunit/g protein', 'milliunit/gram protein'),
        ('milliunit', 'milliunit'),
        ('milliunit/day', 'milliunit/day'),
        ('milliunit/g', 'milliunit/gram'),
        ('milliunit/h', 'milliunit/hour'),
        ('milliunit/kg/day', 'milliunit/kilogram/day'),
        ('mU/L', 'milliunit/litre'),
        ('milliunit/min', 'milliunit/minute'),
        ('mU/mL', 'milliunit/millilitre'),
        ('milliunit/kg/dose', 'milliunit/kilogram/dose'),
        ('milliunit/kg/h', 'milliunit/kilogram/hour'),
        ('milliunit/kg/min', 'milliunit/kilogram/minute'),
        ('mV', 'millivolt'),
        ('nebule', 'nebule'),
        ('ng', 'nanogram'),
        ('ng/day', 'nanogram/day'),
        ('ng/dL', 'nanogram/decilitre'),
        ('ng/h', 'Nanogram/hour'),
        ('ng/kg/day', 'Nanogram/kilogram/day'),
        ('ng/kg/h', 'Nanogram/kilogram/hour'),
        ('ng/L', 'nanogram/litre'),
        ('ng/min', 'Nanograms/minute'),
        ('ng/mL', 'nanogram/millilitre'),
        ('ng/mL/h', 'Nanograms/milliliter/hour'),
        ('ng/24 h', 'nanogram/24 hour'),
        ('ng/g', 'Nanograms/gram'),
        ('ng/kg', 'nanogram/kilogram'),
        ('ng/kg/min', 'nanogram/kilogram/minute'),
        ('ng/m2/dose', 'Nanograms/square meter/dose'),
        ('ng/m2/day', 'Nanograms/square meter/day'),
        ('ng/m2/h', 'Nanograms/square meter/hour'),
        ('ng/m2/min', 'Nanograms/square meter/minute'),
        ('ng/mcL', 'Nanograms/microliter'),
        ('nm', 'Nanometers'),
        ('nmol', 'Nanomoles'),
        ('nmol/day', 'nanomole/day'),
        ('nmol/dL', 'Nanomoles/deciliter'),
        ('nmol/g', 'Nanomoles/gram'),
        ('nmol/h/mL', 'nanomole/hour/millilitre'),
        ('nmol/L', 'nanomole/litre'),
        ('nmol/mL', 'Nanomoles/milliliter'),
        ('nmol/mmol', 'Nanomoles/millimole'),
        ('nmol bone collagen equiv', 'Nanomoles bone collagen equivalents'),
        ('nmol/dL GF', 'Nanomoles/deciliter of glomerular filtrate'),
        ('nmol/h/mg', 'nanomole/hour/milligram'),
        ('nmol/mg Cr', 'Nanomoles/milligram creatinine'),
        ('nmol/mmol creatinine', 'nanomole/millimole creatinine'),
        ('ocular_system', 'ocular_system'),
        ('OD', 'Optical density'),
        ('oz', 'ounce'),
        ('packs', 'Packs'),
        ('package', 'package'),
        ('packet', 'packet'),
        ('pad', 'pad'),
        ('paper', 'paper'),
        ('patch', 'patch'),
        ('pacemaker bpm', 'pacemaker beat/minute'),
        ('pen', 'pen'),
        ('% bound', 'Percent bound'),
        ('% deficient', 'Percent deficient'),
        ('%', 'percent'),
        ('% excretion', 'Percent excretion'),
        ('% hemolysis', 'Percent hemolysis'),
        ('% index', 'Percent index'),
        ('% inhibition', 'Percent inhibition'),
        ('% live', 'Percent live'),
        ('% neg ctrl', 'Percent negative control'),
        ('% normal', 'Percent normal'),
        ('% precipitation', 'Percent precipitate'),
        ('% total', 'Percent total'),
        ('% vol', 'Percent volume'),
        ('per uL', 'per microlitre'),
        ('pg', 'picogram'),
        ('pg/dL', 'Picograms/deciliter'),
        ('pg/mL', 'picogram/millilitre'),
        ('pints', 'Pints'),
        ('pmol', 'Picomoles'),
        ('pmol/g', 'Picomole/Gram'),
        ('pmol/L', 'picomole/litre'),
        ('P N unit', 'Protein nitrogen unit'),
        ('pouch', 'pouch'),
        ('ppb', 'Parts/billion'),
        ('ppm', 'part/million'),
        ('protein/kg', 'Protein/kilogram'),
        ('puff', 'puff'),
        ('pump', 'pump'),
        ('quart', 'quart'),
        ('ratio', 'ratio'),
        ('ring', 'Ring'),
        ('sachet', 'sachet'),
        ('scoops', 'Scoops'),
        ('second', 'second'),
        ('serving/day', 'serving/day'),
        ('sponge', 'sponge'),
        ('spray', 'spray'),
        ('stick', 'stick'),
        ('stones', 'Stones'),
        ('strip', 'strip'),
        ('suppository', 'suppository'),
        ('swab', 'swab'),
        ('syringe', 'syringe'),
        ('tab', 'tablet'),
        ('tabminder', 'tabminder'),
        ('tampon', 'tampon'),
        ('tbsp', 'tablespoonfuls'),
        ('K/mcL', 'Thousand/microliter'),
        ('titre', 'titre'),
        ('torr', 'Torr'),
        ('Tot/Mech', 'Total/mechanical'),
        ('tray', 'tray'),
        ('troche', 'troche'),
        ('TSI index', 'thyroid-stimulating immunoglobulin index'),
        ('tsp', 'Teaspoonfuls'),
        ('tuberculin unit', 'tuberculin unit'),
        ('tube', 'tube'),
        ('unit/kg', 'unit/kilogram'),
        ('unit/mmol Cr', 'Unit/millimole creatinine'),
        ('mcg/h', 'mcg/hour'),
        ('mcg/mL', 'microgram/millilitre'),
        ('mcg/mmol cre', 'Micrograms/millimole creatinine'),
        ('mcg elastase/g', 'Micrograms elastase/gram'),
        ('mcmol/24h', 'Micromole/24 hours'),
        ('mcmol/hr/mL', 'Micromole/hour/millilitre'),
        ('umol/L', 'micromole/litre'),
        ('umol/mmol', 'micromole/millimole'),
        ('unit/2h', 'Unit/2hr'),
        ('U/day', 'unit/day'),
        ('unit/dL', 'Unit/Deciliter'),
        ('unit/g', 'unit/gram'),
        ('unit/kg/min', 'unit/kilogram/minute'),
        ('unit/L', 'unit/litre'),
        ('unit/m2/day', 'Units/square meter/day'),
        ('unit/m3', 'Unit/cubic meter'),
        ('unit/min', 'unit/minute'),
        ('unit/mL', 'unit per millilitre'),
        ('unit/10^10', 'Units/10000000000'),
        ('unit/10^10 cells', 'Units/10000000000 cells'),
        ('unit/g Hb', 'Units/gram hemoglobin'),
        ('unit/g P', 'Units/gram protein'),
        ('unit/h', 'unit/hour'),
        ('unit/kg/day', 'Unit/kilogram/day'),
        ('unit/kg/h', 'unit/kilogram/hour'),
        ('unit/m2', 'unit/metre squared'),
        ('U/mL RBC', 'unit/millilitre red blood cell'),
        ('unit', 'unit'),
        ('unit/EA', 'Units/each'),
        ('unknown unit', 'Unknown unit'),
        ('vial', 'vial'),
        ('visit', 'visit'),
        ('wafer', 'wafer'),
        ('WBC', 'white blood cell'),
        ('week', 'week'),
        ('x10^3/mcL', 'X 1000/microliter'),
        ('x10^6/mcL', 'X 1000000/microliter'),
        ('x10^9/L', 'times 10 to the power of 9/litre'),
        ('x10^12/L', 'times 10 to the power of 12/litre'),
        ('x10^6/mL', 'times 10 to the power of 6/millilitre'),
        ('year', 'year'),
        ('BA', 'Bale'),
        ('dozen', 'dozen'),
        ('4F', '100 - Pack'),
        ('jar', 'jar'),
        ('RM', 'Ream'),
        ('BD', 'Bundle'),
        ('HU', 'Hundred'),
        ('PC', 'Piece'),
        ('RA', 'Rack'),
        ('pail', 'pail'),
        ('PL', 'Pallet'),
        ('RD', 'Rod'),
        ('SP', 'Shelf Package'),
        ('TH', 'Thousand'),
        ('TP', 'Ten Pack'),
        ('TK', 'Tank'),
        ('DR', 'Drum'),
        ('SL', 'Sleeve'),
        ('SY', 'Square Yard'),
        ('P5', 'Five Pack'),
        ('sheet', 'sheet'),
        ('YD', 'Yard'),
        ('BC', 'Bucket'),
        ('set', 'set'),
        ('LO', 'Lot'),
        ('book', 'book'),
        ('CY', 'Cubic Yard'),
        ('gross', 'gross'),
        ('card', 'card'),
        ('CF', 'Cubic Feet'),
        ('DAP mcGy m2', 'dose area product in microgray metre squared'),
        ('dps', 'disintegration/second'),
        ('km/h', 'kilometre/hour'),
        ('L O2/L blood', 'litre oxygen/litre blood'),
        ('mAs', 'milliampere second'),
        ('mcSv', 'microsievert'),
        ('minim', 'minim'),
        ('mL/s/1.73 m2', 'millilitre/second/1.73 metre squared'),
        ('MPU', 'standard IgM anti-cardiolipin unit'),
        ('mSv', 'millisievert'),
        ('mW', 'MilliWatts'),
        ('nm/L', 'nanometre/litre'),
        ('ng/L/s', 'nanogram/litre/second'),
        ('nmol/mg/h', 'nanomole/milligram/hour'),
        ('polyamp', 'polyamp'),
        ('psi', 'pound/square inch'),
        ('SI unit', 'International System of Units'),
        ('SMU', 'standard IgM beta-2 glycoprotein unit'),
        ('U/h/mg protein', 'unit/hour/milligram protein'),
        ('ug/g stool', 'microgram/gram stool'),
        ('ug/mL', 'microgram/millilitre (Lab)'),
        ('umol/g Hb', 'micromole/gram hemoglobin'),
        ('umol/mmol creatinine', 'micromole/millimole creatinine'),
        ('US - thermal index in bone (TIB)', 'ultrasound - thermal index in bone'),
        ('wipe', 'wipe'),
        ('x10^6/L', 'times 10 to the power of 6/litre'),
        ('count', 'count'),
        ('DAP cGy cm2', 'dose area product in centigray centimetre squared'),
        ('DAP dGy cm2', 'dose area product in decigray centimetre squared'),
        ('nmol/g dry weight', 'nanomole/gram dry weight'),
        ('nmol/min/mg', 'nanomole/minute/milligram'),
        ('nmol/min/mg protein', 'nanomole/minute/milligram protein'),
        ('pmol/h/spot', 'picomole/hour/spot'),
        ('Sv', 'sievert'),
        ('umol/collection', 'micromole/collection'),
        ('umol/h/mg protein', 'micromole/hour/milligram protein'),
        ('U/L', 'unit/litre (Lab)'),
        ('x10^9', 'times 10 to the power of 9'),
        ('per uL fluid', 'per microlitre fluid'),
        ('pmol/h/uL', 'picomole/hour/microlitre'),
        ('proliferation count', 'proliferation count'),
        ('RU/mL', 'relative unit/millilitre'),
        ('sack', 'sack'),
        ('SGU', 'standard IgG beta-2 glycoprotein unit'),
        ('Sv/h', 'sievert/hour'),
        ('ug/L FEU', 'microgram/litre fibrinogen equivalent unit'),
        ('US - thermal index in soft tissue (TI)', 'ultrasound - thermal index'),
        ('U/mL', 'unit/millilitre (Lab)'),
        ('CTDIw/vol', 'computed tomography dose index, weighted or volume'),
        ('DAP Gy cm2', 'dose area product in gray centimetre squared'),
        ('AK mGy', 'cumulative air kerma in milligray'),
        ('activity', 'activity'),
        ('Lyme_index_value', 'Lyme index value'),
        ('x10^6/kg', 'million per kilogram'),
        ('x10^8/kg', '100 million per kilogram'),
        ('log IU', 'log (base 10) international units'),
        ('umol/mol creatinine', 'micromole/mole creatinine'),
        ('ng(FEU)/mL', 'nanogram fibrinogen equivalent unit per milliliter'),
        ('PRU', 'peripheral vascular resistance unit'),
        ('source measurement unit', 'source measurement unit'),
        ('% risk', 'percent risk'),
        ('mcmol ZPP/mol Hb', 'micromole zinc protoporphyrin per mole hemoglobin'),
        ('mmol/mol creatinine', 'millimole/mole creatinine'),
        ('keU/L', 'kilo enzyme unit per liter'),
        ('mcmol/min/g protein', 'micromole per min per gram protein'),
        ('mg/mg Cr', 'milligram per milligram of creatinine'),
        ('SAU', 'standard Iga beta-2 glycoprotein units'),
        ('specific gravity unit', 'specific gravity unit'),
        ('AU', 'arbitrary unit'),
        ('ARU', 'aspirin response unit'),
        ('cells/mL', 'cells per milliliter'),
        ('Ehrlich unit/dL', 'Ehrlich unit/decilitre'),
        ('% available', 'percent of available'),
        ('/100(WBCs)', 'per 100 white blood cells'),
        ('mL/dL', 'millitier per decilieter'),
        ('mU/g Hb', 'milli enzyme unit per gram of hemoglobin'),
        ('P4', 'Four-pack'),
        ('roll', 'roll'),
        ('pair', 'pair'),
        ('DB Hl', 'decibel Hearing level'),
        ('daPA', 'Decapascal'),
        ('nmol/h/mg protein', 'nanomole/hour/milligram protein'),
        ('nmol1/2Cys/mg protein', 'nanomole one half cysteine/milligram protein'),
        ('per min', 'per minute'),
        ('per min/mg', 'per minute/milligram'),
        ('seed', 'seed'),
        ('umol/g dry weight', 'micromole/gram dry weight'),
        ('US - mechanical index (MI)', 'ultrasound - mechanical index'),
        ('US - thermal index in soft tissue (TIS)', 'ultrasound - thermal index in soft tissue'),
        ('x10^6/g', 'times 10 to the power of 6/gram'),
        ('% of lymph', 'percent of lymphocytes'),
        ('bolt', 'bolt'),
        ('nmol/min/mL plasma', 'nanomole/minute/millilitre plasma'),
        ('per mL', 'per millilitre'),
        ('ug/min', 'microgram/minute'),
        ('x10^3/L', 'times 10 to the power of 3/litre'),
        ('x10^6', 'times 10 to the power of 6'),
        ('AK Gy', 'cumulative air kerma in gray'),
        ('enema', 'enema'),
        ('envelope', 'envelope'),
        ('FL min:sec', 'fluoroscopic time in minute:second'),
        ('g/mol creatinine', 'gram/mole creatinine'),
        ('GBq', 'gigabecquerel'),
        ('GPU', 'standard IgG anti-cardiolipin unit'),
        ('h:min', 'hour:minute'),
        ('jug', 'jug'),
        ('kIU/L', 'kilointernational unit/litre'),
        ('mcg/m2/min', 'microgram/metre squared/minute'),
        ('mcSv/min', 'microsievert/minute'),
        ('mg/g wet weight', 'milligram/gram wet weight'),
        ('mL fetal blood', 'millilitre fetal blood'),
        ('mL whole blood', 'millilitre whole blood'),
        ('J', 'joule'),
        ('dyne/cm2', 'dyne/square centimetre'),
        ('s/co', '(s_co_ratio)'),
        ('copies/mcg', 'copies per microgrram'),
        ('EV', 'EIA value'),
        ('events', 'events'),
        ('fL/nL', 'femtoliter per nanoliter'),
        ('index', 'index'),
        ('mcmol/hr/g', 'micromole per hour per gram'),
        ('mg(Phenylketones)/dL', 'milligram phenylketones per deciliiter'),
        ('nmol/g Cr', 'nanomole per gram of creatinine'),
        ('CGG repeats', 'number of repeat motifs'),
        ('ISR', 'Immune Status Ratio'),
        ('unit/mL WB', 'Units/milli WB'),
        ('CAE units', 'complement activation enzyme immunoassay unit'),
        ('x10^6 (Specimen)', 'MillionPerSpecimen [Unity]'),
        ('4E', '20-Pack'),
        ('DP', 'Dozen Pair'),
        ('OP', 'Two Pack'),
        ('DLP', 'dose length product'),
        ('fraction', 'fraction'),
        ('kV', 'kilovolt'),
        ('kVp', 'kilovolt peak'),
        ('mcSv/h', 'microsievert/hour'),
        ('mg/m2/min', 'milligram/metre squared/minute'),
        ('mmol/mmol creatinine', 'millimole/millimole creatinine'),
        ('mSv/min', 'millisievert/minute'),
        ('ng/10 10', 'nanogram/10 to the power of 10'),
        ('Bq', 'becquerel'),
        ('FL sec', 'fluoroscopic time in second'),
        ('kBq', 'kilobecquerel'),
        ('MCF unit', 'Mean Channel Fluorescence unit'),
        ('mg Eq/L', 'milligram equivalent/litre'),
        ('mSv/h', 'millisievert/hour'),
        ('nmol PABA/min/mL', 'nanomole p-aminobenzoic acid/minute/millilitre'),
        ('applicatorful', 'applicatorful'),
        ('/HPF', 'per high power field'),
        ('L/L', 'Litre per Litre'),
        ('% of B Cell', 'Percent of B Cells'),
        ('% of NK Cell', 'Percent of Natural Killer Cells'),
        ('% of CD4+ T Cell', 'Percent of CD4 positive T Cells'),
        ('% of CD8+ T Cell', 'Percent of CD8 positive T Cells'),
        ('umol/L Erc', 'micromole per litre erythrocyte'),
        ('/uL', 'per microlitre'),
        ('CAE UNIT', 'complement activation enzyme immunoassay unit'),
        ('CAST/LPF', 'cast per low power field'),
        ('Colonies', 'Colonies'),
        ('copie/mL', 'copie per millilitre'),
        ('copy/mL', 'copy per millilitre'),
        ('B.U.', 'bethesda unit'),
        ('E.U.', 'enzyme-linked immunosorbent assay unit'),
        ('EPI/HPF', 'epithelial cells per high power field'),
        ('g/d', 'gram/day'),
        ('grams', 'grams'),
        ('IU/gHb', 'international unit/gram hemoglobin'),
        ('MCFUnits', 'Mean Channel Fluorescence unit'),
        ('mega CFU/L', 'mega CFU/L'),
        ('mg/Eq/L', 'milligram equivalent/litre'),
        ('min', 'minute'),
        ('Minutes', 'Minutes'),
        ('mL/min/M', 'mL/min/M'),
        ('mm Hg', 'mm Hg'),
        ('mm/hr', 'mm/hr'),
        ('mmol/Cre', 'mmol/Cre'),
        ('RBC/HPF', 'red blood cells per high power field'),
        ('RECOVERY', 'RECOVERY'),
        ('sec', 'second'),
        ('Titer', 'Titer'),
        ('U', 'Unit'),
        ('ug FEU/L', 'ug FEU/L'),
        ('ug/g', 'microgram/gram'),
        ('uM/kg/d', 'uM/kg/d'),
        ('umol/Cre', 'umol/Cre'),
        ('UNITS', 'units'),
        ('WBC/HPF', 'white blood cell per high power field'),
        ('x10^6 CFU/L', 'x10^6 CFU/L'),
        ('x10', 'x10'),
        ('/100{WBC}', '/100{WBC}'),
        ('/mL', '/mL'),
        ("[GPL'U]", "[GPL'U]"),
        ('[IU]/g{Hgb}', '[IU]/g{Hgb}'),
        ("[MPL'U]", "[MPL'U]"),
        ('{yy/mm/dd}', '{yy/mm/dd}'),
        ('10*12/L', '10*12/L'),
        ('10*6/L', '10*6/L'),
        ('10*6/mL', '10*6/mL'),
        ('10*6{collection}', '10*6{collection}'),
        ('10*9/L', '10*9/L'),
        ('g{collection}', 'g{collection}'),
        ('g/12.h', 'g/12.h'),
        ('g/mmol', 'g/mmol'),
        ('h', 'h'),
        ('mg{collection}', 'mg{collection}'),
        ('mg/mmol{Creat}', 'mg/mmol{Creat}'),
        ('mL/min/1.73_m2', 'mL/min/1.73_m2'),
        ('mmol/12.h', 'mmol/12.h'),
        ('mmol{collection}', 'mmol{collection}'),
        ('mmol/mmol{Creat}', 'mmol/mmol{Creat}'),
        ('mosm/kg', 'mosm/kg'),
        ('nmol{collection}', 'nmol{collection}'),
        ('nmol/mmol{Creat}', 'nmol/mmol{Creat}'),
        ('s', 'seconds'),
        ('U/1.h', 'U/1.h'),
        ('ug/L{FEU}', 'ug/L{FEU}'),
        ('uL/L', 'uL/L'),
        ('umol/mmol{Creat}', 'umol/mmol{Creat}'),
        ('umol{Collection}', 'umol{Collection}'),
        ('/LPF', '/LPF'),
        ('10\S\9/L', '10\S\9/L'),
        ('10\S\6/L', '10\S\6/L'),
        ('% fetal cell', '% fetal cell'),
        ('A3/uL', 'A3 microliter'),
        ('cm H2O/L', 'centimetre of water/litre'),
        ('count/100mL', 'count per 100 mL'),
        ('ery/uL', 'erythrocytes per microliter'),
        ('Hg', 'mercury'),
        ('kUg/L', 'kilounit gram/litre'),
        ('mmHg X10', 'millimetre mercury X10'),
        ('mmol/kg/dose', 'millimoles/kilogram/dose'),
        ('nmol/L GF', 'nanomoles/lliter of glomerular filtrate'),
        ('nmol/min/g', 'nanomole/minute/gram'),
        ('unit/min/g', 'unit/minute/gram'),
        ('uM', 'uM'),
        ('nmol/g Hb/h', 'nanomole per gram hemoglobin per hour'),
        ('dec-%', 'decimal - percent'),
        ('X', 'X'),
        ('x10^9 (absolute)', 'times 10 to the power of 9 (absolute)'),
        ('10\S\12/L', '10\S\12/L'),
        ('Leu/uL', 'leukocytes per microliter'),
        ('L O2/L', 'liter of oxygen per liter'),
        ('umol/L/h', 'umol/L/h'),
    )
    with Session(engine) as session:
        for display, description in code_values:
            db_get_or_create(
                session,
                CodeValue,
                code_set = 54,
                definition = description,
                description = description,
                display = display,
                display_key = re.sub('[^0-9a-zA-Z]+', '', display).upper()  # remove non-alphanumeric characters
            )


if __name__ == '__main__':
    SU_codevalues_cs54()
