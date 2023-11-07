import { createContext, useState, useEffect } from "react";

import { apiGetAllClothes } from "../utils/ApiCalls";





export const ClothesContext = createContext({
  setClothes: () => {},
  clothes: {},
});

export const ClothesProvider = ({ children }) => {
  const [clothes, setClothes] = useState({});

  const getClothesFromDB = async()=>{
    const clothesFromDb = await apiGetAllClothes();
    // console.log("CONTEXT-DB",clothesFromDb)
    setClothes(clothesFromDb);
  }

  useEffect(() => {
    getClothesFromDB();

  }, []);

  const value = {
    clothes,
    setClothes,
  };

//   console.log("CONTEXT",clothes)
  return (
    <ClothesContext.Provider value={value}>{children}</ClothesContext.Provider>
  );
};
