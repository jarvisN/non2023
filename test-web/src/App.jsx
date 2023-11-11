import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import MyButton from './components/MyButton.jsx'

function App() {

  const [count,setCount] = useState(0)
  const [name,setName] = useState("Non")

  return (
    <>
      <h1>
        My profile
      </h1>
      <p>
        {name}
      </p>
      <MyButton />
    </>
  )
}

export default App
