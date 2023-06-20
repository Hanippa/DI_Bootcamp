const initState = {
    count: 0
};

export const reducer = (state= initState, action={}) => {
    switch (action.type) {
        case 'counterIncrement':
            return{...state, count:state.count + 1}

        case 'counterDecrement':
            return{...state, count:state.count - 1}

        case 'IncrementIfOdd':
            const test = state.count % 2 !== 0 ? {...state, count:state.count + 1} : {...state}
            return test

        case 'IncrementInDelay':
            return{...state, count:state.count + 1}

        default:
            return {...state};
    }
};