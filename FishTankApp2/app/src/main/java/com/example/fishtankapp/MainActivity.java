package com.example.fishtankapp;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
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

    private TextView turbidityStatus, phValue, phStatus, availableFood, needFeeding, progressText;
    private DatabaseReference reference_data, reference_token;
    private String token;
    private ProgressBar progressBar;
    int i = 0;


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
                                progressText.setText(String.valueOf(snapshotData.getValue())+"%");
                                int val = Integer.valueOf(snapshotData.getValue().toString());
                                progressBar.setProgress(val);
                                break;
                            case "Need Feeding":
                                if (snapshotData.getValue().toString().equals("Yes")){
                                    needFeeding.setText("Please Fill the Feeding Bottle");
                                    Toast.makeText(MainActivity.this.getApplicationContext(),"Please Fill the Feeding Bottle",Toast.LENGTH_SHORT).show();
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

                        }
                    }
                }

            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
            }
        });
    }


}