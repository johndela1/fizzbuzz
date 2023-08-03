import java.io.*;
import java.util.*;

class Prefix {
    Vector<String> pref;

    Prefix(Prefix p)
    {
	pref = (Vector<String>) p.pref.clone();
    }

    Prefix(int sz, String str)
    {
	pref = new Vector<>();
	for (int i = 0; i < sz; i++)
	    pref.addElement(str);
    }

    static final int MULTI = 31;
    public int hashCode()
    {
	int h = 0;
	for (int i = 0; i < pref.size(); i++)
	    h= MULTI * h + pref.elementAt(i).hashCode();
	return h;
    }

    public boolean equals(Object o)
    {
	Prefix p = (Prefix) o;
	for (int i = 0; i < pref.size(); i++)
	    if(!pref.elementAt(i).equals(p.pref.elementAt(i)))
		return false;
	return true;
    }
}

class Chain {
    static final int PREF_SZ = 2;
    static final String NONWORD = "\n";
    Hashtable<Prefix,Vector> statetab = new Hashtable<Prefix,Vector>();
    Prefix prefix =  new Prefix(PREF_SZ, NONWORD);
    Random rand = new Random();
    void add(String word)
    {
	Vector suf = (Vector) statetab.get(prefix);
	if (suf == null) {
	    suf = new Vector();
	    statetab.put(new Prefix(prefix), suf);
	}
	suf.addElement(word);
	prefix.pref.removeElementAt(0);
	prefix.pref.addElement(word);
    }

    void build(InputStream in) throws IOException
    {
	StreamTokenizer st = new StreamTokenizer(in);
	st.resetSyntax();
	st.wordChars(0, Character.MAX_VALUE);
	st.whitespaceChars(0, ' ');
	while (st.nextToken() != st.TT_EOF)
	       add(st.sval);
	add(NONWORD);
    }

    void generate(int wcount)
    {
	prefix = new Prefix(PREF_SZ, NONWORD);
	for (int i = 0; i < wcount; i++) {
	    Vector s = (Vector) statetab.get(prefix);
	    int r = Math.abs(rand.nextInt() % s.size());
	    String suf = (String) s.elementAt(r);
	    System.out.println(suf);
	    prefix.pref.removeElementAt(0);
	    prefix.pref.addElement(suf);

	}
    }
}

class Markov {
    static int MAXGEN=10;
    public static void main(String[] args) throws IOException
    {
	Chain chain = new Chain();
	int wcount = MAXGEN;
	chain.build(System.in);
	chain.generate(wcount);
    }
}
