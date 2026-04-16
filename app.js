const express = require('express');
const app = express();

// Middleware and routes setup
app.use(express.json());

app.get('/', (req, res) => {
    res.send('SalesMap API');
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
