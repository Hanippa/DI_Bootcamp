const initState = {users:[]};


export const reducer = (state= initState, action={}) => {

    switch (action.type) {
        case 'USERS':
            return {...state, users: action.payload.filter((item) =>
                item.name.toLowerCase().includes(action.inputSearch.toLowerCase())
            )}

        default:
            return {...state};
    }
};