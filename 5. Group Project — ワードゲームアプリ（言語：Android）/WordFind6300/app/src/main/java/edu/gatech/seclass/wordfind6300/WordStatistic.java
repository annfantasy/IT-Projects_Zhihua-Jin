package edu.gatech.seclass.wordfind6300;

public class WordStatistic implements Comparable<WordStatistic> {
    private String word;
    private int numberOfTimesPlayed;

    public static WordStatistic create(String word) {
        return new WordStatistic(word);
    }

    public WordStatistic(String word) {
        this.word = word;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public int getNumberOfTimesPlayed() {
        return numberOfTimesPlayed;
    }

    public void increment() {
        numberOfTimesPlayed++;
    }

    @Override
    public int compareTo(WordStatistic o) {
        return o.numberOfTimesPlayed - numberOfTimesPlayed;
    }
}
