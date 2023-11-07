import { useNavigate } from 'react-router-dom';


import './addButton.style.scss';
import plus from "../../asset/plus.svg";

const AddButton = ({navigateTo, clasaDimensiuni}) => {
    const navigate = useNavigate()

    const onClickHandler = () => {
        navigate(navigateTo);
        console.log("pressed");
    }

    return(
        <div className={('addButton '+ clasaDimensiuni)} onClick={onClickHandler}>
            <img src={plus}/>
        </div>
    )
}

export default AddButton;