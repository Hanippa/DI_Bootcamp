import React from "react";

class ErrorBoundary extends React.Component{
    constructor(params){
        super(params);
        this.state = {error:null}
    };
    componentDidCatch(error,errorInfo){
        this.setState({error:error})
    }
    render(){
        if(this.state.error){
            return (
                <>
                <h1>Something went wrong :(</h1>
                <h2>{this.state.error.message}</h2>
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
