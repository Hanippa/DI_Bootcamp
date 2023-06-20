
import {useSelector, useDispatch } from 'react-redux';
import { INCREMENT, DECREMENT } from '../redux/actions';

const Counter = props => {
    const age = useSelector((state)=> state.age);
    const dispatch = useDispatch()
    const buttonStyle = {height: '1.5rem'}
    return (
        <div style={{display: 'flex', alignItems: 'center' ,gap: '1rem'}}>
            <button onClick={() => dispatch(INCREMENT())} style={buttonStyle}>+</button>
            <h1>{age}</h1>
            <button onClick={() => dispatch(DECREMENT())} style={buttonStyle}>-</button>
        </div>
    )
}
export default Counter