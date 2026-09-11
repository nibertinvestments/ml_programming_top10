import java.nio.file.*;
public class Main {
    public static void main(String[] args) throws Exception {
        var text = Files.readString(Path.of("input.csv"));
        System.out.println(text.lines().count());
    }
}
