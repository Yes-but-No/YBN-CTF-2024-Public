Program the robot's path to navigate in lakes, land, mountains, and mine fields.

Download the elevation map of the terrain (map.csv). The map is on a grid made out of cells, where the robot can move from each cell (x, y) to any of its 8 neighbours, (x + a, y + b) where −1 ≤ a ≤ 1, −1 ≤ b ≤ 1, a + b ≥ 1.

The robot starts from the bottom left of the map. What is the robot’s lowest cost to reach the enemy base position at top right of the map? 
Round the lowest cost to 1 decimal place.

Within the elevation map:
- Positive values give elevation above ground level.
- Negative values give depth of lake.
- x represents a mine, robot cannot move to.

The energy cost of taking a step is the sum of horizontal cost and climbing cost, where:
- Horizontal cost: √(a^2 + b^2)
- Climbing cost (regardless of what type of land robot moves from):
	- For moving to land and mountains: 5 times the increase in elevation (no climbing cost if going to the same or lower elevation)
	- For moving to lakes: 10 times the increase in elevation (no climbing cost if going to the same or lower elevation)

Flag:
YBN24{<lowest cost to nearest 1 dp>}
E.g. YBN24{900.1}