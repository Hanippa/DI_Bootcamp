
// Exercise 4 : HTML Tags in React
// Instructions

// PART I:

//     In a separate Javascript file, create a new Component called Exercise4 that contains some HTML tags.
//         create a <h1> tag and set its color to red, and the background color to lightblue.
//         create a paragraph, a link, a form, an image and a list.

//     Import Exercise4 to the App.js file and display it.

//     Expected Output:(without the grey border)


// PART II:

//     Add the below object to the component Exercise4. Use this object to style the <h1>.

// const style_header = {
//   color: "white",
//   backgroundColor: "DodgerBlue",
//   padding: "10px",
//   fontFamily: "Arial"
// };


// PART III:

//     Create a new css file named Exercise4.css and import it in your Exercise4 component.
//     Add the following CSS properties to the CSS file, and apply them to the paragraph tag:


import "./Exercises4.css"

const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial"
  };

const Exercise4 = () => {
    return (<>
    {/* <h1 style={{color:"red" , backgroundColor:"lightblue"}}>styled</h1> */}
    <h1 style={style_header}>styled</h1>
    <p className="para">paragraph</p>
    <a href="google.com">link</a>
    <form>
        <input type="text"></input>
        <button type="submit"> Submit</button>
    </form>
    <img src="https://img.freepik.com/free-vector/cute-panda-eating-bamboo-leaves-watercolor-painting_24797-1939.jpg?w=2000" width="200" height="150"/>
    <ul>
        <li>list item 1</li>
        <li>list item 2</li>
        <li>list item 3</li>
    </ul>
    </>)

}

export default Exercise4