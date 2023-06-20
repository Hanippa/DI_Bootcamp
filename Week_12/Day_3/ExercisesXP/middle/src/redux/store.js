import { createStore, applyMiddleware} from 'redux';
import { reducer } from './reducer';
import thunk from 'redux-thunk'

const delay = (store) => (next) => (action) => {
    if (action.type === 'IncrementInDelay') {
        setTimeout(()=> {
            next(action)
        }, 1000)
    }else{
        next(action)
    }
}

const store = createStore(reducer, applyMiddleware(delay ,thunk));

export default store;