const MovieList = () => {
    import {useSelector, useDispatch } from 'react-redux';
    import { showInfo } from '../redux/actions';
    const MovieList = props => {
        const list = useSelector(state=> state.list);
        const selected = useSelector(state=> state.selected);
        const dispatch = useDispatch();
        console.log(selected);
        
    
        const listStyle = {
            display:'flex', 
            gap:"1.5rem", 
            alignItems:'center', 
            justifyContent:'space-between'}
    
        const buttonStyle = {
            padding: '1rem', 
            height:'2rem', 
            display:'flex', 
            alignItems:'center', 
            borderRadius:'2rem', 
            backgroundColor:'#ffffff', 
            border:'none'}
    
        return (
            <div style={{display:'flex', gap:"10rem"}}>
                <div>
                    {
                        list.map((item, i)=>{
                            return (
                                <div key={i} style={listStyle}>
                                    <p>{item.title}</p>
                                    <button style={buttonStyle} onClick={() => dispatch(showInfo(item))}>show info</button>
                                </div>
                            )
                        })
                    }
                </div>
                <div style={{width:'25rem', marginTop:'5rem', }}>
                    <h2>Movie Information:</h2>
                    <p>title: {selected.title}</p>
                    <p>Release Date: {selected.releaseDate}</p>
                    <p>Rating: {selected.rating}</p>
                </div>
            </div>
        )
    }
    
    export default MovieList