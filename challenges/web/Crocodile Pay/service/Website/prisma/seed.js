import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function main() {
    const items = [
        {
            item_id: 1,
            item_name: 'Crocodile Plush Toy',
            cost: 25,
            image: '/items/item1.jpg',
            description: 'A soft and cuddly crocodile plush, perfect for children and collectors.',
        },
        {
            item_id: 2,
            item_name: 'Crocodile Leather Wallet',
            cost: 150,
            image: '/items/item2.jpg',
            description: 'A genuine crocodile leather wallet, offering durability and a luxurious feel',
        },
        {
            item_id: 3,
            item_name: 'Crocodile Keychain',
            cost: 10,
            image: '/items/item3.jpg',
            description: 'A small, metal crocodile keychain, ideal for adding a unique touch to your keys.',
        },
        {
            item_id: 4,
            item_name: 'Crocodile Coffee Mug',
            cost: 15,
            image: '/items/item4.jpg',
            description: 'A ceramic mug featuring a crocodile design, great for animal lovers.',
        },
        {
            item_id: 5,
            item_name: 'Crocodile Socks',
            cost: 12,
            image: '/items/item5.jpg',
            description: 'Comfortable cotton socks adorned with a fun crocodile pattern.',
        },
        {
            item_id: 6,
            item_name: 'Crocodile Backpack',
            cost: 40,
            image: '/items/item6.jpg',
            description: 'A stylish backpack with a crocodile print, suitable for daily use.',
        },
        {
            item_id: 7,
            item_name: 'Crocodile Hat',
            cost: 20,
            image: '/items/item7.jpg',
            description: 'A baseball cap featuring an embroidered crocodile logo.',
        },
        {
            item_id: 8,
            item_name: 'Crocodile Slippers',
            cost: 30,
            image: '/items/item8.jpg',
            description: 'Cozy slippers designed to look like crocodiles, adding fun to your loungewear.',
        },
        {
            item_id: 9,
            item_name: 'Crocodile Phone Case',
            cost: 20,
            image: '/items/item9.jpg',
            description: 'A phone case with a crocodile skin texture, providing protection and style.',
        },
        {
            item_id: 10,
            item_name: 'Crocodile T-Shirt',
            cost: 25,
            image: '/items/item10.jpg',
            description: 'A cotton t-shirt featuring a graphic crocodile design, perfect for casual wear.',
        },
        {
            item_id: 11,
            item_name: 'Crocodile Flag',
            cost: 1000000000,
            image: '/items/flag.webp',
            description: 'A crocodile themed- hey wait who put this here???',
        },
    ];

    for (const item of items) {
        await prisma.items.upsert({
            where: { item_id: item.item_id },
            create: item,
            update: item
        });
    }
}

main()
    .catch((e) => {
        console.error(e);
        process.exit(1);
    })
    .finally(async () => {
        await prisma.$disconnect();
    });
