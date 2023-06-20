export const getUsers = (inputSearch) => (dispatch) => {
    fetch('https://jsonplaceholder.typicode.com/users')
    .then(res => res.json())
    .then(data=> {
    dispatch({type:'USERS', payload:data, inputSearch})
    })
}