

const User = (props) => {
    return (
        <div>
             <img src={`https://robohash.org/${props.id}?size=150x150`} alt="Bot" width="150" height="150"/> 
            <h2>name : {props.name} </h2>
            <p>email : {props.email} </p>
        </div>
    )
}

export default User