# Position and Move analysis and comparison

For these tests a series of human games were evaluated at each position (both white and black) by Stockfish 9 and by LCZero using different neural networks.

**Stockfish 9 64 bit**
- Depth: 24

**LCZero (lc0)**
- lc0-CUDNN client
- Various networks (weight files)
- Nodes: 10k

These kind of tests are possibly better than Elo tests, and can be performed at a higher depth much faster.

## Evaluation test (possibly Value Head): SF9 eval vs LC0 eval

For each position in each game, the evaluations from SF9 and lc0 were recorded.

Below is a plot of the negative absolute difference between the the evaluations from the two engines. A mean closer to zero (higher up the graph) approximates SF9 more closely, which is desirable at this stage in LCZero development. Also a standard deviation closer to zero is desirable because it implies more consistency (lower variance).

<img src="https://raw.githubusercontent.com/Neurodynasoft/LCZero-Tools/master/EvaluationTests/EvalComparison.png"  alt=""   style="float: left; margin-right: 10px;" />

## Move Test (Overall Strength/Accuracy): SF9 moves vs LC0 moves

*IN PROGRESS...*

## Depth 1 Test (Policy Head): SF9 moves vs LC0 moves at depth=1
