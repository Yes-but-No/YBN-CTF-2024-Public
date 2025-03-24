import React, { createContext } from 'react';

interface DuckPosition {
    x: number;
    y: number;
}

interface DuckPositionContextType {
    duckPos: DuckPosition;
    setDuckPosCtx: React.Dispatch<React.SetStateAction<DuckPosition>>;
}

export const DuckPositionContext = createContext<DuckPositionContextType>({
    duckPos: { x: 0, y: 0 },
    setDuckPosCtx: () => {},
});
