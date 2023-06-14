import data from './data.json'

const PostList = () => {
    return data.map(datapoint => {
        return (
                <div style={{display:'flex',flexDirection:'column',textAlign:'center',border:'3px solid #0d6efd',width:'500px', margin:'30px',padding:'10px'}}>
                <h1>{datapoint.title}</h1>
                <h3>{datapoint.content}</h3>
                <h4>date : {datapoint.date}</h4>
                <h4>id : {datapoint.id}</h4>
                <h4>slug : {datapoint.slug}</h4>
                </div>
                )})
}

export default PostList