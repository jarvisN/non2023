import { useState } from 'react'
import './App.css'
import MyButton from './components/MyButton.jsx'
import { Routes, Route, useNavigate } from 'react-router-dom';
import Router from './Router.jsx';

function App() {

  const navigate = useNavigate();

  return (
    <Router>
      <h1>
        My profile
      </h1>
      <p>
      </p>
      <MyButton />
    </Router>
  )
}

export default App
