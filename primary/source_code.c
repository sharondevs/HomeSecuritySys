
/*#include"delay.h"
#include"lcd.h"
#include"keypad.h" */
/******************
motor PIN
******************/

#include<reg51.h>
#include<string.h>
sbit a1= P2^0;
sbit a2= P2^1;
sbit a3= P2^2;
sbit a4= P2^3;
sbit a5= P2^4;
sbit a6=P2^5;
sbit  n= P2^6;
sbit breach = P3^3;
void motor();
//Port allocation

unsigned char ar[5];

unsigned char com[5]={"13467"}; //Passcode

unsigned int f,m=1,p;


void delay_ff()  // fully fixed delay
{
    unsigned int i,j;
	
    for(i=0;i<80;i++)
    for(j=0;j<120;j++);
}

void delay_pf(unsigned int x)  // partial variable delay
{
	unsigned int i,j;
	
	for(i=0;i<x;i++)
	for(j=0;j<50;j++);
}

void delay_fv(unsigned int x,y)  // fully variable delay
{
	unsigned int i,j;
		
	for(i=0;i<x;i++)
	for(j=0;j<y;j++);
}


void motor()
{ 
	unsigned int i;
	
	for(i=0;i<5;i++)
	{
		a2=a3=a4=0;
		a1=1;
		delay_ff();
		a1=a3=a4=0;
		a2=1;
		delay_ff();
		a1=a2=a4=0;
		a3=1;
		delay_ff();
		a1=a2=a3=0;
		a4=1;
		delay_ff();
 }
	delay_fv(100,100);
	
	for(i=0;i<5;i++)
	{
		a2=a3=a1=0;
		a4=1;
		delay_ff();
		a1=a2=a4=0;
		a3=1;
		delay_ff();
		a1=a3=a4=0;
		a2=1;
		delay_ff();
		a4=a2=a3=0;
		a1=1;
		delay_ff();
	}
}

//For the display config
sbit rs=P3^0;
sbit rw=P3^1;
sbit en=P3^2;
sfr lcd=0x90;

void lcd_display(unsigned int x)  // lcd display fuction
{
	unsigned int i;
	lcd=x;
	rs=1;
	rw=0;
	en=1;
	for(i=0;i<100;i++);
	en=0;
 
}
 
void cmd(unsigned char m)  // lcd command fuction
{
	unsigned int i;
	lcd=m;
	rs=0;
	rw=0;
	en=1;
	for(i=0;i<10;i++);
	en=0;
}
 
void lcd_ini()   // lcd initilize
{
	cmd(0x38);
	cmd(0x0e);
	cmd(0x01);
	cmd(0x06);
	cmd(0x90);
}	
void lcd_str(unsigned char *str)   // display string on lcd
{
	while(*str!='\0')  
	{
	  lcd_display(*str);
	  str++;
	}
}

sbit r1=P0^0; // row 1
sbit r2=P0^1; // row 2
sbit r3=P0^2; // row 3
sbit r4=P0^3; // row 4
sbit c1=P0^4; // column 1
sbit c2=P0^5; // column 2
sbit c3=P0^6; // column 3
sbit c4=P0^7; // column 4

unsigned int c;
void breached() // This method is used for indicating the security breach 
{
	if(breach==1){
			
		 char* dat = " Security Breach!!";
			lcd_ini();
			lcd_str(dat);
			while(breach==1){
			
			}
		   }
}

