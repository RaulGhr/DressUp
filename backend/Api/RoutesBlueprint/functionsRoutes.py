import base64
from flask_restful import reqparse
from sqlalchemy import distinct

from RoutesBlueprint import my_blueprint

from dbModels import ClothesModel, db
from bgRemover import removeBg

removeBg_post_args = reqparse.RequestParser()
removeBg_post_args.add_argument("imagine", type=str, help="Base64 encoded img", required=True)


@my_blueprint.route('/removeBg', methods=['POST'])
def postRemoveBg():
    args = removeBg_post_args.parse_args()

    img_base64 = args['imagine']
    img_binary = base64.b64decode(img_base64)
    # with open("compare.jpg", "wb") as file:
    #     file.write(img_binary)
    imagine_prelucarata = removeBg(img_binary)
    unique_types = db.session.query(distinct(ClothesModel.tip)).all()
    lista_tipuri = [tip for tip, in unique_types]

    return {
        "imagine": imagine_prelucarata,
        "tipuri": lista_tipuri
    }



