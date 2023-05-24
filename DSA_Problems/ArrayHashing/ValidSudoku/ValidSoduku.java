package DSA_Problems.ArrayHashing.ValidSudoku;

import java.util.HashSet;
import java.util.Set;

public class ValidSoduku {

    public static boolean isValidSoduku(char[][] board) {

        Set<String> seen = new HashSet<String>();
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char number = board[r][c];
                if (number != '.')
                    if (!seen.add(number + " in row " + r) ||
                            !seen.add(number + " in column " + c) ||
                            !seen.add(number + " in block " + r / 3 + "-" + c / 3))
                        return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        char[][] board = {
        {'5', '3', '.', '.', '7', '.', '.' , '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };


    char[][] board2 = {
        {'8', '3', '.', '.', '7', '.', '.' ,'.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };

        System.out.println(isValidSoduku(board));
        System.out.println(isValidSoduku(board2));
    }
}
