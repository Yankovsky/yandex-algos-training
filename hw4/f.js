// Не проходит лимит по времени на 66 тесте, но дело не в решении, а в js

const readline = require('readline');

const customers = {}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

rl.on('line', (data) => {
    const [customer, item, quantity] = data.split(' ')

    if (!customers[customer])
        customers[customer] = {}

    if (!customers[customer][item])
        customers[customer][item] = 0

    customers[customer][item] += +quantity
});

rl.on('close', () => {
    Object.keys(customers).sort().forEach(customer => {
        console.log(`${customer}:`)
        const items = customers[customer]
        Object.keys(items).sort().forEach(item => {
            console.log(`${item} ${items[item]}`)
        })
    })
});
