package com.example.fishtankapp;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.firebase.messaging.FirebaseMessaging;

public class MainActivity extends AppCompatActivity {

    private TextView turbidityStatus, phValue, phStatus, availableFood, needFeeding, progressText,lastUpdatePH,lastUpdateFeeder;
    static DatabaseReference reference_data, reference_token;
    private int feedNow = 0;
    private String token;
    private ProgressBar progressBar;
    int i = 0;

    public MainActivity() {
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        turbidityStatus = findViewById(R.id.turbidityStatus);
        phValue = findViewById(R.id.phValue);
        phStatus = findViewById(R.id.phStatus);
        needFeeding = findViewById(R.id.needFeeding);
        progressBar = findViewById(R.id.progress_bar);
        progressText = findViewById(R.id.progress_bar_text);
        lastUpdatePH= findViewById(R.id.lastUpdatePH);
        lastUpdateFeeder = findViewById(R.id.lastUpdateFeeder);

        reference_data = FirebaseDatabase.getInstance().getReference().child("Sensor Data");
        reference_token = FirebaseDatabase.getInstance().getReference().child("Tokens");


        FirebaseMessaging.getInstance().getToken()
                .addOnCompleteListener(new OnCompleteListener<String>() {
                    @Override
                    public void onComplete(@NonNull Task<String> task) {
                        if (!task.isSuccessful()) {
                            Log.w("TAG", "Fetching FCM registration token failed", task.getException());
                            return;
                        }
                        // Get new FCM registration token
                        token = task.getResult();
                        Log.d("TAG", token);
                        reference_token.child(token).setValue(token);
                    }
                });

        reference_data.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if (snapshot.exists()) {
                    for (DataSnapshot snapshotData : snapshot.getChildren()) {
                        switch (snapshotData.getKey().toString()) {
                            case "Available food":

                                int val = Integer.valueOf(snapshotData.getValue().toString());
                                if(val>0){
                                    feedNow = 1;
                                }
                                else feedNow = 0;
                                if(val<0){
                                    val = 0;
                                }
                                progressBar.setProgress(val);
                                progressText.setText(String.valueOf(val)+"%");
                                break;
                            case "Need Feeding":
                                if (snapshotData.getValue().toString().equals("Yes")){
                                    needFeeding.setText("Please Fill the Feeding Bottle");
//                                    Toast.makeText(MainActivity.this.getApplicationContext(),"Please Fill the Feeding Bottle",Toast.LENGTH_SHORT).show();
                                }
                                else{
                                    needFeeding.setText("");
                                }
                                break;
                            case "PH Status":

                                phStatus.setText(snapshotData.getValue().toString());

                                break;
                            case "PH Value":
                                phValue.setText(snapshotData.getValue().toString());
                                break;
                            case "Turbidity":
                                turbidityStatus.setText(snapshotData.getValue().toString());
                                break;
                            case "LastPh":
                                lastUpdatePH.setText(snapshotData.getValue().toString());
                                break;
                            case "LastFeeder":
                                lastUpdateFeeder.setText(snapshotData.getValue().toString());
                                break;
                        }
                    }
                }

            }
            @Override
            public void onCancelled(@NonNull DatabaseError error) {
            }
        });
    }

    public void feedNow(View view) {
        if(feedNow != 0){
            reference_data.child("Feed Now").setValue("True");
            Toast.makeText(MainActivity.this.getApplicationContext(),"Feeding Done",Toast.LENGTH_SHORT).show();
        }
        else{
            reference_data.child("Feed Now").setValue("False");
            Toast.makeText(MainActivity.this.getApplicationContext(),"Please Fill the Feeding Bottle",Toast.LENGTH_SHORT).show();
        }
    }



}