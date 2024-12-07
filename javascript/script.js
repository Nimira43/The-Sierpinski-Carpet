document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('sierpinskiCanvas')
  canvas.width = 600
  canvas.height = 600
  const ctx = canvas.getContext('2d')

  function sierpinskiCarpet(x, y, size, depth) {
      if (depth == 0) {
          ctx.fillRect(x, y, size, size)
      } else {
          const newSize = size / 3
          for (let i = 0; i < 3; i++) {
              for (let j = 0; j < 3; j++) {
                  if (i == 1 && j == 1) continue; // Skip the center square
                  sierpinskiCarpet(x + i * newSize, y + j * newSize, newSize, depth - 1)
              }
          }
      }
  }

  ctx.fillStyle = 'black';
  sierpinskiCarpet(0, 0, 600, 4);  // Start at (0,0) with size 600 and depth 4
})
