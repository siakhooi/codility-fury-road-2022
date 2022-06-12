package nsh.codility;

public class FuryRoad2022A implements FuryRoad2022Interface {

	public int solution(String R) {
		int N = R.length();
		int S[] = new int[N];
		int F[] = new int[N];
		int current = 0;
		for (int i = 0; i < R.length(); i++) {
			char C = R.charAt(i);
			current += ((C == 'A') ? 5 : 40);
			S[i] = current;
		}

		int r = S[N - 1];
		current = 0;
		for (int i = R.length() - 1; i >= 0; i--) {
			char C = R.charAt(i);
			current += ((C == 'A') ? 20 : 30);
			F[i] = current;

			if (i > 0)
				r = Math.min(r, F[i] + S[i - 1]);
		}

		return Math.min(r, F[0]);
	}
}
