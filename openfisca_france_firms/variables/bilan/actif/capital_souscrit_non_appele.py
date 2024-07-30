from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.variables import Variable
from openfisca_france_entreprises.entities import UniteLegale  # noqa F401


class capital_souscrit_non_appele_brut(Variable):
    cerfa_field = "AA"
    value_type = int
    unit = 'currency'
    entity = UniteLegale
    label = "Capital souscrit non appelé"
    definition_period = YEAR
