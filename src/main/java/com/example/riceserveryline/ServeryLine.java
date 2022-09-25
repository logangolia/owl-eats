package com.example.riceserveryline;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

public class ServeryLine extends AppCompatActivity {
    static boolean hasStarted = false;

    Button buttonWest;
    Button buttonSeibel;
    Button buttonNorth;
    Button buttonSouth;

    TextView textWestWaitTime;
    TextView textSeibelWaitTime;
    TextView textNorthWaitTime;
    TextView textSouthWaitTime;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_servery_line);
        buttonWest = (Button) findViewById(R.id.bWest);
        buttonSeibel = (Button) findViewById(R.id.bSeibel);
        buttonNorth = (Button) findViewById(R.id.bNorth);
        buttonSouth = (Button) findViewById(R.id.bSouth);
        textWestWaitTime = (TextView) findViewById(R.id.tWestTime);
        textSouthWaitTime = (TextView) findViewById(R.id.tSouthTime);
        textNorthWaitTime = (TextView) findViewById(R.id.tNorthTime);
        textSeibelWaitTime = (TextView) findViewById(R.id.tSeibelTime);

        ArrayList<String> waitTimes = new ArrayList<>();
        if (!hasStarted) {

            BufferedReader reader = null;
            try {
                reader = new BufferedReader(
                        new InputStreamReader(getAssets().open("wait_times.txt")));

                // do reading, usually loop until end of file reading
                String mLine = null;
                while ((mLine = reader.readLine()) != null) {
                    System.out.println(mLine);
                    waitTimes.add(mLine);
                }
            } catch (IOException e) {
                //log the exception
                System.out.println(e.getMessage());
            }

            System.out.println("# : " + waitTimes.size());

            // hasStarted = true;
            Thread t1 = new Thread(new Runnable() {
                @Override
                public void run() {
                    while (true) {
                        Date date = new Date();
                        SimpleDateFormat formatter = new SimpleDateFormat("kk:mm:ss");

                        // System time
                        // String time = formatter.format(date);

                        // Demonstration time
                        String time = "12:30";

                        // check meal time
                        int hour = Integer.parseInt(time.substring(0,2));
                        int min = Integer.parseInt(time.substring(3,5));

                        String waitTime = "0";
                        if ((hour >= 11 && min >= 25)  && (hour <= 13  && min <= 30)) {
                            // take wait time
                            int index = (hour - 11) * 60 + min - 25;
                            waitTime = waitTimes.get(index);
                        }

                        System.out.println(formatter.format(date));

                        // same time for all due to the lack of data
                        textWestWaitTime.setText(waitTime + " min");
                        textSeibelWaitTime.setText(waitTime + " min");
                        textSouthWaitTime.setText(waitTime + " min");
                        textNorthWaitTime.setText(waitTime + " min");

                        try {
                            Thread.sleep(1000);
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                    }
                }
            });
            t1.start();
        }

        View.OnClickListener buttonWestClickListener = new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent i = new Intent(ServeryLine.this, WestServery.class);
                startActivity(i);
            }
        };

        buttonWest.setOnClickListener(buttonWestClickListener);

        View.OnClickListener buttonSeibelClickListener = new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent i = new Intent(ServeryLine.this, WestServery.class);
                startActivity(i);
            }
        };

        buttonSeibel.setOnClickListener(buttonSeibelClickListener);

        View.OnClickListener buttonSouthClickListener = new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent i = new Intent(ServeryLine.this, WestServery.class);
                startActivity(i);
            }
        };

        buttonSouth.setOnClickListener(buttonSouthClickListener);

        View.OnClickListener buttonNorthClickListener = new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent i = new Intent(ServeryLine.this, WestServery.class);
                startActivity(i);
            }
        };

        buttonNorth.setOnClickListener(buttonNorthClickListener);
    }
}