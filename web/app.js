const express = require('express');
const app = express();
const port = 3000;

// Serve static files from 'public' directory
app.use(express.static('public'));
// Body parser middleware to parse form data
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/submit-form', (req, res) => {
  const { name, email, message } = req.body;
  // Process form data here
  console.log(name, email, message);
  res.send('Form submitted');
});

app.get('/test_get', (req,res) =>{
  res.send('test');
});

app.post('/testData', (req, res) => {
    const { username, password } = req.body;
    // Process form data here
    console.log(username, password);
    res.send('Form submitted');
  });

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
