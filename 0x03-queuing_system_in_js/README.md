# 0x03. Queuing System in JS

## Description
This project focuses on implementing a queuing system in JavaScript using various technologies such as Redis, Node.js, and Express.js. It covers fundamental concepts like setting up a Redis server, interacting with Redis using a client interface, and building a basic Express app integrated with Redis and a queuing system.

## Technologies
- Back-end
- JavaScript (ES6)
- Redis
- Node.js
- Express.js
- Kue

## Learning Objectives
- Running a Redis server locally
- Performing basic operations with the Redis client
- Using a Redis client with Node.js for basic operations
- Storing hash values in Redis
- Handling asynchronous operations with Redis
- Implementing a queuing system using Kue
- Building a basic Express app interacting with a Redis server
- Building a basic Express app interacting with a Redis server and queuing system

## Requirements
- Ubuntu 18.04
- Node.js 12.x
- Redis 5.0.7
- All files should use the `.js` extension
- Code should be compiled/interpreted using Babel and ES6
- A `README.md` file is mandatory
- Run `$ npm install` to install dependencies from `package.json`

## Resources
- [Redis quick start](https://redis.io/topics/quickstart)
- [Redis client interface](https://redis.io/clients)
- [Redis client for Node.js](https://www.npmjs.com/package/redis)
- [Kue (deprecated)](https://github.com/Automattic/kue)

## Tasks Overview
1. **Install a redis instance**
   - Download, extract, and compile Redis
   - Start Redis server, perform basic operations, and copy `dump.rdb`
2. **Node Redis Client**
   - Connect to Redis server using `node_redis` and ES6
3. **Node Redis client and basic operations**
   - Implement basic Redis operations using callbacks
4. **Node Redis client and async operations**
   - Modify operations to use async/await with `promisify`
5. **Node Redis client publisher and subscriber**
   - Implement Redis publisher and subscriber with two separate scripts
6. **Create the Job creator**
   - Implement a job creator using Kue queue
7. **Create the Job processor**
   - Implement a job processor to process jobs from the queue
8. **Track progress and errors with Kue: Create the Job creator**
   - Track job progress and errors in the job creator
9. **Track progress and errors with Kue: Create the Job processor**
   - Track job progress and errors in the job processor
10. **Writing the job creation function**
    - Implement a function to create push notifications jobs
11. **Writing the test for job creation**
    - Write tests for the job creation function
12. **In stock?**
    - Implement a web application to manage product stock using Express.js and Redis

## Repository Structure
- **alx-backend**
  - **0x03-queuing_system_in_js**
    - `README.md`
    - `dump.rdb`
    - `package.json`
    - `babelrc`
    - `0-redis_client.js`
    - `1-redis_op.js`
    - `2-redis_op_async.js`
    - `4-redis_advanced_op.js`
    - `5-subscriber.js`
    - `5-publisher.js`
    - `6-job_creator.js`
    - `6-job_processor.js`
    - `7-job_creator.js`
    - `7-job_processor.js`
    - `8-job.js`
    - `8-job-main.js`
    - `8-job.test.js`
    - `9-stock.js`

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-backend/0x03-queuing_system_in_js
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Follow the instructions in each task's description to execute the respective scripts or web application.
