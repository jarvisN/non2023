import { useState } from 'react'
import './App.css'
import MyButton from './components/MyButton.jsx'
import { Routes, Route, useNavigate } from 'react-router-dom';
import Router from './Router.jsx';

function App() {
  const [count, setCount] = useState(0)
  const [name, setName] = useState("Non")

  const navigate = useNavigate();
  // const navigateToAbout = () => {
  //   navigate('/about');
  // };

  // const navigateHome = () => {
  //   navigate('/');
  // };

  return (
    // <>
    <Router>
      <h1>
        My profile
      </h1>
      <p>
        {name}
      </p>
      <MyButton />
      {/* <button onClick={navigateHome}> Home </button>
      <button onClick={navigateToAbout}> About </button> */}
    </Router>
    // </>
  )
}

export default App
