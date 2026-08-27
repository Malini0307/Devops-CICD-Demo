import React, { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async () => {
    try {
      const response = await fetch(
        "/register",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: name,
            email: email,
          }),
        }
      );

      const data = await response.json();

      setMessage(data.message);

      if (data.success) {
        setName("");
        setEmail("");
      }

    } catch (error) {
      setMessage("Unable to connect to server");
      console.error(error);
    }
  };

  return (
    <div
      style={{
        width: "500px",
        margin: "30px auto",
        padding: "20px",
        border: "1px solid #ccc",
        borderRadius: "10px",
      }}
    >
      <h1>Employee Registration</h1>

      <div>
        <label>Employee Name</label>
        <br />
        <input
          type="text"
          placeholder="Enter Employee Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          style={{
            width: "100%",
            padding: "8px",
          }}
        />
      </div>

      <br />

      <div>
        <label>Email</label>
        <br />
        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{
            width: "100%",
            padding: "8px",
          }}
        />
      </div>

      <br />

      <button
        onClick={handleRegister}
        style={{
          padding: "10px 20px",
          cursor: "pointer",
        }}
      >
        Register
      </button>

      <br />
      <br />

      {message && (
        <div
          style={{
            color: message.includes("successfully")
              ? "green"
              : "red",
            fontWeight: "bold",
          }}
        >
          {message}
        </div>
      )}
    </div>
  );
}

export default App;