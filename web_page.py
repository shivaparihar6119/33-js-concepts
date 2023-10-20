<!DOCTYPE html>
<html>
<head>
  <title>JavaScript Example</title>
</head>
<body>
  <h1>Click the button to change the background color</h1>
  <button id="colorButton">Change Color</button>

  <script>
    // JavaScript code
    const colorButton = document.getElementById("colorButton");
    const body = document.body;

    colorButton.addEventListener("click", function () {
      const randomColor = getRandomColor();
      body.style.backgroundColor = randomColor;
    });

    function getRandomColor() {
      const letters = "0123456789ABCDEF";
      let color = "#";
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
  </script>
</body>
</html>
