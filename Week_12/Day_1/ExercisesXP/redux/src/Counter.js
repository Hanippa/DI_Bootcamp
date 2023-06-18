
import { plus, minus } from "./actions"
import {useSelector , useDispatch} from 'react-redux'


const Counter = props => {
    const count = useSelector((state) => state.count)
    const dispatch = useDispatch()
    return (
        <div>
        <button onClick={() =>dispatch(plus())}>+</button>
        <h1>{count}</h1>
        <button onClick={() =>dispatch(minus())}>-</button>
        </div>
    )
}

export default Counter