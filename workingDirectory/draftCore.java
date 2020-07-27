

import java.util.Random;
import java.util.*;

public class draftCore {

  private int arrayLength = 50;
  private int[][] fullSpace = new int[arrayLength][50];
  private Map<Integer, Integer> ruleSet = new HashMap();

  public draftCore(int length) {
    this.arrayLength = length;
    generateInitialArray();
  }

  private void setRules(HashMap.Entry<Integer,Integer>[] rules) {
    for (HashMap.Entry<Integer, Integer> r : rules) {
      ruleSet.put(r.getKey(), r.getValue());
    }
  }

  private void generateInitialArray() {
    int[] arr = new int[arrayLength];
    Random rng = new Random();
    int n = 0;
    while (n < arrayLength) {
      arr[n] = rng.nextInt(2);
      n++;
    }
    fullSpace[0] = arr;
  }

  private int findPatternForIndex(int index, int cycleCount) {
    int[] currArray = fullSpace[cycleCount];
    int pattern = 0;
      if (index == 0) {
        pattern += (10 * fullSpace[cycleCount][index]) + fullSpace[cycleCount][index + 1];
      } else if (index == arrayLength - 1) {
        pattern += (100 * fullSpace[cycleCount][index - 1]) + (10 * fullSpace[cycleCount][index]);
      } else {
        pattern += (100 * fullSpace[cycleCount][index - 1]) + (10 * fullSpace[cycleCount][index]) + fullSpace[cycleCount][index + 1];
      }
      return pattern;
  }

  private int patternAnalysis(int index, int cycleCount) {
    int pattern = findPatternForIndex(index, cycleCount);
    return ruleSet.get(pattern);

  }

  private void runAtCount(int cycleCount) {
    int[] tempArr = new int[arrayLength];
    int index = 0;
    while(index < arrayLength) {
      tempArr[index] = patternAnalysis(index, cycleCount);
      index++;
    }
  }

  private void fillSpace() {
    int cycleCount = 1;
    while (cycleCount < arrayLength) {
      runAtCount(cycleCount);
      cycleCount++;
    }
  }

}
