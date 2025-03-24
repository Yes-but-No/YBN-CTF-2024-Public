import { NextRequest, NextResponse } from 'next/server';
import jwt from 'jsonwebtoken';
import { PrismaClient } from '@prisma/client';
import { serialize } from 'cookie';
import { cookies } from 'next/headers';

const prisma = new PrismaClient();

interface UserDetails {
  username: string;
  profile: string;
}

export async function POST(req: NextRequest, { params } : { params: Promise<{ adminToken: string }> }) {
  try {
    const cookieStore = await cookies();
    const { adminToken } = await params
    const token = cookieStore.get("token")?.value || null;

    if (!token || !adminToken) {
      return NextResponse.json({ error: 'No token provided' }, { status: 401 });
    }
    if (adminToken !== process.env.ADMIN_TOKEN) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const secret = process.env.JWT_SECRET!;
    const decodedToken = jwt.verify(token, secret) as jwt.JwtPayload; 
    if (!decodedToken) {
      return NextResponse.json({ error: 'Invalid token' }, { status: 401 });
    }

    const body = await req.json() as UserDetails;
    const { username, profile }: UserDetails = body;

    if (!username || !profile) {
      return NextResponse.json({ error: 'Username and profile picture are required' }, { status: 400 });
    }

    prisma.users.update({
        where: { user_id: decodedToken.id },
        data: { username, profile_picture: profile },
    });

    const newToken = jwt.sign(
        { id: decodedToken.id, name: username, profile },
        secret,
        { expiresIn: '24h' }
    );
    
    const response = NextResponse.json({ message: 'Profile updated successfully', newToken }, { status: 200 });
    response.headers.set(
        'Set-Cookie',
        serialize('token', token, {
          httpOnly: false,
          secure: process.env.NODE_ENV === 'production',
          sameSite: 'strict',
          maxAge: 3600, 
          path: '/',
        })
      );


    return response;
  } catch (error) {
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 401 });
  }
}
