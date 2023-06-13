import React from "react";

class ErrorBoundary extends React.Component{
    constructor(){
        super()
    }
    render(){
        return (
            this.props.children
        )
         
    }
    componentDidCatch(error, errorInfo){
        console.log(error , errorInfo)
    }
}

export default ErrorBoundary