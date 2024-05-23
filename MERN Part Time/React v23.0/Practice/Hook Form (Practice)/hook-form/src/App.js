import React, { useState } from 'react';
import './App.css';
import UserForm from './components/UserForm';
import UserView from './components/UserView';

function App() {
  const [user, setUser] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  return (
    <div className="App">
      <UserForm user={user} setUser={setUser} />
      <UserView user={user} />
    </div>
  );
}

export default App;
