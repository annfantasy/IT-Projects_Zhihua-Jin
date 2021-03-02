package edu.gatech.seclass.wordfind6300;

import com.google.auto.value.AutoValue;
import com.google.common.base.Preconditions;

import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;

@AutoValue
public abstract class BoardSquare implements Comparable<BoardSquare> {
    public abstract int x();
    public abstract int y();

    public static BoardSquare create(int x, int y) {
        return new AutoValue_BoardSquare(x, y);
    }

    public enum Direction {
        NONE(false),
        HORIZONTAL(false),
        VERTICAL(false),
        DIAGONAL1(false),
        DIAGONAL2(false),
        DIAGONAL3(true),
        DIAGONAL4(false);

        private boolean reverse;

        Direction(boolean reverse) {
            this.reverse = reverse;
        }

        public boolean isReverse() {
            return reverse;
        }
    }

    public Direction adjacent(BoardSquare other) {
        if(y() == other.y() && (x() - 1 == other.x() || x() + 1 == other.x())) {
            return Direction.HORIZONTAL;
        }
        if(x() == other.x() && (y() - 1 == other.y() || y() + 1 == other.y())) {
            return Direction.VERTICAL;
        }
        if(x() - 1 == other.x() && y() - 1 == other.y()) {
            return Direction.DIAGONAL1;
        }
        if(x() + 1 == other.x() && y() + 1 == other.y()) {
            return Direction.DIAGONAL2;
        }
        if(x() + 1 == other.x() && y() - 1 == other.y()) {
            return Direction.DIAGONAL3;
        }
        if(x() - 1 == other.x() && y() + 1 == other.y()) {
            return Direction.DIAGONAL4;
        }
        return Direction.NONE;
    }

    @Override
    public int compareTo(BoardSquare boardSquare) {
        // I think this is more important being consistent rather than right.
        // Worst case, switch to O(n^2) solution, there's only up to like 8 squares at most.
        if (x() > boardSquare.x()) {
            return 1;
        } else if(x() == boardSquare.x() && y() > boardSquare.y()) {
            return 1;
        } else if(x() == boardSquare.x() && y() == boardSquare.y()) {
            return 0;
        } else if(y() > boardSquare.y()) {
            return 1;
        }
        return -1;
    }

    /** Checks to see if the {@link BoardSquare} are all next to each other in the same fashion. */
    public static Direction listAdjacent(List<BoardSquare> boardSquares) {
//        Preconditions.checkArgument(!boardSquares.isEmpty(), "Expects at least 1 in it.");
////        if(boardSquares.size() == 1) {
////            return Direction.HORIZONTAL;
////        }
////        PriorityQueue<BoardSquare> queue = new PriorityQueue<>(boardSquares);
////        BoardSquare first = queue.poll();
////        BoardSquare current = queue.poll();
////        Direction direction = first.adjacent(current);
////        while(direction != Direction.NONE && !queue.isEmpty()) {
////            BoardSquare next = queue.poll();
////            if(Direction.NONE != current.adjacent(next)) {
////                return Direction.NONE;
////            }
////            current = next;
////        }
////        return direction;
//        for(int i = 0; i < boardSquares.size(); i++) {
//            boolean foundAdj = false;
//            BoardSquare current = boardSquares.get(i);
//            for(int j = 0; j < boardSquares.size(); j++) {
//                if(i == j) {
//                    continue;
//                }
//                BoardSquare possible = boardSquares.get(j);
//                if(current.adjacent(possible) != Direction.NONE) {
//                    foundAdj = true;
//                    break;
//                }
//            }
//            if(!foundAdj) {
//                return Direction.NONE;
//            }
//        }
        for(BoardSquare bs : boardSquares) {
            HashSet<BoardSquare> visited = new HashSet<>();
            visited.add(bs);
            if(listAdjacent(boardSquares, bs, visited) != Direction.NONE) {
                return Direction.HORIZONTAL;
            }
        }
        return Direction.NONE;
    }

    private static Direction listAdjacent(List<BoardSquare> boardSquares, BoardSquare current, HashSet<BoardSquare> visited) {
        if(visited.size() == boardSquares.size()) {
            return Direction.HORIZONTAL;
        }
        for(BoardSquare bs : boardSquares) {
            if(bs.adjacent(current) != Direction.NONE && !visited.contains(bs)) {
                visited.add(bs);
                if(listAdjacent(boardSquares, bs, visited) != Direction.NONE) {
                    return Direction.HORIZONTAL;
                }
                visited.remove(bs);
            }
        }
        return Direction.NONE;
    }
}
