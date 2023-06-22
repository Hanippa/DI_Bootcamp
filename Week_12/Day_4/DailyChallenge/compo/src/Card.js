

const Card = (props) => {
    return (
        <div className="card-container">
            <span>{props.icon}</span>
            <lable>{props.lable}</lable>
            <h1>{props.number}</h1>
        </div>
    )
}

export default Card