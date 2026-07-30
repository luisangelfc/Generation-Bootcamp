// Task 2: listUsers()
import { getServerURL } from './task1.js';

export function listUsers() {
  return fetch(`${getServerURL()}/users`)
    .then(response => response.json())
    .then(data => {
      console.log("[");
      data.forEach((user, index) => {
        console.log("{");
        console.log(`  id: ${user.id},`);
        console.log(`  first_name: '${user.first_name}',`);
        console.log(`  last_name: '${user.last_name}',`);
        console.log(`  email: '${user.email}'`);
        if (index === data.length - 1) {
          console.log("}");
        } else {
          console.log("},");
        }
      });
      console.log("]");
    });
}
