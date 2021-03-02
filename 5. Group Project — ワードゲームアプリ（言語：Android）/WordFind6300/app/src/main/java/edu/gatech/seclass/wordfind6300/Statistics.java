package edu.gatech.seclass.wordfind6300;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.PriorityQueue;

public class Statistics {
    private static Statistics instance = new Statistics();
    private static boolean fresh = true;

    public static boolean isFresh() {
        boolean ret = fresh;
        fresh = false;
        return ret;
    }

    public static Statistics getInstance() {
        return instance;
    }

    public static void setInstance(Statistics s) {
        fresh = false;
        instance = s;
    }

    private ArrayList<GameStatistic> gameStats = new ArrayList<>();
    private LinkedHashMap<String, WordStatistic> wordStats = new LinkedHashMap<>();

    public void merge(GameStatistic gs) {
        gameStats.add(gs);
    }

    public void updateWord(String word) {
        WordStatistic wordStatistic = wordStats.get(word);
        if(wordStatistic == null) {
            wordStatistic = WordStatistic.create(word);
            wordStats.put(word, wordStatistic);
        }
        wordStatistic.increment();
    }

    public ArrayList<GameStatistic> getGameStats() {
        return gameStats;
    }

    public HashMap<String, WordStatistic> getWordStats() {
        return wordStats;
    }

    public ArrayList<WordStatistic> wordStatisticsDescending() {
        PriorityQueue<WordStatistic> pq = new PriorityQueue<>(wordStats.values());
        ArrayList<WordStatistic> ret = new ArrayList<>();
        while(!pq.isEmpty()) {
            ret.add(pq.poll());
        }
        return ret;
    }

    public ArrayList<GameStatistic> gameStatisticsDescending() {
        PriorityQueue<GameStatistic> pq = new PriorityQueue<>(gameStats);
        ArrayList<GameStatistic> ret = new ArrayList<>();
        while(!pq.isEmpty()) {
            ret.add(pq.poll());
        }
        return ret;
    }
}
