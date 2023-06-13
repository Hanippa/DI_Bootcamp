import Input from "./Input"
import './Form.css'


function isValid(email , regex) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }


const Form = (props) => {




    return (
        <div className="sform">
        <Input name='FirstName' />
        <Input name='LastName'/>
        <Input name='Phone'/>
        <Input name='Email'/>
        </div>
    )
}

export default Form