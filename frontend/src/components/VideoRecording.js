import React, { useState, useRef } from "react";
import Webcam from "react-webcam";

const VideoRecording = () => {
  const webcamRef = useRef(null);
  const [recording, setRecording] = useState(false);
  const [videoUrl, setVideoUrl] = useState(null);

  let mediaRecorder;
  let chunks = [];

  const handleStartRecording = () => {
    const videoConstraints = {
      facingMode: "user", // or 'environment' for rear camera
    };

    const options = { mimeType: "video/webm" };

    if (webcamRef.current) {
      const stream = webcamRef.current.stream.getVideoTracks()[0];

      mediaRecorder = new MediaRecorder(stream, options);
      mediaRecorder.start();

      mediaRecorder.ondataavailable = (event) => {
        chunks.push(event.data);
      };

      setRecording(true);
    }
  };

  const handleStopRecording = () => {
    mediaRecorder.stop();

    mediaRecorder.onstop = () => {
      const videoBlob = new Blob(chunks, { type: "video/webm" });
      const videoUrl = URL.createObjectURL(videoBlob);
      setVideoUrl(videoUrl);
      chunks = [];
    };

    setRecording(false);
  };

  return (
    <div>
      <Webcam audio={true} ref={webcamRef} />

      <video src={videoUrl} controls />

      {recording ? (
        <button onClick={handleStopRecording}>Stop Recording</button>
      ) : (
        <button onClick={handleStartRecording}>Start Recording</button>
      )}
    </div>
  );
};

export default VideoRecording;
