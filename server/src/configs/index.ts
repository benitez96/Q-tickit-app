import express, { Express } from 'express';
import logger from 'morgan';
import cors from 'cors';
import "reflect-metadata"
import dotenv from 'dotenv';
import { DataSource } from "typeorm"

dotenv.config();

export const db = new DataSource({
    type: "postgres",
    host: process.env.DB_HOST,
    port: Number( process.env.DB_PORT ),
    username: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    synchronize: true,
    logging: false,
    entities: [
      '../models/*.{ts,js}', // we need to read final build
    ],
    migrations: [],
    subscribers: [],
})

export default ( app: Express ) => {

  app.disable('x-powered-by')
  app.set('env', process.env.NODE_ENV)

  if ( process.env.NODE_ENV !== 'test' )
    app.use( logger('dev') )

  app.use( express.json() )
  app.use( express.urlencoded({ extended: false }) )
  app.use( cors() )

  db.initialize()
    .then(() => console.log('Database initializated'))
    .catch( err => console.error('Error during database initialization: ', err) )
}
