//Nate Schneider

import java.util.Random;
import java.util.*;

public class draftCore {

  private static int arrayLength;  //The length or each array
  private int[][] fullSpace = new int[10][arrayLength]; //The array that contains each iteration as a value
  private Map<Integer, Integer> ruleSet = new HashMap();  //The rule set used to determine how the seed data evolves. Stored as a HashMap for lookup time purposes


  /**
    Constructor for the class. Currently it only takes in the standard length of
      each array. To be clear, this is not the number of iterations. Each iteration
      is an array with a set length that is determined by the Constructor call.
      The Constructor calls the method generateInitialArray to set up the seed
      data stored as iteration 0.
    @param length  this is the length or width of the arrays
  */

  public draftCore(int length) {
    this.arrayLength = length;
    generateInitialArray();
  }

  /**
    This method is a simple setter method that takes in the rule set as a HashMap
      with key/value both being of type int. The key is the "pattern" that represents
      the neighborhood of a certain index. This is the list of patterns and their
      corresponding outcomes.
    @param rules This is the rule set being passed in.
  */

  public void setRules(HashMap<Integer,Integer> rules) {
    ruleSet = rules;
  }

  /**
    Instantiates a one dimensional array populated with default values. Creates a
      rng from the java util library. Iterates over the array replacing each value
      with a new value from the rng. The values are either 1 or 0 ie binary. This
      new array is assigned to fullSpace index 0. We call this the seed data.
  */
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

  /**
    Indexs into the array at cycleCount in fullSpace. Makes a number using the value
      and the values directly adjeacent to it. This number maintains the order of
      each value by multiplying it with the magnitudes 100, 10, or 1 dependent on
      if the value is at index-1, index, or index+1 respectively. This number is called
      a pattern which will be a key in the ruleSet.
    @param index the current index
    @param cycleCount the current iteration that is being analyzed
    @return the resulting pattern
  */

  private int findPatternForIndex(int index, int cycleCount) {
    int[] currArray = fullSpace[cycleCount];
    int pattern = 0;
      if (index == 0) {
        pattern += (10 * currArray[index]) + currArray[index + 1];
        System.out.println("pattern:" + ((10 * currArray[index]) + currArray[index + 1]));
      } else if (index == arrayLength - 1) {
        pattern += (100 * currArray[index - 1]) + (10 * currArray[index]);
        System.out.println("pattern:" + ((100 * currArray[index - 1]) + (10 * currArray[index]) + currArray[index + 1]));
      } else {
        pattern += (100 * currArray[index - 1]) + (10 * currArray[index]) + currArray[index + 1];
        System.out.println("pattern:" + ((100 * currArray[index - 1]) + (10 * currArray[index]) + + currArray[index + 1]));
      }
      return pattern;
  }

  /**
    Uses the pattern of for the index in iteration cycleCount to determine
      the value of the index in cycleCount +1. Calls method findPatternForIndex to
      get the pattern corresponding to the index and iteration.
    @param index  the current index
    @param cycleCount the currnet iteration that is being analyzed
    @return either 1 or 0 representing T or F that is based on the ruleSet and pattern
  */

  private int patternAnalysis(int index, int cycleCount) {
    int pattern = findPatternForIndex(index, cycleCount);
    System.out.println(pattern + " : " + ruleSet.get(pattern));
    return ruleSet.get(pattern);

  }


  /**
    *Method runs the creation of a new array
    @param cycleCount the current iteration -1
    @return void
  */
  private void runAtCount(int cycleCount) {
    int[] tempArr = new int[arrayLength];
    int index = 0;
    while(index < arrayLength - 1) {
      tempArr[index] = patternAnalysis(index, cycleCount);
      index++;
    }
    fullSpace[cycleCount + 1] = tempArr;
  }

  /**
    This method runs until the fullSpace is filled
    A new array is generated for each loop and added to fullSpace
    The call to runAtCount(int cycleCount) generates and adds the new array
    @return void
  */

  public void fillSpace() {
    int cycleCount = 0;
    while (cycleCount < arrayLength - 1) {
      runAtCount(cycleCount);
      cycleCount++;
    }
  }

/**
  Traditional toString method
  Returns the fullSpace as one long string where each array is separated
  by \n and each index is separated by " "
  @return String string representation of the fullSpace
*/

  public String toString() {
    String prnt = "";
    for (int[] arr : fullSpace) {
      for (int n : arr) {
        prnt += n + " ";
      }
      prnt += "\n";
    }
    return prnt;

  }

}
