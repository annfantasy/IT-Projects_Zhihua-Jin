package edu.gatech.seclass.wordfind6300;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.dampcake.gson.immutable.ImmutableAdapterFactory;
import com.google.common.collect.ImmutableMap;
import com.google.common.reflect.TypeToken;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonParseException;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String statsFilename = "stats.json";
        String settingsFilename = "settings.json";
        if(Statistics.isFresh()) {
            if(Arrays.asList(fileList()).contains(statsFilename)) {
                try {
                    FileInputStream fis = openFileInput(statsFilename);
                    InputStreamReader inputStreamReader =
                            new InputStreamReader(fis, StandardCharsets.UTF_8);
                    StringBuilder stringBuilder = new StringBuilder();
                    try (BufferedReader reader = new BufferedReader(inputStreamReader)) {
                        String line = reader.readLine();
                        while (line != null) {
                            stringBuilder.append(line).append('\n');
                            line = reader.readLine();
                        }
                    }
                    Gson gson = new GsonBuilder().registerTypeAdapterFactory(Settings.MyAdapterFactory.create()).registerTypeAdapterFactory(ImmutableAdapterFactory.forGuava()).create();
                    Statistics.setInstance(gson.fromJson(stringBuilder.toString(), Statistics.class));
                }catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if(Arrays.asList(fileList()).contains(settingsFilename)) {
                try {
                    FileInputStream fis = openFileInput(settingsFilename);
                    InputStreamReader inputStreamReader =
                            new InputStreamReader(fis, StandardCharsets.UTF_8);
                    StringBuilder stringBuilder = new StringBuilder();
                    try (BufferedReader reader = new BufferedReader(inputStreamReader)) {
                        String line = reader.readLine();
                        while (line != null) {
                            stringBuilder.append(line).append('\n');
                            line = reader.readLine();
                        }
                    }
                    Gson gson = new GsonBuilder().registerTypeAdapterFactory(ImmutableAdapterFactory.forGuava()).create();
                    Settings.setInstance(Settings.typeAdapter(gson).fromJson(stringBuilder.toString()));
                }catch (IOException e) {
                    e.printStackTrace();
                }
            }
        } else {
            try (FileOutputStream fos = openFileOutput(statsFilename, Context.MODE_PRIVATE)) {
                Gson gson = new Gson();
                fos.write(gson.toJson(Statistics.getInstance()).getBytes());
            } catch (IOException e) {
                e.printStackTrace();
            }
            try (FileOutputStream fos = openFileOutput(settingsFilename, Context.MODE_PRIVATE)) {
                Gson gson = new Gson();
                fos.write(gson.toJson(Settings.getInstance()).getBytes());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public void settings(View view) {
        Intent intent = new Intent(this, GameSettings.class);
        startActivity(intent);
    }

    public void newGame(View view) {
        Intent intent = new Intent(this, GameBoard.class);
        startActivity(intent);
    }

    public void stats(View view) {
        Intent intent = new Intent(this, StatsSelector.class);
        startActivity(intent);
    }
}
