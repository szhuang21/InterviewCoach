import React from "react";
import Webcam from "react-webcam";
import { useHistory } from 'react-router-dom';


const videoConstraints = {
  aspectRatio: 1.6,
    facingMode: "user",
    width: { min: 480 },
    height: { min: 480 },
   };
  

const Video = () => {
  const history = useHistory();
  const webcamRef = React.useRef(null);
  const mediaRecorderRef = React.useRef(null);
  const [capturing, setCapturing] = React.useState(false);
  const [recordedChunks, setRecordedChunks] = React.useState([]);

  const handleStartCaptureClick = React.useCallback(() => {
    setCapturing(true);
    mediaRecorderRef.current = new MediaRecorder(webcamRef.current.stream, {
      mimeType: "video/webm"
    });
    mediaRecorderRef.current.addEventListener(
      "dataavailable",
      handleDataAvailable
    );
    mediaRecorderRef.current.start();
  }, [webcamRef, setCapturing, mediaRecorderRef]);

  const handleDataAvailable = React.useCallback(
    ({ data }) => {
      if (data.size > 0) {
        setRecordedChunks((prev) => prev.concat(data));
      }
    },
    [setRecordedChunks]
  );

  const handleStopCaptureClick = React.useCallback(() => {
    mediaRecorderRef.current.stop();
    setCapturing(false);
    // handleDownload();
  }, [mediaRecorderRef, webcamRef, setCapturing]);

  const handleDownload = () => {
    history.push('/Report');
  }
  // = React.useCallback(() => {
  //   if (recordedChunks.length) {
  //     const blob = new Blob(recordedChunks, {
  //       type: "video/webm"
  //     });
  //     const url = URL.createObjectURL(blob);
  //     const a = document.createElement("a");
  //     document.body.appendChild(a);
  //     a.style = "display: none";
  //     a.href = url;
  //     a.download = "react-webcam-stream-capture.mov";
  //     a.click();
  //     window.URL.revokeObjectURL(url);
  //     setRecordedChunks([]);
  //   }
  // }, [recordedChunks]);


  return (
    <>
      <div className="relative">
        <Webcam
          width={1000}
          height={480}
          videoConstraints={videoConstraints}
          audio={true}
          muted={true}
          ref={webcamRef}
          mirrored={true}
          className="bg-blue-400 mb-16"
        />
        <div className="absolute bottom-0 left-1/2 transform -translate-x-1/2">
          {capturing ? (
            <button
              onClick={handleStopCaptureClick}
              className="bg-blue-400 mr-2 px-4 py-2 rounded-md text-white"
            >
              Stop Capture
            </button>
          ) : (
            <button
              onClick={handleStartCaptureClick}
              className="bg-blue-400 mr-2 px-4 py-2 rounded-md text-white"
            >
              Start Capture
            </button>
          )}
          {recordedChunks.length > 0 && (
            <button
              onClick={handleDownload}
              className="bg-blue-400 px-4 py-2 rounded-md text-white"
            >
              Submit
            </button>
          )}
        </div>
      </div>
    </>
  );
  
};

export default Video;