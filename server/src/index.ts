import express, { Express, Request, Response } from 'express';
import dotenv from 'dotenv';

dotenv.config();


AppDataSource.initialize().then(async () => {

    // console.log("Here you can setup and run express / fastify / any other framework.")

}).catch(error => console.log(error))

const app: Express = express();
const port = process.env.PORT;

app.get('/', (req: Request, res: Response) => {
  res.send('Express + TypeScript Server');
});

app.listen(port, () => {
  console.log(`⚡️[server]: Server is running at https://localhost:${port}`);
});
