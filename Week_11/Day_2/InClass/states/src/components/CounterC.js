import React from 'react'

class CounterC extends React.Component {
    constructor(){
        super()
        this.state = {
            count : 0
        }
    }

    handleClick = () => {
        console.log(this.state.count)
        this.setState({count:this.state.count + 1})
    }

    componentDidMount = () => {
        console.log('component mounted')
    }
    componentDidUpdate = () => {
        console.log('component updated')
    }
    render(){
        return (
                <div>
                    <h1>Counter:</h1>
                    <h2>{this.state.count}</h2>
                    <button onClick={this.handleClick}>Add</button>
                </div>
        )
    }
}

export default CounterC