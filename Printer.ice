module Demo
{
    interface Printer
    {
        void printString(string s);
        string upper(string s);
        int length(string s);
    }

    interface Math
    {
        int add(int a, int b);
        int mul(int a, int b);
    }
}
