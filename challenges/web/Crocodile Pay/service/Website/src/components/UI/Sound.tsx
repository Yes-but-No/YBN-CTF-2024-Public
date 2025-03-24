"use client"
import { useEffect, useState } from "react";
import Image from "next/image";
import Cross from "../Icons/Cross";
export default function Sound() {
    const [isPlaying, setIsPlaying] = useState(true);
    const [audio, setAudio] = useState<HTMLAudioElement | null>(null);
    useEffect(() => {
        setAudio(new Audio("/Crocodile Pay.mp3"));
    }, []);

    const handleClick = () => {
        if (isPlaying && audio) {
            audio.pause();
        } else if (audio) {
            audio.play()
        }
        setIsPlaying((prev) => !prev);
    };
    useEffect(() => {
        if (localStorage.getItem("isPlaying") === "true") {
            setIsPlaying(true);
        } else {
            setIsPlaying(false);
        }
    },[])
    useEffect(() => {
        localStorage.setItem("isPlaying", isPlaying.toString());
    }, [isPlaying]);
    useEffect(() => {
        if (isPlaying && audio) {
            audio.play().catch((error) => {
                console.error("Error playing the sound:", error);
            });
        } else if (audio) {
            audio.pause();
        }

        return () => {
            audio?.pause();
        };
    }, [isPlaying, audio]);
    return (<div className="relative cursor-pointer hover:brightness-90 transition-all duration-100" onClick={handleClick}>
        <Image src = "/images/sound.png" alt = "sound" width="50" height="50"/>
        <Cross className = {`absolute scale-50 left-0 top-0 w-[50px] h-[50px] ${isPlaying?'hidden':''}`}/>
    </div>)
}