
import {useSelector, useDispatch } from 'react-redux';
import { INCREMENT, DECREMENT, IncrementIfOdd, IncrementInDelay } from '../redux/actions';

const Counter = props => {
    const count = useSelector((state)=> state.count);
    const dispatch = useDispatch()
    const buttonStyle = {height: '1.5rem'}
    return (
        <div style={{display: 'flex', alignItems: 'center' ,gap: '1rem'}}>
            <button onClick={() => dispatch(INCREMENT())} style={buttonStyle}>+</button>
            <h1>{count}</h1>
            <button onClick={() => dispatch(DECREMENT())} style={buttonStyle}>-</button>
            <button onClick={() => dispatch(IncrementIfOdd())} style={buttonStyle}>if odd</button>
            <button onClick={() => dispatch(IncrementInDelay())} style={buttonStyle}>increment async</button>
        </div>
    )
}
export default Counter