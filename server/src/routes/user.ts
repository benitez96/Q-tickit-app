import express from 'express';


const router = express.Router()


router
  .get('/', (req, res) => {
    res.json({ value: 'Hola mundo' })
  })
  .post('/', (req, res) => res.json(req.body) )


export default router
