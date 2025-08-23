import { useEffect, useState } from 'react'


function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/message")
      .then(res => res.json())
      .then((data) => setMessage(data.message));
  }, []);


  return (
      <div>
        <h1>Message from Flask:</h1>
        <p>{message}</p>
      </div>
  );
}

export default App
