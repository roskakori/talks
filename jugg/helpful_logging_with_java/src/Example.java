import java.util.logging.Logger;

public class Example {

    private static final Logger LOG = Logger.getLogger(Example.class.getName());

    public void greet() {
        LOG.info("Hello world!");
        LOG.fine(() -> String.format("Greetings from %s!", Example.class.getName()));
    }

    public static void main(String[] args) {
        Example example = new Example();
        example.greet();
    }
}
