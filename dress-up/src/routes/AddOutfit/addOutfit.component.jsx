import { useState, useContext, useEffect } from "react";

import "./addOutfit.style.scss";
import { ClothesContext } from "../../contexts/clothes.context";

import cap from "../../asset/cap.svg";
import shirt from "../../asset/shirt.svg";
import pants from "../../asset/pants.svg";
import shoe from "../../asset/shoe.svg";

import DisplayCloth from "../../components/DisplayCloth/displayCloth.component";
import AddOutfitForm from "../../components/AddOutfitForm/addOutfitForm.component";
import AddButton from "../../components/AddButton/addButton.component";

const modelOutfit = {
  Head: null,
  Upper: null,
  Lower: null,
  Shoes: null,
};

const AddOutfit = () => {
  const { clothes } = useContext(ClothesContext);
  const [listaHaine, setListaHaine] = useState([]);
  const [outfitSelectat, setOutfitSelectat] = useState(modelOutfit);
  const [displayClothes, setDiplayClothes] = useState(false);
  const [displayForm, setDiplayForm] = useState(false);

  const clothesTypeSelector = (event) => {
    console.log(event);
    var listaNoua = [];
    Object.values(clothes).map((cl) => {
      if (cl.loc == event.target.id) listaNoua.push(cl);
    });
    setListaHaine(listaNoua);
    setDiplayClothes(true);
    setDiplayForm(false);
    // console.log(event.target.id);
    // console.log(listaNoua);
  };

  const clothClickedHandler = (cloth) => {
    setOutfitSelectat({
      ...outfitSelectat,
      [cloth["loc"]]: cloth,
    });
    // setDiplayClothes(false);
  };

  const displayFormHandler = () => {
    setDiplayClothes(false);
    setDiplayForm(true);
  };

  return (
    <div className="addOutfit">
      <div className="outfit">
        <div
          className="outfitComponent"
          id="Head"
          onClick={clothesTypeSelector}
        >
          {outfitSelectat.Head == null && (
            <img className="capImg" src={cap} id="Head" />
          )}
          {outfitSelectat.Head != null && (
            <img
              src={"data:image/png;base64," + outfitSelectat.Head.imagine}
              id="Head"
            />
          )}
        </div>
        <div
          className="outfitComponent"
          onClick={clothesTypeSelector}
          id="Upper"
        >
          {outfitSelectat.Upper == null && (
            <img className="shirtImg" src={shirt} id="Upper" />
          )}
          {outfitSelectat.Upper != null && (
            <img
              src={"data:image/png;base64," + outfitSelectat.Upper.imagine}
              id="Upper"
            />
          )}
        </div>
        <div
          className="outfitComponent"
          onClick={clothesTypeSelector}
          id="Lower"
        >
          {outfitSelectat.Lower == null && (
            <img className="pantsImg" src={pants} id="Lower" />
          )}
          {outfitSelectat.Lower != null && (
            <img
              src={"data:image/png;base64," + outfitSelectat.Lower.imagine}
              id="Lower"
            />
          )}
        </div>
        <div
          className="outfitComponent"
          onClick={clothesTypeSelector}
          id="Shoes"
        >
          {outfitSelectat.Shoes == null && (
            <img className="shoeImg" src={shoe} id="Shoes" />
          )}
          {outfitSelectat.Shoes != null && (
            <img
              src={"data:image/png;base64," + outfitSelectat.Shoes.imagine}
              id="Shoes"
            />
          )}
        </div>
        {!displayForm && (
          <button
            className="saveButton"
            type="submit"
            onClick={displayFormHandler}
          >
            <i className="fa-solid fa-floppy-disk"></i>
            Save
          </button>
        )}
      </div>

      {displayClothes && (
        <div className="clothes show">
          {listaHaine.map((cl) => (
            <DisplayCloth
              key={cl.id}
              item={cl}
              className="cloth"
              onClick={clothClickedHandler}
            />
          ))}
          <AddButton navigateTo='/addClothes'/>
        </div>
      )}

      {displayForm && (
        <div className="outfitForm">
          <AddOutfitForm outfitSelectat={outfitSelectat} />
        </div>
      )}
    </div>
  );
};

export default AddOutfit;
