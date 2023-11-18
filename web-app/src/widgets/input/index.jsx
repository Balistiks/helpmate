import './index.css'

const Input = (props) => {
  const handleChange = (event) => {
    props.onChange(event.target.value)
  }
  return (
    <>
      <input value={props.value} onChange={handleChange} className='input' type="text" />
    </>
  )
}

export default Input