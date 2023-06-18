import React, { useRef, useState } from "react";

function Video() {
  const videoRef = useRef(null);
  const [recordedVideo, setRecordedVideo] = useState(null);
  const [recording, setRecording] = useState(false);

  const handleStartRecording = () => {
    setRecording(true);
    videoRef.current.srcObject = null;
    videoRef.current.src = null;
    navigator.mediaDevices
      .getUserMedia({ video: true, audio: true })
      .then((stream) => {
        videoRef.current.srcObject = stream;
        videoRef.current.play();
      })
      .catch((error) => {
        console.error("Error accessing media devices:", error);
      });
  };

  const handleStopRecording = () => {
    setRecording(false);
    const stream = videoRef.current.srcObject;
    const tracks = stream.getTracks();
    tracks.forEach((track) => {
      track.stop();
    });
    const recordedBlob = new Blob(recordedChunks, { type: "video/webm" });
    setRecordedVideo(URL.createObjectURL(recordedBlob));
  };

  const recordedChunks = [];
  const handleDataAvailable = (event) => {
    if (event.data.size > 0) {
      recordedChunks.push(event.data);
    }
  };

  return (
    <div>
      <div className="mb-4">
        <video
          ref={videoRef}
          className="w-full"
          muted
          controls
          playsInline
        ></video>
      </div>
      {recordedVideo && (
        <div>
          <p>Recorded video:</p>
          <video
            src={recordedVideo}
            className="w-1/2"
            controls
            loop
            playsInline
          ></video>
        </div>
      )}
      {!recording ? (
        <button
          onClick={handleStartRecording}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Start Recording
        </button>
      ) : (
        <button
          onClick={handleStopRecording}
          className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          Stop Recording
        </button>
      )}
    </div>
  );
}

export default Video;

// function Video() {
//   return (
//     <div>
//       <div>Video</div>
//     </div>
//   );
// }

// export default Video;
