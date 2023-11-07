import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

import "./addOutfitForm.style.scss";
import { apiSaveOutfit, apiGetOutfitsTypes } from "../../utils/ApiCalls";

const formContentBluprint = { nume: null, tip: null, altTip: null };

const AddOutfitForm = ({outfitSelectat}) => {
  const [formContent, setFormContent] = useState(formContentBluprint);
  const [tipuriOutfit, setTipuriOutfit] = useState([]);

  const navigate = useNavigate();

  useEffect(() => {
    getOutfitTypesFromDB();
  }, []);

  const getOutfitTypesFromDB = async () => {
    await apiGetOutfitsTypes().then(({ tipuri }) => {
      setTipuriOutfit(tipuri);
      var a = 0;
      tipuri.map((tip) => a++);
      if (a == 0)
        setFormContent({
          ...formContent,
          tip: "Alt tip",
        });
    });
  };

  const onFormModify = (event) => {
    const { name, value } = event.target;
    setFormContent({ ...formContent, [name]: value });
  };

  const saveOutfit = (event) => {
    event.preventDefault();

    var tip = formContent.tip;
    if (formContent["tip"] == "Alt tip") tip = formContent["altTip"];
    var headId = null;
    var upperId = null;
    var lowerId = null;
    var shoesId = null;
    
    
    if (outfitSelectat.Head !== null) {
      headId = outfitSelectat.Head.id;
    }
    
    if (outfitSelectat.Upper !== null) {
      upperId = outfitSelectat.Upper.id;
    }
    if (outfitSelectat.Lower !== null) {
      lowerId = outfitSelectat.Lower.id;
    }
   
    if (outfitSelectat.Shoes !== null) {
      shoesId = outfitSelectat.Shoes.id;
    }

    var dict = {
      nume: formContent.nume,
      tip: tip,
      headId: headId,
      upperId: upperId,
      lowerId: lowerId,
      shoesId: shoesId,
    };

    apiSaveOutfit(dict);
    navigate("/");
  };

  return (
    <form className="addOutfitForm" onSubmit={saveOutfit}>
      <input
        name="nume"
        type="text"
        placeholder="Nume"
        onChange={onFormModify}
        required
      />

      <select
        name="tip"
        id="lang"
        placeholder="Tip"
        onChange={onFormModify}
        required
      >
        <option value="" disabled selected>
          Tip
        </option>
        {tipuriOutfit.map((tip) => (
          <option key={tip} value={tip}>
            {tip}
          </option>
        ))}

        <option value="Alt tip">Alt tip</option>
      </select>

      {formContent["tip"] === "Alt tip" && (
        <input
          type="text"
          placeholder="Creaza un nou tip"
          name="altTip"
          onChange={onFormModify}
          required
        />
      )}


      <button className="saveButton" type="submit">
        <i className="fa-solid fa-floppy-disk"></i>
        Save to Wardrobe
      </button>
    </form>
  );
};

export default AddOutfitForm;
