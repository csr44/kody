package basics;
import basics.notepad;
import java.io.*;
import java.util.regex.*;
import java.util.Arrays;
import java.util.Date;  
import java.awt.*;  
import java.awt.event.*;  
import javax.swing.*;  
import javax.swing.event.*; 
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.text.BadLocationException;
import javax.swing.text.DefaultHighlighter;
import javax.swing.text.Highlighter;
import javax.swing.text.Highlighter.HighlightPainter;

public class subory implements ActionListener {
	notepad npd;
	JTextField txtReplace;
	JTextField txtFind;
	JFileChooser chose;
	JColorChooser color;
	boolean ulozeny;
	boolean upraveny;
	boolean vytvorenyNovy;
	boolean panel = false;
	FileInputStream fis;
	JDialog dialog,frDialog,bcolordialog;
	File aktualnysubor;
	File cesta;
	String menosubora;
	BufferedReader buf;
	Highlighter highlighter;
	HighlightPainter painter;

	subory(notepad m) {
		this.npd=m;
		menosubora = new String ("Novy dokument");
		aktualnysubor = new File(menosubora); // new FILE!! //fileRef
		m.pan.setTitle(menosubora);
		chose = new JFileChooser();
		upraveny=false;
		ulozeny=false;
		chose.addChoosableFileFilter(new FileNameExtensionFilter("Textove subory", "txt", "java", "py"));
		chose.setCurrentDirectory(new File("."));
		frDialog = new JDialog(npd.pan);
		frDialog.addWindowListener(new WindowAdapter() {public void windowClosing(WindowEvent e) {highlighter.removeAllHighlights();}});
	}

	void ulozAko()
	{
		cesta = null;
		chose.setDialogTitle("Uloz ako");
		chose.setApproveButtonText("Uloz");
		
		do {
			if(chose.showSaveDialog(this.npd.pan)!=JFileChooser.APPROVE_OPTION)
				return;
			cesta = chose.getSelectedFile();
			FileWriter wr = null;
			try {
				wr = new FileWriter(cesta);
				wr.write(npd.plocha.getText());
			}catch(IOException ioe) {System.out.print("Subor nie je mozne ulozit");}
			finally {try{wr.close();}catch(IOException args) {}}
			if(!cesta.exists()) {System.out.print("Subor sa neulozil");return;}
			break;
		}while(true);
		ulozeny=true;
		upraveny=false;
	}
	
	void uloz()
	{
		chose.setApproveButtonText("Uloz");
		FileWriter tem=null;
		if(ulozeny) {
			
			try {
			tem = new FileWriter(cesta);
			tem.write(npd.plocha.getText());
			}catch(IOException ioe) {System.out.print("Nepodarilo sa ulozit subor");}
			finally {try{tem.close();}catch(IOException args) {}}//bez .close() neaktualizuje subor a je ako novy
			ulozeny=true;
			upraveny=false;
			return;
		}
		ulozAko();
		npd.status.setText("Subor: " + cesta + " Bol uspesne ulozeny");
		npd.pan.setTitle(cesta.getName());
	}
	

	
	void otvor() {
		File tmp=null;
		chose.setDialogTitle("Otvor subor");  
		chose.setApproveButtonText("Otvor");  
		String riadok = null; // ak bol dokument upraveny alebo nenulovy obsah tak da vystup TRUE... ak nebol ulozeny alebo upraveny da vystup TRUE a oboje musia byt pravdive aby sa to spytalo
		if((upraveny || npd.plocha.getText().length()!=0)&& (!ulozeny || upraveny)) {
			String sprava = "Subor nie je ulozeny. Chcete ulozit?";
			int temp = JOptionPane.showConfirmDialog(this.npd.pan, sprava,null,JOptionPane.YES_NO_CANCEL_OPTION);
			if(temp == JOptionPane.YES_OPTION) {ulozAko();}
			}
		do {
			if(chose.showOpenDialog(this.npd.pan)!=JFileChooser.APPROVE_OPTION)
				return;
			try {
			tmp=null;
			buf=null;
			npd.plocha.setText("");
			cesta = chose.getSelectedFile();
			tmp = chose.getSelectedFile();
			fis=new FileInputStream(tmp); 
			buf=new BufferedReader(new InputStreamReader(fis));
			while((riadok = buf.readLine())!=null) {
				npd.plocha.append(riadok + "\n");
			}buf.close();
			npd.pan.setTitle(tmp.getName());
			ulozeny=true;
			npd.status.setText("Subor: " + tmp.getPath() + " Bol uspesne nacitany");
			return;
			}catch(IOException ioe) {System.out.print("Nepodarilo sa otvorit subor");return;}
			}while(true);}

