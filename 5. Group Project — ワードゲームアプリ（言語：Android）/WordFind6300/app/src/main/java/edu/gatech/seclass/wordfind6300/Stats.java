package edu.gatech.seclass.wordfind6300;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TableLayout;
import android.widget.TextView;

import java.util.ArrayList;

public class Stats extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stats);
        TableLayout layout = findViewById(R.id.game_table_stats);
        ArrayList<GameStatistic> stats = Statistics.getInstance().gameStatisticsDescending();
        for(final GameStatistic gs : stats) {
            TextView textView = new TextView(this);
            textView.setClickable(true);
            final Activity activity = this;
            textView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    AlertDialog.Builder alertDialog = new AlertDialog.Builder(activity);
                    Settings settings = gs.getSettings();
                    alertDialog.setMessage("Game Board Size: " + settings.sizeOfBoard() + " Length of game: " + settings.lengthOfGame() + " Highest played word: " + gs.bestWord());
                    alertDialog.setNeutralButton("OK", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {}
                    });
                    alertDialog.show();
                }
            });
            textView.setText(String.format("final score: %d number of resets: %d number of words: %d", gs.getScore(), gs.getNumberOfResets(), gs.numberOfWords()));
            layout.addView(textView);
        }
    }

    public void mainMenu(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}
