import Image from "next/image";
import Button from "./Button";
import {ItemData} from "@/utils/types";
interface ItemProps {   
    data: ItemData,
    addToCart: (item: ItemData) => void

}
export default function Item({ data ,addToCart}: ItemProps) {
    const {item_name: name, cost: price, image, description } = data;
    return (
        <div className="flex flex-col bg-[#6EBF7B] p-4 m-4 rounded-lg shadow-lg h-96">
            <Image width = "200" height = "100" src = {image} className = "w-full h-48" alt ={name}/>
            <h2 className="text-3xl font-bold text-[#FDF9D1]">{name}</h2>
            <p className="text-xl text-[#F0E68A]">{description}</p>
            <div className="flex-grow"></div>
            <div className="flex flex-row gap-4 items-center"><p className="font-bold text-2xl text-[#F0E68A]">${price}</p><Button onClick = {() => addToCart(data)}>Add to Cart</Button></div>
            
        </div>
    )
}