import Video from "../components/Video";
import React, { useState } from 'react';

function HomePage() {

  const MyForm = () => {
    const [formData, setFormData] = useState({
      numquestions: 0,
      age: 0,
      workfield: ''
    });
    
    const styles = {
      backgroundColor: 'white',
      margin: 20,
      color: 'black',
      padding: '5px',
      width: 600,
      height: 50
    };

    const style_button = {
      backgroundColor: 'blue',
      margin: 20,
      color: 'white',
    };

    const style_text = {
      color: 'white',
      width: 600,
      height: 50
    };
  
    const handleChange = (event) => {
      const { name, value } = event.target;
      setFormData((prevFormData) => ({
        ...prevFormData,
        [name]: value
      }));
    };
  
    const handleSubmit = (event) => {
      event.preventDefault();
      // Handle form submission here
      console.log(formData);
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <div style={styles}>
          <label htmlFor="numquestions">How many questions would you like to try?  </label>
          <input
            type="number"
            id="numquestions"
            name="numquestions"
            value={formData.numquestions}
            onChange={handleChange}
          />
        </div>
        <div style={styles}>
          <label htmlFor="age">What's your age?   </label>
          <input
            type="number"
            id="age"
            name="age"
            value={formData.age}
            onChange={handleChange}
          />
        </div>
        <div style={styles}>
          <label htmlFor="message">What's your work field?</label>
          <textarea
            style={style_text}
            id="workfield"
            name="workfield"
            value={formData.workfield}
            onChange={handleChange}
          ></textarea>
        </div>
        <button style= {style_button} onClick={handleSubmit}>Submit</button>
      </form>
    );
  };

  const style_h1 = {
    color: 'black',
    margin:20,
    padding: 50,
    size: 60
  };

  return (
    <div>
      <div>
        <h1 style={style_h1}><b>Welcome to InterviewCoach! Let's get started!</b></h1>
      </div>
      <div>
        <MyForm /> 
      </div>
    </div>
  );
}

export default HomePage;
