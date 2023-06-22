
import { connect } from "react-redux";
import { useParams } from "react-router-dom"
import { deletePost } from "../redux/actions";
import { useDispatch } from "react-redux";

const Post = (params) => {
    const dispatch = useDispatch()
    const { id } = useParams()



    const post = params.posts.find(post => post.id === id);
    const handleClick = () => {
        console.log('Deleting');
        params.delete(post.id)
    }
    return (
        post ?
        <div>
        <h1>{post.title}</h1>
        <p>{post.body}</p>
        <button onClick={handleClick}>Delete</button>
        </div>
        :
        <h1>Loading</h1>
    )
    
}
const mapStateToProps = (state) => {
    return { posts: state.posts };
    };
const mapDispatchToProps = (dispatch) => {
    return { delete: (id) => {dispatch(deletePost(id))}};
    };

export default connect(mapStateToProps , mapDispatchToProps)(Post)