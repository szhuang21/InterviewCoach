import React, { useEffect, useState } from "react";

const Report = () => {
  const [top5VisualPositiveEmotions, setTop5VisualPositiveEmotions] = useState(
    []
  );
  const [top5VisualNegativeEmotions, setTop5VisualNegativeEmotions] = useState(
    []
  );
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {}, []);

  const handleReportSubmit = async () => {
    console.log("button was clicked");
    setIsLoading(true); // Set loading state to true before fetching data
    try {
      const formData =
        "/Users/sophiazhuang/Desktop/InterviewCoach/InterviewCoach/backend/test.zip";

      const response = await fetch("http://127.0.0.1:5000/getFullReport", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log("line 26");
        const report = await response.json();
        console.log("report: ", report);
        setTop5VisualPositiveEmotions(report["top_visual_positive_emotions"]);
        setTop5VisualNegativeEmotions(report["top_visual_negative_emotions"]);
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      console.log("top5PositiveEmotions: ", top5VisualPositiveEmotions);
      setIsLoading(false); // Set loading state to false after fetching data
    }
  };

  return (
    <div>
      <button onClick={handleReportSubmit} className="text-center">
        Get Report
      </button>
      <div className="text-xl text-black font-bold font-montserrat mb-1">
        Your Mock Interview Report 💞
      </div>
      <div className="text-lg text-gray-600 font-montserrat">
        Your Top 5 Positive Emotions
      </div>

      <table className="w-1/2">
        <thead>
          <tr>
            <th className="text-left">Key</th>
            <th className="text-left">Value</th>
          </tr>
        </thead>
        <tbody>
          {top5VisualPositiveEmotions?.map((pair, index) => (
            <tr key={index}>
              <td className="border px-4 py-2">{pair[0]}</td>
              <td className="border px-4 py-2">{pair[1]}</td>
            </tr>
          ))}
        </tbody>
      </table>
{/* 
      <ul className="text-lg">
        {top5VisualPositiveEmotions?.map((emotion, index) => (
          <li key={index}>{emotion[0]}</li>
        ))}
      </ul> */}
    </div>
  );
};

export default Report;
