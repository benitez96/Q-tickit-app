import express from 'express';
import dotenv from 'dotenv';


import router from './routes'
import config from './configs';

dotenv.config();

const app = express();
const PORT = process.env.PORT;

config(app)
router(app);

app.listen(PORT, () => {
  console.log(`⚡️[server]: Server is running at https://localhost:${PORT}`);
});
