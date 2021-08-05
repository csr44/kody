package mail_app;
import java.util.Scanner;

public class metody {
	private String meno;
	private String priezvisko;
	private String oddelenie;
	private String heslo;
	private int kapacita;
	private String mail;
	
	public metody(String m, String p) {
		//mail
		this.meno=m;
		this.priezvisko=p;
		System.out.println("Mail vytvoreny: " + this.meno + this.priezvisko);
		//oddelenie a heslo
		this.oddelenie = nastav_oddelenie();
		System.out.print("Odelenie:" + this.oddelenie + "\n");
		this.heslo=nahodneheslo();
		System.out.println("Vygenerovane heslo je:" + this.heslo);
		
		//generuj mail
		mail = meno.toLowerCase() + "." + priezvisko.toLowerCase() + "@" + this.oddelenie + ".comp.com";
		System.out.println("Vygenerovany mail je:"+mail);
	}
	//spytaj sa a nastav oddelenie
	private String nastav_oddelenie()
	{
		System.out.println("Vyber oddelenie\n 1 - Vyroba\n2 - Predaj\n3 - Uctovnictvo\n4 - Fakturacia");
		Scanner vstup = new Scanner (System.in);
		int vstup_int = vstup.nextInt();
		if(vstup_int == 1) {return "vyroba";}
		else if(vstup_int == 2) {return "predaj";}
		else if(vstup_int == 3) {return "uctovnictvo";}
		else {return "fakturacia";}
		
	}
	
	//generuj nahodne heslo
	private String nahodneheslo ()
	{
		String znaky = "ABCDEFGHIJKLMNOPQRSTUWXYZ0123456789!?/*-+";
		char[] heslo = new char [10];//array of characters --- new sequence of characters of the size
		for (int i=0;i<10;i++)
		{

			int rand = (int) (Math.random() * znaky.length());
			heslo[i] = znaky.charAt(rand);
		}
		return new String(heslo);
	}

}













