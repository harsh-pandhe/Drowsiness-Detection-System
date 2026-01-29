const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

/**
 * In a real-world scenario, you would keep your HTML, CSS, and JS 
 * in a 'public' folder. For this implementation, we are serving 
 * the single-file index.html directly.
 */

// Serve static assets if you have them
app.use(express.static(path.join(__dirname, 'public')));

// Main Route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// API endpoint example (if you want to log drowsiness events to a database later)
app.post('/api/log-event', express.json(), (req, res) => {
    const { timestamp, type, earValue } = req.body;
    console.log(`[EVENT] ${type} detected at ${timestamp} (EAR: ${earValue})`);
    res.status(200).json({ status: 'logged' });
});

app.listen(PORT, () => {
    console.log(`-----------------------------------------`);
    console.log(`SentinelEye Server Running`);
    console.log(`URL: http://localhost:${PORT}`);
    console.log(`Environment: Node.js / Express`);
    console.log(`-----------------------------------------`);
});