import React, { useState } from "react";

function Login() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // Email validation regex
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email)) {
      setError("Please enter a valid email");
      return;
    }

    if (password.length < 6) {
      setError("Password must be at least 6 characters");
      return;
    }

    setError("");
    alert("Login Successful");
  };

  return (
    <div style={{textAlign:"center", marginTop:"100px"}}>
      <h2>Login Form</h2>

      <form onSubmit={handleSubmit}>

        <div>
          <label>Email:</label><br/>
          <input
            type="email"
            placeholder="Enter Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <br/>

        <div>
          <label>Password:</label><br/>
          <input
            type="password"
            placeholder="Enter Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <br/>

        <button type="submit">Login</button>

        <p style={{color:"red"}}>{error}</p>

      </form>
    </div>
  );
}

export default Login;