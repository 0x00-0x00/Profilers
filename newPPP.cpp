#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int toLower(string& word)
{
	int b = 0;
	char c;
	while(word[b])
	{
		c=word[b];
		putchar(tolower(c));
		
		b++;
	}
	return 0;
}

int toAlpha(string &word)
{
	int b = 0;
	char c;
	while(word[b])
	{
		c=word[b];
		if(b==0)
		{
			putchar(toupper(c));
		}
		else
		{
			putchar(tolower(c));
		}
		
		b++;
	}
	return 0;
}

int toUpper(string &word)
{
	int b=0;
	char c;
	while(word[b])
	{
		c=word[b];
		putchar(toupper(c));
		b++;
	}
	return 0;
}

int evolve(string& word)
{
	toLower(word); cout << "1" << endl;
	toUpper(word); cout << "1" << endl;
	toAlpha(word); cout << "1" << endl;
	toLower(word); cout << "2" << endl;
	toUpper(word); cout << "2" << endl;
	toAlpha(word); cout << "2" << endl;
	toLower(word); cout << "3" << endl;
	toUpper(word); cout << "3" << endl;
	toAlpha(word); cout << "3" << endl;
	toLower(word); cout << "_1" << endl;
	toUpper(word); cout << "_1" << endl;
	toAlpha(word); cout << "_1" << endl;
	toLower(word); cout << "_2" << endl;
	toUpper(word); cout << "_2" << endl;
	toAlpha(word); cout << "_2" << endl;
	toLower(word); cout << "_3" << endl;
	toUpper(word); cout << "_3" << endl;
	toAlpha(word); cout << "_3" << endl;
	toLower(word); cout << "*1" << endl;
	toUpper(word); cout << "*1" << endl;
	toAlpha(word); cout << "*1" << endl;
	toLower(word); cout << "*2" << endl;
	toUpper(word); cout << "*2" << endl;
	toAlpha(word); cout << "*2" << endl;
	toLower(word); cout << "*3" << endl;
	toUpper(word); cout << "*3" << endl;
	toAlpha(word); cout << "*3" << endl;
	toLower(word); cout << "01" << endl;
	toUpper(word); cout << "01" << endl;
	toAlpha(word); cout << "01" << endl;
	toLower(word); cout << "02" << endl;
	toUpper(word); cout << "02" << endl;
	toAlpha(word); cout << "02" << endl;
	toLower(word); cout << "03" << endl;
	toUpper(word); cout << "03" << endl;
	toAlpha(word); cout << "03" << endl;
	toLower(word); cout << "*01" << endl;
	toUpper(word); cout << "*01" << endl;
	toAlpha(word); cout << "*01" << endl;
	toLower(word); cout << "*02" << endl;
	toUpper(word); cout << "*02" << endl;
	toAlpha(word); cout << "*02" << endl;
	toLower(word); cout << "*03" << endl;
	toUpper(word); cout << "*03" << endl;
	toAlpha(word); cout << "*03" << endl;
	toLower(word); cout << "*11" << endl;
	toUpper(word); cout << "*11" << endl;
	toAlpha(word); cout << "*11" << endl;
	toLower(word); cout << "*22" << endl;
	toUpper(word); cout << "*22" << endl;
	toAlpha(word); cout << "*22" << endl;
	toLower(word); cout << "*33" << endl;
	toUpper(word); cout << "*33" << endl;
	toAlpha(word); cout << "*33" << endl;
	toLower(word); cout << "123" << endl;
	toUpper(word); cout << "123" << endl;
	toAlpha(word); cout << "123" << endl;
	toLower(word); cout << "321" << endl;
	toUpper(word); cout << "321" << endl;
	toAlpha(word); cout << "321" << endl;
	toLower(word); cout << "111" << endl;
	toUpper(word); cout << "111" << endl;
	toAlpha(word); cout << "111" << endl;
	toLower(word); cout << "222" << endl;
	toUpper(word); cout << "222" << endl;
	toAlpha(word); cout << "222" << endl;
	toLower(word); cout << "333" << endl;
	toUpper(word); cout << "333" << endl;
	toAlpha(word); cout << "333" << endl;
	toLower(word); cout << "666" << endl;
	toUpper(word); cout << "666" << endl;
	toAlpha(word); cout << "666" << endl;
	toLower(word); cout << "123*" << endl;
	toUpper(word); cout << "123*" << endl;
	toAlpha(word); cout << "123*" << endl;
	toLower(word); cout << "*123" << endl;
	toUpper(word); cout << "*123" << endl;
	toAlpha(word); cout << "*123" << endl;
	toLower(word); cout << "_123" << endl;
	toUpper(word); cout << "_123" << endl;
	toAlpha(word); cout << "_123" << endl;
	toLower(word); cout << "123_" << endl;
	toUpper(word); cout << "123_" << endl;
	toAlpha(word); cout << "123_" << endl;
	toLower(word); cout << "_321" << endl;
	toUpper(word); cout << "_321" << endl;
	toAlpha(word); cout << "_321" << endl;
	toLower(word); cout << "321_" << endl;
	toUpper(word); cout << "321_" << endl;
	toAlpha(word); cout << "321_" << endl;
	toLower(word); cout << "_111" << endl;
	toUpper(word); cout << "_111" << endl;
	toAlpha(word); cout << "_111" << endl;
	toLower(word); cout << "_222" << endl;
	toUpper(word); cout << "_222" << endl;
	toAlpha(word); cout << "_222" << endl;
	toLower(word); cout << "_333" << endl;
	toUpper(word); cout << "_333" << endl;
	toAlpha(word); cout << "_333" << endl;
	toLower(word); cout << "3321" << endl;
	toUpper(word); cout << "3321" << endl;
	toAlpha(word); cout << "3321" << endl;
	toLower(word); cout << "3322" << endl;
	toUpper(word); cout << "3322" << endl;
	toAlpha(word); cout << "3322" << endl;
	toLower(word); cout << "3323" << endl;
	toUpper(word); cout << "3323" << endl;
	toAlpha(word); cout << "3323" << endl;
	toLower(word); cout << "3324" << endl;
	toUpper(word); cout << "3324" << endl;
	toAlpha(word); cout << "3324" << endl;
	toLower(word); cout << "_3321" << endl;
	toUpper(word); cout << "_3321" << endl;
	toAlpha(word); cout << "_3321" << endl;
	toLower(word); cout << "_3322" << endl;
	toUpper(word); cout << "_3322" << endl;
	toAlpha(word); cout << "_3322" << endl;
	toLower(word); cout << "_3323" << endl;
	toUpper(word); cout << "_3323" << endl;
	toAlpha(word); cout << "_3323" << endl;
	toLower(word); cout << "_3324" << endl;
	toUpper(word); cout << "_3324" << endl;
	toAlpha(word); cout << "_3324" << endl;
	toLower(word); cout << "*3321" << endl;
	toUpper(word); cout << "*3321" << endl;
	toAlpha(word); cout << "*3321" << endl;
	toLower(word); cout << "*3322" << endl;
	toUpper(word); cout << "*3322" << endl;
	toAlpha(word); cout << "*3322" << endl;
	toLower(word); cout << "*3323" << endl;
	toUpper(word); cout << "*3323" << endl;
	toAlpha(word); cout << "*3323" << endl;
	toLower(word); cout << "*3324" << endl;
	toUpper(word); cout << "*3324" << endl;
	toAlpha(word); cout << "*3324" << endl;
	toLower(word); cout << "1234" << endl;
	toUpper(word); cout << "1234" << endl;
	toAlpha(word); cout << "1234" << endl;
	toLower(word); cout << "*1234" << endl;
	toUpper(word); cout << "*1234" << endl;
	toAlpha(word); cout << "*1234" << endl;
	toLower(word); cout << "_1234" << endl;
	toUpper(word); cout << "_1234" << endl;
	toAlpha(word); cout << "_1234" << endl;
	toLower(word); cout << "4321" << endl;
	toUpper(word); cout << "4321" << endl;
	toAlpha(word); cout << "4321" << endl;
	toLower(word); cout << "*4321" << endl;
	toUpper(word); cout << "*4321" << endl;
	toAlpha(word); cout << "*4321" << endl;
	toLower(word); cout << "_4321" << endl;
	toUpper(word); cout << "_4321" << endl;
	toAlpha(word); cout << "_4321" << endl;
	toLower(word); cout << "*123456" << endl;
	toUpper(word); cout << "*123456" << endl;
	toAlpha(word); cout << "*123456" << endl;
	toLower(word); cout << "-123456" << endl;
	toUpper(word); cout << "-123456" << endl;
	toAlpha(word); cout << "-123456" << endl;
	toLower(word); cout << "_123456" << endl;
	toUpper(word); cout << "_123456" << endl;
	toAlpha(word); cout << "_123456" << endl;
	toLower(word); cout << "123456" << endl;
	toUpper(word); cout << "123456" << endl;
	toAlpha(word); cout << "123456" << endl;
	toLower(word); cout << "*" << endl;
	toUpper(word); cout << "*" << endl;
	toAlpha(word); cout << "*" << endl;
	toLower(word); cout << "_" << endl;
	toUpper(word); cout << "_" << endl;
	toAlpha(word); cout << "_" << endl;
	toLower(word); cout << "-" << endl;
	toUpper(word); cout << "-" << endl;
	toAlpha(word); cout << "-" << endl;
	toLower(word); cout << "2000" << endl;
	toUpper(word); cout << "2000" << endl;
	toAlpha(word); cout << "2000" << endl;
	toLower(word); cout << "2001" << endl;
	toUpper(word); cout << "2001" << endl;
	toAlpha(word); cout << "2001" << endl;
	toLower(word); cout << "2002" << endl;
	toUpper(word); cout << "2002" << endl;
	toAlpha(word); cout << "2002" << endl;
	toLower(word); cout << "2003" << endl;
	toUpper(word); cout << "2003" << endl;
	toAlpha(word); cout << "2003" << endl;
	toLower(word); cout << "2004" << endl;
	toUpper(word); cout << "2004" << endl;
	toAlpha(word); cout << "2004" << endl;
	toLower(word); cout << "2005" << endl;
	toUpper(word); cout << "2005" << endl;
	toAlpha(word); cout << "2005" << endl;
	toLower(word); cout << "2006" << endl;
	toUpper(word); cout << "2006" << endl;
	toAlpha(word); cout << "2006" << endl;
	toLower(word); cout << "2007" << endl;
	toUpper(word); cout << "2007" << endl;
	toAlpha(word); cout << "2007" << endl;
	toLower(word); cout << "2008" << endl;
	toUpper(word); cout << "2008" << endl;
	toAlpha(word); cout << "2008" << endl;
	toLower(word); cout << "2009" << endl;
	toUpper(word); cout << "2009" << endl;
	toAlpha(word); cout << "2009" << endl;
	toLower(word); cout << "2010" << endl;
	toUpper(word); cout << "2010" << endl;
	toAlpha(word); cout << "2010" << endl;
	toLower(word); cout << "2011" << endl;
	toUpper(word); cout << "2011" << endl;
	toAlpha(word); cout << "2011" << endl;
	toLower(word); cout << "2012" << endl;
	toUpper(word); cout << "2012" << endl;
	toAlpha(word); cout << "2012" << endl;
	toLower(word); cout << "2013" << endl;
	toUpper(word); cout << "2013" << endl;
	toAlpha(word); cout << "2013" << endl;
	toLower(word); cout << "2014" << endl;
	toUpper(word); cout << "2014" << endl;
	toAlpha(word); cout << "2014" << endl;
	toLower(word); cout << "2015" << endl;
	toUpper(word); cout << "2015" << endl;
	toAlpha(word); cout << "2015" << endl;
	toLower(word); cout << "2016" << endl;
	toUpper(word); cout << "2016" << endl;
	toAlpha(word); cout << "2016" << endl;
	toLower(word); cout << "_2000" << endl;
	toUpper(word); cout << "_2000" << endl;
	toAlpha(word); cout << "_2000" << endl;
	toLower(word); cout << "_2001" << endl;
	toUpper(word); cout << "_2001" << endl;
	toAlpha(word); cout << "_2001" << endl;
	toLower(word); cout << "_2002" << endl;
	toUpper(word); cout << "_2002" << endl;
	toAlpha(word); cout << "_2002" << endl;
	toLower(word); cout << "_2003" << endl;
	toUpper(word); cout << "_2003" << endl;
	toAlpha(word); cout << "_2003" << endl;
	toLower(word); cout << "_2004" << endl;
	toUpper(word); cout << "_2004" << endl;
	toAlpha(word); cout << "_2004" << endl;
	toLower(word); cout << "_2005" << endl;
	toUpper(word); cout << "_2005" << endl;
	toAlpha(word); cout << "_2005" << endl;
	toLower(word); cout << "_2006" << endl;
	toUpper(word); cout << "_2006" << endl;
	toAlpha(word); cout << "_2006" << endl;
	toLower(word); cout << "_2007" << endl;
	toUpper(word); cout << "_2007" << endl;
	toAlpha(word); cout << "_2007" << endl;
	toLower(word); cout << "_2008" << endl;
	toUpper(word); cout << "_2008" << endl;
	toAlpha(word); cout << "_2008" << endl;
	toLower(word); cout << "_2009" << endl;
	toUpper(word); cout << "_2009" << endl;
	toAlpha(word); cout << "_2009" << endl;
	toLower(word); cout << "_2010" << endl;
	toUpper(word); cout << "_2010" << endl;
	toAlpha(word); cout << "_2010" << endl;
	toLower(word); cout << "_2011" << endl;
	toUpper(word); cout << "_2011" << endl;
	toAlpha(word); cout << "_2011" << endl;
	toLower(word); cout << "_2012" << endl;
	toUpper(word); cout << "_2012" << endl;
	toAlpha(word); cout << "_2012" << endl;
	toLower(word); cout << "_2013" << endl;
	toUpper(word); cout << "_2013" << endl;
	toAlpha(word); cout << "_2013" << endl;
	toLower(word); cout << "_2014" << endl;
	toUpper(word); cout << "_2014" << endl;
	toAlpha(word); cout << "_2014" << endl;
	toLower(word); cout << "_2015" << endl;
	toUpper(word); cout << "_2015" << endl;
	toAlpha(word); cout << "_2015" << endl;
	toLower(word); cout << "_2016" << endl;
	toUpper(word); cout << "_2016" << endl;
	toAlpha(word); cout << "_2016" << endl;
	return 0;
}


int main(int argc, char* argv[])
{
	if(argc < 2)
	{
		cout << "Sem arquivo para leitura especificado." << endl << "Para especificar um arquivo de leitura, execute ./newPPP <nome_do_arquivo>" << endl;
	}
	else
	{
		cout << "Arquivo de Leitura: " << argv[1] << endl;
		ifstream infile(argv[1]);
		string a;
		while(infile >> a)
		{
			toLower(a); cout << endl;
			toUpper(a); cout << endl;
			toAlpha(a); cout << endl;
			evolve(a);
		}
	}
	
	return 0;
}
