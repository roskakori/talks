/**
 * Build maps of EBCDIC encodings.
 */
import java.io.UnsupportedEncodingException;

public class EbcdicMapsBuilder {
	public static final void main(String[] arguments) {
		byte[] bytes = new byte[1];
		for (int code = 0; code < 256; code++) {
			bytes[0] = (byte) code;
			String ch;
			try {
				ch = new String(bytes, "ibm273");
			} catch (UnsupportedEncodingException error) {
				ch = null;
			}
			System.out.println(ch);
			
		}
	}
}