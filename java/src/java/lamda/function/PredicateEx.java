package java.lamda.function;

import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

public class PredicateEx {
	public static void main(String[] args) {
		
		// 매겨변수 없고 반환값만 있음
		Supplier<Integer> s = () -> (int)(Math.random()*+1);
		
		// 매개변수 있고, 반환값이 없음 
		Consumer<Integer> c = i -> System.out.println(i+", ");
		
		//매개 변수 있고, 반환값도 있다. 매개변수 2개는 BiFunction
		Function<Integer, Integer> f = i -> i/10*10;

		// 매개변수 있고, 반환값 값은 boolean
		Predicate<Integer> p = i -> i%2 == 0;
		
		///////////////////////
		
		Function<String, Integer> ff = (ss) -> Integer.parseInt(ss,16);
		Function<Integer,String> gg = (ii) -> Integer.toBinaryString(ii);
		
		Function<String,String> hh = ff.addThen(gg);
		Function<Integer,Integer> hh2 = ff.compose(gg);
		
		
		
		
	} 
}
