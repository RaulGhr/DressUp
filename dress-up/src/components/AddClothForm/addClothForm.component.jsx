import { useState } from "react";
import { useNavigate } from 'react-router-dom';

import "./addClothForm.style.scss";

import { apiSaveClothing } from "../../utils/ApiCalls";

const formContentBluprint = { nume: null, tip: null, altTip: null, loc: null };

const AddClothForm = ({ tipuri, imaginePrelucrata }) => {
  const [formContent, setFormContent] = useState(formContentBluprint);
  const navigate = useNavigate();


  const onFormModify = (event) => {
    const { name, value } = event.target;
    setFormContent({ ...formContent, [name]: value });
  };

  const saveClothing = (event) => {
    event.preventDefault();

    var tip = formContent["tip"];
    if (formContent["tip"] == "Alt tip") {
      var tip = formContent["altTip"];
    } 
    const dict = {
    imagine: imaginePrelucrata,
    nume: formContent["nume"],
    loc: formContent["loc"],
    tip: tip,
    };
    console.log(dict);
    apiSaveClothing(dict);
    navigate('/addOutfit');
    
  };

  return (
    <form className="formular" onSubmit={saveClothing}>
      <input
        name="nume"
        type="text"
        placeholder="Nume"
        onChange={onFormModify}
        required
      />

      <select
        name="loc"
        id="lang"
        placeholder="Loc"
        onChange={onFormModify}
        required
      >
        <option value="" disabled selected>
          Loc
        </option>
        <option value="Head">Head</option>
        <option value="Upper">Upper Body</option>
        <option value="Lower">Lower Body</option>
        <option value="Shoes">Shoes</option>
      </select>

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
        {tipuri.map((tip) => (
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
        <i class="fa-solid fa-floppy-disk"></i>
        Save to Wardrobe
      </button>
    </form>
  );
};

export default AddClothForm;
