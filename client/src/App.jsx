import { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Home from './components/Home';

function App() {
  const [user, setUser] = useState(null);
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login setUser={setUser} />} />
        <Route path="/home" element={<Home user={user} />} />
      </Routes>
    </Router>
  );
}

export default App;

