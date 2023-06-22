import React from "react";
import logo from './blog.png';
import { connect } from "react-redux";
import Postcard from "./Postcard";
class Home extends React.Component{

    render(){
        return(
            <div>
            {this.props.posts.length ? this.props.posts.map(post => {
                return (
                    <Postcard key={post.id} body={post.body} title={post.title} img={logo} id={post.id}/>
                )
            }) : <h1>No posts to show</h1>}
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return { posts: state.posts };
    };

export default connect(mapStateToProps)(Home)