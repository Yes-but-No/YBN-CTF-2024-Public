"use server"

import * as fs from "node:fs";
import path from "node:path";

type ResponseData = {
    valid: boolean,
    index: number | null,
    blob: string | null,
}

type RequestLocation = {
    lat: number | null,
    lng: number | null,
    model: string | null,
}

type Location = {
    name: string,
    lat: number,
    lng: number
}

const locations: Location[] = [
    {
        name: "Amanohashidate Station",
        lat: 35.55781000891381,
        lng: 135.18209563101678,
    },
    {
        name: "瑞岩弥勒造像",
        lat: 25.715814,
        lng: 119.470508,
    }
]

const blob_data = fs.readFileSync(path.resolve(process.cwd(), "travelling-intern"));
const totalSize = blob_data.length;
const numberOfLocations = locations.length + 1;

const split_blob: string[] = [];
let start = 0;

// Calculate start and end indices for each chunk
for (let i = 0; i < numberOfLocations; i++) {
    const end = Math.round(((i + 1) * totalSize) / numberOfLocations);
    split_blob.push(blob_data.subarray(start, end).toString("base64"));
    start = end;
}

const distance = (lat1: number, lng1: number, lat2: number, lng2: number): number => {
    const a = Math.abs(lat1 - lat2);
    const b = Math.abs(lng1 - lng2);

    return Math.sqrt(a * a + b * b);
}

export default async function Validate(
    req: RequestLocation
): Promise<ResponseData> {
    const lat = req.lat ?? 0;
    const lng = req.lng ?? 0;

    const model = req.model;

    if (model && model.toLowerCase() === "boeing 777-300er") {
        return { valid: true, index: split_blob.length - 1, blob: split_blob[split_blob.length - 1]};
    }

    const threshold = 0.005;
    const distances = locations.map((loc) => distance(loc.lat, loc.lng, lat, lng));

    const index = distances.findIndex(d => d <= threshold);

    if (index !== -1) {
        return { valid: true, index, blob: split_blob[index]};
    }

    return { valid: false, index: null, blob: null };
}