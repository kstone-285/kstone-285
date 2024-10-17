package src;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.text.Font;
import javafx.scene.text.FontPosture;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.util.Duration;

public class FXMapleTimer extends Application{
    
    private Timeline timeline;
    private int seconds = 120;
    private int remainTime;
    private Text timeText;
    private boolean isRunning = false;
    private boolean isBlinking = false;
    private BorderPane pane = new BorderPane();
    
    @Override
    public void start(Stage priStage) {

        System.setProperty("prism.lcdtext", "false");

        Image image1 = new Image("imageofpotion.jpg");
        ImageView view1 = new ImageView(image1);
        Image image2 = new Image("imageofstop.png");
        ImageView view2 = new ImageView(image2);

        CheckBox chkAutoRestart = new CheckBox();
        chkAutoRestart.setSelected(true);
        BorderPane paneForChk = new BorderPane();
        paneForChk.setCenter(chkAutoRestart);
        Text chkText = new Text("AUTO RESTART");
        chkText.setFont(Font.font("Consolas", FontWeight.BOLD, FontPosture.REGULAR, 12.0));
        paneForChk.setBottom(chkText);
        
        timeText = new Text();
        timeText.setFont(Font.font("Consolas", FontWeight.BOLD, FontPosture.REGULAR, 150.0));
        updateTime(120);

        ComboBox<String> cboTimer = new ComboBox<>();
        cboTimer.getItems().addAll("게임", "운동");
        cboTimer.setValue("게임");
        cboTimer.valueProperty().addListener((ov, oldVal, newVal) -> {

            if(newVal.equals("게임")) {

                seconds = 120;
            }
            else {

                seconds = 60;
            }
            if(!isRunning) {

                updateTime(seconds);
            }
        });

        BorderPane paneForCbo = new BorderPane();
        paneForCbo.setLeft(new Label("                                                    모드를 선택하세요  :"));
        paneForCbo.setCenter(cboTimer);
        paneForCbo.setRight(new Label("                                                "));

        Button btStart = new Button("시작", view1);

        btStart.setOnAction(e -> {

            if(isRunning) {

                return;
            }

            isRunning = true;
            remainTime = seconds;
            timeline = new Timeline(new KeyFrame(Duration.millis(1000), e1 -> {

                remainTime--;
                updateTime(remainTime);
                if ( remainTime <= 10 ) {

                    startBlink();
                }
                if ( remainTime <= 0 ) {

                    if(chkAutoRestart.isSelected()) {
                        
                        remainTime = seconds;
                    }
                    else {

                        isRunning = false;
                        timeline.stop();
                        updateTime(seconds);
                    }
                }
            }));

            timeline.setCycleCount(Timeline.INDEFINITE);
            timeline.play();

        });

        Button btStop = new Button("종료", view2);

        btStop.setOnAction(e -> {

            if(timeline != null) {

                timeline.stop();
            }
            isRunning = false;
            isBlinking = false;
            updateTime(seconds);
            pane.setStyle("-fx-background: white;");
        });

        HBox hBox = new HBox(15);
        hBox.getChildren().addAll(btStart, paneForChk, btStop);
        hBox.setAlignment(Pos.CENTER);

        pane.setTop(paneForCbo);
        pane.setCenter(timeText);
        pane.setBottom(hBox);
        pane.setPadding(new Insets(10,1,10,1));

        Scene scene = new Scene(pane, 500, 250);

        priStage.setTitle("Kyoosuk's Timer");
        priStage.setScene(scene);
        priStage.show();

    }

    private void updateTime(int seconds) {

        int minutes = seconds / 60;
        int secs = seconds % 60;
        timeText.setText(String.format("%02d:%02d", minutes, secs));
    }

    private void startBlink() {

        if(isBlinking) {

            return;
        }

        isBlinking = true;
        Timeline blinkTimeline = new Timeline(new KeyFrame(Duration.millis(500), e -> {

            if ( pane.getStyle().equals("-fx-background-color: #ff634d;")) {

                pane.setStyle("-fx-background-color: white;");
            }
            else {

                pane.setStyle("-fx-background-color: #ff634d;");
            }
        }));

        blinkTimeline.setCycleCount(20);
        blinkTimeline.play();
        blinkTimeline.setOnFinished(e -> {

            pane.setStyle("-fx-background-color: white;");
            isBlinking = false;
        });

    }

    public static void main(String[] args) {
        
        launch(args);
    }
}
