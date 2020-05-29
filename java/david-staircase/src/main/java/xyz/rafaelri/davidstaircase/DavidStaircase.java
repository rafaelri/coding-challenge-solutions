package xyz.rafaelri.davidstaircase;

public class DavidStaircase {
    public static int stepPermsInt(int n) {
        switch (n) {
            case 1: return 1;
            case 2: return 2;
            case 3: return 4;
            default: return stepPermsInt(n-1) + stepPermsInt(n-2) + stepPermsInt(n-3);
        }
    }
    public static int stepPerms(int n) {
        return (int) ((long) stepPermsInt(n) % 10000000007l);
    }
}