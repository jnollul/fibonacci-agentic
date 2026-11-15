import java.math.BigInteger;
import java.util.regex.Pattern;

public final class Fibonacci {
    private static final BigInteger ONE = BigInteger.ONE;
    private static final Pattern INTEGER_PATTERN = Pattern.compile("[+-]?[0-9]+");

    private Fibonacci() {
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            fail("Usage: Fibonacci <non-negative-integer>");
        }

        String rawIndex = args[0];
        if (!INTEGER_PATTERN.matcher(rawIndex).matches()) {
            fail("Index must be an integer.");
        }

        BigInteger index = new BigInteger(rawIndex);
        if (index.signum() < 0) {
            fail("Index must be non-negative.");
        }

        System.out.println(fibonacci(index));
    }

    private static BigInteger fibonacci(BigInteger index) {
        BigInteger previous = BigInteger.ZERO;
        BigInteger current = ONE;
        BigInteger remaining = index;
        while (remaining.signum() > 0) {
            BigInteger next = previous.add(current);
            previous = current;
            current = next;
            remaining = remaining.subtract(ONE);
        }
        return previous;
    }

    private static void fail(String message) {
        System.err.println(message);
        System.exit(2);
    }
}
