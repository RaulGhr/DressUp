from flask import Blueprint

my_blueprint = Blueprint('RoutesBlueprint', __name__)

# Importați și înregistrați rutele din clothesRoutes.py
from . import clothesRoutes
from . import outfitRoutes
from . import functionsRoutes