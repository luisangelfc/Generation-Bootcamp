// List of colors: Green, Blue, Red
const colors = ['#2e7d32', '#1565c0', '#c62828'];

// Function that returns a random color from the list
function getRandomColor() {
  const randomIndex = Math.floor(Math.random() * colors.length);
  return colors[randomIndex];
}

// Function to apply a random color to a given element
function applyRandomColor(element) {
  element.style.color = getRandomColor();
}

// Bind click event to all h5 elements when DOM content is loaded
document.addEventListener('DOMContentLoaded', () => {
  const h5Tags = document.querySelectorAll('h5');
  h5Tags.forEach(tag => {
    tag.addEventListener('click', () => {
      applyRandomColor(tag);
    });
  });
});
