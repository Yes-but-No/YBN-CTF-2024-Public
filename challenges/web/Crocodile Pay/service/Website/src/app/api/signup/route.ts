import { NextRequest, NextResponse } from 'next/server';
import { PrismaClient } from '@prisma/client';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import { serialize } from 'cookie';
import crypto from 'crypto';
import { UserDetails } from '@/utils/types';


const prisma = new PrismaClient();

export async function POST(req: NextRequest) {
    try {
        const body = await req.json() as UserDetails;
        const { username, password } = body;
        
        if (!username || !password) {
            return NextResponse.json({ error: 'Username and password are required' }, { status: 400 });
        }
        if (username.match(/[^a-zA-Z0-9]/)) {
            return NextResponse.json({ error: 'Username must be alphanumeric' }, { status: 400 });
        }
        const userExists = await prisma.users.findFirst({
            where: { username },
        });
        if (userExists) {
            return NextResponse.json({ error: 'Username already exists' }, { status: 400 });
        }

        const hashedPassword = await bcrypt.hash(password, 10);
        const user_id = crypto.randomUUID();

        const pfps = [
            "/profiles/pfp1.jpg", "/profiles/pfp2.jpg", "/profiles/pfp3.jpg",
            "/profiles/pfp4.jpg", "/profiles/pfp5.jpg", "/profiles/pfp6.jpg",
            "/profiles/pfp7.jpg", "/profiles/pfp8.jpg", "/profiles/pfp9.jpg"
        ];
        const pfp = pfps[Math.floor(Math.random() * pfps.length)];

        const user = await prisma.users.create({
            data: { user_id, username, password: hashedPassword,profile_picture:pfp, balance: 1000 },
        });

        

        const token = jwt.sign(
            { id: user.user_id, name: user.username, profile: pfp },
            process.env.JWT_SECRET!,
            { expiresIn: '24h' }
        );

        const response = NextResponse.json({"message":"success"}, { status: 201 });
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
        console.error('User creation failed:', error);
        return NextResponse.json({ error: 'User creation failed' }, { status: 400 });
    }
}
