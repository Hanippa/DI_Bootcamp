import Card from "./Components/Card";
const getusers = async () => {
  const data = await fetch('https://jsonplaceholder.typicode.com/users')
  const json = await data.json()
  return json
}
function App() {
    return (
    
      <div className="App">
        <h1>robots week 12 day 2 daily challenge</h1>
        <input type="text" placeholder="search"/>
        {
          getusers().then(users => {
            return users.map(user => {
              return <Card key={user.id} url={`https://robohash.com/${user.id}`} name={user.name} email={user.email}/>
            })
          })

              
            }
      </div>
    );

}

export default App;
