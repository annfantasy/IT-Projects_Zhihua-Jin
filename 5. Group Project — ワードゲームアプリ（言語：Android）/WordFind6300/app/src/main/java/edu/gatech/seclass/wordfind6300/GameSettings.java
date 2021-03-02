package edu.gatech.seclass.wordfind6300;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.HashMap;

public class GameSettings extends AppCompatActivity {
    private ArrayList<Spinner> weightSpinners = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game_settings);
        Settings settings = Settings.getInstance();
        ((Spinner) findViewById(R.id.board_size)).setSelection(settings.sizeOfBoard() - 4);
        ((Spinner) findViewById(R.id.game_length)).setSelection(settings.lengthOfGame() - 1);
        TableLayout layout = (TableLayout) findViewById(R.id.weight_table);
        TableRow row = new TableRow(this);
        layout.addView(row);
        for(int i = 0; i < 26; i++) {
            if(i != 0 && i % 4 == 0) {
                row = new TableRow(this);
                layout.addView(row);
            }
            TextView textView = new TextView(this);
            char currentChar = (char)('a' + i);
            textView.setText(String.valueOf(currentChar));
            Spinner spinner = new Spinner(this);
            // From https://developer.android.com/guide/topics/ui/controls/spinner.html
            // Create an ArrayAdapter using the string array and a default spinner layout
            ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                    R.array.game_length_array, android.R.layout.simple_spinner_item);
            // Specify the layout to use when the list of choices appears
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
            // Apply the adapter to the spinner
            spinner.setAdapter(adapter);
            spinner.setSelection(settings.weightOfLetters().get(currentChar) - 1);
            row.addView(textView);
            row.addView(spinner);
            weightSpinners.add(spinner);
        }
    }

    public void updateSettings(View view) {
        Settings.Builder settings = Settings.getInstance().toBuilder().setSizeOfBoard(((Spinner) findViewById(R.id.board_size)).getSelectedItemPosition() + 4).setLengthOfGame(((Spinner) findViewById(R.id.game_length)).getSelectedItemPosition() + 1);
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < 26; i++) {
            map.put((char)('a' + i), weightSpinners.get(i).getSelectedItemPosition() + 1);
        }
        Settings.setInstance(settings.setWeightOfLetters(map).build());
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}
