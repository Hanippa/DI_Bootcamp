import { useContext } from 'react';
import { AppContext } from '../App';

const SubName = (props) => {
const {name , setName} = useContext(AppContext)
return (
    <h2>From sub: {name}</h2>
)
}
export default SubName