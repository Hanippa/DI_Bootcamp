import './Herocard.css';
const Herocard = (params) => {
    return (
        <div onClick={() => params.handleClick(params.name)} className="hero-card">
        <img src={params.img} alt="hero-image"/>
        <h3>name : {params.name}</h3>
        <h3>occupation : {params.occupation}</h3>
        </div>
    )
}

export default Herocard