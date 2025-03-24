"use client"
import { useEffect, useState } from "react";
import Item from "../../../components/UI/Item";
import {ItemData} from "@/utils/types";
import Shopping from "@/components/Icons/Shopping";
import ShoppingItem from "@/components/UI/ShoppingItem";
import Button from "@/components/UI/Button";
import jwt from "jsonwebtoken";
import { postRequest } from "@/utils/globals";
export default function Shop() {
    const [cart, setCart] = useState<ItemData[]>([])
    const [data, setData] = useState<ItemData[]>([])
    const [user, setUser] = useState<{name: string, profile: string | undefined}>({name: "", profile: undefined})
    useEffect(() => {
        fetch("/api/items")
        .then(res => res.json())
        .then(data => setData(data))
    }, [])

    const addToCart = (item: ItemData) => {
        setCart([...cart, item])
    }

    useEffect(() => {
        const token = document.cookie.split('; ').find(row => row.startsWith('token='))?.split('=')[1];
        const decodedToken = jwt.decode(token!);
        if (!decodedToken) {
            window.location.href = "/login"
        }
        const {name, profile} = decodedToken as {name: string, profile: string}
        setUser({name, profile})
    }, [])

    const onCheckOut = async () => {
        const cartIds = cart.map(item => item.item_id);
        const response = await postRequest('/api/purchase',{cart:cartIds});
        if (response.error){
            alert(response.error)
        }
        else{
            alert(response.result)
        }
    }
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
                <Button onClick = {onCheckOut}className = "text-3xl w-fit bg-[#6EBF7B]">Checkout</Button>
            </div>
        </section>
    )
}