// import { useState } from "react";

// export default function DelayedMessageApp() {
//   const [time, setTime] = useState(1000);
//   const [message, setMessage] = useState("");
//   const [displayMessage, setDisplayMessage] = useState("");
//   const [timeoutId, setTimeoutId] = useState(null);

//   const startTimer = () => {
//     if (time < 0) return;
//     setDisplayMessage(""); // Clear old message
//     if (timeoutId) clearTimeout(timeoutId); // Clear any previous timeout

//     const id = setTimeout(() => {
//       setDisplayMessage(message);
//     }, time);

//     setTimeoutId(id);
//   };

//   const reset = () => {
//     setTime(1000);
//     setMessage("");
//     setDisplayMessage("");
//     if (timeoutId) clearTimeout(timeoutId);
//   };

//   return (
//     <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
//       <h1 className="text-2xl font-bold mb-4">Delayed Message</h1>
      
//       <input
//         type="number"
//         value={time}
//         onChange={(e) => setTime(Number(e.target.value))}
//         min="0"
//         className="border p-2 rounded mb-4 w-40 text-center"
//         placeholder="Enter time (ms)"
//       />
      
//       <input
//         type="text"
//         value={message}
//         onChange={(e) => setMessage(e.target.value)}
//         className="border p-2 rounded mb-4 w-64 text-center"
//         placeholder="Enter your message"
//       />
      
//       <div className="flex space-x-4 mb-4">
//         <button onClick={startTimer} className="bg-blue-500 text-white px-4 py-2 rounded">Start</button>
//         <button onClick={reset} className="bg-gray-500 text-white px-4 py-2 rounded">Reset</button>
//       </div>

//       {displayMessage && <h2 className="text-green-500 text-xl mt-4">{displayMessage}</h2>}
//     </div>
//   );
// }
