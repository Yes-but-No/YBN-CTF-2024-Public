import { NextRequest, NextResponse } from 'next/server';
import jwt from 'jsonwebtoken';
import { PrismaClient } from '@prisma/client';
import { cookies } from 'next/headers';

const prisma = new PrismaClient();

export async function GET(req: NextRequest, { params } : { params: Promise<{ adminToken: string }> } ) {
  try {
    // Extract cookies and token
    const cookieStore = await cookies();
    const userToken = cookieStore.get('token')?.value || null;
    const {adminToken} = await params;
    const deductToken = cookieStore.get('deductToken')?.value || null; // The more tokens = more secure, right?
    // The more tokens = more secure, right?

    if (!userToken || !adminToken || !deductToken) {
      return NextResponse.json({ error: 'No token provided' }, { status: 401 });
    }
    if (adminToken !== process.env.ADMIN_TOKEN) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 402 });
    }
    if (deductToken !== process.env.DEDUCT_TOKEN) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 403 });
    }
    const secret = process.env.JWT_SECRET!;
    const decodedToken = jwt.verify(userToken, secret) as jwt.JwtPayload & { id: string };
    if (!decodedToken) {
      return NextResponse.json({ error: 'Invalid token' }, { status: 401 });
    }

    const { searchParams } = req.nextUrl; 
    const amount = searchParams.get('amount'); 

    if (!amount) {
      return NextResponse.json({ error: 'Amount to update by is required' }, { status: 400 });
    }
    await prisma.users.update({
      where: { user_id: decodedToken.id },
      data: { balance: { increment: -parseInt(amount) } },
    });

    const response = NextResponse.json({ message: 'Balance updated successfully' }, { status: 200 });
    return response
  } catch (error) {
    console.error('Deduct error:', error);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
