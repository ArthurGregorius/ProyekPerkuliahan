import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MainMenu extends JFrame implements ActionListener{

    GameFrame frame;
    static final int GAME_WIDTH = 1000;
    static final int GAME_HEIGHT = (int)(GAME_WIDTH * (0.5555));
    private JButton startButton;
    private JLabel textMenu;

    public MainMenu() {
        setTitle("THE PONG GAME MENU");
        setSize(GAME_WIDTH, GAME_HEIGHT);
        setLayout(null);
        getContentPane().setBackground(Color.BLACK);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setLocationRelativeTo(null);

        startButton = new JButton("START");
        startButton.setFont(new Font("Helvetica", Font.BOLD, 30));
        startButton.setBounds(365, 265, 250, 50);
        startButton.setBackground(Color.BLACK);
        startButton.setForeground(Color.WHITE);
        startButton.setBorderPainted(true);
        startButton.setBorder(BorderFactory.createLineBorder(Color.WHITE));
        startButton.addActionListener(this);
        add(startButton);

        textMenu = new JLabel("WELCOME TO THE PONG GAME");
        textMenu.setFont(new Font("Helvetica", Font.BOLD, 50));
        textMenu.setBounds(100, 165, 1000, 100);
        textMenu.setForeground(Color.WHITE);
        add(textMenu);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == startButton) {
            frame = new GameFrame();
            System.out.println("Start Game button clicked!");
        }
    }
}