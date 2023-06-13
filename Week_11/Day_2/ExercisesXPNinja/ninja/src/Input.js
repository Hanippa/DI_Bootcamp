const Input = (props) => {
    return (
        <>
        <label for={props.name}>{props.name}</label>
        <input id={props.name} type="text"/>
        
        </>
    )
}

export default Input