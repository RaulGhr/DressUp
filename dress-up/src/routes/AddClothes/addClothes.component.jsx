import React, { useState } from "react";


import {apiRemoveImgBackground, apiSaveClothing} from '../../utils/ApiCalls'
import shirt from "../../asset/shirt.svg";
import './addClothes.style.scss'

import AddClothForm from "../../components/AddClothForm/addClothForm.component";

// const formContentBluprint = { nume: null, tip: null, altTip: null, loc: null };

const AddClothes = () => {
  const [imaginePrelucrata, setImaginePrelucrata] = useState(null);
  const [isLoading, setLoading] = useState(false);
  // const [formContent, setFormContent] = useState(formContentBluprint);
  const [tipuriHaine, setTipuriHaine] = useState([]);

  const onFileChange = async (event) => {
    const imagineIncarcata = event.target.files[0];

    setImaginePrelucrata(null);
    setLoading(true);
    await apiRemoveImgBackground(imagineIncarcata).then(
      ({ imagine, tipuri }) => {
        setImaginePrelucrata(imagine);
        setTipuriHaine(tipuri);
      }
    );

    setLoading(false);
  };

  

  return (
    <div className="addClothes">

      <div className="images">
        <label className="custom-file-upload">
          <input type="file" onChange={onFileChange} />
          {/* {imaginePrelucrata == null && <i class="fa-solid fa-shirt" />} */}
          {imaginePrelucrata == null && (
            <img className="shirtImg" src={shirt} />
          )}
          {imaginePrelucrata == null && <h2>Upload a file</h2>}
          {imaginePrelucrata && (
            <img src={"data:image/png;base64," + imaginePrelucrata} />
          )}
        </label>
      </div>

      {isLoading != false && <h4 className="loading">Loading...</h4>}

      {imaginePrelucrata != null && (
        <AddClothForm tipuri={tipuriHaine} imaginePrelucrata={imaginePrelucrata}/>
      )}
    </div>
  );
};

export default AddClothes;
