import { NextRequest, NextResponse } from 'next/server';
import jwt from 'jsonwebtoken';
import { PrismaClient } from '@prisma/client';
import { cookies } from 'next/headers';


const prisma = new PrismaClient();

export async function GET(req: NextRequest, { params } : { params: Promise<{ adminToken: string }> }) {
  try {
    // Extract cookies and token
    const cookieStore = await cookies();
    const userToken = cookieStore.get('token')?.value || null;
    const {adminToken} = await params;
    if (!userToken || !adminToken) {
      return NextResponse.json({ error: 'No token provided' }, { status: 401 });
    }
    if (adminToken !== process.env.ADMIN_TOKEN) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const secret = process.env.JWT_SECRET!;
    const decodedToken = jwt.verify(userToken, secret) as jwt.JwtPayload & { id: string };
    if (!decodedToken) {
      return NextResponse.json({ error: 'Invalid token' }, { status: 401 });
    }

    const cart: number[] = JSON.parse(req.nextUrl.searchParams.get('cart') || '[]');

    if (cart.length === 0) {
      return NextResponse.json({ error: 'Cart is Required' }, { status: 400 });
    }
    // Fetch prices from database
    const items = await prisma.items.findMany({
        select: { item_id: true, cost: true },
    });
    let totalCost = 0;
    let flag = false;

    for (const item of cart) {
        const dbItem = items.find((dbItem) => dbItem.item_id === item);
        if (!dbItem) {
            return NextResponse.json({ error: 'Item not found' }, { status: 404 });
        }
        totalCost += dbItem.cost;
        flag = flag || dbItem.item_id === 11;
    }

    const userBalance = await prisma.users.findFirst({
        where: { user_id: decodedToken.id },
        select: { balance: true },
    });
    if (!userBalance) {
        return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }
    if (userBalance.balance! < totalCost) {
        return NextResponse.json({ error: 'Insufficient balance' }, { status: 400 });
    }

    const response = NextResponse.json({ message: `Sufficient Balance. Items will be delivered shortly. 
                                            ${flag?"Seems you ordered flag too? How did you get enough money for that? Whatever here's the flag: "+ process.env.FLAG:""}`,
                                        amount: totalCost }, { status: 200 });
    return response
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
