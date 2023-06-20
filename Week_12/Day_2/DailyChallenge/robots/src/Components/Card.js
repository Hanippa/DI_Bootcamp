const Card = (params) => {
    return (
        <div className="card-container"> 
            <img src={params.url} alt="robopic"/>
            <h1>{params.name}</h1>
            <h3>{params.email}</h3>
        </div>
    )
}

export default Card