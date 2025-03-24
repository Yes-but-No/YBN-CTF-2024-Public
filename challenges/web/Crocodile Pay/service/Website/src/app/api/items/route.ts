import { PrismaClient } from '@prisma/client';
import { NextResponse } from 'next/server';

const prisma = new PrismaClient();

export async function GET() {
  const items = await prisma.items.findMany();
  return NextResponse.json(items);
}
