

import java.util.Random;

public class Generator {

  private arrayLength = 50;
  private fullSpace = [][50];
  private Map<int, int> ruleSet = new HashMap

  public Generator(int length) {
    this.arrayLength = length
    fullSpace[0] = generateInitialArray();
  }

  private int[] generateInitialArray() {
    int[] arr = [arrayLength];
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
      } else if (index = arrayLength - 1) {
        pattern += (100 * fullSpace[cycleCount][index - 1]) + (10 * fullSpace[cycleCount][index]);
      } else {
        pattern += (100 * fullSpace[cycleCount][index - 1]) + (10 * fullSpace[cycleCount][index]) + fullSpace[cycleCount][index + 1];
      }
      return pattern;
  }

  private patternAnalysis(int index, int cycleCount) {
    int pattern =
  }

  private runAtCount(int cycleCount) {
    int[] tempArr = [0] * arrayLength;
    int index = 0;
    while(index < arrayLength) {
      tempArr[index] = patternAnalysis(index, cycleCount);
      index++;
    }
  }

  private fillSpace() {
    int cycleCount = 1;
    while (cyclesCount < arrayLength) {
      runAtCount(cycleCount);
    }
  }







}
