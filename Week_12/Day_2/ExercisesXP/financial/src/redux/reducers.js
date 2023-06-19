

let initState
if (localStorage.getItem('transactions-storage')){
    initState = {transactions:JSON.parse(localStorage.getItem('transactions-storage')), currentIndex:-1};
}

else{
    initState = {transactions:[], currentIndex:-1};
}


export const reducer = (state= initState, action={}) => {
    console.log(state.transactions)
    const insert = (payload) => {
        const arr = [...state.transactions]
        arr.push(payload)
        return {...state, transactions:arr}
    }
    const deletes = (index) => {
        const arr = [...state.transactions]
        arr.splice(index, 1)
        localStorage.setItem('transactions-storage' , JSON.stringify(arr))
        return {...state, transactions:arr}
    }
    const update = (payload) => {
        const arr = [...state.transactions]
        arr[state.currentIndex] = payload
        return {...state, transactions:arr}
    }
    



    switch (action.type) {
        case 'INSERT':
            console.log(action.payload)
            return insert(action.payload)
        
        case 'UPDATE':
            return update(action.payload)

        case 'UPDATE-INDEX':
            return{...state, currentIndex: action.payload }

        case 'DELETE':
            return deletes(action.payload)

        default:
            return {...state};
    }
};