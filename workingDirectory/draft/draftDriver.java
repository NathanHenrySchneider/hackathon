import java.util.HashMap;

public class draftDriver {

  public static void main(String[] args) {
    draftCore drftCor = new draftCore(10);
    HashMap<Integer, Integer> ruleSet = new HashMap<Integer, Integer>()
      {{put(111, 0);
      put(110, 0);
      put(101, 0);
      put(100, 1);
      put(11, 1);
      put(10, 1);
      put(1, 1);
      put(0, 0);}};
    drftCor.setRules(ruleSet);
      // new HashMap.SimpleEntry<Integer, Integer>(111, 0), new HashMap.SimpleEntry<Integer, Integer>(110, 0), new HashMap.SimpleEntry<Integer, Integer>(101, 0), new HashMap.SimpleEntry<Integer, Integer>(011, 1), new HashMap.SimpleEntry<Integer, Integer>(100, 1), new HashMap.SimpleEntry<Integer, Integer>(001, 1), new HashMap.SimpleEntry<Integer, Integer>(010, 1), new HashMap.SimpleEntry<Integer, Integer>(000, 0)})
    drftCor.fillSpace();
    System.out.println(drftCor.toString());


  }
}
