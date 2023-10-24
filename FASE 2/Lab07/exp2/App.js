import React from 'react';
import { UserProvider } from './UserContext';
import UserProfile from './UserProfile';

function App() {
  return (
    <UserProvider>
      <div>
        <h1>Aplicacion con React Context</h1>
        <UserProfile />
      </div>
    </UserProvider>
  );
}

export default App;
