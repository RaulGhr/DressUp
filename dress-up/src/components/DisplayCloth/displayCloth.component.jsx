import './displayCloth.style.scss';

const DisplayCloth = ({item,onClick}) => {
    // {id,imagine,nume,tip,loc} = cloth
    // console.log("CLOTH",cloth)

    const onClickHandler = () => {
        onClick(item);
    }

    return(
        <div className="cloth" onClick={onClickHandler}>
            <img src={("data:image/png;base64,"+item["imagine"])} alt="" />
            {/* <h4 >{item["nume"]}</h4> */}
        </div>
    )
}
export default DisplayCloth;