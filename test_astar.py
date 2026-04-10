import numpy as np
from classical.astar import a_star


def test_astar_path_exists():
    grid = np.zeros((5, 5))

    path, explored = a_star(grid, (0, 0), (4, 4))

    assert path[0] == (0, 0)
    assert path[-1] == (4, 4)
    assert len(path) > 0


def test_astar_no_path():
    grid = np.ones((3, 3))  # all blocked

    grid[0, 0] = 0
    grid[2, 2] = 0

    path, explored = a_star(grid, (0, 0), (2, 2))

    assert path == []


def test_astar_start_equals_goal():
    grid = np.zeros((3, 3))

    path, explored = a_star(grid, (1, 1), (1, 1))

    assert path == [(1, 1)]


def test_astar_handles_obstacles():
    grid = np.zeros((5, 5))

    # Add obstacle wall
    grid[1, :] = 1
    grid[1, 2] = 0  # small gap

    path, explored = a_star(grid, (0, 0), (4, 4))

    assert path[0] == (0, 0)
    assert path[-1] == (4, 4)
    assert len(path) > 0


def test_astar_exploration_not_empty():
    grid = np.zeros((5, 5))

    path, explored = a_star(grid, (0, 0), (4, 4))

    assert len(explored) > 0