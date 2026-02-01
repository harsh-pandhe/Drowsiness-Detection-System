const express = require("express");
const app = express();
const PORT = 3000;

app.use(express.static(__dirname));

app.listen(PORT, "0.0.0.0", () => {
  console.log(`🚀 SentinelDrive Dashboard running at http://localhost:${PORT}`);
  console.log(`📷 Camera will be accessed directly in the browser`);
});
