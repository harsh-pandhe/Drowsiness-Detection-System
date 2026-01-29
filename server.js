const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

/**
 * SentinelEye Driver Drowsiness Detection System
 * This server handles routing and static file delivery.
 */

// Middleware to parse JSON (useful for future logging features)
app.use(express.json());

// Serve static assets from a 'public' folder if it exists
app.use(express.static(path.join(__dirname, 'public')));

// Main Route: Serves the Eye Tracking Interface
app.get('/', (req, res) => {
    // Using path.resolve to ensure the file is found correctly
    res.sendFile(path.resolve(__dirname, 'index.html'));
});

// API endpoint for logging drowsiness events
app.post('/api/log-event', (req, res) => {
    const { timestamp, type, earValue } = req.body;
    console.log(`[ALARM] ${type} detected at ${timestamp} | EAR: ${earValue}`);
    res.status(200).json({ status: 'success', message: 'Event logged to server console' });
});

// Error handling for missing files
app.use((req, res) => {
    res.status(404).send('Resource not found. Ensure index.html is in the root directory.');
});

app.listen(PORT, () => {
    console.log(`\x1b[32m%s\x1b[0m`, `-----------------------------------------`);
    console.log(`\x1b[36m%s\x1b[0m`, `SentinelEye System Active`);
    console.log(`Monitoring Port: ${PORT}`);
    console.log(`Local Access: http://localhost:${PORT}`);
    console.log(`\x1b[32m%s\x1b[0m`, `-----------------------------------------`);
    console.log(`Press Ctrl+C to stop the server`);
});