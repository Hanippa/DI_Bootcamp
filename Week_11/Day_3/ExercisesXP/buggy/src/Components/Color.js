
import React from 'react';
class Child extends React.Component{

    componentWillUnmount(){
        alert('unmounted');
    }
    render(){
        return (
            <>
            <header>Hello World!</header>
            <button onClick={this.state.setState({show:false})}>delete</button>
            </>
        )
    }
}
class Color extends React.Component{
    constructor(){
        super();
        this.state = {
            favoritecolor: "red",
            show:true
        };
    };

    componentDidUpdate(){
        
    }

    shouldComponentUpdate(){
        return true;
    }

    changecolor = () => {
        this.setState({favoritecolor:'blue'})
    }

    componentDidMount = () =>{
        setTimeout(() => {
            this.setState({favoritecolor:'yellow'})
        },5000)
        
    }

    render(){
        return (
            <div>
            <h1>my favorite color is {this.state.favoritecolor}</h1>
            <button onClick={this.changecolor}>change color</button>
            </div>
        );
    };
}

export {Color , Child}