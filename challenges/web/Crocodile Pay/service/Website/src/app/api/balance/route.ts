import { NextRequest, NextResponse } from 'next/server';
import jwt from 'jsonwebtoken';
import { PrismaClient } from '@prisma/client';
import { cookies } from 'next/headers';

const prisma = new PrismaClient();

export async function GET(req: NextRequest) {
  try {
    // Extract cookies and token
    const cookieStore = await cookies();
    const token = cookieStore.get('token')?.value || null;

    if (!token) {
      return NextResponse.json({ error: 'No token provided' }, { status: 401 });
    }

    const secret = process.env.JWT_SECRET!;
    const decodedToken = jwt.verify(token, secret) as jwt.JwtPayload & { id: string };
    if (!decodedToken) {
      return NextResponse.json({ error: 'Invalid token' }, { status: 401 });
    }

    // Extract balance 
    const user = await prisma.users.findFirst({
        where: { user_id: decodedToken.id },
        select: { balance: true },
        });
    if (!user) {
        return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }
    const balance = user.balance;
    return NextResponse.json({ balance }, { status: 200 });
  } catch (error) {
    console.error('Error:', error);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
