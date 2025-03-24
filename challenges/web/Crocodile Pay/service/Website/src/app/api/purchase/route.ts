import { PrismaClient } from '@prisma/client';
import { NextRequest, NextResponse } from 'next/server';
import { cookies } from 'next/headers';

export async function POST(req: NextRequest) {
  try {
    // Parse the incoming request body
    const body = await req.json();
    const { cart } = body;

    // Extract the token from cookies
    const cookieStore = await cookies();
    const userToken = cookieStore.get('token')?.value || null;

    if (!userToken || !cart) {
      return NextResponse.json(
        { error: "Missing token or cart data" },
        { status: 400 }
      );
    }
    const ADMIN_URL = process.env.ADMIN_URL ?? "http://localhost:12345/visit"
    const response = await fetch(ADMIN_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', 
      },
      body: JSON.stringify({ userToken, cart }), 
    });

    const data = await response.json();

    return NextResponse.json(data, { status: response.status });
  } catch (error) {
    console.error('Error sending POST request:', error);
    return NextResponse.json(
      { error: 'Failed to send POST request to the external API' },
      { status: 500 }
    );
  }
}
