import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const getUsersData = async () => {
      const response = await fetch("http://127.0.0.1:8090/api/users");
      const data = await response.json();
      setUsers(data.users);
    };

    getUsersData();
  }, []);

  return (
    <div>
      <h2>User List</h2>
      <ul>
        {users.map((user, index) => (
          <li key={index}>{user.user_name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Users;
