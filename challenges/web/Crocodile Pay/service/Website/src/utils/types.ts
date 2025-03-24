interface UserDetails {
    username: string;
    password: string;
}
interface ItemData {
    item_name: string;
    cost: number;
    image: string;
    description: string;
    item_id: number;
}

export type {UserDetails, ItemData}