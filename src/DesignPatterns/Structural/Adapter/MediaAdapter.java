package DesignPatterns.Structural.Adapter;

public class MediaAdapter implements MediaPlayer {

    private AdvancedMediaPlayer advancedMediaPlayer;

    public MediaAdapter(String audioType) {
        this.advancedMediaPlayer = new AdvancedMediaPlayer();
    }

    @Override
    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedMediaPlayer.playVLC("vlc");
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedMediaPlayer.playMP4("mp4");
        }
    }
}
