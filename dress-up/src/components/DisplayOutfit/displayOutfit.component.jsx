import './displayOutfit.style.scss';

const DisplayOutfit = ({item,onClick}) => {

    const onClickHandler = () => {
        // onClick(item);
    }

    return(
        <div className="displayOutfit" onClick={onClickHandler}>
            <img src={("data:image/png;base64,"+item["imagine"])} alt="" />
            <h4 >{item["nume"]}</h4>
        </div>
    )
}
export default DisplayOutfit;