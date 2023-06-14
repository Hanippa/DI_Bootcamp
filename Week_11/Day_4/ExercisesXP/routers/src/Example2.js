import data2 from './data2.json'

const Example2 = () => {
    return data2.Skills.map(skill => {
        return (<div><h1>{skill.Area}</h1>
        {skill.SkillSet.map(lang => {return (<li>{lang.Name}</li>)})}
        </div>)
    })
    }

export default Example2

