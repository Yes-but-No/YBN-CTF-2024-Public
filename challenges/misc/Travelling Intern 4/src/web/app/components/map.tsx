"use client"

import { APIProvider, Map, MapMouseEvent, Marker } from "@vis.gl/react-google-maps";
import { useContext, useState } from "react";
import Validate from "@/app/actions/validate";
import { DuckPositionContext } from "@/app/contexts/DuckPositionContext";

type CustomMarker = {
    id: number,
    lat: number,
    lng: number,
    isValid: boolean
}

export default function MapComponent() {
    const { duckPos } = useContext(DuckPositionContext);

    const [isLoading, setIsLoading] = useState(false);
    const [markers, setMarkers] = useState<CustomMarker[]>([]);

    const legendStyle = {
        position: 'fixed' as const,
        top: '20px',
        left: '20px',
        backgroundColor: 'white',
        padding: '15px',
        borderRadius: '10px',
        boxShadow: '0 2px 6px rgba(0,0,0,0.3)',
        zIndex: 1000,
        fontFamily: 'Arial, sans-serif',
        color: '#000000'
    };

    const legendItemStyle = {
        display: 'flex',
        alignItems: 'center',
        marginBottom: '8px'
    };

    const legendIconStyle = {
        width: '20px',
        height: '20px',
        marginRight: '8px'
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

    const onMapClick = async (e: any) => {
        const clickX = e.domEvent.clientX;
        const clickY = e.domEvent.clientY;

        const duckX = duckPos.x;
        const duckY = duckPos.y;
        const duckWidth = 69;
        const duckHeight = 69;

        if (
            clickX >= duckX &&
            clickX <= duckX + duckWidth &&
            clickY >= duckY &&
            clickY <= duckY + duckHeight
        ) {
            return;
        }

        setIsLoading(true);

        const data = {
            lat: e.detail.latLng?.lat ?? 0,
            lng: e.detail.latLng?.lng ?? 0,
            model: null
        }

        const id = markers.length + 1;

        setMarkers(cur => [...cur, {
            id: id,
            isValid: false,
            ...data
        }])

        const res = await Validate({
            ...data
        })

        setMarkers(cur => cur.map(marker =>
            marker.id === id
                ? { ...marker, isValid: res.valid }
                : marker
        ));

        setIsLoading(false);

        if (!res.valid) {
            return;
        }

        // Save file
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
    }

    return (
        <APIProvider apiKey="AIzaSyD8mSmcI-jLX0iO30u_eYhdG3M1OxHwa4Y">
            <div style={legendStyle}>
                <h3 style={{
                    marginTop: 0,
                    marginBottom: '15px',
                    paddingBottom: '8px',
                    borderBottom: '2px solid #333',
                    fontWeight: 'bold'
                }}>Legend</h3>
                <div style={legendItemStyle}>
                    <img
                        src="http://maps.google.com/mapfiles/ms/icons/green-dot.png"
                        style={legendIconStyle}
                        alt="Valid marker"
                    />
                    <span>— Valid Location</span>
                </div>
                <div style={legendItemStyle}>
                    <img
                        src="http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                        style={legendIconStyle}
                        alt="Invalid marker"
                    />
                    <span>— Invalid Location</span>
                </div>
            </div>

            <Map
                style={{ width: '100vw', height: '100vh' }}
                defaultCenter={{ lat: 22.54992, lng: 0 }}
                defaultZoom={3}
                gestureHandling={'greedy'}
                disableDefaultUI={true}
                onClick={onMapClick}
            >
                {markers.map((marker, i) => (
                    <Marker
                        key={i}
                        position={{
                            lat: marker.lat,
                            lng: marker.lng,
                        }}
                        icon={{
                            url: `http://maps.google.com/mapfiles/ms/icons/${marker.isValid ? 'green' : 'red'}-dot.png`
                        }}
                    />
                ))}
            </Map>

            {isLoading && (
                <div style={{
                    position: 'fixed',
                    top: 0,
                    left: 0,
                    width: '100%',
                    height: '100%',
                    backgroundColor: 'rgba(128, 128, 128, 0.7)',
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    zIndex: 1000
                }}>
                    <div className="loading-spinner" style={{
                        width: '50px',
                        height: '50px',
                        border: '5px solid #f3f3f3',
                        borderTop: '5px solid #3498db',
                        borderRadius: '50%',
                        animation: 'spin 1s linear infinite'
                    }}/>
                </div>
            )}
        </APIProvider>
    );
}
