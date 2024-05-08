/**
 * Using promisify, modify the function displaySchoolValue to use ES6 async / await
 * Same result as 1-redis_op.js
 */

import redis from 'redis';

const client = redis.createClient();
const { promisify } = require('util');


client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const getAsync = promisify(client.get).bind(client);
    const reply = await getAsync(schoolName);
    console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
