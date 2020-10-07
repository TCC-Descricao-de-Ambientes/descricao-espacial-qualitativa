package com.example.tcc;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.MediaStore;
import android.renderscript.Sampler;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import org.apache.http.entity.mime.HttpMultipartMode;
import org.apache.http.entity.mime.MultipartEntity;
import org.apache.http.entity.mime.content.ByteArrayBody;
import org.apache.http.entity.mime.content.ContentBody;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;


public class MainActivity extends AppCompatActivity {
    public static final int PICK_IMAGE = 1;
    Button btnPick;
    Button btnProcess;
    ImageView imageView;
    //MyDrawable myDrawable = new MyDrawable();
    Bitmap bitmap;
    TextView textView;
    Canvas canvas;
    Paint paint;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        final Intent intentProcess = new Intent();
        intentProcess.setType("image/*");
        setContentView(R.layout.activity_main);

        imageView = findViewById(R.id.myImage);
        btnProcess = findViewById(R.id.button_process);

        btnPick = findViewById(R.id.button_choose);

        textView = findViewById(R.id.resultado);

        btnPick.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent();
                intent.setType("image/*");
                intent.setAction(Intent.ACTION_GET_CONTENT); // solicita a ação de pegar uma foto da galeria
                startActivityForResult(Intent.createChooser(intent, "Selecione a imagem"), PICK_IMAGE);

            }
        });

    }

    @SuppressLint("MissingSuperCall")
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable final Intent data) {
        if (requestCode == PICK_IMAGE && resultCode == RESULT_OK && data != null) {
            final Uri imageData = data.getData();
            imageView.setImageURI(imageData); // coloca a imagem escolhida na ImageView

            try {
                bitmap = MediaStore.Images.Media.getBitmap(this.getContentResolver(), imageData);

            } catch (IOException e) {
                e.printStackTrace();
                Log.d("erro", "erro", e);
            }

            bitmap = bitmap.copy(Bitmap.Config.ARGB_8888, true); // precisa disso para que possa mudar ele
            canvas = new Canvas(bitmap); // cria a "tela" para desenhar algo
            paint = new Paint(Paint.ANTI_ALIAS_FLAG);// cria o pincel

            canvas.drawText("xablau", 100, 100, paint);
            paint.setTextSize(20);

            paint.setColor(Color.rgb(255, 255, 0)); // cor do pincel


            btnProcess.setOnClickListener(new View.OnClickListener() {

                @Override
                public void onClick(View v) {

                    new Xablau().execute();


                }
            });

        }
    }

    private class Xablau extends AsyncTask<Void, Void, String> {

        @Override
        protected String doInBackground(Void... voids) {
            String url1 = "https://ssd-mobilenet-api.herokuapp.com/api/v1/mobilenet";

            String filename = "filename.png";
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            bitmap.compress(Bitmap.CompressFormat.JPEG, 100, bos);
            ContentBody contentPart = new ByteArrayBody(bos.toByteArray(), filename);

            MultipartEntity reqEntity = new MultipartEntity(HttpMultipartMode.BROWSER_COMPATIBLE);
            reqEntity.addPart("picture", contentPart);
            return multipost(url1, reqEntity);
        }

        @Override
        protected void onPostExecute(String response) {
            // Call activity method with results
            //req(response);
        }

        private String multipost(String urlString, MultipartEntity reqEntity) {
            try {
                URL url = new URL(urlString);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setReadTimeout(10000);
                conn.setConnectTimeout(15000);
                conn.setRequestMethod("POST");
                conn.setUseCaches(false);
                conn.setDoInput(true);
                conn.setDoOutput(true);

                conn.setRequestProperty("Connection", "Keep-Alive");
                conn.addRequestProperty("Content-length", reqEntity.getContentLength() + "");

                conn.addRequestProperty("Content-Type", "image/jpeg");
                conn.addRequestProperty(reqEntity.getContentType().getName(), reqEntity.getContentType().getValue());

                OutputStream os = conn.getOutputStream();
                reqEntity.writeTo(conn.getOutputStream());
                os.close();
                conn.connect();

                if (conn.getResponseCode() == HttpURLConnection.HTTP_OK) {
                    return readStream(conn.getInputStream());
                }

            } catch (Exception e) {
                Log.e("TAG", "multipart post error " + e + "(" + urlString + ")");
            }

            return null;
        }

        private String readStream(InputStream in) {
            BufferedReader reader = null;
            StringBuilder builder = new StringBuilder();
            try {
                reader = new BufferedReader(new InputStreamReader(in));
                String line = "";
                while ((line = reader.readLine()) != null) {
                    builder.append(line);
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (reader != null) {
                    try {
                        reader.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }

            return builder.toString();
        }
    }

    public void req(String response) {
        float bitWidth = bitmap.getWidth();
        float bitHeight = bitmap.getHeight();

        canvas.getWidth();

        for (int i = 0; i < 21; i++) {
            canvas.drawLine((bitWidth / 5) * i, 0, (bitWidth / 5) * i, bitHeight, paint);
            canvas.drawLine(0, ((bitHeight + 2) / 3) * i, bitWidth, (bitHeight / 3) * i, paint);
        }
        imageView.setImageBitmap(bitmap);
    }


}





