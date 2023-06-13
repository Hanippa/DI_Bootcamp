import React, { useState } from 'react';

function App() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    age: '',
    gender: '',
    country: '',
    restrictions: [],
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: type === 'checkbox' ? (checked ? [...prevFormData[name], value] : prevFormData[name].filter((item) => item !== value)) : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <>
    <form style={{ display: 'flex', flexDirection: 'column' }} onSubmit={handleSubmit}>
      <input type="text" placeholder="firstName" name="firstName" onChange={(e) => handleChange(e)} />
      <input type="text" placeholder="lastName" name="lastName" onChange={(e) => handleChange(e)} />
      <input type="text" placeholder="age" name="age" onChange={(e) => handleChange(e)} />

      <input type="radio" name="gender" value="male" id="male" onChange={(e) => handleChange(e)} />
      <label htmlFor="male">male</label>

      <input type="radio" name="gender" value="female" id="female" onChange={(e) => handleChange(e)} />
      <label htmlFor="female">female</label>

      <input type="radio" name="gender" value="other" id="other" onChange={(e) => handleChange(e)} />
      <label htmlFor="other">other</label>

      <select name="country" onChange={(e) => handleChange(e)}>
        <option value="china">China</option>
        <option value="greenland">Greenland</option>
        <option value="mongolia">Mongolia</option>
      </select>

      <input type="checkbox" name="restrictions" value="nuts" id="nuts" onChange={(e) => handleChange(e)} />
      <label htmlFor="nuts">nuts</label>

      <input type="checkbox" name="restrictions" value="sesame" id="sesame" onChange={(e) => handleChange(e)} />
      <label htmlFor="sesame">sesame</label>

      <input type="checkbox" name="restrictions" value="dairy" id="dairy" onChange={(e) => handleChange(e)} />
      <label htmlFor="dairy">dairy</label>

      <input type="submit" />
    </form>
    <div>
          <h2>Entered information:</h2>
          <p>Name: {formData.firstName} {formData.lastName}</p>
          <p>Age: {formData.age}</p>
          <p>Gender: {formData.gender}</p>
          <p>Destination: {formData.country}</p>
          <p><strong>Dietary restrictions:</strong></p>
          {
            formData.restrictions.map(item=> {
              return <p>- {item}</p>
            })
          }
        </div>


    </>
    
  );
}

export default App;
