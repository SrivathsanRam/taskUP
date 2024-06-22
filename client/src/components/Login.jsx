/* eslint-disable react/prop-types */
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = ({ setUser }) => {
  const [nric, setNric] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ nric, password }),
      });

      if (response.ok) {
        const data = await response.json();
        setUser(data);
        navigate("/home");
      } else {
        setError("Invalid credentials");
      }
    } catch (err) {
      setError("An error occurred. Please try again.");
    }
  };

  return (
    <div className="container-sm mt-5 shadow p-3 mb-5 bg-body rounded">
      <h2 className="mt-5 mb-4">Login with Singpass</h2>
      <form onSubmit={handleSubmit} className="mb-4">
        <div className="mb-3">
          <label htmlFor="nric" className="form-label">
            NRIC:
          </label>
          <input
            type="text"
            id="nric"
            className="form-control shadow-sm bg-light"
            value={nric}
            onChange={(e) => setNric(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">
            Password:
          </label>
          <input
            type="password"
            id="password"
            className="form-control shadow-sm bg-light"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Login
        </button>
      </form>
      {error && <p className="text-danger">{error}</p>}
    </div>
  );
};

export default Login;
