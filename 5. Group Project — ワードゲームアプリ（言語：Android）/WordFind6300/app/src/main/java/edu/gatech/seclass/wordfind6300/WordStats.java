package edu.gatech.seclass.wordfind6300;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TableLayout;
import android.widget.TextView;

import java.util.ArrayList;

public class WordStats extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_word_stats);
        TableLayout layout = findViewById(R.id.word_stats_table);
        ArrayList<WordStatistic> stats = Statistics.getInstance().wordStatisticsDescending();
        for(WordStatistic ws : stats) {
            TextView textView = new TextView(this);
            textView.setText(String.format("%s was played %d", ws.getWord(), ws.getNumberOfTimesPlayed()));
            layout.addView(textView);
        }
    }

    public void mainMenu(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}
