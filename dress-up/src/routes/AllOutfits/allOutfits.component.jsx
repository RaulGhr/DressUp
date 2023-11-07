import { useState, useEffect } from "react";
import "./allOutfits.style.scss";
import { apiGetAllOutfits } from "../../utils/ApiCalls";

import DisplayOutfit from "../../components/DisplayOutfit/displayOutfit.component";
import AddButton from "../../components/AddButton/addButton.component";

const AllOutfits = () => {
  const [outfitsList, setOutfitsList] = useState({});

  const getOutfitsFromDB = async () => {
    const outfitsFromDB = await apiGetAllOutfits();
    setOutfitsList(outfitsFromDB);
    console.log(outfitsList);
  };

  useEffect(() => {
    getOutfitsFromDB();
    const element = document.querySelector("#container");

    element.addEventListener('wheel', (event) => {
      event.preventDefault();

      element.scrollBy({
        left: event.deltaY < 0 ? -30 : 30,
    
  });
});
  }, []);
  return (
    <div className="allOutfits">
      <div className="outfitsContainer" id="container">
        {outfitsList &&
          Object.values(outfitsList).map((outfit) => (
            <DisplayOutfit key={outfit.id} item={outfit} />
          ))}
        <AddButton navigateTo="/addOutfit" clasaDimensiuni="addButtonDim" />
      </div>
    </div>
  );
};

export default AllOutfits;
