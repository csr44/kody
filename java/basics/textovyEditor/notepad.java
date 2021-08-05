package basics;
import java.io.*;  
import java.util.Date;  
import java.awt.*;  
import java.awt.event.*;  
import javax.swing.*;  
import javax.swing.event.*;  
//import java.text.*;  
import java.util.*;  
public class notepad implements ActionListener {
	JFrame pan;
	JMenuBar menu0;
	JMenu menu1,menu2,menu3;
	JTextArea plocha;
	JMenuItem i0,i1,i2,i3,e1,e2,e3,e4,e5,e6,e7,f1;
	JLabel status;
	subory kont;
	JDialog frDialog;
	
	public notepad() {
		pan = new JFrame("Textovy editor");
		kont = new subory(this);
		//CREATE MENU
		menu0 = new JMenuBar();
		menu1= new JMenu("S˙bor");
		menu2 = new JMenu("⁄pravy");
		menu3 = new JMenu("Form·tuj");
		//PRIDANIE JMENU DO JMENUBAR
		menu0.add(menu1);
		menu0.add(menu2);
		menu0.add(menu3);
		//PRIDANIE ITEMOV DO MENU

		i3=new JMenuItem("Nov˝");
		i1=new JMenuItem("Otvor");
		i0=new JMenuItem("Uloû");
		i2=new JMenuItem("Uloû Ako");
		e1=new JMenuItem("Prejsù na riadok");
		e2=new JMenuItem("N·jdi");
		e6=new JMenuItem("Vybraù vöetko");
		e3=new JMenuItem("Vystrihni");
		e4=new JMenuItem("KopÌruj");
		e5=new JMenuItem("Prilep");
		e7=new JMenuItem("Zobraz Ëas a d·tum");
		f1=new JMenuItem("Nastav pozadie");


		//ACTION LISTENER

		i3.addActionListener(this);
		i1.addActionListener(this);
		i0.addActionListener(this);
		i2.addActionListener(this);
		e1.addActionListener(this);
		e2.addActionListener(this);
		e6.addActionListener(this);
		e3.addActionListener(this);
		e4.addActionListener(this);
		e5.addActionListener(this);
		e7.addActionListener(this);
		f1.addActionListener(this);

		//PRIADANIE ITEMOV DO JMenu.. Jmenu je pridane do JMenuBar
		menu1.add(i3);
		menu1.add(i1);
		menu1.add(i0);
		menu1.add(i2);
		
		menu2.add(e1);
		menu2.add(e2);
		menu2.add(e6);
		menu2.add(e3);
		menu2.add(e4);
		menu2.add(e5);
		menu2.add(e7);
		
		menu3.add(f1);

		plocha = new JTextArea(30,60);
		status = new JLabel(("Riadok 1, Slov 0 "), JLabel.RIGHT);
		pan.add(new JScrollPane(plocha),BorderLayout.CENTER);
		pan.add(status,BorderLayout.SOUTH);


		pan.setJMenuBar(menu0);
		pan.setVisible(true);
		pan.pack(); 
		pan.setLocation(150,50);
		
		pan.addWindowListener(new WindowAdapter() {public void windowClosing(WindowEvent e) {System.exit(0);}});
		DocumentListener mmr = new DocumentListener()  
		{  
		public void changedUpdate(DocumentEvent e){kont.upraveny=true;}  
		public void removeUpdate(DocumentEvent e) {kont.upraveny=true;}  
		public void insertUpdate(DocumentEvent e){kont.upraveny=true;}  
		}; 
		plocha.getDocument().addDocumentListener(mmr);
		plocha.addCaretListener(
				new CaretListener() {
					@Override
					public void caretUpdate(CaretEvent arg0) {
						// TODO Auto-generated method stub
						int riadok=0,slov=0;
						try {
						int pozicia=plocha.getCaretPosition();
						riadok=plocha.getLineOfOffset(pozicia);
						int dlzka_plochy = plocha.getText().length();
						String text = plocha.getText();
						char ch[] = new char[dlzka_plochy];
						int pocet = 0;
						for(int i=0;i<dlzka_plochy;i++) {
							ch[i] =  text.charAt(i);
							if( ((i>0)&&(ch[i]!=' ')&&(ch[i-1]==' ')) || ((ch[0]!=' ')&&(i==0)) )  
			                    pocet++;  
						}
						slov=pocet;
						}catch(Exception ex) {}
						if(plocha.getText().length()==0) {riadok=0;slov=0;}
						status.setText("Riadok "+(riadok+1)+", Slov "+slov+" ");																		
						}
					}								
				);
		
	}

	public static void main(String[] args) {
		new notepad();
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		String command = e.getActionCommand();
		if(command == "Uloû Ako")
			kont.ulozAko();
		if(command == "Nov˝")
			kont.Novy();
		if(command == "Uloû")
			kont.uloz();
		if(command == "Otvor")
			kont.otvor();
		if(command == "Prejsù na riadok")
			kont.prejstna();
		if(command == "Vystrihni")
			plocha.cut();
		if(command == "KopÌruj")
			plocha.copy();
		if(command == "Prilep")
			plocha.paste();
		if(command == "N·jdi")
		{
			kont.najdi();
		}
		if(command == "Vybraù vöetko")
		{
			plocha.selectAll();
		}
		if(command == "Zobraz Ëas a d·tum")  
		    plocha.insert(new Date().toString(),plocha.getSelectionStart()); 
		if(command == "Nastav pozadie") {
			kont.setbackground();
		}
		
		
	}


}
