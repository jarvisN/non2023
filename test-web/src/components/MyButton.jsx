import React from 'react'

function myButton() {
  function handleCick() {
    alert("you clicked me!")
  }
  return (
    <button onClick={handleCick}>myButton</button>
  )
}

export default myButton