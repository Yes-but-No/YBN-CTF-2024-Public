// index.js
const express = require('express')
const path = require('path')
const app = express()
const port = 3000   

function solve(graph) {
    const queue = [];
    const visited = new Set();
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]];

    // Add the initial position (0, 0) along with an empty path to the queue
    queue.push({ position: [0, 0], path: [] });

    while (queue.length > 0) {
        const length = queue.length;
        
        for (let i = 0; i < length; i++) {
            // Dequeue the first element
            const { position, path } = queue.shift();
            const altitude = graph[position[0]][position[1]].altitude;
            const [x, y] = position;

            // Skip invalid or already visited positions
            if (x < 0 || x >= graph.length || y < 0 || y >= graph[0].length || visited.has([x, y].toString())) {
                continue;
            }

            // Mark the position as visited
            visited.add([x, y].toString());

            // If the cell is a wall, skip it
            if (graph[x][y].type === "wall") {
                continue;
            }

            // If the cell is an endpoint, return the path
            if (graph[x][y].type === "endpoint") {
                return path;
            }

            // If the cell is empty, explore its neighbors
            for (const [dx, dy] of directions) {
                const newX = x + dx;
                const newY = y + dy;
                if (newX < 0 || newX >= graph.length || newY < 0 || newY >= graph[0].length) {
                    continue;
                }
                const newAltitude = graph[newX][newY].altitude;
                if (newAltitude - altitude > 1) {
                    continue;
                }
                queue.push({
                    position: [newX, newY],
                    path: [...path, [dx, dy]] // Add the current direction to the path
                });
            }
        }
    }

    // If no path is found, return an empty array
    return [];
}

app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'ejs');
app.use('/static', express.static(path.join(__dirname, 'static')));

app.get('/', (req,res) => {
    res.render('index');
})

app.get('/graph', (req,res) => {
    res.render('graph', {graph:null, path:null});
})


app.post('/graph', (req,res) => {
    const data = JSON.parse(req.body.data)
    const graph = []
    const size = 10
    for (let i = 0; i < size; i++) {
        const row = []
        for (let j = 0; j < size; j++) {
            row.push({"type": "empty", "altitude": 0})
        }
        graph.push(row)
    }
    const points = data.points
    console.log(points)
    for (let i = 0; i < points.length; i++) {
        const {x, y, typeOrAlt, value} = points[i]
        graph[x][y][typeOrAlt] = value
    }
    
    const path = solve(graph)
    res.render('graph', {graph, path});
})
app.listen(port, () => {
  console.log(`Graph Theory Solver listening on port ${port}`)
})