**ABXpy score**
================

We use the ABXpy package for evaluating model performance on minimal pair discrimination tasks.

Organization
============

The package is organized into three main modules, along with several submodules:

- `Task Module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#task-module>`_:
Used to create new tasks and preprocess the data.
In our setup, we use both across-speaker and within-speaker tasks, each producing results in their respective folders.

- `Distance Module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.distances.html>`_:
Calculates the distances between features, which are necessary for computing the ABX score.

- `Score Module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#score-module>`_: 
Computes the ABX score based on the generated tasks and calculated distances.

- `Analyze module <https://docs.cognitive-ml.fr/ABXpy/ABXpy.html#analyze-module>`_: 
Provides tools to analyze the evaluation results and summarize performance.

``Across task`` example:


===============  ===========  ==========  ===========  ==============  ==========  ====== 
     phone_1      speaker_1     phone_2    speaker_2      by              score      n
---------------  -----------  ----------  -----------  --------------  ----------  ------
      k            G10208          l         G11139     ('aɪ', 'aɪ')	      1.0       1
===============  ===========  ==========  ===========  ==============  ==========  ======


``Within task`` example:

===============  ==========  ========================  =========  ==========   
     phone_1      phone_2           by                   score        n         
---------------  ----------  ------------------------  ---------  ---------- 
      n              l	        ('G00473', 'aɪ', 'd')	     0.9	        30
===============  ==========  ========================  =========  ==========  




