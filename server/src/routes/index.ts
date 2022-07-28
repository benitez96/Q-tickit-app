import { Express } from 'express';

import userRouter from './user';


export default ( app: Express ) => {
  app.use('/user', userRouter)
}
