import React, { useEffect, useState } from "react";
import Plotly from "plotly.js-basic-dist";

const Report = () => {
  const [top5VisualPositiveEmotions, setTop5VisualPositiveEmotions] = useState(
    []
  );
  const [top5VisualNegativeEmotions, setTop5VisualNegativeEmotions] = useState(
    []
  );
  const [graph, setGraph] = useState([]);
  const [imageSrc, setImageSrc] = useState("");

  const renderGraph = (fig) => {
    console.log('inside of renderGraph');
    Plotly.newPlot("graph-container", fig.data, fig.layout);
  };
  const handleReportSubmit = async () => {
    console.log("button was clicked");
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
        setGraph(report["graph"]);
        setImageSrc(report["image_src"]);
        renderGraph(report["graph"]);
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      console.log("top5PositiveEmotions: ", top5VisualPositiveEmotions);
    }
  };


  return (
    <div className="pl-8 pt-8">
      <button
        onClick={handleReportSubmit}
        className="flex justify-center items-center mb-8"
      >
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
            <th className="text-left">Emotion</th>
            <th className="text-left">Score</th>
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
      {imageSrc && (
        <div>
          <h2>Image:</h2>
          <img src={imageSrc} alt="Report Image" />
        </div>
      )}
    </div>
  );
};

export default Report;
