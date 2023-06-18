import React, { useState, useEffect } from "react";

const Timer = () => {
  const [time, setTime] = useState(5 * 60); // 5 minutes in seconds
  const [isActive, setIsActive] = useState(false);

  useEffect(() => {
    let interval = null;

    if (isActive && time > 0) {
      interval = setInterval(() => {
        setTime((prevTime) => prevTime - 1);
      }, 1000);
    } else if (time === 0) {
      clearInterval(interval);
      setIsActive(false);
    }

    return () => clearInterval(interval);
  }, [isActive, time]);

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const formattedMinutes = String(minutes).padStart(2, "0");
    const remainingSeconds = seconds % 60;
    const formattedSeconds = String(remainingSeconds).padStart(2, "0");

    return `${formattedMinutes}:${formattedSeconds}`;
  };

  const handleStartTimer = () => {
    setIsActive(true);
    setTime(5 * 60);
  };

  const handleStopTimer = () => {
    setIsActive(false);
    setTime(5 * 60);
  };

  return (
    <div className="flex flex-col items-center">
      <div className="text-6xl font-bold mb-4">{formatTime(time)}</div>

      {!isActive ? (
        <button
          className="px-6 py-3 bg-blue-500 text-white rounded"
          onClick={handleStartTimer}
        >
          Start Timer
        </button>
      ) : (
        <button
          className="px-6 py-3 bg-red-500 text-white rounded"
          onClick={handleStopTimer}
        >
          Stop Timer
        </button>
      )}
    </div>
  );
};

export default Timer;
