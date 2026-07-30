// Task 4: delUser(number)
import { getServerURL } from './task1.js';

export function delUser(id) {
  return fetch(`${getServerURL()}/users/${id}`, {
    method: 'DELETE'
  })
  .then(response => response.json());
}
