package edu.gatech.seclass.wordfind6300;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Random;

public class Game {
    private char[][] boardState;
    private Settings settings;
    private GameStatistic gameStatistic;

    static final HashSet<Character> VOWELS_SET = new HashSet<>();
    static {
        VOWELS_SET.add('a');
        VOWELS_SET.add('e');
        VOWELS_SET.add('i');
        VOWELS_SET.add('o');
        VOWELS_SET.add('u');
    }

    public Game() {
        this.settings = Settings.getInstance();
        gameStatistic = new GameStatistic(settings);
        createBoard();
    }

    public void reset() {
        gameStatistic.addReset();
        createBoard();
    }

    public void createBoard() {
        boardState = new char[settings.sizeOfBoard()][settings.sizeOfBoard()];
        int totalLetters = settings.sizeOfBoard() * settings.sizeOfBoard();
        int vowels = (int)Math.ceil(totalLetters * .2);
        Random random = new Random();
        random.setSeed(System.currentTimeMillis());
        ArrayList<Character> vowelsToSelect = new ArrayList<>();
        for(Character c : VOWELS_SET) {
            for(int i = 0; i < settings.weightOfLetters().get(c); i++) {
                vowelsToSelect.add(c);
            }
        }
        ArrayList<Character> otherLetters = new ArrayList<>();
        for(char c = 'a'; c <= 'z'; c++) {
            if(VOWELS_SET.contains(c)) {
                continue;
            }
            for(int i = 0; i < settings.weightOfLetters().get(c); i++) {
                otherLetters.add(c);
            }
        }
        for(int i = 0; i < settings.sizeOfBoard(); i++) {
            for(int j = 0; j < settings.sizeOfBoard(); j++) {
                if(vowels > 0) {
                    boolean vowel;
                    if(totalLetters == vowels) {
                        vowel = true;
                    } else {
                        vowel = random.nextInt(101) <= 25;
                    }
                    if(vowel) {
                        boardState[i][j] = vowelsToSelect.get(random.nextInt(vowelsToSelect.size()));
                        vowels--;
                    } else {
                        boardState[i][j] = otherLetters.get(random.nextInt(otherLetters.size()));
                    }
                } else {
                    boardState[i][j] = otherLetters.get(random.nextInt(otherLetters.size()));
                }
                totalLetters--;
            }
        }
    }

    public int finishGame() {
        Statistics.getInstance().merge(gameStatistic);
        return gameStatistic.getScore();
    }

    public boolean playWord(List<BoardSquare> list) {
        if(list.isEmpty()) {
            return false;
        }
        BoardSquare.Direction dir = BoardSquare.listAdjacent(list);
        if(dir == BoardSquare.Direction.NONE) {
            return false;
        }
        String word = getWord(list);
//        if(dir.isReverse()) {
//            word = new StringBuilder().append(word).reverse().toString();
//        }
        if(!gameStatistic.addWord(word)) {
            return false;
        }
        for(BoardSquare bs : list) {
            clearSquare(bs);
        }
        return true;
    }

    public String getWord(List<BoardSquare> list) {
//        PriorityQueue<BoardSquare> squares = new PriorityQueue<>(list);
        StringBuilder word = new StringBuilder();
        for(BoardSquare bs : list) {
            String square = getBoardSquare(bs);
            word.append(square);
        }
        return word.toString();
    }

    public String getBoardSquare(BoardSquare boardSquare) {
        String s = String.valueOf(boardState[boardSquare.x()][boardSquare.y()]);
        if(s.equals("q")) {
            s = "qu";
        }
        return s;
    }

    public void clearSquare(BoardSquare boardSquare) {
        boardState[boardSquare.x()][boardSquare.y()] = ' ';
    }
}
