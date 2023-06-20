import { useSelector, useDispatch } from 'react-redux';
import { getUsers } from '../redux/actions';

const Users = props => {
    const users = useSelector((state) => state.users);
    const dispatch = useDispatch()

    const handleSearch = (e) => {
        dispatch(getUsers(e.target.value))
    };

    return (
        <div>
            <input
                type="text"
                onChange={handleSearch}
                placeholder="Search by name"
            />
            <div>
                {users.map((item) => (
                    <div key={item.id}>
                        <img src={`https://robohash.org/${item.id}`} alt='bot'/>
                        <h2>{item.name}</h2>
                        <p>{item.email}</p>
                    </div>
                    
                ))}
            </div>
        </div>
    );
}
export default Counter