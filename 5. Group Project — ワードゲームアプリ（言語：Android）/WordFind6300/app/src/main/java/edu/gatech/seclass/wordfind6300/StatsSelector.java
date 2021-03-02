package edu.gatech.seclass.wordfind6300;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class StatsSelector extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stats_selector);
    }

    public void mainMenu(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }

    public void wordStats(View view) {
        Intent intent = new Intent(this, WordStats.class);
        startActivity(intent);
    }

    public void gameStats(View view) {
        Intent intent = new Intent(this, Stats.class);
        startActivity(intent);
    }
}
