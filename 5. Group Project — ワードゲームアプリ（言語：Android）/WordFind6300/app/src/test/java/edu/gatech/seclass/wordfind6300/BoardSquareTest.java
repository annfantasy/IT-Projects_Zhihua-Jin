package edu.gatech.seclass.wordfind6300;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import java.util.ArrayList;

import static edu.gatech.seclass.wordfind6300.BoardSquare.create;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

@RunWith(JUnit4.class)
public class BoardSquareTest {
    @Test
    public void boardSquareAdjacentOnX_returnsTrue() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(51,50);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.HORIZONTAL, result);
    }

    @Test
    public void boardSquareAdjacentOnXNegative_returnsTrue() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(49,50);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.HORIZONTAL, result);
    }

    @Test
    public void boardSquareAdjacentOnY_returnsTrue() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(50,51);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.VERTICAL, result);
    }

    @Test
    public void boardSquareAdjacentOnYNegative_returnsTrue() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(50,49);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.VERTICAL, result);
    }

    @Test
    public void boardSquareAdjacentOnYInvalid_returnsFalse() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(50,52);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.NONE, result);
    }

    @Test
    public void boardSquareAdjacentOnDiagonal_returnsTrue() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(49,49);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.DIAGONAL1, result);
    }

    @Test
    public void boardSquareAdjacentOnDiagonal2_returnsTrue() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(51,49);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.DIAGONAL3, result);
    }

    @Test
    public void boardSquareAdjacentOnDiagonal3_returnsTrue() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(51,51);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.DIAGONAL2, result);
    }

    @Test
    public void boardSquareAdjacentOnDiagonal4_returnsTrue() {
        BoardSquare boardSquare = create(50, 50);
        BoardSquare other = create(49,51);

        BoardSquare.Direction result = boardSquare.adjacent(other);

        assertEquals(BoardSquare.Direction.DIAGONAL4, result);
    }

    @Test
    public void listAdjacent_validInputVert_returnsTrue() {
        ArrayList<BoardSquare> list = new ArrayList<>();
        list.add(create(50,50));
        list.add(create(50,51));
        list.add(create(50,52));
        list.add(create(50,49));

        boolean result = BoardSquare.listAdjacent(list) == BoardSquare.Direction.NONE;

        assertFalse(result);
    }

    @Test
    public void listAdjacent_validInputHorz_returnsTrue() {
        ArrayList<BoardSquare> list = new ArrayList<>();
        list.add(create(50,50));
        list.add(create(51,50));
        list.add(create(52,50));
        list.add(create(49,50));

        boolean result = BoardSquare.listAdjacent(list) == BoardSquare.Direction.NONE;

        assertFalse(result);
    }

    @Test
    public void listAdjacent_validInputDiag_returnsTrue() {
        ArrayList<BoardSquare> list = new ArrayList<>();
        list.add(create(50,50));
        list.add(create(51,51));
        list.add(create(52,52));
        list.add(create(49,49));

        boolean result = BoardSquare.listAdjacent(list) == BoardSquare.Direction.NONE;

        assertFalse(result);
    }

    @Test
    public void listAdjacent_validInputDiagInvalid_returnsFalse() {
        ArrayList<BoardSquare> list = new ArrayList<>();
        list.add(create(50,50));
        list.add(create(51,51));
        list.add(create(52,52));
        list.add(create(49,51));

        boolean result = BoardSquare.listAdjacent(list) == BoardSquare.Direction.NONE;

        assertFalse(result);
    }

    @Test
    public void listAdjacent_validInputDiag2_returnsTrue() {
        ArrayList<BoardSquare> list = new ArrayList<>();
        list.add(create(10,0));
        list.add(create(9,1));
        list.add(create(8, 2));
        list.add(create(7,3));

        boolean result = BoardSquare.listAdjacent(list) == BoardSquare.Direction.NONE;

        assertFalse(result);
    }

    @Test
    public void listAdjacent_validInputDiag3_returnsTrue() {
        ArrayList<BoardSquare> list = new ArrayList<>();
        list.add(create(0,10));
        list.add(create(1,9));
        list.add(create(2, 8));
        list.add(create(3,7));

        boolean result = BoardSquare.listAdjacent(list) == BoardSquare.Direction.NONE;

        assertFalse(result);
    }
}
