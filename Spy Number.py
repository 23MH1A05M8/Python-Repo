import java.util.Scanner;
public class Spy{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n;
        n=sc.nextInt();
        int s=0,m=1;
        while(n!=0)
        {
            int res;
        res=n%10;
        s=s+res;
        m=m*res;
        n=n/10;
        }
        if(m==s)
        {
            System.out.println("Spy Number");
        }
        else 
        {
            System.out.println("Not Spy Number");
        }

    }
}