

let initState
if (localStorage.getItem('transactions-storage')){
    console.log(localStorage.getItem('transactions-storage'));
    initState = {transactions:JSON.parse(localStorage.getItem('transactions-storage')), currentIndex:-1};
}

else{
    initState = {transactions:[], currentIndex:-1};
}

export const reducer = (state= initState, action={}) => {

    const insert = (payload) => {
        const arr = [...state.transactions]
        arr.push(payload)
        return arr
    }
    const deletes = (index) => {
        const arr = [...state.transactions]
        arr.splice(index, 1)
        localStorage.setItem('transactions-storage' , JSON.stringify(arr))
        return arr
    }
    const update = (payload) => {
        const arr = [...state.transactions]
        arr[state.currentIndex] = payload
        return {state, transaction:arr}
    }
    



    switch (action.type) {
        



        case 'INSERT':
            return{...state, transactions:[...insert(action.payload)]}
        
        case 'UPDATE':
            return{...state, transactions:[...update(action.payload)]}

        case 'UPDATE-INDEX':
            return{...state, currentIndex: action.payload }

        case 'DELETE':
            return{...state, transactions:[...deletes(action.payload)]}

        default:
            return {...state};
    }
};