/**
 * Data
 * 
 * Create an array listProducts containing the list of the following products:
 * Id: 1, name: Suitcase 250, price: 50, stock: 4
 * Id: 2, name: Suitcase 450, price: 100, stock: 10
 * Id: 3, name: Suitcase 650, price: 350, stock: 2
 * Id: 4, name: Suitcase 1050, price: 550, stock: 5
 * 
 * Data access
 * 
 * Create a function named getItemById:
 * It will take id as argument
 * It will return the item from listProducts with the same id
 * 
 * Server
 * 
 * Create an express server listening on the port 1245. (You will start it via: npm run dev 9-stock.js)
 *
 * Products
 * 
 * Create the route GET /list_products that will return the list of every available product with the following JSON format:
 */


import express from 'express';

const app = express();
const port = 1245;
const host = 'localhost';


const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];


const getItemById = (id) => {
    return listProducts.find((product) => product.id === id);
}

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});


/**
 * In stock in Redis
 * Create a client to connect to the Redis server:
 * 
 * Write a function reserveStockById that will take itemId and stock as arguments:
 * It will set in Redis the stock for the key item.ITEM_ID
 * Write an async function getCurrentReservedStockById, that will take itemId as an argument:
 * It will return the reserved stock for a specific item
 * Product detail
 * Create the route GET /list_products/:itemId, that will return the current product and
 * the current available stock (by using getCurrentReservedStockById) with the
 * following JSON format:
 * {"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4,"currentQuantity":4}
 * 
 * If the item does not exist, it should return: { status: 'Product not found' }
 */

import redis from 'redis';
const client = redis.createClient();


const reserveStockById = (itemId, stock) => {
    client.set(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
    // Use promisify to convert the Redis.get method to a promise
    const getAsync = promisify(client.get).bind(client);
    return await getAsync(`item.${itemId}`);
}

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);

    if (!item) {
        res.json({ status: 'Product not found' });
        return;
    }

    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({
        itemId: item.id,
        itemName: item.name,
        price: item.price,
        initialAvailableQuantity: item.stock,
        currentQuantity: Number(currentQuantity)
    });
});


/**
 * Reserve a product
 * Create the route GET /reserve_product/:itemId:
 * If the item does not exist, it should return: { status: 'Product not found' }
 * If the item exists, it should check that there is at
 * least one stock available. If not it should return: { status: 'Not enough stock available' }
 * If there is enough stock available, it should reserve one item (by using reserveStockById),
 * and return: { status: 'Reservation confirmed', itemId: 1 }
 */

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);

    if (!item) {
        res.json({ status: 'Product not found' });
        return;
    }

    const currentQuantity = await getCurrentReservedStockById(itemId);
    if (currentQuantity >= item.stock) {
        res.json({ status: 'Not enough stock available' });
        return;
    }

    reserveStockById(itemId, Number(currentQuantity) + 1);
    res.json({ status: 'Reservation confirmed', itemId: item.id });
});


app.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});
