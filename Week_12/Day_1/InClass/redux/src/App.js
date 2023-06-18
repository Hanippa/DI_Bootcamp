import React from 'react';
import Lesson from './Lesson';
import { createStore } from 'redux'
import { connect } from 'react-redux'
import reducer from "./reducers";


const initialState = { subject: "Javascript" };
const store = createStore(reducer, initialState);

class App extends React.Component {

  render() {
    return (
      <div>
        <Lesson subject={store.getState().subject} />
      </div>
    )
  }
}

const mapStateToProps = (state) => {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(App);