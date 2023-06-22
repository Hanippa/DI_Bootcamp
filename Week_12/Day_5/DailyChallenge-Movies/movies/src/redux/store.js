import { createStore, applyMiddleware} from 'redux';
import { reducer } from './reducer.js';


const store = createStore(reducer);

export default store;