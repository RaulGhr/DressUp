import { Routes, Route } from 'react-router-dom';

import Navigation from "./routes/Navigation/navigation.component";
import AddClothes from "./routes/AddClothes/addClothes.component";
import AllClothes from './routes/AllClothes/allClothes.component';
import AddOutfit from './routes/AddOutfit/addOutfit.component';
import AllOutfits from './routes/AllOutfits/allOutfits.component';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigation />}>
        <Route index element={<AllOutfits />} />
        <Route path='addClothes' element={<AddClothes />} />
        <Route path='allClothes' element={<AllClothes />} />
        <Route path='addOutfit' element={<AddOutfit />} />
        {/* <Route path='allOutfits' element={<AllOutfits />} /> */}
      </Route>
    </Routes>
  );
};

export default App;
