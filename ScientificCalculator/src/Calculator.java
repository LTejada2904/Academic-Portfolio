import java.awt.Color;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JRadioButton;
import javax.swing.SwingConstants;
import javax.swing.ButtonGroup;
import java.awt.Toolkit;

public class Calculator {

	private JFrame frmScientificCalculator;
	private JTextField textField;
	
	
	
	double first;
	double second;
	double result;
	String operation;
	String answer;
	
	private final ButtonGroup buttonGroup = new ButtonGroup();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Calculator window = new Calculator();
					window.frmScientificCalculator.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Calculator() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmScientificCalculator = new JFrame();
		frmScientificCalculator.setIconImage(Toolkit.getDefaultToolkit().getImage("C:\\Users\\luist\\Desktop\\Icon.png"));
		frmScientificCalculator.getContentPane().setBackground(new Color(0, 0, 0));
		frmScientificCalculator.setResizable(false);
		frmScientificCalculator.setTitle("Scientific Calculator");
		frmScientificCalculator.setBounds(100, 100, 410, 700);
		frmScientificCalculator.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmScientificCalculator.getContentPane().setLayout(null);
		
		textField = new JTextField();
		textField.setForeground(new Color(255, 255, 255));
		textField.setFont(new Font("Arial", Font.BOLD, 35));
		textField.setBounds(0, 0, 394, 151);
		textField.setBackground(Color.BLACK);
		frmScientificCalculator.getContentPane().add(textField);
		textField.setColumns(10);
		
