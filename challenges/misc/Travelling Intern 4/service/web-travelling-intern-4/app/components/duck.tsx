"use client";

import { useContext, useEffect, useRef, useState } from "react";
import Image from "next/image";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { DuckPositionContext } from "@/app/contexts/DuckPositionContext";
import Validate from "@/app/actions/validate";
import { toast } from "@/hooks/use-toast";

export default function DuckComponent() {
    const [duckPos, setDuckPos] = useState({ x: 0, y: 0 });
    const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
    const [lastUpdate, setLastUpdate] = useState(0);
    const [direction, setDirection] = useState("right");
    const [isMoving, setIsMoving] = useState(true);
    const [isFormOpen, setIsFormOpen] = useState(false);

    const { setDuckPosCtx } = useContext(DuckPositionContext);

    const SPEED = 3;
    const THRESHOLD = 10;
    const FRAME_TIME = 1000 / 60;

    const duckPosRef = useRef(duckPos);
    const mousePosRef = useRef(mousePos);
    const lastUpdateRef = useRef(lastUpdate);

    useEffect(() => {
        duckPosRef.current = duckPos;
        setDuckPosCtx(duckPos);
    }, [duckPos]);

    useEffect(() => {
        mousePosRef.current = mousePos;
    }, [mousePos]);

    useEffect(() => {
        lastUpdateRef.current = lastUpdate;
    }, [lastUpdate]);

    const handleMouseMove = (e: any) => {
        setMousePos({ x: e.clientX, y: e.clientY });
    };

    const base64ToUint8Array = (base64: string): Uint8Array => {
        const binary_string = window.atob(base64);
        const len = binary_string.length;
        const bytes = new Uint8Array(len);
        for (let i = 0; i < len; i++) {
            bytes[i] = binary_string.charCodeAt(i);
        }
        return bytes;
    }

    useEffect(() => {
        window.addEventListener("mousemove", handleMouseMove);

        const moveTowardsMouse = (currentTime: any) => {
            if (currentTime - lastUpdateRef.current < FRAME_TIME) {
                requestAnimationFrame(moveTowardsMouse);
                return;
            }

            const dx = mousePosRef.current.x - duckPosRef.current.x - 50;
            const dy = mousePosRef.current.y - duckPosRef.current.y - 50;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance > THRESHOLD) {
                const vx = (dx / distance) * SPEED;
                const vy = (dy / distance) * SPEED;

                setDuckPos((prev) => {
                    const newX = prev.x + vx;
                    const newY = prev.y + vy;

                    // Update direction based on horizontal velocity
                    const newDirection = vx < 0 ? "left" : "right";
                    setDirection(newDirection);

                    return { x: newX, y: newY };
                });

                setIsMoving(true); // Duck is moving
            } else {
                setIsMoving(false); // Duck stops moving
            }

            setLastUpdate(currentTime);
            requestAnimationFrame(moveTowardsMouse);
        };

        const animationId = requestAnimationFrame(moveTowardsMouse);

        // Global click handler
        const handleDocumentClick = (e: any) => {
            const clickX = e.clientX;
            const clickY = e.clientY;

            // Get duck's position and size
            const duckX = duckPosRef.current.x;
            const duckY = duckPosRef.current.y;
            const duckWidth = 69;
            const duckHeight = 69;

            // Check if click is within the duck's bounding box
            if (
                clickX >= duckX &&
                clickX <= duckX + duckWidth &&
                clickY >= duckY &&
                clickY <= duckY + duckHeight
            ) {
                e.stopPropagation();
                e.preventDefault();
                setIsFormOpen(true);
            }
        };

        document.addEventListener("click", handleDocumentClick);

        return () => {
            window.removeEventListener("mousemove", handleMouseMove);
            cancelAnimationFrame(animationId);
            document.removeEventListener("click", handleDocumentClick);
        };
    }, []);

    return (
        <>
            <Image
                src={isMoving ? "/sprites/duck-waddle.gif" : "/sprites/duck-still.png"}
                alt={"Duck Waddling"}
                width={69}
                height={69}
                style={{
                    position: "absolute",
                    left: duckPos.x,
                    top: duckPos.y,
                    zIndex: 10,
                    pointerEvents: "none", // Allow events to pass through
                    transform: direction === "left" ? "scaleX(-1)" : "none",
                    transformOrigin: "center",
                }}
            />

            {/* Dialog for the input form */}
            <Dialog open={isFormOpen} onOpenChange={setIsFormOpen}>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>Plane Model</DialogTitle>
                        <DialogDescription>
                            Please help me find the model of my plane!
                        </DialogDescription>
                    </DialogHeader>
                    <form
                        onSubmit={async (e: any) => {
                            e.preventDefault();

                            const res = await Validate({
                                lat: null,
                                lng: null,
                                model: e.target.model.value,
                            })

                            setIsFormOpen(false); // Close the form after submission

                            if (!res.valid) {
                                toast({
                                    variant: "destructive",
                                    title: "Wrong Aircraft Model",
                                    description: "Wrong aircraft model specified. Please try again.",
                                });
                                return;
                            }

                            const bytes = base64ToUint8Array(res.blob ?? "");
                            const blob = new Blob([bytes], { type: 'application/octet-stream' });
                            const url = URL.createObjectURL(blob);
                            const link = document.createElement('a');
                            link.href = url;
                            link.download = `binary-${res.index}`;  // TODO: Set proper filename
                            document.body.appendChild(link);
                            link.click();
                            document.body.removeChild(link);
                            URL.revokeObjectURL(url);

                            toast({
                                title: "Congratulations!",
                                description: "The aircraft model is correct!",
                            })
                        }}
                    >
                        <div className="space-y-4 py-4">
                            <div>
                                <Label htmlFor="model">Model</Label>
                                <Input id="model" placeholder="Airbus A350-900ULR" required/>
                            </div>
                        </div>
                        <DialogFooter>
                            <Button type="submit">Submit</Button>
                            <Button
                                variant="secondary"
                                onClick={() => setIsFormOpen(false)}
                            >
                                Cancel
                            </Button>
                        </DialogFooter>
                    </form>
                </DialogContent>
            </Dialog>
        </>
    );
}
