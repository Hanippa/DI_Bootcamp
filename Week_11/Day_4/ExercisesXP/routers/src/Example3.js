import data2 from './data2.json'

const Example3 = () => {
    return data2.Experiences.map(company => {
        return (<div>
            <img src={company.logo} alt='logo'/>
            <a href={company.url}>{company.url}</a>
            {company.roles.map(role => {
                return (<div>
                    <h1>{role.title}</h1>
                    <h3>{role.startDate}</h3>
                    <h3>{role.location}</h3>
                    <h3>{role.description}</h3>
                </div>)
            })}
                </div>)
    })
    }

export default Example3

