package edu.gatech.seclass.wordfind6300;

import java.util.LinkedHashSet;

public class GameStatistic implements Comparable<GameStatistic> {
    private int score;
    private int numberOfResets;
    private LinkedHashSet<String> usedWords = new LinkedHashSet<>();
    private Settings settings;

    public GameStatistic(Settings settings) {
        this.settings = settings;
    }

    public boolean addWord(String word) {
        if(usedWords.add(word)) {
            score += word.length();
            Statistics.getInstance().updateWord(word);
        } else {
            return false;
        }
        return true;
    }

    public int getNumberOfResets() {
        return numberOfResets;
    }

    public int numberOfWords() {
        return usedWords.size();
    }

    public String bestWord() {
        if(usedWords.isEmpty()) {
            return "";
        }
        String bestWord = usedWords.iterator().next();
        for(String str : usedWords) {
            if(str.length() > bestWord.length()) {
                bestWord = str;
            }
        }
        return bestWord;
    }

    public void addReset() {
        numberOfResets++;
        score -= 5;
    }

    public int getScore() {
        return score;
    }

    @Override
    public int compareTo(GameStatistic o) {
        return o.getScore() - getScore();
    }

    public Settings getSettings() {
        return settings;
    }
}
