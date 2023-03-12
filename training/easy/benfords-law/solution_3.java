import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        double log[] = new double[10];
        for (int i = 0; i < N; i++) {
            String transaction = in.nextLine();
            for(char c:transaction.toCharArray()) {
                if(Character.isDigit(c) && c != '0') {
                    log[c - '1']++;
                    break;
                }
            }
        }
        boolean check = false;
        double ben[] = {30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6};
        for(int i = 0; i < 9; i++) {
            log[i] = log[i] *100.0 / N;
            if(Math.abs(log[i] - ben[i]) > 10.0) {
                check = true;
                break;
            }
        }
        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(check);
    }
}

