import base64
from flask_restful import reqparse

import uuid

from RoutesBlueprint import my_blueprint

from dbModels import ClothesModel, db



@my_blueprint.route('/getAllClothes')
def getAllClothes():
    cls = ClothesModel.query.all()
    # cls = db.getAllClothes()
    cl_dict = {}
    # print("bau")
    for cl in cls:
        with open("./imageDB/" + cl.imagine, "rb") as img:
            img_string = base64.b64encode(img.read()).decode('utf-8')
        cl.imagine = img_string
        cl_dict[cl.id] = cl.toDictionar()

    # print(cl_dict)
    cl_dict_final = {}
    cl_dict_final["Clothing"] = cl_dict

    return cl_dict_final



saveClothing_post_args = reqparse.RequestParser()
saveClothing_post_args.add_argument("imagine", type=str, help="Base64 encoded img", required=True)
saveClothing_post_args.add_argument("nume", type=str, help="Nume", required=True)
saveClothing_post_args.add_argument("tip", type=str, help="Tip", required=True)
saveClothing_post_args.add_argument("loc", type=str, help="Loc", required=True)


@my_blueprint.route('/clothing', methods=['POST'])
def postCloth():
    args = saveClothing_post_args.parse_args()
    img_base64 = args['imagine']
    img_binary = base64.b64decode(img_base64)
    unique_filename = str(uuid.uuid4())
    unique_adress = "./imageDB/" + unique_filename + ".png"
    with open(unique_adress, "wb") as file:
        file.write(img_binary)

    cl = ClothesModel(unique_filename, args['nume'], args['tip'], args['loc'])
    db.session.add(cl)
    db.session.commit()

    return "Adaugat cu succes"


deleteClothing_args = reqparse.RequestParser()
deleteClothing_args.add_argument("id", type=int, help="id clothing")
deleteClothing_args.add_argument("tip", type=str, help="tip clothing", )


@my_blueprint.route('/clothing', methods=['DELETE'])
def deleteCloth():
    args = deleteClothing_args.parse_args()
    clothToDelete = None
    if args["id"]:
        idCloth = args["id"]
        clothToDelete = ClothesModel.query.get(idCloth)
        db.session.delete(clothToDelete)
    elif args["tip"]:
        tipCloth = args["tip"]
        clothToDelete = ClothesModel.query.filter(ClothesModel.tip == tipCloth).all()
        for c in clothToDelete:
            db.session.delete(c)

    if clothToDelete:

        db.session.commit()
        return "Stergere reusita"
    else:
        return "Nu s-a putut efectua stergerea"
