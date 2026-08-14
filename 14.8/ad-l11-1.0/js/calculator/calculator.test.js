const calculator = require('./calculator');

test('adds 1 + 2 to equal 3', () => {
  expect(calculator.add(1, 2)).toBe(3);
});

test('adds -4 + 8 to equal 4', () => {
  expect(calculator.add(-4, 8)).toBe(4);
});

test('subtract 5 - 4 to equal 1', () => {
  expect(calculator.subtract(5, 4)).toBe(1);
});

test('subtract -5 - -10 to equal 5', () => {
  expect(calculator.subtract(-5, -10)).toBe(5);
});

test('divide 10 / 2 to equal 5', () => {
  expect(calculator.divide(10, 2)).toBe(5);
});

test('divide 9 / 3 to equal 3', () => {
  expect(calculator.divide(9, 3)).toBe(3);
});

test('multiply 3 * 3 to equal 9', () => {
  expect(calculator.multiply(3, 3)).toBe(9);
});

test('multiply -2 * 4 to equal -8', () => {
  expect(calculator.multiply(-2, 4)).toBe(-8);
});

test('divide by zero throws Error', () => {
  expect(() => calculator.divide(10, 0)).toThrow('No se puede dividir por cero');
});