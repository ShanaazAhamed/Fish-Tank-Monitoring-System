package com.example.fishtankapp;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.widget.TextView;

import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {

    TextView turbidityStatus;
    TextView phValue;
    TextView phStatus;
    TextView availableFood;
    TextView needFeeding;
    DatabaseReference reference;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        turbidityStatus = findViewById(R.id.turbidityStatus);
        phValue = findViewById(R.id.phValue);
        phStatus = findViewById(R.id.phStatus);
        availableFood = findViewById(R.id.availableFood);
        needFeeding = findViewById(R.id.needFeeding);

        reference = FirebaseDatabase.getInstance().getReference().child("DB Object name");

        reference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if (snapshot.exists()) {
                    for (DataSnapshot snapshotData : snapshot.getChildren()) {
                        switch (snapshotData.getKey().toString()) {
                            case "Available food":
                                availableFood.setText(snapshotData.getValue().toString());
                                break;
                            case "Need Feeding":
                                needFeeding.setText(snapshotData.getValue().toString());
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
                    sendNotification("Need Feeding", "Please fill the Feeder");
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });
    }

    @Override
    protected void onStop () {
        super .onStop() ;
//        startService( new Intent( this, NotificationService. class )) ;
    }

    private void sendNotification(String messageTitle,String messageBody) {
        Intent intent = new Intent(this, MainActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0 /* Request code */, intent,
                PendingIntent.FLAG_ONE_SHOT);

        String channelId = "My channel ID";
        Uri defaultSoundUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
        NotificationCompat.Builder notificationBuilder =
                new NotificationCompat.Builder(this, channelId)
                        .setSmallIcon(R.drawable.ic_stat_notification)
                        .setContentTitle(messageTitle)
                        .setContentText(messageBody)
                        .setAutoCancel(true)
                        .setSound(defaultSoundUri)
                        .setContentIntent(pendingIntent);

        NotificationManager notificationManager =
                (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);

        // Since android Oreo notification channel is needed.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(channelId,
                    "Channel human readable title",
                    NotificationManager.IMPORTANCE_DEFAULT);
            notificationManager.createNotificationChannel(channel);
        }

        notificationManager.notify(0 /* ID of notification */, notificationBuilder.build());
    }


}