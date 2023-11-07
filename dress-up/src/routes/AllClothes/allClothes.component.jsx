import { useContext } from "react";
import { ClothesContext } from "../../contexts/clothes.context";

import DisplayCloth from "../../components/DisplayCloth/displayCloth.component";

import "./allClothes.style.scss";

const AllClothes = () => {
  const { clothes } = useContext(ClothesContext);
  // console.log("allClothes",clothes)

  return (
    <div className="allClothes">
      {clothes &&
        Object.values(clothes).map((clothing) => (
          <DisplayCloth key={clothing.id} item={clothing} />
        ))}
      {/* {console.log("allClothes",typeof(Object.values(clothes)),Object.values(clothes))} */}
    </div>
  );
};

export default AllClothes;
