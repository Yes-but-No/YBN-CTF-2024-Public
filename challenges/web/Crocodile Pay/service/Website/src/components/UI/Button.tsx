import { twMerge } from 'tailwind-merge'

interface ButtonProps {
    children: React.ReactNode;
    className?: string;
    onClick?: () => void;
    id?: string;
}
export default function Button({ children, className, onClick, id }: ButtonProps) {
    const newClassName = twMerge('bg-[#D8C55A] text-black px-8 py-1 rounded-full shadow-lg hover:brightness-90 transition-all duration-200',className)
    return (
        <button id = {id} onClick = {onClick} className = {newClassName}>
            {children}
        </button>
    )
}