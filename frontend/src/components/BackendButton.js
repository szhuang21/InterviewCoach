import React, { useState } from "react";

const BackendButton = () => {
  const [response, setResponse] = useState("");
  const [response2, setResponse2] = useState("");
  const [top5PositiveEmotions, setTop5PositiveEmotions] = useState([]);
  const [top5NegativeEmotions, setTop5NegativeEmotions] = useState([]);

  const handleButtonClick = () => {
    fetch("http://127.0.0.1:5000")
      .then((res) => res.text())
      .then((data) => setResponse(data))
      .catch((error) => console.error("Error:", error));
  };

  const handleButton2Click = async () => {
    console.log("button was clicked");
    try {
      const formData =
        "/Users/sophiazhuang/Desktop/InterviewCoach/InterviewCoach/backend/test.zip";

      const response = await fetch("http://127.0.0.1:5000/getReport", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log("line 26");
        const report = await response.json();
        console.log("report: ", report);
        setTop5PositiveEmotions(report["top_positive_emotions"]);
        setTop5NegativeEmotions(report["top_negative_emotions"]);
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <button onClick={handleButtonClick}>Fetch Response</button>
      <p>{response}</p>

      <button onClick={handleButton2Click}>Send Zip and Get Response</button>
      <p>{response2}</p>
    </div>
  );
};

export default BackendButton;
