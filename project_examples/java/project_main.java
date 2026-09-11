public class Main {
    public static void main(String[] args) {
        int[] items = {12, 18, 21, 9, 31};
        int total = 0;
        for (int value : items) total += value;
        System.out.println("Total: " + total);
        System.out.println("Average: " + (total / (double) items.length));
    }
}
