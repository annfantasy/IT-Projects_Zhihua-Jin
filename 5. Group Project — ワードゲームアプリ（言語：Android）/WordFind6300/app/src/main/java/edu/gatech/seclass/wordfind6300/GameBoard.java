package edu.gatech.seclass.wordfind6300;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.Gravity;
import android.view.View;
import android.widget.CompoundButton;
import android.widget.LinearLayout;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.widget.ToggleButton;

import java.util.ArrayList;

public class GameBoard extends AppCompatActivity {
    private CountDownTimer countDownTimer;
    private Game game = new Game();
    private ArrayList<BoardSquare> checked = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game_board);
        Settings settings = Settings.getInstance();
        final TextView timer = findViewById(R.id.timer);
        timer.setText(getTime(settings.lengthOfGame() * 60 * 1000));
        countDownTimer = new CountDownTimer(settings.lengthOfGame() * 60 * 1000, 1000) {
            @Override
            public void onTick(long millisUntilFinished) {
                timer.setText(getTime(millisUntilFinished));
            }

            @Override
            public void onFinish() {
                exit(null);
            }
        };
        createBoard();
        countDownTimer.start();
    }

    private String getTime(long countdownMillis) {
        long minutes = countdownMillis / 1000 / 60;
        long seconds = countdownMillis / 1000 % 60;
        return String.format("Minutes %d Seconds %d", minutes, seconds);
    }

    public void createBoard() {
        checked.clear();
        TableLayout layout = findViewById(R.id.game_board);
        layout.removeAllViews();
        Settings settings = Settings.getInstance();
        for(int i = 0; i < settings.sizeOfBoard(); i++) {
            TableRow row = new TableRow(this);
            layout.addView(row);
            for(int j = 0; j < settings.sizeOfBoard(); j++) {
                ToggleButton toggleButton = new ToggleButton(this);
//                toggleButton.setMinWidth(0);
//                toggleButton.setMinHeight(0);
//                toggleButton.setWidth(layout.getWidth()/settings.sizeOfBoard());
//                toggleButton.setHeight(layout.getHeight()/settings.sizeOfBoard());
//                toggleButton.setPadding(10,10,0,0);
//                toggleButton.setGravity(Gravity.LEFT);
                final BoardSquare pos = BoardSquare.create(i, j);
                final String square = game.getBoardSquare(pos);
                toggleButton.setLayoutParams(new TableRow.LayoutParams((int)toggleButton.getPaint().measureText("A") * 4, TableRow.LayoutParams.WRAP_CONTENT));
                toggleButton.setText(square);
                if(square.isEmpty() || square.equals(" ")) {
                    toggleButton.setClickable(false);
                }
                toggleButton.setTextOff(square);
                toggleButton.setTextOn(square);
                row.addView(toggleButton);
                toggleButton.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
                    @Override
                    public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                        if(isChecked) {
                            checked.add(pos);
                        } else {
                            checked.remove(pos);
                        }
                    }
                });
            }
        }
    }

    public void submit(View view) {
        if(checked.size() < 2 || !game.playWord(checked)) {
            AlertDialog.Builder alertDialog = new AlertDialog.Builder(this);
            alertDialog.setMessage("Invalid word " + game.getWord(checked));
            final Activity activity = this;
            alertDialog.setNeutralButton("OK", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                }
            });
            alertDialog.show();
        }
        createBoard();
    }

    public void reset(View view) {
        game.reset();
        createBoard();
    }

    public void exit(View view) {
        countDownTimer.cancel();
        AlertDialog.Builder alertDialog = new AlertDialog.Builder(this);
        alertDialog.setMessage("Your score is " + game.finishGame());
        final Activity activity = this;
        alertDialog.setNeutralButton("OK", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Intent intent = new Intent(activity, MainActivity.class);
                startActivity(intent);
            }
        });
        alertDialog.show();
    }
}
