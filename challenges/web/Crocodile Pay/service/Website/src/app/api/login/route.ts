import { NextRequest, NextResponse } from 'next/server';
import { PrismaClient } from '@prisma/client';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import { serialize } from 'cookie';
import { UserDetails } from '@/utils/types';

const prisma = new PrismaClient();

export async function POST(req: NextRequest) {
  try {
    const body = await req.json() as UserDetails;
    const { username, password }: UserDetails = body;

    if (!username || !password) {
      return NextResponse.json({ error: 'Name and password are required' }, { status: 400 });
    }

    const user = await prisma.users.findFirst({
      where: { username },
      select: { user_id: true, username: true, password: true, profile_picture: true }, // Include fields needed for the JWT payload
    });

    if (!user) {
      return NextResponse.json({ error: 'User not found' }, { status: 404 });
    }

    const isPasswordValid = await bcrypt.compare(password, user.password!);
    if (!isPasswordValid) {
      return NextResponse.json({ error: 'Invalid password' }, { status: 401 });
    }

    const token = jwt.sign(
      { id: user.user_id, name: user.username, profile: user.profile_picture },
      process.env.JWT_SECRET!,
      { expiresIn: '24h' }
    );

    const response = NextResponse.json({ message: 'Login successful', token }, { status: 200 });
    response.headers.set(
      'Set-Cookie',
      serialize('token', token, {
        httpOnly: false,
        secure: false,
        sameSite: 'strict',
        maxAge: 3600, 
        path: '/',
      })
    );

    return response;

  } catch (error) {
    console.error('Login error:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