		JButton btn0 = new JButton("0");
		btn0.setEnabled(false);
		btn0.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn0.getText();
				textField.setText(number);
			}
		});
		btn0.setBackground(new Color(0, 0, 0));
		btn0.setOpaque(true);
		btn0.setForeground(new Color(0, 128, 255));
		btn0.setFont(new Font("Verdana", Font.BOLD, 25));
		btn0.setBounds(10, 575, 150, 75);
		frmScientificCalculator.getContentPane().add(btn0);
		
		JButton btn1 = new JButton("1");
		btn1.setEnabled(false);
		btn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn1.getText();
				textField.setText(number);
			}
		});
		btn1.setBackground(new Color(0, 0, 0));
		btn1.setOpaque(true);
		btn1.setForeground(new Color(0, 128, 255));
		btn1.setFont(new Font("Verdana", Font.BOLD, 25));
		btn1.setBounds(10, 500, 75, 75);
		frmScientificCalculator.getContentPane().add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.setEnabled(false);
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn2.getText();
				textField.setText(number);
			}
		});
		btn2.setBackground(new Color(0, 0, 0));
		btn2.setOpaque(true);
		btn2.setForeground(new Color(0, 128, 255));
		btn2.setFont(new Font("Verdana", Font.BOLD, 25));
		btn2.setBounds(85, 500, 75, 75);
		frmScientificCalculator.getContentPane().add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.setEnabled(false);
		btn3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn3.getText();
				textField.setText(number);
			}
		});
		btn3.setBackground(new Color(0, 0, 0));
		btn3.setOpaque(true);
		btn3.setForeground(new Color(0, 128, 255));
		btn3.setFont(new Font("Verdana", Font.BOLD, 25));
		btn3.setBounds(160, 500, 75, 75);
		frmScientificCalculator.getContentPane().add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.setEnabled(false);
		btn4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn4.getText();
				textField.setText(number);
			}
		});
		btn4.setBackground(new Color(0, 0, 0));
		btn4.setOpaque(true);
		btn4.setForeground(new Color(0, 128, 255));
		btn4.setFont(new Font("Verdana", Font.BOLD, 25));
		btn4.setBounds(10, 425, 75, 75);
		frmScientificCalculator.getContentPane().add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.setEnabled(false);
		btn5.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn5.getText();
				textField.setText(number);
			}
		});
		btn5.setBackground(new Color(0, 0, 0));
		btn5.setOpaque(true);
		btn5.setForeground(new Color(0, 128, 255));
		btn5.setFont(new Font("Verdana", Font.BOLD, 25));
		btn5.setBounds(85, 425, 75, 75);
		frmScientificCalculator.getContentPane().add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.setEnabled(false);
		btn6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn6.getText();
				textField.setText(number);
			}
		});
		btn6.setBackground(new Color(0, 0, 0));
		btn6.setOpaque(true);
		btn6.setForeground(new Color(0, 128, 255));
		btn6.setFont(new Font("Verdana", Font.BOLD, 25));
		btn6.setBounds(160, 425, 75, 75);
		frmScientificCalculator.getContentPane().add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.setEnabled(false);
		btn7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn7.getText();
				textField.setText(number);
			}
		});
		btn7.setBackground(new Color(0, 0, 0));
		btn7.setOpaque(true);
		btn7.setForeground(new Color(0, 128, 255));
		btn7.setFont(new Font("Verdana", Font.BOLD, 25));
		btn7.setBounds(10, 350, 75, 75);
		frmScientificCalculator.getContentPane().add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.setEnabled(false);
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn8.getText();
				textField.setText(number);
			}
		});
		btn8.setBackground(new Color(0, 0, 0));
		btn8.setOpaque(true);
		btn8.setForeground(new Color(0, 128, 255));
		btn8.setFont(new Font("Verdana", Font.BOLD, 25));
		btn8.setBounds(85, 350, 75, 75);
		frmScientificCalculator.getContentPane().add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.setEnabled(false);
		btn9.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btn9.getText();
				textField.setText(number);
			}
		});
		btn9.setBackground(new Color(0, 0, 0));
		btn9.setOpaque(true);
		btn9.setForeground(new Color(0, 128, 255));
		btn9.setFont(new Font("Verdana", Font.BOLD, 25));
		btn9.setBounds(160, 350, 75, 75);
		frmScientificCalculator.getContentPane().add(btn9);
		
		JButton btnDot = new JButton(".");
		btnDot.setEnabled(false);
		btnDot.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String number= textField.getText()+btnDot.getText();
				textField.setText(number);
			}
		});
		btnDot.setBackground(new Color(0, 0, 0));
		btnDot.setOpaque(true);
		btnDot.setForeground(new Color(0, 128, 255));
		btnDot.setFont(new Font("Verdana", Font.PLAIN, 25));
		btnDot.setBounds(160, 575, 75, 75);
		frmScientificCalculator.getContentPane().add(btnDot);
		
		JButton btnSign = new JButton("+/-");
		btnSign.setEnabled(false);
		btnSign.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Double.parseDouble(String.valueOf(textField.getText()));
				a=a*(-1);
				textField.setText(String.valueOf(a));
			}
		});
		btnSign.setOpaque(true);
		btnSign.setForeground(new Color(255, 255, 255));
		btnSign.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnSign.setBackground(new Color(128, 128, 128));
		btnSign.setBounds(235, 575, 75, 75);
		frmScientificCalculator.getContentPane().add(btnSign);
		
		JButton btnDel = new JButton("DEL");
		btnDel.setEnabled(false);
		btnDel.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String backSpace=null;
				
				if(textField.getText().length()>0);
				{
					StringBuilder str=new StringBuilder(textField.getText());
					str.deleteCharAt(textField.getText().length()-1);
					backSpace=str.toString();
					textField.setText(backSpace);
				}
			}
		});
		btnDel.setBackground(new Color(0, 0, 160));
		btnDel.setOpaque(true);
		btnDel.setForeground(new Color(0, 128, 255));
		btnDel.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnDel.setBounds(235, 350, 75, 75);
		frmScientificCalculator.getContentPane().add(btnDel);
		
		JButton btnAC = new JButton("AC");
		btnAC.setEnabled(false);
		btnAC.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				textField.setText(null);
			}
		});
		btnAC.setBackground(new Color(0, 0, 160));
		btnAC.setOpaque(true);
		btnAC.setForeground(new Color(0, 128, 255));
		btnAC.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnAC.setBounds(310, 350, 75, 75);
		frmScientificCalculator.getContentPane().add(btnAC);
		
		JButton btnSum = new JButton("+");
		btnSum.setEnabled(false);
		btnSum.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				first=Double.parseDouble(textField.getText());
				textField.setText("");
				operation="+";
			}
		});
		btnSum.setBackground(new Color(0, 0, 160));
		btnSum.setOpaque(true);
		btnSum.setForeground(new Color(0, 128, 255));
		btnSum.setFont(new Font("Verdana", Font.PLAIN, 25));
		btnSum.setBounds(235, 500, 75, 75);
		frmScientificCalculator.getContentPane().add(btnSum);
		
		JButton btnRest = new JButton("-");
		btnRest.setEnabled(false);
		btnRest.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				first=Double.parseDouble(textField.getText());
				textField.setText("");
				operation="-";
			}
		});
		btnRest.setBackground(new Color(0, 0, 160));
		btnRest.setOpaque(true);
		btnRest.setForeground(new Color(0, 128, 255));
		btnRest.setFont(new Font("Verdana", Font.PLAIN, 25));
		btnRest.setBounds(310, 500, 75, 75);
		frmScientificCalculator.getContentPane().add(btnRest);	
		
		JButton btnMult = new JButton("x");
		btnMult.setEnabled(false);
		btnMult.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				first=Double.parseDouble(textField.getText());
				textField.setText("");
				operation="x";
			}
		});
		btnMult.setBackground(new Color(0, 0, 160));
		btnMult.setOpaque(true);
		btnMult.setForeground(new Color(0, 128, 255));
		btnMult.setFont(new Font("Verdana", Font.PLAIN, 25));
		btnMult.setBounds(235, 425, 75, 75);
		frmScientificCalculator.getContentPane().add(btnMult);
		
		JButton btnDiv = new JButton("÷");
		btnDiv.setEnabled(false);
		btnDiv.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				first=Double.parseDouble(textField.getText());
				textField.setText("");
				operation="÷";
			}
		});
		btnDiv.setBackground(new Color(0, 0, 160));
		btnDiv.setOpaque(true);
		btnDiv.setForeground(new Color(0, 128, 255));
		btnDiv.setFont(new Font("Verdana", Font.PLAIN, 25));
		btnDiv.setBounds(310, 425, 75, 75);
		frmScientificCalculator.getContentPane().add(btnDiv);
		
		JButton btnFact = new JButton("n!");
		btnFact.setEnabled(false);
		btnFact.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Double.parseDouble(textField.getText());
				double fact=1;
				while(a!=0)
				{
					fact=fact*a;
					a--;
				}
				textField.setText("");
				textField.setText(textField.getText()+fact);
			}
		});
		btnFact.setOpaque(true);
		btnFact.setForeground(Color.WHITE);
		btnFact.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnFact.setBackground(Color.GRAY);
		btnFact.setBounds(10, 162, 75, 60);
		frmScientificCalculator.getContentPane().add(btnFact);
		
		JButton btnExp = new JButton("exp");
		btnExp.setEnabled(false);
		btnExp.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.exp(Double.parseDouble(textField.getText()));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnExp.setOpaque(true);
		btnExp.setForeground(Color.WHITE);
		btnExp.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnExp.setBackground(Color.GRAY);
		btnExp.setBounds(85, 162, 75, 60);
		frmScientificCalculator.getContentPane().add(btnExp);
		
		JButton btnInv = new JButton("inv");
		btnInv.setEnabled(false);
		btnInv.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=1/(Double.parseDouble(textField.getText()));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnInv.setOpaque(true);
		btnInv.setForeground(Color.WHITE);
		btnInv.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnInv.setBackground(Color.GRAY);
		btnInv.setBounds(160, 162, 75, 60);
		frmScientificCalculator.getContentPane().add(btnInv);
		
		JButton btnSqrt = new JButton("√");
		btnSqrt.setEnabled(false);
		btnSqrt.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.sqrt(Double.parseDouble(textField.getText()));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnSqrt.setOpaque(true);
		btnSqrt.setForeground(Color.WHITE);
		btnSqrt.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnSqrt.setBackground(Color.GRAY);
		btnSqrt.setBounds(10, 220, 75, 60);
		frmScientificCalculator.getContentPane().add(btnSqrt);
		
		JButton btnLog = new JButton("log");
		btnLog.setEnabled(false);
		btnLog.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.log(Double.parseDouble(textField.getText()));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnLog.setOpaque(true);
		btnLog.setForeground(Color.WHITE);
		btnLog.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnLog.setBackground(Color.GRAY);
		btnLog.setBounds(85, 220, 75, 60);
		frmScientificCalculator.getContentPane().add(btnLog);
		
		JButton btnPerc = new JButton("%");
		btnPerc.setEnabled(false);
		btnPerc.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				first=Double.parseDouble(textField.getText());
				textField.setText("");
				operation="%";
			}
		});
		btnPerc.setOpaque(true);
		btnPerc.setForeground(Color.WHITE);
		btnPerc.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnPerc.setBackground(Color.GRAY);
		btnPerc.setBounds(10, 279, 75, 60);
		frmScientificCalculator.getContentPane().add(btnPerc);
		
		JButton btnPower = new JButton("xⁿ");
		btnPower.setEnabled(false);
		btnPower.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				first=Double.parseDouble(textField.getText());
				textField.setText("");
				operation="xⁿ";
			}
		});
		btnPower.setOpaque(true);
		btnPower.setForeground(Color.WHITE);
		btnPower.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnPower.setBackground(Color.GRAY);
		btnPower.setBounds(85, 279, 75, 60);
		frmScientificCalculator.getContentPane().add(btnPower);
		
		JButton btnSin = new JButton("sin");
		btnSin.setEnabled(false);
		btnSin.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.sin(Math.toRadians(Double.parseDouble(textField.getText())));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnSin.setOpaque(true);
		btnSin.setForeground(Color.WHITE);
		btnSin.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnSin.setBackground(Color.GRAY);
		btnSin.setBounds(160, 220, 75, 60);
		frmScientificCalculator.getContentPane().add(btnSin);
		
		JButton btnCos = new JButton("cos");
		btnCos.setEnabled(false);
		btnCos.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.cos(Math.toRadians(Double.parseDouble(textField.getText())));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnCos.setOpaque(true);
		btnCos.setForeground(Color.WHITE);
		btnCos.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnCos.setBackground(Color.GRAY);
		btnCos.setBounds(235, 220, 75, 60);
		frmScientificCalculator.getContentPane().add(btnCos);
		
		JButton btnTan = new JButton("tan");
		btnTan.setEnabled(false);
		btnTan.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.tan(Math.toRadians(Double.parseDouble(textField.getText())));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnTan.setOpaque(true);
		btnTan.setForeground(Color.WHITE);
		btnTan.setFont(new Font("Verdana", Font.PLAIN, 20));
		btnTan.setBackground(Color.GRAY);
		btnTan.setBounds(310, 220, 75, 60);
		frmScientificCalculator.getContentPane().add(btnTan);
		
		JButton btnAsin = new JButton("asin");
		btnAsin.setEnabled(false);
		btnAsin.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.toDegrees(Math.asin(Double.parseDouble(textField.getText())));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnAsin.setOpaque(true);
		btnAsin.setForeground(Color.WHITE);
		btnAsin.setFont(new Font("Verdana", Font.PLAIN, 18));
		btnAsin.setBackground(Color.GRAY);
		btnAsin.setBounds(160, 279, 75, 60);
		frmScientificCalculator.getContentPane().add(btnAsin);
		
		JButton btnAcos = new JButton("acos");
		btnAcos.setEnabled(false);
		btnAcos.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.toDegrees(Math.acos(Double.parseDouble(textField.getText())));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnAcos.setOpaque(true);
		btnAcos.setForeground(Color.WHITE);
		btnAcos.setFont(new Font("Verdana", Font.PLAIN, 18));
		btnAcos.setBackground(Color.GRAY);
		btnAcos.setBounds(235, 279, 75, 60);
		frmScientificCalculator.getContentPane().add(btnAcos);
		
		JButton btnAtan = new JButton("atan");
		btnAtan.setEnabled(false);
		btnAtan.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double a=Math.toDegrees(Math.atan(Double.parseDouble(textField.getText())));
				textField.setText("");
				textField.setText(textField.getText()+a);
			}
		});
		btnAtan.setOpaque(true);
		btnAtan.setForeground(Color.WHITE);
		btnAtan.setFont(new Font("Verdana", Font.PLAIN, 18));
		btnAtan.setBackground(Color.GRAY);
		btnAtan.setBounds(310, 279, 75, 60);
		frmScientificCalculator.getContentPane().add(btnAtan);
		
		JButton btnEqual = new JButton("=");
		btnEqual.setEnabled(false);
		btnEqual.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				second=Double.parseDouble(textField.getText());
				if(operation=="+")
				{
					result=first+second;
					answer=String.format("%.2f", result);
					textField.setText(answer);
				}
				else if(operation=="-")
				{
					result=first-second;
					answer=String.format("%.2f", result);
					textField.setText(answer);
				}
				else if(operation=="x")
				{
					result=first*second;
					answer=String.format("%.2f", result);
					textField.setText(answer);
				}
				else if(operation=="÷")
				{
					result=first/second;
					answer=String.format("%.2f", result);
					textField.setText(answer);
				}
				else if(operation=="%")
				{
					result=first%second;
					answer=String.format("%.2f", result);
					textField.setText(answer);
				}
				else if(operation=="xⁿ")
				{
					double result1 =1;
					for(int i = 0; i<second;i++)
					{
					result1=first*result1;
					}
					answer=String.format("%.2f", result1);
					textField.setText(answer);
				}
			}
		});
		btnEqual.setBackground(new Color(0, 128, 255));
		btnEqual.setOpaque(true);
		btnEqual.setForeground(new Color(255, 255, 255));
		btnEqual.setFont(new Font("Verdana", Font.PLAIN, 25));
		btnEqual.setBounds(310, 575, 75, 75);
		frmScientificCalculator.getContentPane().add(btnEqual);
		
		JRadioButton btnOn = new JRadioButton("ON");
		btnOn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				btn0.setEnabled(true);
				btn1.setEnabled(true);
				btn2.setEnabled(true);
				btn3.setEnabled(true);
				btn4.setEnabled(true);
				btn5.setEnabled(true);
				btn6.setEnabled(true);
				btn7.setEnabled(true);
				btn8.setEnabled(true);
				btn9.setEnabled(true);
				
				btnDel.setEnabled(true);
				btnAC.setEnabled(true);
				
				btnSum.setEnabled(true);
				btnRest.setEnabled(true);
				btnMult.setEnabled(true);
				btnDiv.setEnabled(true);
				
				btnEqual.setEnabled(true);
				btnDot.setEnabled(true);
				btnSign.setEnabled(true);
				
				btnSin.setEnabled(true);
				btnCos.setEnabled(true);
				btnTan.setEnabled(true);
				btnAsin.setEnabled(true);
				btnAcos.setEnabled(true);
				btnAtan.setEnabled(true);
				
				btnPerc.setEnabled(true);
				btnPower.setEnabled(true);
				btnLog.setEnabled(true);
				btnSqrt.setEnabled(true);
				btnExp.setEnabled(true);
				btnFact.setEnabled(true);
				btnInv.setEnabled(true);
				
				textField.setEnabled(true);
			}
		});
		buttonGroup.add(btnOn);
		btnOn.setForeground(new Color(255, 255, 255));
		btnOn.setBackground(new Color(0, 0, 0));
		btnOn.setHorizontalAlignment(SwingConstants.CENTER);
		btnOn.setBounds(235, 158, 75, 60);
		frmScientificCalculator.getContentPane().add(btnOn);
		
		JRadioButton btnOff = new JRadioButton("OFF");
		btnOff.setSelected(true);
		btnOff.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				textField.setText(null);
				
				btn0.setEnabled(false);
				btn1.setEnabled(false);
				btn2.setEnabled(false);
				btn3.setEnabled(false);
				btn4.setEnabled(false);
				btn5.setEnabled(false);
				btn6.setEnabled(false);
				btn7.setEnabled(false);
				btn8.setEnabled(false);
				btn9.setEnabled(false);
				
				btnDel.setEnabled(false);
				btnAC.setEnabled(false);
				
				btnSum.setEnabled(false);
				btnRest.setEnabled(false);
				btnMult.setEnabled(false);
				btnDiv.setEnabled(false);
				
				btnEqual.setEnabled(false);
				btnDot.setEnabled(false);
				btnSign.setEnabled(false);
				
				btnSin.setEnabled(false);
				btnCos.setEnabled(false);
				btnTan.setEnabled(false);
				btnAsin.setEnabled(false);
				btnAcos.setEnabled(false);
				btnAtan.setEnabled(false);
				
				btnPerc.setEnabled(false);
				btnPower.setEnabled(false);
				btnLog.setEnabled(false);
				btnSqrt.setEnabled(false);
				btnExp.setEnabled(false);
				btnFact.setEnabled(false);
				btnInv.setEnabled(false);
				
				textField.setEnabled(false);
			}
		});
		buttonGroup.add(btnOff);
		btnOff.setForeground(new Color(255, 255, 255));
		btnOff.setBackground(new Color(0, 0, 0));
		btnOff.setHorizontalAlignment(SwingConstants.CENTER);
		btnOff.setBounds(310, 158, 75, 60);
		frmScientificCalculator.getContentPane().add(btnOff);
	}
}