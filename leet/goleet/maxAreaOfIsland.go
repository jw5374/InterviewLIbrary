package main

func MaxAreaOfIsland(grid [][]int) int {
    var res int = 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 0 {
                continue
            }
            grid[i][j] = 0
            islandArea := checkNeighbors(i, j, &grid)
            if res < islandArea {
                res = islandArea
            }
        }
    }
    return res
}

func checkNeighbors(i int, j int, grid *[][]int) int {
    var (
        neighbors [][]int
        res int = 1
    )
    neighbors = append(neighbors, neighborCells(i, j, grid)...)
    for len(neighbors) > 0 {
        currCell, newNeighbors := neighbors[0], neighbors[1:]
        neighbors = newNeighbors
        if (*grid)[currCell[0]][currCell[1]] == 0 {
            continue
        }
        (*grid)[currCell[0]][currCell[1]] = 0
        neighbors = append(neighbors, neighborCells(currCell[0], currCell[1], grid)...)
        res++
    }
    return res
}

func neighborCells(i int, j int, grid *[][]int) [][]int {
    var potentialN [][]int = [][]int{
            { i+1, j },
            { i-1, j },
            { i, j+1 },
            { i, j-1 },
        }
    var res [][]int
    for _, n := range potentialN {
        if (n[0] < 0 || n[0] > len(*grid)-1) || (n[1] < 0 || n[1] > len((*grid)[0])-1) {
            continue
        }
        if (*grid)[n[0]][n[1]] != 0 {
            res = append(res, n)
        }
    }
    return res
}
