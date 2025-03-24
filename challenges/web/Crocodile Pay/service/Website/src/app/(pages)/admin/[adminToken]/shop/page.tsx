"use client"
import { useEffect, useState } from "react";
import { useParams } from 'next/navigation';
import { getRequest } from "@/utils/globals";
import Item from "@/components/UI/Item";
import {ItemData} from "@/utils/types";
import Shopping from "@/components/Icons/Shopping";
import ShoppingItem from "@/components/UI/ShoppingItem";
import Button from "@/components/UI/Button";
import jwt from "jsonwebtoken";
export default function Shop() {
    
    const [cart, setCart] = useState<ItemData[]>([])
    const [data, setData] = useState<ItemData[]>([])
    const [user, setUser] = useState<{name: string, profile: string | undefined}>({name: "", profile: undefined})
    const [result, setResult] = useState<string>("")
    const addToCart = (item: ItemData) => {
        setCart([...cart, item])
    }
    const params = useParams();
    const adminToken = params.adminToken;

    const purchaseItems = async () => {
        const data = {
            cart: JSON.stringify(cart.map(item => item.item_id))
        }
        const response = await getRequest(`/api/admin/${adminToken}/purchase`, data)
        if (response && !response.error){
            setResult(response.message)
            const deductableAmount = response.amount
            await getRequest(`/api/admin/${adminToken}/deduct`, {amount: deductableAmount})
            
        } else {
            setResult(response.error)
        }
    }
    useEffect(() => {
        fetch("/api/items")
        .then(res => res.json())
        .then(data => setData(data))
    }, [])
    useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        if (params.has('cart')){
            const cartParam = JSON.parse(params.get('cart')!);
            for (const id of cartParam){
                const item = data.find(item => item.item_id === id);
                if (item){
                    setCart([...cart, item])
                }
            }
        }
        const token = document.cookie.split('; ').find(row => row.startsWith('token='))?.split('=')[1];
        const decodedToken = jwt.decode(token!);
        if (!decodedToken) {
            window.location.href = "/login"
        }
        const {name, profile} = decodedToken as {name: string, profile: string}
        setUser({name, profile})
    }, [data])
    

    return (
        <section>
            <h1 className="text-7xl text-center my-4 flex items-center justify-center gap-4">Welcome {user.name} <img className = "inline-block w-16 h-16 rounded-full" alt = "profile" src = {user.profile} /></h1>
            <div className="grid w-3/4 px-16">
                <div className="grid grid-cols-2">
                    {data.map((item, idx) => (
                        <Item key={idx} data={item} addToCart={addToCart} />
                    ))}
                </div>
                
            </div>
            <div className="flex flex-col fixed right-0 w-1/4 h-5/6 top-1/2 -translate-y-1/2 bg-[#FDF9D1] px-10  py-4">
                <div className="flex justify-evenly items-center my-4">
                    <Shopping />
                    <h2 className="text-4xl">List</h2>
                    
                </div>
                <div className="flex flex-col overflow-auto">
                    {cart.map((item,idx) => (
                        <ShoppingItem key = {idx} data = {item}/>
                    ))}
                </div>
                <div className="flex-grow"></div>
                <div className="flex flex-row justify-between py-2 border-t-2 border-secondary">
                    <p className="text-3xl font-bold">Total</p>
                    <p className="text-3xl text-tetriary font-bold" >${cart.reduce((acc, item) => acc + item.cost, 0)}</p>
                </div>
                <Button id = "purchase" className = "text-3xl w-fit bg-[#6EBF7B]" onClick = {purchaseItems}>Purchase</Button>
                <div id = "result">
                    {result}
                </div>
            </div>
        </section>
    )
}