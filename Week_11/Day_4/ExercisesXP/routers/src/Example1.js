import data2 from './data2.json'

const Example1 = () => {
    return data2.SocialMedias.map(social => {
        return (
            <li>{social}</li>
        )
    })
}
export default Example1