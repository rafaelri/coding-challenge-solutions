package xyz.rafaelri.davidstaircase;

public class DavidStaircase {
    public static int stepPerms(int n) {
        switch(n) {
            case 1:
            return 1;
            case 2:
            return 2;
            case 3: 
            return 4;
            default:
                int[] res = new int[n+1];
                res[1] = 1;
                res[2] = 2;
                res[3] = 4;
                for (int i=4;i<=n;i++) {
                  res[i]=res[i-1]+res[i-2]+res[i-3];
             }
             return (int) (res[n] % 10000000007l);
        }
    }
}