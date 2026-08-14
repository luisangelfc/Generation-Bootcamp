const UserController = require("./user-controller");
const User = require("./user");

let userController;

beforeEach(() => {
  userController = new UserController();
});

test('add user to userController', () => {    
    let user = new User(1234,"Santiago", "santiago@generation.org");
    userController.add(user);    
    expect(userController.getUsers()).toContain(user);
  });

test('remove user to userController', () => {    
    let user = new User(1234,"Santiago", "santiago@generation.org");
    userController.add(user);    
    userController.remove(user);
    expect(userController.users).not.toContain(user);
  });

test('add a new user that is not in the list', () => {
    let user = new User(5678, "Juan", "juan@generation.org");
    expect(userController.getUsers()).not.toContain(user);
    userController.add(user);
    expect(userController.getUsers()).toContain(user);
  });

test('remove a user that is not in the list', () => {
    let user = new User(8888, "Maria", "maria@generation.org");
    expect(userController.getUsers()).not.toContain(user);
    userController.remove(user);
    expect(userController.getUsers()).not.toContain(user);
  });

test('findByEmail returns user when user exists', () => {
    let user = new User(111, "Ana", "ana@generation.org");
    userController.add(user);
    expect(userController.findByEmail("ana@generation.org")).toEqual(user);
  });

test('findByEmail returns undefined when user does not exist', () => {
    expect(userController.findByEmail("nonexistent@generation.org")).toBeUndefined();
  });

test('findById returns user when user exists', () => {
    let user = new User(222, "Carlos", "carlos@generation.org");
    userController.add(user);
    expect(userController.findById(222)).toEqual(user);
  });

test('findById returns undefined when user does not exist', () => {
    expect(userController.findById(9999)).toBeUndefined();
  });

