import base64
from flask_restful import reqparse
from PIL import Image
import uuid
from sqlalchemy import distinct

from RoutesBlueprint import my_blueprint

from dbModels import OutfitModel, db, ClothesModel
from imageMerger import mergeImg

# @my_blueprint.route('/getAllClothes')
# def getAllClothes():
#     cls = ClothesModel.query.all()
#     # cls = db.getAllClothes()
#     cl_dict = {}
#     # print("bau")
#     for cl in cls:
#         with open("./imageDB/" + cl.imagine, "rb") as img:
#             img_string = base64.b64encode(img.read()).decode('utf-8')
#         cl.imagine = img_string
#         cl_dict[cl.id] = cl.toDictionar()
#
#     # print(cl_dict)
#     cl_dict_final = {}
#     cl_dict_final["Clothing"] = cl_dict
#
#     return cl_dict_final

# id = db.Column(db.Integer, primary_key=True)
# imagine = db.Column(db.String(100), nullable=False)
# imagineRealitate = db.Column(db.String(100))
# nume = db.Column(db.String(50), nullable=False)
# tip = db.Column(db.String(20), nullable=False)
# headId = db.Column(db.Integer)
# upperId = db.Column(db.Integer)
# lowerId = db.Column(db.Integer)
# shoesId = db.Column(db.Integer)

saveOutfit_post_args = reqparse.RequestParser()
saveOutfit_post_args.add_argument("nume", type=str, help="Nume", required=True)
saveOutfit_post_args.add_argument("tip", type=str, help="Tip", required=True)
saveOutfit_post_args.add_argument("headId", type=int, help="headId")
saveOutfit_post_args.add_argument("upperId", type=int, help="upperId")
saveOutfit_post_args.add_argument("lowerId", type=int, help="lowerId")
saveOutfit_post_args.add_argument("shoesId", type=int, help="shoesId")


@my_blueprint.route('/outfit', methods=['POST'])
def postOutfit():
    args = saveOutfit_post_args.parse_args()

    images = []
    if args['headId']:
        images.append(Image.open("./imageDB/" + ClothesModel.query.get(args['headId']).imagine))
    if args['upperId']:
        images.append(Image.open("./imageDB/" + ClothesModel.query.get(args['upperId']).imagine))
    if args['lowerId']:
        images.append(Image.open("./imageDB/" + ClothesModel.query.get(args['lowerId']).imagine))
    if args['shoesId']:
        images.append(Image.open("./imageDB/" + ClothesModel.query.get(args['shoesId']).imagine))

    imagine = mergeImg(images)
    unique_filename = str(uuid.uuid4())
    unique_adress = "./imageDB/" + unique_filename + ".png"
    imagine.save(unique_adress, "PNG")

    imaigineRealitate = None
    outfit = OutfitModel(unique_filename, imaigineRealitate, args['nume'], args['tip'], args['headId'], args['upperId'],
                         args['lowerId'],
                         args['shoesId'])
    db.session.add(outfit)
    db.session.commit()

    return "Adaugat cu succes"


@my_blueprint.route('/getAllOutfits')
def getAllOutfits():
    outfits = OutfitModel.query.all()
    cl_dict = {}
    for cl in outfits:
        with open("./imageDB/" + cl.imagine + ".png", "rb") as img:
            img_string = base64.b64encode(img.read()).decode('utf-8')
        cl.imagine = img_string
        cl_dict[cl.id] = cl.toDictionar()

    cl_dict_final = {}
    cl_dict_final["Outfits"] = cl_dict

    return cl_dict_final


@my_blueprint.route('/outfitTypes', methods=['GET'])
def getOutfitTypes():
    unique_types = db.session.query(distinct(OutfitModel.tip)).all()
    lista_tipuri = [tip for tip, in unique_types]

    return {
        "tipuri": lista_tipuri
    }


deleteOutfit_args = reqparse.RequestParser()
deleteOutfit_args.add_argument("id", type=int, help="id outfit", )
deleteOutfit_args.add_argument("tip", type=str, help="tip outfit", )


@my_blueprint.route('/outfit', methods=['DELETE'])
def deleteOutfit():
    args = deleteOutfit_args.parse_args()

    outfitToDelete = None

    if args["id"]:
        idOutfit = args["id"]
        outfitToDelete = OutfitModel.query.get(idOutfit)
        db.session.delete(outfitToDelete)

    elif args["tip"]:
        tipOutfit = args["tip"]
        outfitToDelete = OutfitModel.query.filter(OutfitModel.tip == tipOutfit).all()
        for c in outfitToDelete:
            db.session.delete(c)

    if outfitToDelete:

        db.session.commit()
        return "Stergere reusita"
    else:
        return "Nu s-a putut efectua stergerea"
