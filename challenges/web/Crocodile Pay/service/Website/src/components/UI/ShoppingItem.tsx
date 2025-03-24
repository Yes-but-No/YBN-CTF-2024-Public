import {ItemData} from "@/utils/types";
interface ItemProps {   
    data: ItemData

}
export default function ShoppingItem({ data : {item_name: name, cost: price}}: ItemProps) {
    return (
        <div className="flex flex-row justify-between py-2 px-2 ">
            <p className="text-3xl font-bold">{name}</p>
            <p className="text-3xl font-bold text-tetriary">${price}</p>
        </div>
    )
}