	void Novy() {
		do {
			if(npd.plocha.getText().length()==0)break;
			if((upraveny || npd.plocha.getText().length()!=0)&& (!ulozeny || upraveny)){
				do {
				String sprava = "Subor nie je ulozeny. Chcete ulozit?";
				int temp = JOptionPane.showConfirmDialog(this.npd.pan, sprava,null,JOptionPane.YES_NO_CANCEL_OPTION);
				if(temp==JOptionPane.NO_OPTION) break; 
				if(temp == JOptionPane.CANCEL_OPTION)return;
				if(temp==JOptionPane.YES_OPTION) {
					ulozAko();
					break;
				}
				else return;
				}while(true);break;
			}break;
		}while(true);
		this.npd.plocha.setText("");
		npd.pan.setTitle(menosubora);
		aktualnysubor = new File(menosubora);
		ulozeny=false;
		
	}
	void prejstna()  
	{  
	try  
	{  
	int riadok=0;
	String tem=JOptionPane.showInputDialog(npd.pan, "Vloz cislo riadka:");
	riadok=Integer.parseInt(tem);  
	npd.plocha.setCaretPosition(npd.plocha.getLineStartOffset(riadok-1));  
	}catch(Exception e){}  
	}
	void setbackground() {
		if(color==null)  
		    color=new JColorChooser();  
		if(bcolordialog==null)  
			bcolordialog=JColorChooser.createDialog(npd.pan,"Farba pozadia", false,color,new ActionListener(){public void actionPerformed(ActionEvent evvv){npd.plocha.setBackground(color.getColor());}},null);        
		bcolordialog.setVisible(true);
		}  
	

	
	void najdi() {
		if(panel)return;
		

        frDialog.setLayout(new GridLayout(3,4));

		

        txtFind = new JTextField();
        txtReplace = new JTextField();
        
        JButton btnFind = new JButton("Nájdi");
        JButton btnReplace = new JButton("Nahraï");
        JButton btnReplaceAll = new JButton("Nahraï všetko");
        
        
        frDialog.add(new JLabel("Nájdi: "));
        frDialog.add(txtFind);
        frDialog.add(new JLabel(""));
        frDialog.add(btnFind);
        frDialog.add(new JLabel("Nahraï slovom: "));
        frDialog.add(txtReplace);
        frDialog.add(new JLabel(""));
        frDialog.add(btnReplace);
        frDialog.add(new JLabel(""));
        frDialog.add(new JLabel(""));
        frDialog.add(new JLabel(""));
        frDialog.add(btnReplaceAll);
        frDialog.pack();
        frDialog.setVisible(true);
        
        btnFind.addActionListener(this);
        panel=true;
        
	    

	}

	@Override
	public void actionPerformed(ActionEvent k) {
		// TODO Auto-generated method stub
		String command = k.getActionCommand();
		if(command == "Nájdi") {
			String text = npd.plocha.getText();
			String slovo = this.txtFind.getText();
			Pattern slovo0 = Pattern.compile(slovo);
			Matcher match = slovo0.matcher(text);
		    highlighter = npd.plocha.getHighlighter();
		    painter = new DefaultHighlighter.DefaultHighlightPainter(Color.cyan);
		    try {
		    	while (match.find()) {
				highlighter.addHighlight(match.start(), (match.end()), painter );
				}
			} catch (BadLocationException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			}
		}
	

	}
	




