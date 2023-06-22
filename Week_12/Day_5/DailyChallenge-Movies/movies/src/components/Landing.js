
import React from "react";
import { Link } from 'react-router-dom';

const Landing = () => {
    return (
        <div className="row">
        <form className="col s12">
          <div className="row">
         
            <div className="input-field col s12">
                
                <form style={{display:"flex"}}>
              <input id="email" type="email" className="validate"/>
              <button class="btn waves-effect waves-light" type="submit" name="action">search
    <i class="material-icons right">send</i>
  </button>
              </form>
              
              <label for="email">search</label>
             
              <span className="helper-text" data-error="wrong" data-success="right">search for a movie!</span>
            </div>
          </div>
        </form>
      </div>
    )
}

export default Landing