import React from 'react';
import { useUser } from './UserContext';

function UserProfile() {
  const { user, setUser } = useUser();

  const handleLogin = () => {
    setUser("usurio nuevo");
  };

  return (
    <div>
      <h1>{`ALO, ${user}!`}</h1>
      <button onClick={handleLogin}>Cambiar usuario</button>
    </div>
  );
}

export default UserProfile;