char keypad1()  
{	
	P2=0xff;
	while(1)
	{
		r1=0;
		r4=1;
		if(c1==0)
		{
			c='1';
			delay_pf(1000);
			return c;
		}
		else if(c2==0)
		{
			c='2';
			delay_pf(1000);
			return c;
		}
		else if(c3==0)
		{
			c='3';
			delay_pf(1000);
			return c;
		}
		else if(c4==0)
		{
			c='A';
			delay_pf(1000);
			return c;
		}

		r1=1;
		r2=0;
		if(c1==0)
		{
			c='4';
			delay_pf(1000);
			return c;
		}
		else if(c2==0)
		{

			c='5';
			delay_pf(1000);
			return c;
		}
		else if(c3==0)
		{
			c='6';
			delay_pf(1000);
			return c;
		}
		else if(c4==0)
		{
			c='B';
			delay_pf(1000);
			return c;
		}

		r2=1;
		r3=0;
		if(c1==0)
		{
			c='7';
			delay_pf(1000);
			return c;
		}
		else if(c2==0)
		{

			c='8';
			delay_pf(1000);
			return c;
		}
		else if(c3==0)
		{
			c='9';
			delay_pf(1000);
			return c;
		}
		else if(c4==0)
		{
			c='C';
			delay_pf(1000);
			return c;
		}
		
		r3=1;
		r4=0;
		if(c1==0)
		{
			delay_pf(1000);
			cmd(0x01);
		}
		else if(c2==0)
		{

			c='0';
			delay_pf(1000);
			return c;
		}
		else if(c3==0)
		{
			c='#';
			delay_pf(1000);
			return c;
		}
		else if(c4==0)
		{
			c='D';
			delay_pf(1000);
			return c;
		}
		breached();
	}
}

void entered()
{
 	while(1){
		if(n==1){  //For allowing the user to open the door seamlessly
			motor();
			}
					
		if(a6==1){   // When the security mode is activated
			break;		
			}
		}			
}

	


/******************
main program
******************/
void main()
{
	unsigned int i;
		
	lcd_ini();
	
	cmd(0x01);
	lcd_str(" WELCOME!");
	delay_pf(2000);
	breached();
	while(1)
	{
		breached();
		cmd(0X01);
		cmd(0x06);
		lcd_str(" ENTER YOUR");
		cmd(0xc0);
		lcd_str(" PASSWORD");
		
		breached();
		for(i=0;i<5;i++)
		{
			keypad1();
			
			ar[i]=c;
			
			if(i==0)
			{
			  cmd(0x01);
				lcd_display(' ');
			}
			lcd_display('*');
		}

			//compare();
		if(ar[0]==com[0] && ar[1]==com[1] && ar[2]==com[2] && ar[3]==com[3] && ar[4]==com[4])
		{
			m=1;  //If the passcode is right
		}
		else
		{
			m=0; //Wrong passcode
		}
		if(m==1)
		{
			cmd(0x01);
			lcd_str(" PASSWORD MATCHED");
			cmd(0xc0);
			lcd_str(" ACCESS GRANTED");
			a5=0;
			
			motor();
			p=0;
			delay_fv(1000,100);
			cmd(0x01);
			lcd_str(" DOOR IS OPEN");
			entered();
			
			
			
		}
		else if(m==0)  //Wrong passcode 
		{
			p++; 
			cmd(0x01);
			lcd_str(" WRONG PASSWORD");
			cmd(0xc0);
			lcd_str(" ACCESS DENIED");
			delay_fv(1000,100);
			delay_fv(1000,100);
			m=1;
			if(p==3)   //The user has a countdown of 25 seconds
			{
					cmd(0x01);
					lcd_str(" PLEASE CONTACT");
					cmd(0xc0);
					lcd_str(" THE ADMIN....");
					delay_pf(2000);
					cmd(0x01);
					lcd_str(" TRY AGAIN IN:");
				cmd(0x8e);
				lcd_str("1");
				delay_pf(1500);
				cmd(0x8e);	
				lcd_str("2");
				delay_pf(1500);
				cmd(0x8e);
				lcd_str("3");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("4");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("5");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("6");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("7");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("8");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("9");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("10");
				delay_pf(1500);
				lcd_str("11");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("12");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("13");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("14");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("15");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("16");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("17");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("18");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("19");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("20");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("21");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("22");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("23");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("24");
				cmd(0x8e);
				delay_pf(1500);
				lcd_str("25");
				cmd(0x8e);
				delay_pf(1500);
				cmd(0x01);
				p=0;	
			}
		}
	}

}



