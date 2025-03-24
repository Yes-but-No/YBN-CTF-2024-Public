import Link from "next/link";

export default function NavItem({ children, link }: { children: React.ReactNode; link?: string }) {
    const baseClasses = "text-lg md:text-xl font-medium text-white px-3 py-2 transition duration-200";
    const hoverClasses = "hover:text-blue-300 focus-visible:ring-2 focus-visible:ring-blue-400";
    const activeClasses = "active:text-blue-400";

    return (
        <>
            {link ? (
                <Link 
                    className={`${baseClasses} ${hoverClasses} ${activeClasses}`} 
                    href={link}
                    aria-label={children?.toString()}
                >
                    {children}
                </Link>
            ) : (
                <div 
                    className={`${baseClasses} ${hoverClasses} ${activeClasses}`} 
                    tabIndex={0}
                >
                    {children}
                </div>
            )}
        </>
    );
}
