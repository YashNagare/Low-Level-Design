package DesignPatterns.Structural.Adapter;

public class AdvancedMediaPlayer {

    public void playVLC(String fileName) {
        System.out.println("Playing VLC file: " + fileName);
    }

    public void playMP4(String fileName) {
        System.out.println("Playing MP4 file: " + fileName);
    }

}
