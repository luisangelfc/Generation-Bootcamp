// Task 3: addUser(first_name, last_name, email)
import { getServerURL } from './task1.js';

export function addUser(first_name, last_name, email) {
  // First, fetch the current users to determine the next sequential ID
  return fetch(`${getServerURL()}/users`)
    .then(response => response.json())
    .then(users => {
      // Find the maximum existing ID, default to 0 if no users exist
      const maxId = users.reduce((max, user) => {
        const idNum = parseInt(user.id, 10);
        return idNum > max ? idNum : max;
      }, 0);
      
      const nextId = maxId + 1;

      // POST the new user with the ID specified as the first property
      return fetch(`${getServerURL()}/users`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          id: nextId,
          first_name,
          last_name,
          email
        })
      });
    })
    .then(response => response.json());
}
