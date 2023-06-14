import React from "react";

class ErrorBoundary extends React.Component{
    constructor(params){
        super(params);
        this.state = {hasError:false}
    };

    componentDidCatch(){
        this.setState({hasError:true})
    }
    render(){
        if(this.state.hasError){
            return (
                <>
                <h1>Something went wrong :(</h1>
                <h2>{this.state.hasError.message}</h2>
                </>
            )
        }
        else{
            return (
                this.props.children
            )
        }

    }
}

export default ErrorBoundary
