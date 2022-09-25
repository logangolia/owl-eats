package com.example.riceserveryline;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.util.EmptyStackException;

public class MainActivity extends AppCompatActivity {
    Button buttonLogIn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        buttonLogIn = (Button) findViewById(R.id.bLogIn);

        View.OnClickListener buttonLogInClickListener = new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent i = new Intent(MainActivity.this, ServeryLine.class);
                startActivity(i);
            }
        };

        buttonLogIn.setOnClickListener(buttonLogInClickListener);
    }
}