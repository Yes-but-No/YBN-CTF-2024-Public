import { NextRequest, NextResponse } from 'next/server';
import jwt from 'jsonwebtoken';
import { serialize } from 'cookie';


export async function POST(req: NextRequest, { params } : { params: Promise<{ adminToken: string }> }) {
  try {
    const body = await req.json();
    const { adminToken } = await params;
    const { userToken } = body;

    if (!userToken || !adminToken) {
      return NextResponse.json({ error: 'No token provided' }, { status: 401 });
    }
    if (adminToken !== process.env.ADMIN_TOKEN) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const decodedToken = jwt.verify(userToken, process.env.JWT_SECRET!);
    if (!decodedToken) {
      return NextResponse.json({ error: 'Invalid token' }, { status: 401 });
    }
    const response = NextResponse.json({ message: 'Login successful', userToken }, { status: 200 });
    response.headers.set(
      'Set-Cookie',
      serialize('token', userToken, {
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
