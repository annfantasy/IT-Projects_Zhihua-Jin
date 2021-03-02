package edu.gatech.seclass.wordfind6300;

import com.google.auto.value.AutoValue;
import com.google.common.collect.ImmutableMap;
import com.google.gson.Gson;
import com.google.gson.TypeAdapter;
import com.google.gson.TypeAdapterFactory;
import com.ryanharter.auto.value.gson.GsonTypeAdapterFactory;

import java.util.HashMap;

@AutoValue
public abstract class Settings {
    private static Settings instance = Settings.newBuilder().build();

    public static void setInstance(Settings s) {
        instance = s;
    }

    public static Settings getInstance() {
        return instance;
    }

    public abstract int lengthOfGame();
    public abstract int sizeOfBoard();
    public abstract ImmutableMap<Character, Integer> weightOfLetters();
    public static Builder newBuilder() {
        HashMap<Character, Integer> map = new HashMap<>();
        for(char c = 'a'; c <= 'z'; c++) {
            map.put(c, 1);
        }
        return new AutoValue_Settings.Builder().setLengthOfGame(3).setSizeOfBoard(4).setWeightOfLetters(map);
    }

    public Builder toBuilder() {
        return newBuilder().setLengthOfGame(lengthOfGame()).setSizeOfBoard(sizeOfBoard()).setWeightOfLetters(weightOfLetters());
    }

    public static TypeAdapter<Settings> typeAdapter(Gson gson) {
        return new AutoValue_Settings.GsonTypeAdapter(gson);
    }

    public HashMap<Character, Integer> mutableMap() {
        return new HashMap<>(weightOfLetters());
    }

    @AutoValue.Builder
    public abstract static class Builder {
        public abstract Builder setLengthOfGame(int lengthOfGame);
        public abstract Builder setSizeOfBoard(int sizeOfBoard);
        public abstract Builder setWeightOfLetters(ImmutableMap<Character, Integer> weightOfLetters);
        public Builder setWeightOfLetters(HashMap<Character, Integer> map) {
            return setWeightOfLetters(ImmutableMap.copyOf(map));
        }
        abstract Settings autoBuild();
        public Settings build() {
            // TODO: check constraints here
            return autoBuild();
        }
    }

    // From https://github.com/rharter/auto-value-gson
    @GsonTypeAdapterFactory
    public static abstract class MyAdapterFactory implements TypeAdapterFactory {

        // Static factory method to access the package
        // private generated implementation
        public static TypeAdapterFactory create() {
            return new AutoValueGson_Settings_MyAdapterFactory();
        }

    }
}
