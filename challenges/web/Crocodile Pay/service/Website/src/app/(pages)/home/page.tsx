import Image from "next/image"
import Link from "next/link"
export default function HomePage() {
    return (
        <>
        <section className = "h-screen flex flex-col justify-center items-center gap-10 relative px-20">
            <h1 className = "text-7xl text-tetriary drop-shadow-[0_0_4px_#D8C55A]">Crocodile Pay <Image src = "/images/croc1.png" alt = "croc" width="175" height="175" className = "absolute left-1/2 -translate-x-1/2 bottom-0 translate-y-10 -z-10"/> </h1>
            <h2 className= "text-4xl">Your Go to Service to pay for Crocoitems</h2>
        </section>
        <section className = "h-screen flex flex-col justify-center items-center gap-10 relative px-20">
            <Image src = "/images/hand.png" alt = "hand" width="300" height="300" className = "absolute left-0 bottom-1/2 translate-y-1/2 -z-10"/>
            <h2 className= "text-4xl w-1/2 text-center">Need a secure way to buy items for your crocodile pet? Crocodile Pay is your solution.</h2>
            <Image src = "/images/croc2.png" alt = "croc" width="300" height="300" className = "absolute right-0 bottom-1/2 translate-y-1/2 -z-10"/>
        </section>
        <section className = "h-screen flex flex-col justify-center items-end gap-10 relative px-20">
            <Image src = "/images/support.png" alt = "hand" width="400" height="400" className = "absolute left-1/4 -translate-x-1/2 bottom-1/2 translate-y-1/2 -z-10"/>
            <h2 className= "text-4xl w-1/2 text-center">The Number 1 most trusted form of payment</h2>
        </section>
        <section className = "h-screen flex flex-col justify-center items-center gap-10 relative px-20">
            <Link href = "/signup" className="w-3/4 flex justify-center items-center relative h-3/4">
                <Image src = "/images/catalog.png" alt = "hand" width="400" height="400" className = "absolute left-1/2 -translate-x-1/2 bottom-1/2 translate-y-1/2 -z-10 w-full h-full"/>
                <h2 className= "text-6xl w-1/2 text-center">Click to Browse our Vast catalog</h2>
            </Link>
        </section>
        </>
    )
}