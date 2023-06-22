import { Link } from "react-router-dom"

const Postcard = (params) => {
    return (
        <div className="row home">
        <div className="col s12 m6">
          <div className="card blue-grey darken-1">
            <div className="card-content white-text post">
                
              <span className="card-title">  {params.title}</span>
              <p>{params.body}</p>
              <img src={params.img}/>
            </div>
            <div className="card-action">
            <Link to={`/post/${params.id}`}>go to post</Link>
             
            </div>
          </div>
        </div>
      </div>
    )
}

export default Postcard