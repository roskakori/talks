/**
 * Code snipplets for talk on "Helpful logging with Java".
 */
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Stream;

public class Snipplets {

    private static final Logger LOG = Logger.getLogger(Snipplets.class.getName());
    private static final String CUSTOMERS_TXT_PATH = "customers.txt";
    private static final Path CUSTOMERS_PATH = Paths.get(CUSTOMERS_TXT_PATH);

    class SomeException extends RuntimeException {
        SomeException(String message) {
            super(message);
        }

        SomeException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    void doSomething() {
        LOG.info("doing something");
        if (false) {
            throw new SomeException("something else must be something");
        }
    }

    void logPerformance() {
        String name = "Hugo";
        int sizeInCm = 172;

        // BAD: Build string before logging even nothing might be logged.
        LOG.info(name + " has a size of " + sizeInCm + "cm");

        // BAD: Always resolve String.format().
        LOG.info(String.format("%s has a size of %dcm", name, sizeInCm));

        // GOOD: Log using supplier (or pattern with Log4j).
        LOG.info(() -> String.format("%s has a size of %dcm", name, sizeInCm));
        // TODO: LOG.debug("{} has a size of {}cm", name, sizeInCm);

        // BAD: with slf4j - always compute number even if might not be logged
        // TODO: LOG.debug("processing {} foos", someComputedNumber());

        // GOOD: with slf4j - conditional logging of computed information
        /* TODO
        if (LOG.isDebugEnabled()) {
            LOG.debug("processing {} foos", someComputedNumber());
        } */

        // GOOD: java.util.logging - String.format() is a Supplier
        LOG.fine(() -> String.format("processing %f foos", someComputedNumber()));

    }

    private double someComputedNumber() {
        // NOTE: Normally this would take a while to compute.
        return 17.3;
    }

    public void logWithStackTrace() {
        try {
            String[] data = new String[]{};
            System.out.println(data[17]);
        } catch (ArrayIndexOutOfBoundsException error) {
            LOG.log(Level.SEVERE, "cannot print data", error);
        }
    }

    private void writeCustomers() throws IOException {
        try (Writer writer = new BufferedWriter(new FileWriter(new File(CUSTOMERS_TXT_PATH)))) {
            for (int i = 0; i < 73; i++) {
                writer.write(String.format("customer %d\n", i + 1));
            }
        }
    }

    private void processCustomer(String line) {
        // Do nothing.
    }

    public void processCustomersWithoutLogging(Path customerPath) throws IOException {
        try (Stream<String> lines = Files.lines(customerPath)) {
            lines.forEach(this::processCustomer);
        }
    }

    public void processCustomersWithLogging(Path customerPath) throws IOException {
        LOG.info(() -> String.format("processing customers from \"%s\"", customerPath));
        AtomicInteger customerCounter = new AtomicInteger(0);
        try (Stream<String> lines = Files.lines(customerPath)) {
            lines.forEach(line -> {
                processCustomer(line);
                customerCounter.getAndIncrement();
            });
        }
        ;
        LOG.info(() -> String.format("processed %d customers", customerCounter.get()));
    }

    public void errorHandlingTemplates() {
        int actualValue = 2;
        int expectedValue = 3;

        if (actualValue != expectedValue) {
            // handle error
        }

        try {
            doSomething();
        } catch (SomeException error) {
            // handle error
        }

        if (actualValue != expectedValue) {
            LOG.severe(() -> String.format("some value is %s but must be %s",
                    actualValue, expectedValue));
        }

        try {
            doSomething();
        } catch (SomeException error) {
            // Log exception message without stack trace.
            LOG.severe(() -> String.format("cannot do something: %s", error));
        }
    }

    public void logAndThrowError(Path customerPath) throws IOException {
        // BAD EXAMPLE, don't use this template
        try (Stream<String> lines = Files.lines(customerPath)) {
            lines.forEach(this::processCustomer);
        } catch (IOException error) {
            LOG.log(Level.SEVERE,
                    String.format(
                            "cannot process customers in \"%s\"", customerPath),
                    error);
            throw error;
        }
    }

    public void processCustomers(Path customerPath) {
        try (Stream<String> lines = Files.lines(customerPath)) {
            lines.forEach(this::processCustomer);
        } catch (IOException error) {
            String message = String.format(
                    "cannot process customers in \"%s\"", customerPath);
            throw new SomeException(message, error);
        }
    }

    public static void main(String[] args) throws IOException {
        Snipplets snipplets = new Snipplets();
        snipplets.doSomething();
        snipplets.logPerformance();
        snipplets.logWithStackTrace();
        snipplets.writeCustomers();
        snipplets.processCustomersWithoutLogging(CUSTOMERS_PATH);
        snipplets.processCustomersWithLogging(CUSTOMERS_PATH);
        snipplets.logAndThrowError(CUSTOMERS_PATH);
        snipplets.processCustomers(CUSTOMERS_PATH);
    }
}
