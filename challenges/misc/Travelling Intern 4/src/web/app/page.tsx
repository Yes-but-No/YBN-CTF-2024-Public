"use client"

import MapComponent from "@/app/components/map";
import DuckComponent from "@/app/components/duck";
import { useState } from "react";
import { DuckPositionContext } from "@/app/contexts/DuckPositionContext";

export default function Home() {
    const [duckPos, setDuckPosCtx] = useState({ x: 0, y: 0 });

    return (
        <main className="relative h-screen">
            <DuckPositionContext.Provider value={{ duckPos, setDuckPosCtx }}>
                <DuckComponent/>
                <MapComponent/>
            </DuckPositionContext.Provider>
        </main>
    );
}
