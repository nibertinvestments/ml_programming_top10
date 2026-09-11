public class Main {
    public static void main(String[] args) {
        int[] values = {12, 18, 21, 9, 31};
        int total = 0;
        for (int value : values) total += value;
        System.out.println("Total: " + total);
        System.out.println("Average: " + (total / (double) values.length));
    }
}
