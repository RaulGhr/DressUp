import axios from "axios";

import { encodeImgToBase64String } from "./FilesUtils";

const baseURL = "http://192.168.1.128:5000/";

export const apiRemoveImgBackground = async (imagine) => {
  const encoded_img = await encodeImgToBase64String(imagine);

  // Request made to the backend api
  // Send formData object
  try {
    const res = await axios.post(baseURL + "removeBg", {
      imagine: encoded_img,
    });
    //   const imaginePrelucrata = "data:image/png;base64," + res.data.imagine;
    //   return imaginePrelucrata;
    // console.log(res.data);
    imagine = res.data.imagine
    const tipuri = res.data.tipuri
    return {imagine,tipuri};
  } catch (error) {
    console.log("EROARE API", error);
  }
};

export const apiSaveClothing = async (dict) => {

  try {
    const res = await axios.post(baseURL + "clothing", dict);

    console.log("salvare reusita");
  } catch (error) {
    console.log("EROARE API", error);
  }
};

export const apiSaveOutfit = async (dict) => {

  try {
    const res = await axios.post(baseURL + "outfit", dict);

    console.log("salvare reusita");
  } catch (error) {
    console.log("EROARE API", error);
  }
};

export const apiGetAllClothes = async () =>{
  try {
    const res = await axios.get(baseURL + "getAllClothes");

    console.log("API",res.data.Clothing);
    return(res.data.Clothing);
  } catch (error) {
    console.log("EROARE API", error);
  }
};

export const apiGetAllOutfits = async () =>{
  try {
    const res = await axios.get(baseURL + "getAllOutfits");

    // console.log("API",res.data.Clothing);
    return(res.data.Outfits);
  } catch (error) {
    console.log("EROARE API", error);
  }
};

export const apiGetOutfitsTypes = async () => {
 
  try {
    const res = await axios.get(baseURL + "outfitTypes");
    const tipuri = res.data.tipuri
    console.log("API",res.data);
    return {tipuri};
  } catch (error) {
    console.log("EROARE API", error);
  }
};